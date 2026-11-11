nama = input("Masukkan nama Mahasiswa: ")

if nama == "Andi" :
    target = 70
elif nama == "budi" :
    target == 75
elif nama == "Citra" :
    target == 80
else :
    print("Nama Mahasiswa :", nama)
    print("target nilai :", target)

ulang = 1
lulus = False

while ulang <= 3:
    nilai = int(input("Masukkan nilai ujian ke-" + str(ulang) + ": "))

    if nilai >= target :
        lulus = True
        break
    else:
        print("Nilai belum mencapai target!")
        ulang += 1

print("\nHASIL AKHIR")

if lulus:
    print(nama, "berhasil lulus!")
    print("UJian ke-", ulang)
else :
    print(nama, "tidak lulus setelah 3 kali ujian.")