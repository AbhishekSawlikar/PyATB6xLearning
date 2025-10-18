#Check if the user can log in based on correct username and password.
#I/p
#username = "admin"
#password = "1234"
#O/p ✅ Login Successful
#For the Fail condition Other O/P = ❌ Invalid Credentials

stored_username = "admin"
stored_password = "1234"

username= input("Please enter the username: ".strip())
password= input("Please enter the password: ".strip())

if not username or not password:
    print("⚠️ Invalid input! Username or password cannot be blank.")

elif username.lower() != stored_username.lower():
    print("❌ Incorrect Username")
elif password != stored_password:
    print("❌ Incorrect Password")
else:
    print("The username and password are matched and user logged in")