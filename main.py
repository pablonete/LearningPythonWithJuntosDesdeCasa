import time

WIDTH = 40
def typeprint(text):
  for i in range(0, len(text), WIDTH):
    typeprintline(text[i:min(i + WIDTH, len(text))])

def typeprintline(text):
  for i in range(1, len(text) + 1):
    print(text[0:i], end='\r' if i<len(text) else '\n')
    time.sleep(0.05)

typeprint("Hello World! Hello World! Hello World! Hello World! Hello World! Hello World! Hello World! Hello World! Hello World! Hello World!")

numero_de_latas = 2
contenido_de_latas = "judías"
print(numero_de_latas)
print(contenido_de_latas)

typeprint("Necesito comprar {} de {}".format(numero_de_latas, contenido_de_latas))

hay_latas = False

lista_compra = ["Leche", "Café", "Pipas", "Quicos"]

precios = {"Leche": 1, "Café": 2, "Jamón": 4}

print(lista_compra[1:3])
print(precios["Leche"])

hay_leche = True

typeprint("Hola, sr. Mercadona, ¿hay leche?")
if hay_leche:
  typeprint("Sí, hay leche")
else:
  typeprint("No, no hay leche")

for alimento in lista_compra:
  typeprint("- Compra {} si hay".format(alimento))

lista_numeros = [4, 6, 8, 10, 15, 20, 60, 100]
total = 0
print(total)
for numero in lista_numeros:
  total = total + numero
  typeprint(" + {} = {}".format(numero, total))

seguir = input("¿Quieres seguir?")
if seguir == "si":
  typeprint("Allá vamos")
else:
  typeprint("Pues adiós")

