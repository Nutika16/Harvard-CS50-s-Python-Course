# balance = 0

# def main():
#     deposit(100)
#     withraw(50)
#     print("Balance:",balance)

# def deposit(n):
#     global balance
#     balance += n

# def withraw(n):
#     global balance 
#     balance -= n

# if __name__ == "__main__":
#     main()

'''We can solve this same question using the Oop concept'''

class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self,n):
        self._balance += n

    def withraw(self,n):
        self._balance -= n

def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withraw(50)
    print("Balance:", account.balance)

if __name__ == "__main__":
    main()


    
