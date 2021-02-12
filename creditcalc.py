import argparse
import sys
import math

parser = argparse.ArgumentParser()

parser.add_argument('--type', choices=['diff', 'annuity'])
parser.add_argument('--payment')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')

args = parser.parse_args()

loananswer = [args.type, args.payment, args.principal, args.periods, args.interest]
negativecheck = 0

for i in range(1, len(loananswer)):
    if i < 0:
        negativecheck += 1
    else:
        pass
if len(sys.argv) == 5:
    if negativecheck == 0:
        if loananswer[0] == 'diff':
            if loananswer[1] is None:
                principal = float(loananswer[2])
                months = int(loananswer[3])
                interest = float(loananswer[4])
                nominal = interest / 12 / 100
                month = 1
                overpay = []
                for i in range(1, months + 1):
                    differentiated = math.ceil(principal / months + nominal * (principal
                                                                               - (principal * (month - 1) / months)))
                    overpay.append(differentiated)
                    print('Month ' + str(month) + ': payment is ' + str(differentiated))
                    month += 1
                print()
                print('Overpayment = ' + str(sum(overpay) - principal))
            else:
                print('Incorrect parameters')
        elif loananswer[0] == 'annuity':
            if loananswer[1] is None:  # monthly payments
                principal = float(loananswer[2])
                months = int(loananswer[3])
                interest = float(loananswer[4])
                nominal = interest / 12 / 100
                annuity = math.ceil(principal * ((nominal * pow(1 + nominal, months))
                                                 / (pow(1 + nominal, months) - 1)))
                overpayment = annuity * months - principal
                print('Your monthly payment = ' + str(annuity) + '!')
                print('Overpayment = ' + str(math.ceil(overpayment)))
            elif loananswer[2] is None:  # principal
                annuity = float(loananswer[1])
                months = int(loananswer[3])
                interest = float(loananswer[4])
                nominal = interest / 12 / 100
                principal = annuity / ((nominal * ((1 + nominal) ** months)) / (((1 + nominal) ** months) - 1))
                overpayment = annuity * months - principal
                print('Your loan principal = ' + str(round(principal)) + '!')
                print('Overpayment = ' + str(math.ceil(overpayment)))
            elif loananswer[3] is None:  # time in months
                principal = float(loananswer[2])
                mpayment = float(loananswer[1])
                interest = float(loananswer[4])
                nominal = interest / 12 / 100
                payments = math.ceil(math.log((mpayment / (mpayment - nominal * principal)), (1 + nominal)))
                overpayment = mpayment * payments - principal
                if payments < 12:
                    if math.ceil(payments % 12) > 1:
                        print('It will take ' + str(math.ceil(payments % 12)) + ' months to repay your loan!')
                        print('Overpayment = ' + str(math.ceil(overpayment)))
                    else:
                        print('It will take 1 month to repay your loan!')
                        print('Overpayment = ' + str(math.ceil(overpayment)))
                else:
                    if payments % 12 == 0:
                        if (payments / 12) > 1:
                            print('It will take ' + str(int(payments / 12)) + ' years to repay this loan!')
                            print('Overpayment = ' + str(math.ceil(overpayment)))
                        else:
                            print('It will take 1 year to repay this loan!')
                            print('Overpayment = ' + str(math.ceil(overpayment)))
                    else:
                        years = payments // 12
                        months = math.ceil(payments % 12)
                        if years == 1:
                            if months == 1:
                                print('It will take 1 year and 1 month to repay this loan!')
                                print('Overpayment = ' + str(math.ceil(overpayment)))
                            else:
                                print('It will take 1 year and ' + str(months) + ' months to repay this loan!')
                                print('Overpayment = ' + str(math.ceil(overpayment)))
                        else:
                            if months == 1:
                                print('It will take ' + str(years) + ' years and 1 month to repay this loan!')
                                print('Overpayment = ' + str(math.ceil(overpayment)))
                            else:
                                print(
                                    'It will take ' + str(years) + ' years and ' + str(
                                        months) + ' months to repay this loan!')
                                print('Overpayment = ' + str(math.ceil(overpayment)))
    else:
        pass
else:
    print('Incorrect parameters')
