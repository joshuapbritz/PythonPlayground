class Account():
    def __init__(self, account_holder, account_balance):
        self.account_balance = account_balance
        self.account_holder = account_holder

    def __str__(self):
        return f'Acount holder: {self.account_holder}\nAccount Balance: R{self.account_balance}.00'

    def deposit(self, amount):
        if type(amount) == int:
            self.account_balance = self.account_balance + amount
            return 'Success'
        else:
            return 'Sorry, something went wrong'

    def withdraw(self, amount):
        if type(amount) == int:
            if amount < self.account_balance - 20:
                self.account_balance = self.account_balance - amount
                return 'Success'
            else:
                return 'Insufficient Funds'
        else:
            return 'Sorry, something went wrong'


card_pin = None
attempts = 0
working = False

while not card_pin:
    pin = int(input('What is you pin?: '))
    if pin == 5678:
        working = True
        break
    elif attempts < 3:
        attempts += 1
        print('You have ' + str(3 - attempts) + ' attempts left')
        continue
    else:
        print('Your card has been swallowed')
        quit()

my_account = Account('Joshua Britz', 90000)

while working:
    action = int(
        input(
            '1: Withdrawal\n2: Deposit\n3: Check Balance\n4: Log Out\nWhat would you like to do?: '
        ))
    if action == 1:
        amt = int(input('How much would you like to withdraw?: '))
        result = my_account.withdraw(amt)
        print('\n\n\n')
        print(result)
        print('\n\n\n')
    elif action == 2:
        amt = int(input('How much would you like to deposit?: '))
        result = my_account.deposit(amt)
        print('\n\n\n')
        print(result)
        print('\n\n\n')
    elif action == 3:
        print(f'\n\n\nYour balance is R{my_account.account_balance}.00\n\n\n')
    elif action == 4:
        print(f'Thank you {my_account.account_holder}')
        working = False
    else:
        continue

print(my_account)
