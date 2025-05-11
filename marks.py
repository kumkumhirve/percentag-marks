'''Q9: Write a program that accepts marks of five subjects
subject from user and calculate the total marks and then calculate
the percentage out of 500?'''

s1 = float(input("enter the marks sub1:"))
s2 = float(input("enter the marks sub2:"))
s3 = float(input("enter the marks sub3:"))
s4 = float(input("enter the marks sub4:"))
s5 = float(input("enter the marks sub5:"))

total_sum = s1+s2+s3+s4+s5

parcentage = (total_sum/500)*100

print(total_sum)
print(parcentage)
