from Operations import createAccount,transactions


answer=int(input("Hello! To be able to make transactions you need an account\n"+
          "1.Log In\n"+"2.Create a new account\n"))
if answer==1:
    transactions()
elif answer==2:
    createAccount()
    transactions()
else:
   print("Invalid input!")
