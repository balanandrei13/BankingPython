from Account import Account
import Account
listAccounts=[]

mihai=Account.Account("Mihai","Stefanescu","mihai","1234",10,200)
ionut=Account.Account("Ionut","Cristescu","ionut","0000",11,300)
#hard coded accounts for testing and log in function
listAccounts.append(ionut)
listAccounts.append(mihai)

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
# I wanted the function to keep promting you for a username or a password until you log in.
def login():
    # boolean variable used to enter the loop
    loggedIn=False
    # boolean used to enter the loop for username. I used it also to not print "Invalid Username" for each of the accounts being iterated.
    foundUsername=False
    # initialize a new account so i can give it the value of i(the account found with the username required) in the next for loop, and use it outside of the loop
    account=Account.Account("","","","",0,0)

    while loggedIn==False:
        usernameEntered=input("Please enter your username: ")
        if usernameEntered=="finished":
                break
        for i in listAccounts:
            if usernameEntered==i.username:
                foundUsername=True
                account=i
                break
            else:
                foundUsername=False
        
        if foundUsername==True:
            password=input("Please enter your passoword: ")
            if password=="finished":
                break
            if password==account.password:
                print("Log In Successfull!")
                return account
            else:
                print("Invalid Password!")
        elif foundUsername==False:
            print("Invalid Username!")

# this function finds an account that the account you are logged onto can make transactions with. 
def accountFinder():
    try:
        accountFinder=int(input("What account do you want to use?: "))
        for i in listAccounts:
            if accountFinder==i.accountNumber:
                return i
            else:
                return -1
    except:
        print("Invalid input!")
        return -1
        
#deposit function changes the value of the credit to the one you had minus the amount from input
def withdraw(account):
    try:
        withdrawAmount=int(input("How much money would you like to withdraw?: "))
        if withdrawAmount<=account.credit:
            account.credit-=withdrawAmount
            print("You have withdrawn: "+str(withdrawAmount)+
                "RON and your credit is: "+str(account.credit)+"RON.")
        else:
            print("Insufficient funds!")
    except:
        print("Invalid Input!")

#deposit function changes the value of the credit to the one you had plus the amount from input
def deposit(account):
    try:
        depositAmount=int(input("How much money would you like to deposit?: "))
        account.credit += depositAmount
        print("You have deposited: "+str(depositAmount)+
            "RON and your credit is now :"+str(account.credit)+"RON.")
    except:
        print("Invalid input")

# transfer function deducts the amount from the account you are transfering, and adds it to the one, you are transfering to
def transfer(account1,account2):
    try:
        transferAmount=int(input("How much money would you like to transfer?: "))    
        if transferAmount<=account1.credit:
            account1.credit -= transferAmount
            account2.credit += transferAmount
            print(account2.credit)
            print("You have transfered: "+str(transferAmount)+"RON to the account: "
                +str(account2.accountNumber)+ "\n Your remaining balance is now : "+
                str(account1.credit)+"RON.")
        else:
            print("Insufficient funds!")
    except:
        print("Invalid input")   
# this function enables you to make transations with the account that you are logged into and also transfer money to other accounts
def transactions():
    finishedTransactions=False
    accountToBeUsed=login()
    
    while(finishedTransactions==False):
        #promt the user to select an action to be made with the account he is logged into
        action=input("What would you like to do?: \n1. Whitdraw\n2. Deposit\n3.Transfer\n")
        # check for users transaction choice from input
        if action=="1":
            withdraw(accountToBeUsed)
        elif action=="2":
            deposit(accountToBeUsed)
        elif action=="3":
            #uses the accountFound() function to find an account in the list made of Account Objects to add the amount to.
            accountFound=accountFinder()
            if accountFound==-1:
                print("There is no such account number")
                continue
            transfer(accountToBeUsed,accountFound)
        elif action=="Finish" or action=="0" or action=="finish":
            break
        else:
            print("There is no such choice in the list!")