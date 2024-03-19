hasil = ""

x = int(input("Masukkan jumlah :"))
bar = x

while bar >= 0:
    
    kol = bar
    while kol > 0:
        hasil += "   "
        kol -= 1
        
    kanan = 1
    while kanan < (x - (bar-1)):
        hasil += " * "
        kanan += 1

    hasil = hasil + "\n"
    bar -= 1

print(hasil)
