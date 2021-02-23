import random
import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute('DELETE FROM card')
cur.execute('''CREATE TABLE IF NOT EXISTS card (
        id INTEGER,
        number TEXT,
        pin TEXT,
        balance INTEGER DEFAULT 0)
        ;''')


class Account:
    def __init__(self):
        self.cardnumber = ''
        self.pin = ''
        self.balance = 0
        self.accountinfo = {'Card Number': [], 'PIN': '', 'Balance': self.balance}
        self.numbers = []

    def new_card(self):
        newnumber = []
        luhn = [4, 0, 0, 0, 0, 0]
        for n in range(0, 9):
            newnumber.append(str(random.randint(0, 9)))
        for t in range(len(newnumber)):
            luhn.append(int(newnumber[t]))
        for x in range(0, len(luhn)):
            if (x + 1) % 2 != 0:
                luhn[x] = luhn[x] * 2
        for y in range(0, len(luhn)):
            if luhn[y] > 9:
                luhn[y] = luhn[y] - 9
        if sum(luhn) % 10 == 0:
            luhn = 0
        else:
            luhn = 10 - sum(luhn) % 10
        new_number = [4, 0, 0, 0, 0, 0]
        for b in newnumber:
            new_number.append(int(b))
        new_number.append(luhn)
        self.cardnumber = ''.join(str(h) for h in new_number)
        self.accountinfo['Card Number'] = self.cardnumber
        self.numbers.append(self.cardnumber)

    def new_pin(self):
        newpin = []
        for i in range(0, 4):
            newpin.append(str(random.randint(0, 9)))
        self.pin = ''.join(newpin)
        self.accountinfo['PIN'] = self.pin

    def add_to_database(self):
        add_new = 'INSERT INTO card(number, pin, balance) VALUES (?, ?, ?)'
        add_values = self.cardnumber, self.pin, 0
        cur.execute(add_new, add_values)
        conn.commit()

    def balance(self):
        acct_conf = 'SELECT balance FROM card WHERE number =(?)'
        acct_num = [str(self.cardnumber)]
        cur.execute(acct_conf, acct_num)
        current = cur.fetchall()
        print(current)

    def luhn_algorithm(self, card):
        luhn = [int(c) for c in card]
        for a in range(0, len(luhn) - 1):
            if (a + 1) % 2 != 0:
                luhn[a] = luhn[a] * 2
        for b in range(len(luhn)):
            if luhn[b] > 9:
                luhn[b] = luhn[b] - 9
        check = luhn.pop(-1)
        if (sum(luhn) + check) % 2 != 0:
            return False
        else:
            return True


scott = Account()

while True:
    main_menu = int(input('1. Create an account\n2. Log into account\n0. Exit\n'))
    if main_menu == 1:
        scott.new_card()
        scott.new_pin()
        scott.add_to_database()
        print('\nYour card has been created\nYour card number:\n' + ''.join(str(h) for h in scott.cardnumber) +
              '\n Your card PIN:\n' + ''.join(scott.pin) + '\n')
    elif main_menu == 2:
        card_num = input('Enter your card number:\n')
        pin_num = input('Enter your PIN:\n')
        if card_num in scott.numbers:
            scott.cardnumber = card_num
            cur.execute('SELECT pin FROM card WHERE number ={}'.format(scott.cardnumber))
            scott.pin = cur.fetchone()[0]
            conn.commit()
            print(scott.pin, scott.cardnumber)
            if pin_num == scott.pin:
                print('You have successfully logged in!\n')
                while True:
                    acct_menu = int(input('1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n'
                                          '5. Log out\n0. Exit\n'))
                    if acct_menu == 1:
                        cur.execute('SELECT balance FROM card WHERE number={}'.format(scott.cardnumber))
                        print('\nBalance: ' + str(cur.fetchone()[0]) + '\n')
                    elif acct_menu == 2:
                        add_val = int(input('\nEnter income:\n')), scott.cardnumber
                        add_inc = 'UPDATE card SET balance = (balance + ?) WHERE number =(?);'
                        cur.execute(add_inc, add_val)
                        conn.commit()
                        cur.execute('SELECT balance FROM card')
                        scott.balance += cur.fetchone()[0]
                        print('Income was added!\n')
                    elif acct_menu == 3:
                        verify = input('Transfer\nEnter card number:\n')
                        if scott.luhn_algorithm(verify) is False:
                            print('Probably you made a mistake in the card number. Please try again!\n')
                        elif verify not in scott.numbers:
                            print('Such a card does not exist.\n')
                        else:
                            xfer_amt = int(input('Enter how much money to transfer:\n'))
                            cur.execute('SELECT balance FROM card WHERE number={};'.format(scott.cardnumber))
                            scott.balance = cur.fetchone()[0]
                            if xfer_amt > scott.balance:
                                print('Not enough money!\n')
                                print(scott.balance)
                            else:
                                added = 'UPDATE card SET balance = (balance + {}) WHERE number ={};'.format(xfer_amt,
                                                                                                            verify)
                                taken = 'UPDATE card SET balance = (balance - {}) WHERE number ={};'.format(xfer_amt,
                                                                                                            scott.cardnumber)
                                cur.execute(added)
                                cur.execute(taken)
                                conn.commit()
                                print('Success!')
                    elif acct_menu == 4:
                        cur.execute('DELETE FROM card WHERE number ={}'.format(scott.cardnumber))
                        conn.commit()
                        scott.numbers.remove(scott.cardnumber)
                        print(scott.numbers)
                        print('\nThe account has been closed!\n')
                        break
                    elif acct_menu == 5:
                        break
                    else:
                        print('\nBye!')
                        exit()
            else:
                print('Wrong card number or PIN!\n')
                pass
        else:
            print('Wrong card number or PIN!\n')
            pass
    else:
        print('\nBye!')
        break
