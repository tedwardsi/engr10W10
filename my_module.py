import matplotlib.pyplot as plt
import numpy as np
import random 
#function that generates a plot given a function name and the range of x values
#The Chooser class from the OOP lecture
#solution to leetcode problem 

def generate_plot(f,r):
    y_values = f(r)
    plt.plot(r,y_values)
    plt.show()

class Chooser:
    def __init__(self,list = [1,2,3,4,5,6]):
        self._myList = list
        self._random = random.randint(0,len(self._myList) - 1)
    def get_value(self):
        return self._myList[self._random]
    def choose_item(self):
        self._random = random.randint(0,len(self._myList) - 1)
        return self._myList[self._random]

# Two-Sum leet code problem

def twoSum(nums, target):
    numAndIndex = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in numAndIndex:
            return[numAndIndex[complement],i]
        
        numAndIndex[num] = i 

if __name__ == "__main__":
    function = np.sin
    x_values = np.linspace(0,2*np.pi,20)
    generate_plot(function,x_values)
    c = Chooser()
    print(c.get_value())
    print(c.choose_item())
    print(twoSum([1,2,3,4,5,6,7],9))
