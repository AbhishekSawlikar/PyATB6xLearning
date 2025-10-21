# You receive an API response code from your test script.
# Write an if-else block to check whether the response is successful (status code 200) or not.
#
# I/P response = 404 , O/P ❌ Failed API Request
# I/P response = 200 , O/P ✅ Passed API Request

code = int(input("Enter the code: "))

if code == 200:
    print("O/P ✅ Passed API Request")
elif code == 404:
    print("O/P ❌ Failed API Request")
else:
    print("Enter correct code")