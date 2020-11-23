from operation import*

a=10
b=2
c=7
d=5
e=12
f=34
print(a, '+',b,'=', jumlah(a,b))
print(c, '+',d,'=', jumlah(c,d))
print(e, '-',f,'=', kurang(e,f))
print(jumlah(a,b), '/',jumlah(c,d),'=', bagi(jumlah(a,b),jumlah(c,d)))
print(bagi(jumlah(a,b),jumlah(c,d)), '/',kurang(e,f),'=', bagi(bagi(jumlah(a,b),jumlah(c,d)),kurang(e,f)))
 
