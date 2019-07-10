
# 1. Write a Python program to sum all the items in A, A = [5, 8, 15, 7, 3]

count = 0
A = [5, 8, 15, 7, 3]
for x in A :
    count += x
print(x,sum)

#2 Months = ['January', 'February', 'DSN', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November']


# 2.1. Write a Python program to  Get Months sorted in increasing order
# 2.2. Add **December** to months
# 2.3. Reverse elements of Months
# 2.4. remove/delete 'DSN' form months
    
               # Question 1 solution1

months = ['January', 'February', 'DSN', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November']

#Write a Python program to  Get Months sorted in increasing order

months[::-1]= months
print(months)

                #QUESTION 2 SOLUTION 2
months.append("Decemeber")
print(months)

            #QUESTION 3SOLUTION 3

months.reverse()
print(months)

                #QUESTION 4 SOLUTION 4

months.pop(3)
print (months)