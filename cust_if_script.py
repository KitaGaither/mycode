#!/usr/bin/env python3

# custom if, elif, else statements

echo = ("Let's find your letter grade")

grade = int(input("Enter grade between 1-100: "))

if grade > 100:
    print("Let's not be a show off!")
elif grade == 100 or grade  >= 90:
    print("Congrats, you got an A")
elif grade == 89 or grade >= 80: 
    print("Congrats on your B")
elif grade == 79 or grade >= 70:
    print("C's mean you're trying")
elif grade ==69 or grade >= 60:
    print("D means you're almost there buddy")
else:
    print("F means you need to repeat subject")
