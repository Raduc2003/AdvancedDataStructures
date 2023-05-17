from MaxHeap import *
import sys
 
sys.stdout=  open('AdvancedDataStructures/MaxHeap/result.out', 'w')
f = open("AdvancedDataStructures\MaxHeap\input.in")

n=int(f.readline())
heap = MaxHeap()
for i in range(n):
    l =f.readline().split(" ")
    if len(l)==2:
        c,a=[int(x) for x in l]
    else:
        c,a,b=[int(x) for x in l]
    if c==1:
        tree.insert(a)
    if c==2:
        tree.remove(a)
    if c==3:
        r = tree.findKey(a)
        if(r):
            print(1)
        else: print(0)

# def compare_files(file1, file2):
#     with open(file1, 'r') as f1, open(file2, 'r') as f2:
#         lines1 = f1.readlines()
#         lines2 = f2.readlines()

#     if lines1 == lines2:
#         print("OK")
#     else:
#         for line_num, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
#             if line1 != line2:
#                 print(f"Difference found at line {line_num}:")
#                 print(f"File 1: {line1.strip()}")
#                 print(f"File 2: {line2.strip()}")
#                 break

# file1 = "AdvancedDataStructures/BinarySearchTree/result.out"
# file2 = "AdvancedDataStructures/BinarySearchTree/grader_test9.ok"
# sys.stdout = sys.__stdout__
# compare_files(file1, file2)