# make bank account
# deposit
# withdraw- shouldn't exceed balance
# print balances, individual data

class Bank:

    def __init__(self,name, bank_balance=  0):
        self.name = name
        assert type(bank_balance) == int
        self.bank_balance = bank_balance

        # print("Account holder name: {}".format(self.name))
        # print("Account Balance: ${}".format(self.bank_balance))
        print("Your current bank balance is ${}".format(self.bank_balance))


    def deposits(self, deposit_amount):
        assert type(deposit_amount) == int
        self.bank_balance = self.bank_balance + deposit_amount
        print("Account updated with ${}".format(deposit_amount))
        print("Updated bank balance is ${}".format(self.bank_balance))

    def withdraw(self,withdraw_amount):
        assert type(withdraw_amount) == int
        if self.bank_balance >= withdraw_amount:
            self.bank_balance = self.bank_balance - withdraw_amount
            print("Account updated with ${}".format(withdraw_amount))
            print("Updated bank balance is ${}".format(self.bank_balance))
        else:
            print("Your account balance is low. Please enter a value less than ${}".format(self.bank_balance))
            exit

    def __str__(self):
        return ("Account holder name: {} \nAccount Balance: ${}".format(self.name, self.bank_balance))


bank = Bank("Vandana", 1000)
# print(bank.name)
# print(bank.bank_balance)
# print(Bank)
print(bank)
# print(bank.deposits(2000))
# bank.deposits(2000)
take_money = bank.withdraw(500)
take_money = bank.withdraw(500)
# print(take_money)


