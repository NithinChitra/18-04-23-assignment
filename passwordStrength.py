password=input("Enter password That Should contain len 8 and capital letter and small letter and can contain special characters like(@,#,$,&):")
length=len(password)
hasCapital=False
hasSmall=False
hasSpecialChar=False
for i in password:
    if i>='A' and i<='Z':
        hasCapital=True
    if i>='a' and i<='z':
        hasSmall=True
    if ('@' in password) or ('#' in password) or ('$' in password) or ('&' in password):
        hasSpecialChar=True
#checking password
if length>=8 and (hasCapital==True) and (hasSmall==True) and (hasSpecialChar==True):
    print("password is Strong")
else:
    print("password is weak")

