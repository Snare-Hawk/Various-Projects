"""
Collatz Conjecture - Start with a number n > 1. Find the number of steps it takes to reach one using the following process: 
If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
"""
def countSteps(num, stepNum):
    if num == 1:
        return stepNum
    if num % 2 == 0:
        stepNum = countSteps(num / 2, stepNum + 1)
    else:
        stepNum = countSteps(3 * num + 1, stepNum + 1)
    return stepNum

print("Please input a number: ", end="")
num = input()

print(f"Using the Collatz Conjecture, it would take {countSteps(int(num), 0)} steps to reach one.")