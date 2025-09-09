# Cek Kategori dengan if .. else
usia = 15

if usia < 13:
    print("Anak")
elif usia <= 17:
    print("Remaja")
elif usia < 60:
    print("Dewasa")
else:
    print("Lansia")

# Program print angka kelipatan 3
for i in range(0,21):
    if i % 3 == 0:
        print(i)

# Fizzbuzz
for i in range(1,21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Program cek bilangan prima dengan input user
angka = int(input("Input: "))

if angka > 1:
    for i in range(2, angka):
        if angka % i == 0:
            print(f"output: {angka} bukan bilangan prima")
            break
    else:
        print(f"output: {angka} adalah bilangan prima")
else:
    print(f"output: {angka} bukan bilangan prima")

# Cek jumlah huruf vokal
# Program hitung jumlah huruf vokal
kata = input("Masukkan kata: ").lower()  # biar semua jadi huruf kecil
vokal = "aiueo"
jumlah = 0

for huruf in kata:
    if huruf in vokal:
        jumlah += 1

print(f"Ada {jumlah} huruf vokal dalam kata '{kata}'")

# Pengembangan dari hitung jumlah huruf vokal
# Program cek huruf vokal + tampilkan vokal yang ada
kata = input("Masukkan kata: ").lower()
vokal = "aiueo"
jumlah = 0
huruf_vokal = []

for huruf in kata:
    if huruf in vokal:
        jumlah += 1
        if huruf not in huruf_vokal:  # supaya gak dobel
            huruf_vokal.append(huruf)

print(f"Ada {jumlah} huruf vokal dalam kata '{kata}'")
print("Huruf vokal yang muncul:", ", ".join(huruf_vokal))


# pengembangan huruf vokal 2
# Program cek huruf vokal + hitung frekuensi tiap vokal
kata = input("Masukkan kata: ").lower()
vokal = "aiueo"
hitung_vokal = {}

for huruf in kata:
    if huruf in vokal:
        if huruf in hitung_vokal:
            hitung_vokal[huruf] += 1
        else:
            hitung_vokal[huruf] = 1

# Total semua vokal
total_vokal = sum(hitung_vokal.values())

print(f"Ada {total_vokal} huruf vokal dalam kata '{kata}'")
print("Detail jumlah tiap vokal:")
for v, jumlah in hitung_vokal.items():
    print(f"{v} = {jumlah} kali")
