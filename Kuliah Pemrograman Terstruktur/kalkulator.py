#input angka
angka1= float(input("masukkan angka pertama: "))
angka2= float(input("masukkan angka kedua: "))

#rumus
hasilTambah = angka1 + angka2
hasilKurang = angka1 - angka2
hasilKali = angka1 * angka2
hasilBagi = angka1 / angka2
hasilSisaBagi = angka1 % angka2

#hasil
print(f"angka 1: {angka1}")
print(f"angka 2: {angka2}")
print(f"hasil penjumlahan: {hasilTambah}")
print(f"hasil Pengurangan: {hasilKurang}")
print(f"hasil Perkalian: {hasilKali}")
print(f"hasil Pembagian: {hasilBagi}")
print(f"hasil Sisa Bagi: {hasilSisaBagi}")