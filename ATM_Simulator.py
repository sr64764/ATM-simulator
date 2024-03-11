def atm_simulation():

    balance=10000
    print('''
            ***** Welcome To ATM Machine Simulator *****
         ''')

    pin=int(input('Enter Your Pin: '))
    print('''
            Options you can Excercise are:
            1) Balance
            2) Withdraw
            3) Deposite
            4) Exit
         ''')
    choose=int(input('Select Your Transaction from the above options: '))
    if choose==1:
        print(f'Available A/C Balance Is {balance}')
    elif choose==2:
        withdraw=int(input('Enter Amount: '))
        if withdraw<=balance:
            balance-=withdraw
            print(f'Your availabe balance is {balance}')
        else:
            print('Insufficient Balance')
    elif choose==3:
        amount=int(input('Enter Amount: '))
        balance+=amount
        print(f'New Balance is {balance}')
    elif choose==4:
        exit()
    else:
        print('No Selected Transaction')

    return

if __name__ == "__main__":

    atm_simulation()