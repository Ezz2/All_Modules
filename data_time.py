# By  Ezz

# -----------------------------------
# -- Date And Time => Introduction --
# -----------------------------------

import datetime as d

# print(dir(datetime))
# print(dir(datetime.datetime))

# Print Current Date And Time

print(d.datetime.now())

print("_" * 10)

# Print Current Year, month, day, today

print(d.date.today())
print(d.datetime.now().year)
print(d.datetime.now().month)
print(d.datetime.now().day)

print("_" * 10)

# Print Start And End Of Date

print(d.datetime.min)
print(d.datetime.max)

print("_" * 10)

# Print The Current Time
print(d.datetime.now().time())

# Print the Current Time Hour, Minute, Second
print(d.datetime.now().time().hour)
print(d.datetime.now().time().minute)
print(d.datetime.now().time().second)

print("_" * 10)

# Print Start And End Of Time

print(d.time.min)
print(d.time.max)

print("_" * 10)

# Print Specific Date

print(d.datetime(2006, 10, 21))
print(d.datetime(2006, 10, 21, 10, 45, 55, 134846))

print("_" * 10)

myBirthday = d.datetime(2006, 10, 20)
nowDate = d.datetime.now()

print(f"My Birthday is {myBirthday} And ", end="")
print(f"Date Now is {nowDate}")

print(f"I Lived For {nowDate - myBirthday} Days")
print(f"I Lived For {(nowDate - myBirthday).days } Days")

print("_" * 50)

# ----------------------------------
# -- Date And Time => Format Date --
# ----------------------------------
# https://strftime.org/
# ---------------------

myBirthday = d.datetime(2006, 10, 20)

print(myBirthday.strftime("%a"))
print(myBirthday.strftime("%A"))
print(myBirthday.strftime("%b"))
print(myBirthday.strftime("%B"))

print("_" * 10)

print(myBirthday.strftime("%d %B %Y"))
print(myBirthday.strftime("%d, %B, %Y"))
print(myBirthday.strftime("%d/%B/%Y"))
