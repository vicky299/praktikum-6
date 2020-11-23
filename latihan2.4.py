#sum
def sum(*myData):
    sum = 0
    i = 0
    for data in myData:
        sum+=data
        i += 1

    penjumlahan = sum
    print('jumlah :', penjumlahan)

#rerata
def rerata(*myData):
    sum = 0
    i = 0
    for data in myData:
        sum+=data
        i += 1

    ratarata = sum/i
    print('rata ratanya:', ratarata)

#max
def max(*myData):
    max = 0
    i = 0
    for data in myData:
        max = data
        i = data

    maksimal= max
    print('nilai maks:', maksimal)

#min
def min(*myData):
    min = 0
    i = 0
    for data in myData:
        min = data-i
        i = min

    minimal = min
    print('nilai min:', minimal)
