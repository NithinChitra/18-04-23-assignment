marks=int(input("Enter marks obtained by student:))
if marks>=95:
    grade='O'
elif marks>=85:
    grade='A'
elif marks>=75:
    grade='B'
elif marks>=65:
    grade='C'
elif marks>=55:
    grade='D'
else:
    grade='F'
print("Student grade is: "+grade)
