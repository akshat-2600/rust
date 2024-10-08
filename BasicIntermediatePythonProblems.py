
# Basic level :
'''Q1 Write a Python program to print the numbers from 1 to 10 using a `for` loop.'''

for i in range(1,11) :
    print(i)
1
2
3
4
5
6
7
8
9
10
'''Q2 Create a program that calculates the sum of all numbers in a list using a `for` loop.'''

lst = eval(input("Enter a list :"))
sum = 0
for i in lst :
    sum += i
print("Sum of all numbers in list :", sum)
Sum of all numbers in list : 55
'''Q3 Write a program to print the characters of a string in reverse order using a `for` loop.'''

string = input("Enter a string ")
for char in string[::-1] :
    print(char)
s
l
l
i
k
S
 
w
P
'''Q4 Develop a program that finds the factorial of a given number using a `for` loop.'''

def fact_num(n) :
    product = 1
    if 0 <= n <= 1 :
        return 1
    else :
        for i in range(2,n+1) :
            product *= i
        return product
    
n = int(input("Enter a number :"))
factorial = fact_num(n)
print("Factorial of ",n ,": ", factorial)
Factorial of  7 :  5040
'''Q5 Create a program to print the multiplication table of a given number using a `for` loop.'''

n = int(input("Enter number for which you want multiplication table :"))
for i in range(1,11) :
    print(f"{n} x {i} = {n*i}")
19 x 1 = 19
19 x 2 = 38
19 x 3 = 57
19 x 4 = 76
19 x 5 = 95
19 x 6 = 114
19 x 7 = 133
19 x 8 = 152
19 x 9 = 171
19 x 10 = 190
'''Q6 Write a program that counts the number of even and odd numbers in a list using a `for` loop.'''

count_even = 0
count_odd = 0
lst = eval(input("Enter a list :"))
for i in lst :
    if i%2 == 0 :
        count_even += 1
    if i%2 != 0 :
        count_odd += 1
print("Number of odd numbers in list :", count_odd)
print("Number of even numbers in list :", count_even)
Number of odd numbers in list : 6
Number of even numbers in list : 6
'''Q7 Develop a program that prints the squares of numbers from 1 to 5 using a `for` loop.'''

print("Squares of numbers from 1 to 5 :")
for i in range(1,6) :
    print(i**2)
Squares of numbers from 1 to 5 :
1
4
9
16
25
'''Q8 Create a program to find the length of a string without using the `len()` function.'''

length = 0
string = input("Enter a string :")
for i in string :
    length += 1
    
print("Length of string :", length)
Length of string : 13
'''Q9 Write a program that calculates the average of a list of numbers using a `for` loop.'''

sum = 0
lst = eval(input("Enter a list :"))
for i in lst :
    sum += i
    
avg = sum/len(lst)
print("Average of list of numbers :", avg)
Average of list of numbers : 5.5
'''Q10 Develop a program that prints the first `n` Fibonacci numbers using a `for` loop.'''

a,b = 0,1   #initializing 1st two fibonacci numbers
n = int(input("Enter number of Fibonacci numbers you want :"))
print("First", n ,"Fibonacci numbers :")
for i in range(n) :
    print(a)
    a,b = b,a+b
First 10 Fibonacci numbers :
0
1
1
2
3
5
8
13
21
34
 
# Intermediate Level:
'''Q11 Write a program to check if a given list contains any duplicates using a `for` loop.'''

lst = eval(input("Enter a list :"))
new_lst = []
for i in lst :
    if i in new_lst :
        print("Given list contains duplicate entries")
        break
    else :
        new_lst.append(i)
else :
    print("Given list does not have any duplicate entries")
Given list contains duplicate entries
'''Q12 Create a program that prints the prime numbers in a given range using a `for` loop.'''

def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1) :
        if num % i == 0 :
            return False
    return True

a = int(input("Enter uppper limit of range :"))
b = int(input("Enter lower limit of range :"))
print(f"Prime numbers in range({a},{b}) :")

for i in range(a,b+1) :
    if check_prime(i) :
        print(i)
Prime numbers in range(50,100) :
53
59
61
67
71
73
79
83
89
97
'''Q13 Develop a program that counts the number of vowels in a string using a `for` loop.'''

