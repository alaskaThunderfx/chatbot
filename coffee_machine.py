class CoffeeMachine:
    def __init__(self):
        self.current = [400, 540, 120, 9, 550]
        self.fillerup = [0, 0, 0, 0, 0]
        self.selection = ''
        self.choices = [[-250, 0, -16, -1, 4],  # espresso
                        [-350, -75, -20, -1, 7],  # latte
                        [-200, -100, -12, -1, 6]]  # cappuccino

    def state(self):
        print('The coffee machine has:\n' + str(self.current[0]) + ' of water\n' + str(self.current[1]) + ' of milk\n'
              + str(self.current[2]) + ' of coffee beans\n' + str(self.current[3]) + ' of disposable cups\n' + str(
            self.current[4])
              + ' of money')
        print()

    def take(self):
        print('I gave you $' + str(self.current[4]))
        self.current[4] -= self.current[4]
        print()

    def fill(self):
        self.fillerup = [int(input('Write how many ml of water do you want to add:')),
                         int(input('Write how many ml of milk do you want to add:')),
                         int(input('Write how many grams of coffee beans do you want to add:')),
                         int(input('Write how many disposable cups of coffee do you want to add:')), 0]
        self.current = [self.current[i] + self.fillerup[i] for i in range(len(self.current))]
        print()

    def updated(self):
        self.current = [self.current[i] + self.choices[int(self.selection) - 1][i] for i in range(0, 5)]

    def buy(self):
        self.selection = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        unable = 0
        if self.selection == "back":
            pass
        else:
            for i in range(0, 4):
                if self.current[i] + self.choices[int(self.selection) - 1][i] < 0:
                    unable += 1
                else:
                    pass
            if unable < 1:
                print('I have enough resources, making you a coffee!')
                if self.selection == "1":
                    self.updated()
                elif self.selection == "2":
                    self.updated()
                elif self.selection == "3":
                    self.updated()
            else:
                print('Sorry, not enough resources!')
            print()


coffee_machine = CoffeeMachine()

while True:
    options = input('Write action (buy, fill, take, remaining, exit):')
    print()
    if options == 'buy':
        coffee_machine.buy()
    elif options == 'fill':
        coffee_machine.fill()
    elif options == 'take':
        coffee_machine.take()
    elif options == 'remaining':
        coffee_machine.state()
    else:
        break
