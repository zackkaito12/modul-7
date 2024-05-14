def konversi_suhu(suhu, satuan):
    if satuan == 'C':
        if 0 <= suhu <= 100:
            fahrenheit = (suhu * 9/5) + 32
            reamur = suhu * 4/5
            kelvin = suhu + 273.15
            print(f"suhu {suhu} derajat Celcius dapat dikonversi menjadi:")
            print("|| Satuan suhu ||  derajat suhu ||")
            print("||-------------||---------------||")
            print(f"|| Reaumur     ||{reamur:.2f}    \t||")
            print(f"|| Fahrenheit  ||{fahrenheit:.2f}\t\t||")
            print(f"|| Kelvin      ||{kelvin:.2f}    \t||")
        else:
            print("Suhu yang Anda inputkan tidak sesuai.")
    elif satuan == 'F':
        if 32 <= suhu <= 212:
            celcius = (suhu - 32) * 5/9
            reamur = (suhu - 32) * 4/9
            kelvin = (suhu - 32) * 5/9 + 273.15
            print(f"suhu {suhu} derajat Fahrenheit dapat dikonversi menjadi:")
            print("|| Satuan suhu ||  derajat suhu ||")
            print("||-------------||---------------||")
            print(f"|| Reaumur     ||{reamur:.2f} \t||")
            print(f"|| Celcius     ||{celcius:.2f}\t||")
            print(f"|| Kelvin      ||{kelvin:.2f} \t||")
        else:
            print("Suhu yang Anda inputkan tidak sesuai.")
    elif satuan == 'R':
        if 0 <= suhu <= 80:
            celcius = suhu * 5/4
            fahrenheit = (suhu * 9/4) + 32
            kelvin = suhu * 5/4 + 273.15
            print(f"suhu {suhu} derajat Reaumur dapat dikonversi menjadi:")
            print("|| Satuan suhu ||  derajat suhu ||")
            print("||-------------||---------------||")
            print(f"|| Celcius     ||{celcius:.2f}   \t||")
            print(f"|| Fahrenheit  ||{fahrenheit:.2f}\t\t||")
            print(f"|| Kelvin      ||{kelvin:.2f}    \t||")
        else:
            print("Suhu yang Anda inputkan tidak sesuai.")
    elif satuan == 'K':
        if 273 <= suhu <= 373:
            celcius = suhu - 273.15
            fahrenheit = (suhu - 273.15) * 9/5 + 32
            reamur = (suhu - 273.15) * 4/5
            print(f"suhu {suhu} derajat Kelvin dapat dikonversi menjadi:\n12")
            print("|| Satuan suhu ||  derajat suhu ||")
            print("||-------------||---------------||")
            print(f"|| Celcius       ||\t{celcius:.2f}   \t||")
            print(f"|| Fahrenheit    ||\t{fahrenheit:.2f}[t\t||")
            print(f"|| Reaumur       ||\t{reamur:.2f}    \t||")
        else:
            print("Suhu yang Anda inputkan tidak sesuai.")

suhu = float(input("Masukkan suhu: "))
satuan = input("Masukkan satuan suhu (C/F/R/K): ").upper()

konversi_suhu(suhu, satuan)
