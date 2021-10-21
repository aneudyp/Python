# Aprendiendo un poco de Python

#Imprimiento por pantalla

print("Hola Mundo!")

#TIPOS DE DATOS
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

#FUNCIONES

def MostrarAltura():
    Altura = 170.18
    if Altura >= 180:
        print("Eres una persona alta!")
    else:
        print("Eres bajito!")

#Llamar funcion
MostrarAltura()

#ENVIANDO PARAMETROS

VarAltura= int(input("Cúal es tu altura (cm)?: "))
def MostrarAltura(Altura):
    if Altura >= 180:
        print("Eres una persona alta!")
    else:
        print("Eres bajito!")

MostrarAltura(VarAltura)

#EXTRAER DATO DE FUNCION


def MostrarAltura(Altura):
    resultado= "" 
    if Altura >= 180:
        print("Eres una persona alta!")
    else:
        print("Eres bajito!")
    return resultado

print(MostrarAltura(VarAltura))

#LISTAS
    
familia= ["Aneudy", "Paula", "Kylian", "Annelys", "Mia"]
print(familia) #imprime todo el listado

#Imprime la posicion dentro de la lista 0,1,2,3,4,n
print(familia[0]) #Imprime: Aneudy

#BUCLE FOR
#La variable Persona captura el valor de Familia y lo imprime hasta que finalice
for persona in familia:
    print(persona)