import os, string
available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]


for x in available_drives:
    print(x)

from pathlib import Path
home = str(Path.home())
print(home)

import random

def key_gen():
    keylist = random.choice('abcdefghijklmnopqrstuvwxyz')
    return keylist

number = 0
list_item = ''
while number < 20:
    number = number + 1
    list_item = list_item + key_gen()

print(list_item)    
