# Question 2 : An API sometimes fails due to network delays.

# Write a program to retry the API call 3 times until the response code becomes 200.
# If it still fails after 3 tries, print a failure message.

# Hint: Use a while loop with a counter.

# Expected Output Example:
# Attempt 1: Response 500
# Attempt 2: Response 200
# ✅ Test Passed

# response_code = int(input("Enter response Code: "))
# if response_code == 200:
#     print(f"The response code is {response_code}\n"
#           f"✅ Test Passed")
# elif response_code != 200:
#     for i in range(1,4):
#         if response_code != 200:
#             print(f"The response code is {response_code}\n"
#                   f"Retrying......{i}")
#             response_code = int(input("Enter response code again: "))
#
#         else :
#             print(f"The response code is {response_code}\n"
#                   f"✅ Test Passed")

response_code = int(input("Enter response Code: "))
if response_code == 200:
    print(f"The response code is {response_code}\n"
          f"✅ Test Passed")
else:
    i = 1
    print("Response code not matched.\n"
          "Reattempting start.........")
    while response_code != 200 and i < 3:

        if response_code == 200:
            print(f"The response code is {response_code}\n"
                  f"✅ Test Passed")
        else:
            print(f"Attempt {i} failed: Response {response_code}")
            print("-" * 100)
            i = i + 1
            response_code = int(input("Enter response code again: "))


    if response_code == 200:
        print(f"The response code is {response_code}\n"
              f"✅ Test Passed")
    else:
        print(f"All the 3 attempts failed.\n"
              f"❌ Test Failed")