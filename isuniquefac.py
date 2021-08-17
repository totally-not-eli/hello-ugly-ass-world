"""
This code will show the all the combinations of integer came across with such that when its individual factorial is taken, it will be equal to the integer given.

e.g.
1 = 1!
145 = 1! + 4! + 5!
"""

import keyboard

class Stack:
    def __init__(self):
        self.stack = ["1"]
    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
    def peek(self):     
        return self.stack[-1]
    def len(self):
        return len(self.stack)

def fac(n):
    if n >= 0 and n <= 1:
        return 1
    else:
        return n*fac(n-1)

def iscount(count):
    if str(count)[-1] == "1":
        print("this is the {}st iteration".format(count))
    elif str(count)[-1] == "2":
        print("this is the {}nd iteration".format(count))
    elif str(count)[-1] == "3":
        print("this is the {}rd iteration".format(count))
    else:
        print("this is the {}th iteration".format(count))

def isuniquefac():
    lis = Stack()
    ans = []
    count = 0
    while True:
        i = lis.peek()
        hold = 0 
        count += 1
        for c in i:
            hold += fac(int(c))
        if hold == int(i):
            print("{} is actually a unique factorial, check it :)".format(i))
            iscount(count)
            ans.append(hold)
            lis.add(str(int(i)+1))
        else:
            iscount(count)
            lis.add(str(int(i)+1))
        print("Made {} iterations, here are the values that suits the value for unique factorial {}".format(lis.len(),ans))