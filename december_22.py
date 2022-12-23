'''
Given an array of integers nums and an integer target, return indices of the two numbers such that
they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Учитывая массив целых чисел nums и целочисленную цель, вернуть индексы двух чисел так, чтобы они складывались в цель.
Вы можете предположить, что каждый вход будет иметь ровно одно решение,
и вы не можете использовать один и тот же элемент дважды. Вы можете вернуть ответ в любом порядке.
'''


class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))
# Output: [0,1]
nums = [3, 2, 4]
target = 6
print(Solution().twoSum(nums, target))
# Output: [1,2]
nums = [3, 3]
target = 6
print(Solution().twoSum(nums, target))
# Output: [0,1]

'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not,
return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
Учитывая отсортированный массив различных целых чисел и целевое значение, верните индекс, если целевое значение найдено.
Если нет, верните индекс туда, где он был бы, если бы он был вставлен по порядку.
Вы должны написать алгоритм с O(log n) сложностью во время выполнения.
'''


class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
        return len(nums)


nums = [1, 3, 5, 6]
target = 5
print(Solution().searchInsert(nums, target))
# Output: 2
nums = [1, 3, 5, 6]
target = 2
print(Solution().searchInsert(nums, target))
# Output: 1
nums = [1, 3, 5, 6]
target = 7
print(Solution().searchInsert(nums, target))
# Output: 4
'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
Учитывая неотрицательное целое число x, верните квадратный корень из x, округленный в меньшую сторону до ближайшего целого числа. 
Возвращаемое целое число также должно быть неотрицательным.
Вы не должны использовать какую-либо встроенную функцию экспоненты или оператор.
Например, не используйте pow(x, 0.5) в c++ или x ** 0.5 в python.
'''


class Solution(object):
    def mySqrt(self, x):
        return int(x ** 0.5)


x = 4
print(Solution().mySqrt(x))
# Output: 2
x = 8
print(Solution().mySqrt(x))
# Output: 2

'''
You are given two arrays of integers nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.
Combine nums1 and nums2 into one array, sorted in non-decreasing order.
The final sorted array should not be returned by the function, but should be stored inside the nums1 array.
To accommodate this, nums1 is m + n long, where the first m elements denote the elements to be concatenated,
and the last n elements are set to 0 and should be ignored. nums2 has length n.

'''


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[:] = sorted(nums1[:m] + nums2)


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
Solution().merge(nums1, m, nums2, n)
print(nums1)
# Output: [1,2,2,3,5,6]
nums1 = [1]
m = 1
nums2 = []
n = 0
Solution().merge(nums1, m, nums2, n)
print(nums1)
# Output: [1]

'''
Последовательность n-битного кода Грея представляет собой последовательность из 2n целых чисел, где:
Каждое целое число находится в инклюзивном диапазоне [0, 2n - 1],
Первое целое число равно 0,
Целое число встречается в последовательности не более одного раза,
Двоичное представление каждой пары смежных целых чисел отличается ровно на один бит, и
Двоичное представление первого и последнего целых чисел отличается ровно на один бит.
Учитывая целое число n, вернуть любую допустимую n-битную последовательность кода Грея.
'''


class Solution(object):
    def grayCode(self, n):
        return [i ^ (i >> 1) for i in range(2 ** n)]


n = 2
print(Solution().grayCode(n))
# Output: [0,1,3,2]
n = 1
print(Solution().grayCode(n))
# Output: [0,1]


'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''


class Solution(object):
    def isSymmetric(self, root):
        def isMirror(t1, t2):
            if not t1 and not t2: return True
            if not t1 or not t2: return False
            return (t1.val == t2.val) and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)

        return isMirror(root, root)


root = [1, 2, 2, 3, 4, 4, 3]
print(Solution().isSymmetric(root))
# Output: True
# root = [1,2,2,null,3,null,3]
# print(Solution().isSymmetric(root))
# Output: False

'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
'''


class Solution(object):
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)


nums = [2, 2, 1]
print(Solution().singleNumber(nums))
# Output: 1
nums = [4, 1, 2, 1, 2]
print(Solution().singleNumber(nums))
# Output: 4


''''
Решите уравнение в натуральных числах 28n + 30k + 31m = 365.
Примечание. Используйте вложенный цикл for. В первую очередь запишите решение с наименьшим значением n.
'''
for n in range(1, 100):
    for k in range(1, 100):
        for m in range(1, 100):
            if 28 * n + 30 * k + 31 * m == 365:
                print(n, k, m)
                break


'''
Имеется 100 рублей. Сколько быков, коров и телят можно купить на все эти деньги, если плата за быка – 10 рублей, 
за корову – 5 рублей, за теленка – 0.5 рубля и надо купить 100 голов скота?
Примечание. Используйте вложенный цикл for.
'''
for b in range(1, 100):
    for c in range(1, 100):
        for t in range(1, 100):
            if b + c + t == 100 and b * 10 + c * 5 + t * 0.5 == 100:
                print(b, c, t)
                break
'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
'''
class Solution(object):
    def getRow(self, rowIndex):
        res = [1]
        for i in range(rowIndex):
            res = [x + y for x, y in zip([0] + res, res + [0])]
        return res
rowIndex = 3
print(Solution().getRow(rowIndex))
# Output: [1,3,3,1]
rowIndex = 0
print(Solution().getRow(rowIndex))
# Output: [1]
rowIndex = 1
print(Solution().getRow(rowIndex))
# Output: [1,1]

'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that 
adding up all the values along the path equals targetSum.
A leaf is a node with no children.
'''
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
        return self.hasPathSum(root.left, hasPathSum - root.val) or self.hasPathSum(root.right, hasPathSum - root.val)
'''
Given two binary strings a and b, return their sum as a binary string.
'''
class Solution(object):
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]
a = "11"
b = "1"
print(Solution().addBinary(a, b))
# Output: "100"
a = "1010"
b = "1011"
print(Solution().addBinary(a, b))
# Output: "10101"


