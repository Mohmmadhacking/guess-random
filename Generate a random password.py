import random
import string 
chars = "abcdefghigklmnopqrstuvwxyz"
charsl = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!@#$%^&*()_+-=[]{}|;':\",./<>"
all = chars + charsl + numbers + symbols

password = ''.join(random.choice(all) for i in range(25))

print(password)
