import random


class Account:
    def __init__(self):
        self.cardnumber = ''
        self.pin = ''
        self.balance = 0
        self.accountinfo = {'Card Number': '', 'PIN': '', 'Balance': self.balance}

    def new_card(self):
        newnumber = []
        for i in range(0, 10):
            newnumber.append(str(random.randint(0, 9)))
        self.cardnumber = '400000' + ''.join(newnumber)
        self.accountinfo['Card Number'] = self.cardnumber

    def new_pin(self):
        newpin = []
        for i in range(0, 4):
            newpin.append(str(random.randint(0, 9)))
        self.pin = ''.join(newpin)
        self.accountinfo['PIN'] = self.pin


scott = Account()

while True:
    main_menu = int(input('1. Create an account\n2. Log into account\n0. Exit\n'))
    if main_menu == 1:
        scott.new_card()
        scott.new_pin()
        print('\nYour card has been created\nYour card number:\n' + ''.join(scott.cardnumber) +
              '\n Your card PIN:\n' + ''.join(scott.pin) + '\n')
    elif main_menu == 2:
        card_num = input('Enter your card number:\n')
        pin_num = input('Enter your PIN:\n')
        if card_num == scott.cardnumber:
            if pin_num == scott.pin:
                print('You have successfully logged in!\n')
                while True:
                    acct_menu = int(input('1. Balance\n2. Log out\n0. Exit\n'))
                    if acct_menu == 1:
                        print('\nBalance: ' + str(scott.balance) + '\n')
                    elif acct_menu == 2:
                        print('\nYou have successfully logged out!\n')
                        break
                    else:
                        print('\nBye!')
                        break

    else:
        print('\nBye!')
        break
