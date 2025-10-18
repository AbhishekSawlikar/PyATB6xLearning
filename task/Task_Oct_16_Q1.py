# You receive an API response code from your test script.
# Write an if-else block to check whether the response is successful (status code 200) or not.
#
# I/P response = 404 , O/P ❌ Failed API Request
# I/P response = 200 , O/P ✅ Passed API Request

response = int(input("Enter the response code:"))

if response < 0:
    print("⚠️ Invalid input! Response code cannot be negative.")
elif response > 599:
    print("⚠️ Invalid input! Response code exceeds standard HTTP range (0–599).")
elif response== 200:
    print("Pass the API request ✅")
else:
    print("Failed API Request ❌ ")