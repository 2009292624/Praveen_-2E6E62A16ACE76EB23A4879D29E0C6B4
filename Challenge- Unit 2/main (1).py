# 1.2 Write a program that determines whether a year entered by the user is a leap year or not using ifelif-else statements.

input_year = int(input("Enter the Year to be checked: "))
if (input_year%400 == 0):
          print("%d is a Leap Year" %input_year)
elif (input_year%100 == 0):
          print("%d is Not the Leap Year" %input_year)
elif (input_year%4 == 0):
          print("%d is a Leap Year" %input_year)
else:
          print("%d is Not the Leap Year" %input_year)