import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
signs = "~`|•√π÷×¶∆£¢€¥^°={}\%©®™✓[]@#$_&-+()/*':;!?"
all = lower+upper+number+signs
print("Enter the length of your password.")
print("Short password is better to break.")
print("pls be sure your password is between 8-50")
length = int(input("Aravind@061==> ")

print("".join(random.sample(all,length)
