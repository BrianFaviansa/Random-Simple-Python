# Latihan konversi satuan temperature

# Program konversi suhu celcius

print("\nPROGRAM KONVERSI SUHU CELCIUS\n")
celcius = float(input("Masukkan Suhu dalam celcius : "))
print("Suhu adalah", celcius, "Celcius")

# Reamur = 4/5C
reamur = (4/5) * celcius
print("Suhu dalam Reamur adalah", reamur, "Reamur")

# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam Fahrenheit adalah", fahrenheit, "Fahrenheit")

# Kelvin 
kelvin = celcius + 273
print("Suhu dalam Kelvin adalah", kelvin, "Kelvin")

# Program konversi suhu reamur 

print("\nPROGRAM KONVERSI SUHU REAMUR\n")
reamur = float(input("Masukkan Suhu dalam reamur : "))
print("Suhu adalah", reamur, "Reamur")

# Reamur = 5/4C
celcius = (5/4) * reamur
print("Suhu dalam celcius adalah", celcius, "celcius")

# Fahrenheit
fahrenheit = ((9/4) * reamur) + 32
print("Suhu dalam Fahrenheit adalah", fahrenheit, "Fahrenheit")

# Kelvin 
kelvin = (5/4) * reamur + 273
print("Suhu dalam Kelvin adalah", kelvin, "Kelvin")

# Program konversi suhu Faherenheit

print("\nPROGRAM KONVERSI SUHU FAHRENHEIT\n")
fahrenheit = float(input("Masukkan Suhu dalam fahrenheit : "))
print("Suhu adalah", fahrenheit, "Fahrenheit")

# Celcius
celcius = (5/9) * (fahrenheit - 32)
print("Suhu dalam celcius adalah", celcius, "celcius")

# Reamur
reamur = ((4/9) * (fahrenheit - 32))
print("Suhu dalam Reamur adalah", reamur, "Reamur")

# Kelvin 
kelvin = (((5/9) * (fahrenheit - 32)) + 273)
print("Suhu dalam Kelvin adalah", kelvin, "Kelvin")

# Program konversi suhu Kelvin

print("\nPROGRAM KONVERSI SUHU KELVIN\n")
kelvin = float(input("Masukkan Suhu dalam kelvin : "))
print("Suhu adalah", kelvin, "Kelvin")

# Celcius
celcius = kelvin - 273
print("Suhu dalam celcius adalah", celcius, "celcius")

# Reamur
reamur = (4/5) * (kelvin-273) 
print("Suhu dalam Reamur adalah", reamur, "Reamur")

# Fahrenheit
fahrenheit = ((((9/5) * (kelvin - 273))) + 32)
print("Suhu dalam Fahrenheit adalah", fahrenheit, "Fahrenheit")