#You want to check whether a web page loads within 3 seconds (performance test condition).
#load_time = 4.2
# ⚠️ Page load too slow: 4.2 seconds

load_time=float(input("Enter the load time:").strip())

if load_time <= 0:
    print("Please enter valid load time")
elif load_time <= 3:
    print("Page loads properly")
else:
    print("⚠️ Page load too slow")