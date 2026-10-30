nama_mahasiswa =input("Masukkan nama mahasiswa:")
nilaialgoritma = int(input("Masukkan nilai algoritma: "))
nilaiagama = int(input("Masukkan nilai agama: "))
nilaibasisdata = int(input("Masukkan nilai basis data: "))
nilaipancasila = int(input("Masukkan nilai pancasila: "))

rata_rata = (nilaialgoritma + nilaiagama + nilaibasisdata + nilaipancasila) / 4

if rata_rata >= 80 and rata_rata <= 100:
    print("Nilai A")
elif rata_rata >= 70 and rata_rata < 80:
    print("Nilai B")        
elif rata_rata >= 60 and rata_rata < 70:
    print("Nilai C")
elif rata_rata >= 50 and rata_rata < 60:
    print("Nilai D")
elif rata_rata >= 0 and rata_rata < 50:
    print("Nilai E")
else:
    print("tidak lulus")
print(rata_rata)