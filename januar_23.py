'''
You are given an array of n strings strs, all of the same length.
The strings can be arranged such that there is one on each line, making a grid. For example, strs = ["abc", "bce", "cae"] can be arranged as:
abc
bce
cae
You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted while column 1 ('b', 'c', 'a') is not, so you would delete column 1.
Return the number of columns that you will delete.
'''



class Solution:
    def minDeletionSize(self, strs):
        count = 0
        for i in range(len(strs[0])):
            for j in range(len(strs)-1):
                if strs[j][i] > strs[j+1][i]:
                    count += 1
                    break
        return count
strs = ["cba","daf","ghi"]
print(Solution().minDeletionSize(strs))

'''
We define the usage of capitals in a word to be right when one of the following cases holds:
All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.
'''
class Solution(object):
    def detectCapitalUse(self, word):
        if word.isupper() or word.islower() or word.istitle():
            return True
        else:
            return False
word = "USA"
print(Solution().detectCapitalUse(word))

'''
На вход программе подается натуральное число n. Напишите программу, которая находит цифровой корень данного числа. 
Цифровой корень числа nn получается следующим образом: если сложить все цифры этого числа, затем все цифры найденной 
суммы и повторить этот процесс, то в результате будет получено однозначное число (цифра), которое и называется цифровым 
корнем данного числа.
Формат входных данных
На вход программе подается одно натуральное число.
Формат выходных данных
Программа должна вывести цифровой корень введенного числа.
Примечание. Используйте вложенные циклы while.
'''
n = int(input())
while n > 9:
    n = sum(map(int, str(n)))
print(n)

'''
Дано натуральное число nn. Напишите программу, которая выводит значение суммы 1!+2!+3!+...+n!.
Формат входных данных
На вход программе подается одно натуральное число.
Формат выходных данных
Программа должна вывести значение суммы 1!+2!+3!+...+n!.
Примечание 1. Факториалом натурального числа nn, называется произведение всех натуральных чисел от 1 до n, то есть
n!=1⋅2⋅3⋅…⋅n
Примечание 2. Задачу можно решить без вложенного цикла. Напишите две версии программы =)
'''
n = int(input())
factorial = 1
sum = 0
for i in range(1, n + 1):
    factorial *= i
    sum += factorial
print(sum)

'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
'''
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
list1 = [1,2,4]
list2 = [1,3,4]
print(Solution().mergeTwoLists(list1, list2))
#Output: [1,1,2,3,4,4]

'''
На вход программе подается два натуральных числа aa и bb (a < ba< b). Напишите программу, которая находит все простые числа от aa до bb включительно.

Формат входных данных
На вход программе подаются два числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести все простые числа от aa до bb включительно, каждое на отдельной строке.

Примечание. Число 11 простым не является.
'''
a=int(input())
b=int(input())
for i in range(a,b+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)

'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''
class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


'''
It is a sweltering summer day, and a boy wants to buy some ice cream bars.

At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 

Return the maximum number of ice cream bars the boy can buy with coins coins.

Note: The boy can buy the ice cream bars in any order.
'''
from typing import List
class Solution:

    def maxIceCream(self, costs, coins):
        costs.sort()
        count = 0
        for i in costs:
            if coins >= i:
                coins -= i
                count += 1
            else:
                break
        return count

coins = 7
costs = [1,3,2,4,1]
#Output: 4
'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
'''

from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
nums = [3,2,2,3]
val = 3
print(Solution().removeElement(nums, val))
#Output: 2, nums = [2,2]

'''
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
'''
from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            if gas[i] >= cost[i]:
                tank = gas[i] - cost[i]
                j = (i + 1) % n
                while j != i:
                    tank += gas[j] - cost[j]
                    if tank < 0:
                        break
                    j = (j + 1) % n
                if j == i:
                    return i
        return -1
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(Solution().canCompleteCircuit(gas, cost))
#Output: 3

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_wer, curr_wer = 0, 0
        starting_station = 0
        for i in range(len(gas)):
            total_wer += gas[i] - cost[i]
            curr_wer += gas[i] - cost[i]

            if curr_wer < 0:
                starting_station = i + 1

                curr_wer = 0
        return starting_station if total_wer >= 0 else -1

'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.
'''
from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        res = 0
        for i in range(len(points)):
            d = {}
            same = 1
            for j in range(i + 1, len(points)):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    same += 1
                elif points[i][0] == points[j][0]:
                    d['inf'] = d.get('inf', 0) + 1
                else:
                    k = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                    d[k] = d.get(k, 0) + 1
            res = max(res, same + (max(d.values()) if d else 0))
        return res

points = [[1,1],[2,2],[3,3]]
print(Solution().maxPoints(points))
#Output: 3
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
print(Solution().maxPoints(points))
#Output: 4

'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - min_price)
        return max_profit
prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))
#Output: 5
