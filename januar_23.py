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
            for j in range(len(strs) - 1):
                if strs[j][i] > strs[j + 1][i]:
                    count += 1
                    break
        return count


strs = ["cba", "daf", "ghi"]
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


list1 = [1, 2, 4]
list2 = [1, 3, 4]
print(Solution().mergeTwoLists(list1, list2))
# Output: [1,1,2,3,4,4]

'''
На вход программе подается два натуральных числа aa и bb (a < ba< b). Напишите программу, которая находит все простые числа от aa до bb включительно.

Формат входных данных
На вход программе подаются два числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести все простые числа от aa до bb включительно, каждое на отдельной строке.

Примечание. Число 11 простым не является.
'''
a = int(input())
b = int(input())
for i in range(a, b + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
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
costs = [1, 3, 2, 4, 1]
# Output: 4
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


nums = [3, 2, 2, 3]
val = 3
print(Solution().removeElement(nums, val))
# Output: 2, nums = [2,2]

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


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(Solution().canCompleteCircuit(gas, cost))


# Output: 3

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


points = [[1, 1], [2, 2], [3, 3]]
print(Solution().maxPoints(points))
# Output: 3
points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
print(Solution().maxPoints(points))
# Output: 4

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


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))
# Output: 5


'''
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 

'''


class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        res = 0
        for i in range(len(columnTitle)):
            res = res * 26 + ord(columnTitle[i]) - ord('A') + 1
        return res


columnTitle = "A"
print(Solution().titleToNumber(columnTitle))
# Output: 1
columnTitle = "AB"
print(Solution().titleToNumber(columnTitle))
# Output: 28

'''
Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. 
You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect 
all apples in the tree, starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge 
connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that 
vertex i has an apple; otherwise, it does not have any apple.
 
'''


class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        rian = [[] for _ in range(n)]
        for i, j in edges:
            rian[i].append(j)
            rian[j].append(i)

        def dabl(i, par):
            temp = 0
            for children in rian[i]:
                if (children != par):
                    temp += dabl(children, i)
            if ((temp > 0 or hasApple[i]) and par != -1):
                temp += 2
            return temp

        return dabl(0, -1)


n = 7
edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
hasApple = [False, False, True, False, True, True, False]
print(Solution().minTime(n, edges, hasApple))
# Output: 8

'''
You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature in Celsius.

You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].

Return the array ans. Answers within 10-5 of the actual answer will be accepted.

Note that:

Kelvin = Celsius + 273.15
Fahrenheit = Celsius * 1.80 + 32.00
'''


class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        return [celsius + 273.15, celsius * 1.80 + 32.00]


'''
Вам дано дерево (т. е. связный неориентированный граф, не имеющий циклов), состоящее из n узлов, пронумерованных от 0 до
n - 1 и ровно n - 1 ребер. Корнем дерева является узел 0, и каждый узел дерева имеет метку, которая представляет собой
символ нижнего регистра, заданный в метках строки (т. е. узел с номером i имеет метку labels[i]).
Массив ребер задается в виде ребер [i] = [ai, bi], что означает наличие ребра между узлами ai и bi в дереве.
Возвращает массив размера n, где ans[i] — количество узлов в поддереве i-го узла, имеющих одинаковую метку.
как узел я.
Поддерево дерева T — это дерево, состоящее из узла T и всех его узлов-потомков.
'''

from collections import defaultdict, Counter
class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
                :type n: int
                :type edges: List[List[int]]
                :type labels: str
                :rtype: List[int]
                """
        tree = defaultdict(list)
        for s, e in edges:
            tree[s].append(e)
            tree[e].append(s)

        dog = [0] * n

        def cat(node, par):
            nonlocal dog
            count = Counter()
            for nei in tree[node]:
                if nei != par:
                    count += cat(nei, node)

            count[labels[node]] += 1
            dog[node] = count[labels[node]]

            return count

        cat(0, -1)
        return dog


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # Построим дерево, используя ребра.
        # Поскольку дерево не ориентировано, нам нужно добавить в дерево оба направления.
        tree = defaultdict(list)
        for s, e in edges:
            tree[s].append(e)
            tree[e].append(s)

        # Результат длины n будет возвращен в конце.
        # Он модифицируется в файле dog.
        dog = [0] * n

        # node текущий node мы изучаем.
        # par является прямым родительским узлом узла.
        def cat(node, par):
            nonlocal dog
            # Использовать count для хранения количества каждой буквы в поддереве с корнем в текущем узле.
            # Размер этой хэш-карты (количество) будет не более 26,
            # Поскольку существует не более 26 строчных английских букв
            count = Counter()
            for nei in tree[node]:
                # Убедиться, что мы не возвращаемся к его родительскому узлу.
                if nei != par:
                    # Обновить счетчик с частотой букв в дочерних узлах
                     #Это то же самое, что пройти от a до z и увеличить частоту каждой буквы.
                    count += cat(nei, node)

            # Добавление 1 к счету с текущей меткой
            count[labels[node]] += 1
            # Обновить результат.
            dog[node] = count[labels[node]]

            return count

        # Начиная с узла 0, и назначить для него фальшивый родитель -1.
        cat(0, -1)
        return dog

'''
Вам дано большое целое число, представленное в виде целочисленного массива цифр, где каждая цифра[i] — это i-я цифра целого числа.
Цифры упорядочены от наиболее значащего к наименее значащему в порядке слева направо. Большое целое число не содержит ведущих нулей.

Увеличьте большое целое число на единицу и верните результирующий массив цифр.
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        i = 10 ** (len(digits) - 1)
        for x in range(0, len(digits)):
            num = num + digits[x] * i
            i = i / 10
        num += 1
        digits = list(map(int, str(num)))
        return digits

    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        digits.append(0)
        digits[0] = 1
        return digits

'''

'''

class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
nums = [1,1,2]
print(Solution().removeDuplicates(nums))
'''
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
'''
class Solution:
    def findJudge(self, n, trust):
        if n == 1:
            return 1
        trust_dict = {}
        for i in range(1, n + 1):
            trust_dict[i] = 0
        for i in trust:
            trust_dict[i[0]] -= 1
            trust_dict[i[1]] += 1
        for i in trust_dict:
            if trust_dict[i] == n - 1:
                return i
        return -1
n = 3
trust = [[1,3],[2,3]]
print(Solution().findJudge(n, trust))

'''
Требуется написать регулярное выражение, которое находит все:

Слова, состоящие из кириллических символов, но в них есть как минимум 1 некириллический символ
Слова, состоящие из некириллических символов, но в них есть как минимум 1 кириллический символ
Слова, состоящие полностью из кириллических или некириллических символов игнорируем. Знаки препинания  странными символами не считаются.

Примеры:
Input 1:
О, х0т табc. A что такое табс? Я зашéл нe туда, кyда н4до. Почему это твич не 3абанил - не совсем понятно. Господа, я полагаю стрим надо быстро заканчивать, и удалять...
Output 1:
х0т табc зашéл нe кyда н4до 3абанил
Input 2:
Я в шkaфy пpячycь.
Output 2:
шkaфy пpячycь
Input 3:
Бpо, тeбe нaд0 тp3нирÖвÆтьçя.
Output 3:
Бpо тeбe нaд0 тp3нирÖвÆтьçя
Input 4:
Нacтaл0 ßремя бросить 3aгaд0чный взгляд B мек©иканской шляпe и начать план $cаm.
Output 4:
Нacтaл0 ßремя 3aгaд0чный мек©иканской шляпe $cаm
'''
import re
s = input()

