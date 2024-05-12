# import sys

# print(sys.path)
# sys.path.append('D:\\')
# print(sys.path)

# import sub
# sub.sample_a()
# class_a = sub.ClassA()
# class_a.print_a()
# print(sub.VAR)


# from sub import sample_a
# sample_a()

# from sub import sample_a as sa, ClassA as ca

# sa()

# ins = ca()
# ins.print_a()

# from sub import *

# print(VAR)
# sample_a()

# import dir1.base1 as base1
# base1.print_msg()

# import dir1.base2 as base2
# base2.print_msg()

# from dir1.base1 import print_msg as base1_print
# from dir1.base2 import print_msg as base2_print

# base1_print()
# base2_print()

# from dir1 import *

# base1.print_msg()
# base2.print_msg()

from dir1 import *
from dir1 import base1_msg

base1_msg()
base2_msg()

#from math import round