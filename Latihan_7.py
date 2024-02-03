print("Pilihan kota")
print("1. Prabumulih")
print("2. Muara Enim")
print("3. Lubuklinggau")
kota = int(input("mau ke kota mana?"))

print("pilihan kelas")
print("1. Ekonomi")
print("2. Bisnis")
print("3. Eksekutif")
kelas = int(input("kelas apa?"))

tiket = int(input("berapa banyak tiket?"))

Harga = 0

if kota == 1:
    if kelas == 1:
        Harga = 100000
    elif kelas == 2:
        Harga = 400000
    elif kelas == 3:
        Harga = 700000
    else:
        print("invalid")
elif kota == 2:
    if kelas == 1:
        Harga = 200000
    elif kelas == 2:
        Harga = 500000
    elif kelas == 3:
        Harga = 800000
    else:
        print("invalid")
elif kota == 3:
    if kelas == 1:
        Harga = 300000
    elif kelas == 2:
        Harga = 600000
    elif kelas == 3:
        Harga = 900000
    else:
        print("invalid")
else:
    print("invalid")     
        
subTotal = Harga * tiket
total = 0

if kota == 2 and kelas == 1:
    kode_promo = input("apakah ada kode promo?")
    if kode_promo == "igs":
        total = subTotal * 90 / 100
        print("anda mendapatkan diskon 10%")
        
if kota == 3 and kelas == 3:
    kode_promo = input("apakah ada kode promo?")
    if kode_promo == "igs":
        total = subTotal * 90 / 100
        print("anda mendapatkan diskon 10%")
    
print("subtotal =", subTotal)
print("total anda adalah =", total)