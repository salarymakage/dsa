class Main:
    def __init__(self):
        self.options = {  # Renamed from self.name to self.options
            '1': self.option1,
            '2': self.option2,
            '3': self.option3,
            '4': self.option4,
            '5': self.option5,
            '6': self.option6,
            '7': self.exit  # Changed from 'self.memu' to 'self.exit'
        }

    def display_menu(self):  # Renamed from menu to display_menu to avoid confusion
        print('1. Insert an element.')
        print('2. Insert new element.')
        print('3. Display the array.')
        print('4. Delete your element.')
        print('5. Search ')
        print('6. Bubble Sort.')
        print('7. Exit')

    def option1(self):
        print('You are in option 1.')

    def option2(self):
        print('You are in option 2.')

    def option3(self):
        print('You are in option 3.')

    def option4(self):
        print('You are in option 4.')

    def option5(self):
        print('You are in option 5.')

    def option6(self):
        print('You are in option 6.')

    def exit(self):  # Added exit method to quit the menu
        print('Exiting the menu...')
        exit(0)

    def run(self):
        while True:
            self.display_menu()  # Changed from self.menu() to self.display_menu()
            choice = input('Enter number:')
            action = self.options.get(choice)
            if action:
                action()
            else:
                print("Invalid Option")

# Create an instance of the Main class and run the menu
menu = Main()
menu.run()
