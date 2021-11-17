# Aprendiendo un poco de Python

#Imprimiento por pantalla

print("Hola Mundo!")
print("INF", "ISW") #Imprimiendo algumentos separados por coma
#Variables
universidad="UAPA"
recinto="Santo Domingo"
print("Universidad ", universidad, " Recinto..:", recinto)
print(f"Universidad ", {universidad}, " Recinto..:", {recinto}) #Usando F para pasar variables con {}

#ENTRADA input

print("Bienvenido, su nombre es ?")
nombre=input()
print(f" Buenas noches {nombre} ")

a_nacimiento= int(input("Año de nacimiento..:"))
a_actual= int(input("Año actual..:"))
edad= a_actual - a_nacimiento
print(f"Edad..: {edad}")

#Condicional IF

if (edad >=18):
    print("Usted es MAYOR de edad!")
else :
    print("Usted es MENOR de edad!")

nota=int(input("Calificacion Final..: "))
if (nota>90 and nota<=100):
    literal="A"
elif (nota>=80 and nota<=89):
    literal="B"
elif (nota>=70):
    literal="C"
elif (nota>=60):
    literal="D"
else:
    literal="F"
print(f"Literal : {literal}")

#Estructuras repetitivas For - While
for numero in range(1,11):
    print(numero)

mi_lista= [1,15,20]
for numero in mi_lista:
    print(numero)

mi_diccionario={"Santiago":"Aguilas","Santo Domingo":"Licey","Capital":"Escogido","San Pedro":"Estrellas", "San Francisco":"Gigantes","Romana":"Los Toros"}
for numero in mi_diccionario:
    print(numero) #Imprime la clave

mi_diccionario={"Santiago":"Aguilas","Santo Domingo":"Licey","Capital":"Escogido","San Pedro":"Estrellas", "San Francisco":"Gigantes","Romana":"Los Toros"}
for numero in mi_diccionario:
    print(mi_diccionario[numero]) #Imprime el valor


#TIPOS DE DATOS
texto= "Aprendiendo Python"
nombre="Aneudy Patiño"
year= 40
altura= "170.18cm" #5'7 

#CONCATENANDO
#print(f"{texto} – {nombre} – {year}")
#print(texto + nombre + (str(year))) #str() convierte a String

#VARIABLES ENTRADA
#sitioweb= input("Cuál es tu web favorita?: ")
#print(sitioweb + " es tu sitio web favorito!")

#CONDICIONALES
''' Altura = 187
if Altura >= 180:
	print("Eres una persona alta!")
else:
	print("Eres bajito!") '''

#FUNCIONES

''' def MostrarAltura():
    Altura = 170.18
    if Altura >= 180:
        print("Eres una persona alta!")
    else:
        print("Eres bajito!") '''

#Llamar funcion
# MostrarAltura()

#ENVIANDO PARAMETROS

''' VarAltura= int(input("Cúal es tu altura (cm)?: "))
def MostrarAltura(Altura):
    if Altura >= 180:
        print("Eres una persona alta!")
    else:
        print("Eres bajito!")

MostrarAltura(VarAltura) '''

#EXTRAER DATO DE FUNCION


''' def MostrarAltura(Altura):
    resultado= "" 
    if Altura >= 180:
        print("Eres una persona alta!")
    else:
        print("Eres bajito!")
    return resultado

print(MostrarAltura(VarAltura)) '''

#LISTAS
    
''' familia= ["Aneudy", "Paula", "Kylian", "Annelys", "Mia"]
print(familia) #imprime todo el listado '''

#Imprime la posicion dentro de la lista 0,1,2,3,4,n
# print(familia[0]) #Imprime: Aneudy

#BUCLE FOR
#La variable Persona captura el valor de Familia y lo imprime hasta que finalice
# for persona in familia:
#     print(persona)