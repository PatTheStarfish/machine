status = {"water": 400, "milk": 540, "coffee_beans": 120, "cups": 9, "money": 550}

class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550

    def get_action(self):
        while True:
            action = input("Write action (buy, fill, take):")
            if action == "buy":
                action = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
                if action == "back":
                    continue
                elif action == "1" or action == "2" or action == "3":
                    return action
                else:
                    print("Wrong input, try again")
                    continue
            elif action == "fill" or action == "take" or action == "remaining":
                return action
            elif action == "exit":
                exit(0)


    def make_coffee(self, action):
        if action == "1":
            if self.water < 250:
                print("Sorry, not enough water!")
            elif self.coffee_beans < 16:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough cups!")
            else:
                self.water -= 250
                self.coffee_beans -= 16
                self.cups -= 1
                self.money += 4
                print("I have enough resources, making you a coffee!")
        elif action == "2":
            if self.water < 350:
                print("Sorry, not enough water!")
            elif self.milk < 75:
                print("Sorry, not enough milk!")
            elif self.coffee_beans < 20:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough cups!")
            else:
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.cups -= 1
                self.money += 7
                print("I have enough resources, making you a coffee!")
        elif action == "3":
            if self.water < 200:
                print("Sorry, not enough water!")
            elif self.milk < 100:
                print("Sorry, not enough milk!")
            elif self.coffee_beans < 12:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough cups!")
            else:
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.cups -= 1
                self.money += 6
                print("I have enough resources, making you a coffee!")


    def fill_machine(self):
        self.water += int(input("Write how many ml of water you want to add:"))
        self.milk += int(input("Write how many ml of milk you want to add:"))
        self.coffee_beans += int(input("Write how many grams of coffee beans you want to add:"))
        self.cups += int(input("Write how many disposable coffee cups you want to add:"))


    def take_money(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def print_status(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")

    def process_input(self):
        action = self.get_action()
        if action == "fill":
            self.fill_machine()
        elif action == "take":
            self.take_money()
        elif action == "remaining":
            self.print_status()
        else:
            self.make_coffee(action)


coffee_machine = CoffeeMachine()
while True:
    coffee_machine.process_input()
