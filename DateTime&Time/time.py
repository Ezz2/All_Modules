# By Ezz

import time

seconds = time.time()
print("Time Per Second:", seconds)

print("_" * 20)

seconds = time.time()
local_time = time.ctime(seconds)
print("Local time:", local_time)

print("_" * 20)

print("This Is Printed immediately")
time.sleep(2.4)
print("This Is Wait 2.4 Second Then Print")
