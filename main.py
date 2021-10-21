# Aprendiendo un poco de Python

#Imprimiento por pantalla

print("Hola Mundo!")

#VARIABLES
texto= "Aprendiendo Python"
nombre="Aneudy Patiño"
year= 40
altura= "170.18cm" #5'7 

#CONCATENANDO
print(f"{texto} – {nombre} – {year}")
print(texto + nombre + (str(year))) #str() convierte a String

#VARIABLES ENTRADA
sitioweb= input("Cuál es tu web favorita?: ")
print(sitioweb + " es tu sitio web favorito!")

#CONDICIONALES
Altura = 187
if Altura >= 180:
	print("Eres una persona alta!")
else:
	print("Eres bajito!")


