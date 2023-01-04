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
