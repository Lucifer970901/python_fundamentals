#-----------1 way---------
'''import welcome
welcome.welcome_all()'''

# if you want to import specific function
'''from welcome import add
x = add (4,5)
print(x)'''
#if you want to import all the functions 
'''from welcome import *
x = add(2,9)
welcome_all()
print(x)'''

#import functions from different files test.py and test2.py
'''from test1 import *
from test2 import *
test() #takes the test2.py contents'''

#to prevent the overlapping
'''import test1 as t1

import test2 as t2

t1.test()'''

#import from subfolder
import sub_folder.test3 as t3
print(t3.multiply(2,3))

