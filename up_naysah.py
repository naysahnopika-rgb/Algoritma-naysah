print("=== TOKO SERBA ADA ===")

nama_barang = input("Masukkan nama barang      : ")
stok = int(input("Masukkan jumlah stok awal : "))

lanjut = "y"
while lanjut.lower() == "y":

    print("\n--- Pilih Transaksi ---")
    print("1. Barang Masuk")
    print("2. Barang Keluar")
    pilihan = input("Pilihan (1/2): ")

    if pilihan == "1":
        jumlah = int(input("Jumlah barang masuk  : "))
        stok = stok + jumlah
        print("Stok bertambah sebanyak", jumlah)

    elif pilihan == "2":
        jumlah = int(input("Jumlah barang keluar : "))

        if jumlah > stok:
            print("Stok Tidak Mencukupi!")
        else:
            stok = stok - jumlah
            print("Stok berkurang sebanyak", jumlah)

    else:
        print("Pilihan tidak valid!")

    print("Stok", nama_barang, "saat ini:", stok)
    lanjut = input("\nLakukan transaksi lagi? : ")

print("\n=== HASIL AKHIR ===")
print("Nama barang :", nama_barang)
print("Stok akhir  :", stok)
print("Terima kasih!")