#Reverse an Array
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(arr[::-1])
#Count Even and Odd Numbers
import numpy as np
arr = np.array([10, 15, 20, 25, 30, 35])
even = 0
odd = 0
for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even =", even)
print("Odd =", odd)
#Search an Element
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
num = int(input("Enter number: "))
if num in arr:
    print("Element Found")
else:
    print("Element Not Found")
#Find the Index of the Largest Element
import numpy as np
arr = np.array([15, 25, 80, 40, 60])
print("Index =", np.argmax(arr))
#Remove Duplicate Elements
import numpy as np
arr = np.array([10, 20, 20, 30, 40, 40, 50])
print(np.unique(arr))