#input 
nama = input("Masukkan Nama Pelanggan : ")
total_belanja = int(input("Masukkan Total Belanja : "))

#proses/diskon
if total_belanja >= 500000:
    diskon = total_belanja * 10 / 100
elif total_belanja >= 200000 :
    diskon = total_belanja * 5 / 100
elif total_belanja <= 200000 :
    diskon = total_belanja * 0 / 100
else:
    diskon = 0

#bonus 
if total_belanja >= 1000000:
    bonus = 50000
else:
    bonus = 0

total_bayar = total_belanja - diskon 

#output
print("=============== STRUK PEMBELIAN =====================")
print("Nama Pelanggan : ", nama)
print("Total Belanja : Rp.", total_belanja)
print("Diskon : Rp.", diskon)
print("bonus : Rp.", bonus)
print("Total Yang Harus Di Bayar : Rp.", total_bayar)