year=int(input("Enter year:"))
#first we need to check year is a centuary year or not 
if year%400==0:
    print("it is a leap year")
#if year is not divisible by 400 and divisible for 100 is not leap year ex:1990
elif year%100==0:
    print("it is not a leap year")
#if year is not a centuary year then if year is divisible by 4 it is a leap year ex:2004
elif year%4==0:
    print("it is a leap year")
else:
    print("it is not a leap year")