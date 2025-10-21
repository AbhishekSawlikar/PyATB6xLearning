# Question 3 : Simulate a page loading check using a while loop.
# If page_loaded becomes True within 5 seconds, print success; else timeout.
# Hint: Use a counter (like wait_time) and break condition.

import time
import random

print("Page loading started.....")
print("Timer started............")
i=5
a=True
while a:
    print(f"{i} sec remaining.....")
    i=i-1
    time.sleep(1)
    b = random.choice(range(0,5))
    if b == 0:
        print(f"✅Page successfully loaded! with a time loadtime of {5-i} seconds\n"
              "Page loading ended.....")
        a = False
    if b!=0 and i == 0:
        print(f"Time out \n")
        print("❌Page loading failed.....")
        a = False