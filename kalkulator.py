#Penjumlahan
def add(x, y):
    return x + y

#Pengurangan
def subtract(x, y):
    return x - y

#Perkalian
def multiply(x, y):
    return x * y

#Pembagian
def divide(x, y):
    return x / y


print("Pilih Operasi : ")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

while True:
    #Pilihan Operasi
    choice = input("Pilihan(1/2/3/4): ")

    #Masuk ke pilihan operasi
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Masukan nilai pertama: "))
        num2 = float(input("Masukan nilai kedua: "))

        if choice == '1':
            print("Hasil dari ", num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print("Hasil dari ", num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print("Hasil dari ", num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print("Hasil dari ", num1, "/", num2, "=", divide(num1, num2))
        
        next_calculation = input("Ingin mengulangi perhitungan? (y/n): ")
        if next_calculation == "n":
          break
    
    else:
        print("Masukan tidak valid")
