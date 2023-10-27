from Account import Account
import Account
listAccounts=[]

# this function creates the account via user input
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

# this function logs the user in so he can use only a specific account that is his and has authority over it to make transactions
def login():
    usernameEntered=input("Please enter your username: ")
    for i in listAccounts:
        if usernameEntered==i.username:
            passwordEntered=input("Please enter your password: ")
            if passwordEntered==i.password:
                print("Login Successfully!")
                return i

# this function finds an account that the account you are logged onto can make transactions with. 
def accountFinder():
    accountFinder=int(input("What account do you want to use?: "))
    for i in listAccounts:
        if accountFinder==i.accountNumber:
            return i

# this function enables you to make transations with the account that you are logged into and also transfer money to other accounts
def transactions():
    accountToBeUsed=login()
    #promt the user to select an action to be made with the account he is logged into
    action=int(input("What would you like to do?: \n1. Whitdraw\n2. Deposit\n3.Transfer\n"))
    # check for users transaction choice from input
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
        #uses the accountFound() function to find an account in the list made of Account Objects to add the ammount to.
        accountFound=accountFinder()
        transferAmmount=int(input("How much money would you like to transfer?: "))
        accountToBeUsed.credit -= transferAmmount
        accountFound.credit += transferAmmount
        print(accountFound.credit)
        print("You have transfered: "+str(transferAmmount)+"RON to the account: "
              +str(accountFound.accountNumber)+ "\n Your remaining balance is now : "+
              str(accountToBeUsed.credit)+"RON.")