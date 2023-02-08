import sys
from itertools import combinations
import numpy as np
import os
import re
import time
import matplotlib.pyplot as plt
import sys
import time

import argparse
import sys
a = len(sys.argv)
print("Total Command line arguments passed are:", a)
print("\nArguments that were passed:", end = "")
print("\nName of library:", sys.argv[0])
for x in range(1, a):
    print(sys.argv[x], end = "")
Sum = 0
#for y in range(1, a):
#    Sum += int(sys.argv[y])
print("\n\nResult:", Sum)


#print("hello")
# sys.stdout.write('Hello')
#
# parser = argparse.ArgumentParser()
# parser.add_argument("-a", required=True, type=str,
#                     help="algorithme choisi")
# parser.add_argument("-e1", required=True, type=str,
#                     help="path vers e1")
# parser.add_argument("-e2", required=True, type=str,
#                     help="path vers e2")
# parser.add_argument("-p",
#                     help="affiche la matrice résultat")
# args = parser.parse_args()
# sys.stdout.write('Hello')
# print(args)
# argument = sys.argv[1:]
# #print(argument)
#
# time.sleep(5)
#
#
#
