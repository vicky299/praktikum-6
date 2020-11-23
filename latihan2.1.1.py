a= int(input('side A length:'))
b= int(input('side B length:'))
c= int(input('hypotenuse C:'))
def pytha(a,b,c):
    return a**2+b**2 == c**2
if(pytha(a,b,c)):
    print(True)
else:
    print(False)
 
