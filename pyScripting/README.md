# useful_py_scripts
some useful py script that perform certain task


### Two Sum Closest, (binary search logic)
```
import math

def findTwoSumClosest(nums, target):
    min_diff = (math.inf, -1, -1)

    nums.sort()
    start = 0
    end = len(nums) - 1

    while start < end:
        summ = nums[start] + nums[end]
        diff = abs(summ - target)
        if diff < min_diff[0]:
            min_diff = (diff, nums[start], nums[end])

        if summ > target:
            end -= 1
        if summ < target:
            start += 1
    return [min_diff[1], min_diff[2]]

```


### Fibonacci
```
def Fibonacci(n):
   
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
# Driver Program
print(Fibonacci(9))
```
factorial
```
def factorial(n): 
      
    if (n==1 or n==0):
        return 1
    else:
        return (n * factorial(n - 1)) 
        
```
