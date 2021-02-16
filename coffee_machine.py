current = [400, 540, 120, 9, 550]
choices = [[-250, 0, -16, -1, 4],  # espresso
           [-350, -75, -20, -1, 7],  # latte
           [-200, -100, -12, -1, 6]]  # cappuccino


def updated(selection):
    global current
    current = [current[i] + choices[selection][i] for i in range(0, 5)]


def state():
    print('The coffee machine has:\n' + str(current[0]) + ' of water\n' + str(current[1]) + ' of milk\n'
          + str(current[2]) + ' of coffee beans\n' + str(current[3]) + ' of disposable cups\n' + str(current[4])
          + ' of money')
    print()


def buy():
    selection = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    unable = 0
    if selection == "back":
        pass
    else:
        for i in range(0, 4):
            if current[i] + choices[int(selection) - 1][i] < 0:
                unable += 1
            else:
                pass
        if unable < 1:
            print('I have enough resources, making you a coffee!')
            if selection == "1":
                updated(0)
            elif selection == "2":
                updated(1)
            elif selection == "3":
                updated(2)
        else:
            print('Sorry, not enough resources!')
        print()


def fill():
    global current
    fillerup = [int(input('Write how many ml of water do you want to add:')),
                int(input('Write how many ml of milk do you want to add:')),
                int(input('Write how many grams of coffee beans do you want to add:')),
                int(input('Write how many disposable cups of coffee do you want to add:')), 0]
    current = [current[i] + fillerup[i] for i in range(len(current))]
    print()


def take():
    global current
    print('I gave you $' + str(current[4]))
    current[4] -= current[4]
    print()


while True:
    options = input('Write action (buy, fill, take, remaining, exit):')
    print()
    if options == 'buy':
        buy()
    elif options == 'fill':
        fill()
    elif options == 'take':
        take()
    elif options == 'remaining':
        state()
    else:
        break
