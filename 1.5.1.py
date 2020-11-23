from operation import*

a=2
b=4
c=6
print(b, '*',c,'=', kali(b,c))
print(a, '+',kali(b,c),'=', jumlah(a,kali(b,c)))
print(jumlah(a,kali(b,c)), '-',b,'=', kurang(jumlah(a,kali(b,c)),b))