count_vowel = 0
string = input("Enter a string :")
for char in string :
    if char.lower() in ["a","e","i","o","u"] :
        count_vowel += 1
print("Number of vowels in string :", count_vowel)
Number of vowels in string : 8
'''Q14 Write a program to find the maximum element in a 2D list using a nested `for` loop.'''

lst_nested = eval(input("Enter a 2D list :"))   
max_lst = []                                    #candidates for maximum value list
for lst in lst_nested :
    
    if type(lst) == type([]) :
        max_lst.append(max(lst))
    else :
        max_lst.append(lst)

max_num = max(max_lst)
print("Maximum element in 2D list :", max_num)        
Maximum element in 2D list : 6785
'''Q15 Create a program that removes all occurrences of a specific element from a list using a `for` loop.'''

lst = eval(input("Enter a list :"))
new_lst = lst.copy()
element = int(input("Enter element which you want to remove :"))
for i in new_lst :
    if i == element :
        lst.remove(i)
print(f"List after removing {element} : {lst}")       
List after removing 1 : [2, 3, 4, 5, 3, 4, 7, 8, 9, 8, 9, 80]
'''Q16 Develop a program that generates a multiplication table for numbers from 1 to 5 using a nested 
       `for` loop.'''

for num in range(1,6) :
    print(f"Multiplication Table of {num} :")
    for ele in range(1,11) :
        print(f"{num} x {ele} = {num*ele}")
Multiplication Table of 1 :
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
1 x 6 = 6
1 x 7 = 7
1 x 8 = 8
1 x 9 = 9
1 x 10 = 10
Multiplication Table of 2 :
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
Multiplication Table of 3 :
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
Multiplication Table of 4 :
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40
Multiplication Table of 5 :
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
'''Q17 Write a program that converts a list of Fahrenheit temperatures to Celsius using a `for` loop.'''

fah_list = eval(input("Enter a Fahrenheit temperatures list :"))
cel_list = []

for fah_temp in range(len(fah_list)) :
    cel_temp = (fah_temp - 32) * (5/9)
    cel_list.append(cel_temp)
    
print("List of Celsius Temperatures :", cel_list)
List of Celsius Temperatures : [-17.77777777777778, -17.22222222222222, -16.666666666666668, -16.11111111111111, -15.555555555555557, -15.0]
'''Q18 Create a program to print the common elements from two lists using a `for` loop.'''

lst_1 = eval(input("Enter 1st list :"))
lst_2 = eval(input("Enter 2nd list :"))
new_lst = []
print("Common elements between two lists :")
for i in lst_1 :
    for j in lst_2 :
        if i == j :
            if i in new_lst :
                continue
            else :
                new_lst.append(i)
if len(new_lst) == 0 :
    print("No element is common")
for i in new_lst :
    print(i)
Common elements between two lists :
2
4
6
8
10
'''Q19 Develop a program that prints the pattern of right-angled triangles using a `for` loop. Use ‘*’ to draw the
pattern.'''

n = int(input("For how many rows you want to expand right angle triangle :"))
for i in range(1,n+1) :
    for j in range(i) :
        print("*" , end = "")
    print()
*
**
***
****
*****
******
*******
********
*********
**********
'''Q20 Write a program to find the greatest common divisor (GCD) of two numbers using a `for` loop.'''

from functools import reduce 

num_1 = int(input("Enter 1st number :"))
num_2 = int(input("Enter 2nd number :"))
a = num_1
num_1_lst = []
b = num_2
num_2_lst = []
common_factors_lst = []

for i in range(1,num_1 + 1) :
    if a%i == 0 :
        num_1_lst.append(i)

for j in range(1,num_2 + 1) :
    if b%j == 0 :
        num_2_lst.append(j)
        

common_lst = []
for ele_1 in num_1_lst :
    for ele_2 in num_2_lst :
        if ele_1 == ele_2 :
            if ele_1 in common_factors_lst :
                continue
            else :
                common_factors_lst.append(ele_1)
gcd = max(common_factors_lst)
print(f"GCD of {num_1} & {num_2} : {gcd}")
GCD of 56 & 78 : 2
