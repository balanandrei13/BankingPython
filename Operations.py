from Account import Account
import Account
listAccounts=[]

def createAccount():
    finished=False
    accountNum=0
    while finished==False:
        firstName=input("Please enter your first name: ")
        lastName=input("Please enter your last name: ")
        deposit=int(input("Whould you like to deposit money into your new account?: "))
        accountNum+=1
        username=input("Enter a username: ") 
        password=input("Set up a password: ")
        newAccount=Account.Account(firstName,lastName,username,password,accountNum,deposit)
        listAccounts.append(newAccount)
        print("Frist name: "+str(newAccount.firstName) +"\n",
        "Last name: "+str(newAccount.lastName)+"\n",
        "Your account number is: "+str(newAccount.accountNumber)+"\n",
        "Your credit is: "+str(newAccount.credit)+"\n",
        "Your username is: "+str(newAccount.username)+"\n",
        "You have set your password to be: "+str(newAccount.password)+"\n")
        question=input("Would you like to create another one?")
        if question=="Y" or question=="Yes":
            finished=False
        else:
            finished=True
            print(listAccounts)

def login():
    usernameEntered=input("Please enter your username: ")
    for i in listAccounts:
        if usernameEntered==i.username:
            passwordEntered=input("Please enter your password: ")
            if passwordEntered==i.password:
                print("Login Successfully!")
                return i

def accountFinder():
    accountFinder=int(input("What account do you want to use?: "))
    for i in listAccounts:
        if accountFinder==i.accountNumber:
            return i

def transactions():
    accountToBeUsed=login()
    action=int(input("What would you like to do?: \n1. Whitdraw\n2. Deposit\n3.Transfer\n"))
    if action==1:
        withdrawAmmount=int(input("How much money would you like to withdraw?: "))
        accountToBeUsed.credit-=withdrawAmmount
        print("You have withdrawn: "+str(withdrawAmmount)+
              "RON and your credit is: "+str(accountToBeUsed.credit)+"RON.")
    elif action==2:
        depositAmmount=int(input("How much money would you like to deposit?: "))
        accountToBeUsed.credit += depositAmmount
        print("You have deposited: "+str(depositAmmount)+
              "RON and your credit is now :"+str(accountToBeUsed.credit)+"RON.")
    elif action==3:
        accountFound=accountFinder()
        transferAmmount=int(input("How much money would you like to transfer?: "))
        accountToBeUsed.credit -= transferAmmount
        accountFound.credit += transferAmmount
        print(accountFound.credit)
        print("You have transfered: "+str(transferAmmount)+"RON to the account: "
              +str(accountFound.accountNumber)+ "\n Your remaining balance is now : "+
              str(accountToBeUsed.credit)+"RON.")