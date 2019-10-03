#Variaveis
valorhora=70
dias=30
horastrabalho=8
vencimentomensal=valorhora*horastrabalho*dias
nome="phelipe"
print(valorhora)
print(dias)
print(horastrabalho)
print(vencimentomensal)
print(nome)
print(float(valorhora))
print(int(4.6))

#Strings
print(str(4.6))
print(nome[0:5])
print(nome*3)
print("p" in nome)
print("z" in nome)

#Listas
lista=[1,4,3,4,5,6]
print(lista)
lista.append("mizerani")
print(lista)
lista.append(50)
print(lista)
print(lista.index("mizerani"))
print(lista[4])
print(lista.count(4))
lista.remove("mizerani")
print(lista)
lista.reverse()
print(lista)
lista.sort()
print(lista)

#dicionarios
telefones={"mizerani":999999999, "phelipe":888888888, "mozao": 6666666666}
print(telefones)
telefones["fedorento"]=555555555
print(telefones)
del telefones["phelipe"]
print(telefones)

#tuplas
tuplas=("phelipe","mizerani","mozao")
print(tuplas)
print(tuplas[0])
print(tuplas[1])
print(tuplas[2])
print(tuplas[0:2])
print(len(tuplas))
print(tuplas+tuplas)
print(tuplas*4)
print(4 in tuplas)
print("phelipe" in tuplas)
listatuplas=[1,4,"fedorento"]
print(listatuplas)
tuplas2=tuple(listatuplas)
print(tuplas2)

#ifElse
numero=1
if(numero==1):
    print("Numero igual a 1")
if(numero==2):
    print("Numero igual a 2")
numero=2
if(numero==1):
    print("Numero igual a 1")
else:
    print("Numero nao eh igual a 1")

nomemeu="phelipe"
if ("z" in nomemeu):
    print("Tem Z no nome")
elif ("p" in nomemeu):
    print("Tem P no nome")
else:
    pass

#loop
for x in range(0,5):
    print("Valor de X é:", x)

nomeseu="phelipe"
for letra in nomeseu:
    print(letra)

listavalor=["phelipe",28,"mizerani"]
for valor in listavalor:
    print(valor)

numeroquinze=15
while (numeroquinze>0):
    print(numeroquinze)
    numeroquinze=numeroquinze-1

numerovinte=20
while True:
    numerovinte=numerovinte-1
    print(numerovinte)
    if (numerovinte==5):
        break

numerodez=10
while True:
    numerodez=numerodez-1
    if (numerodez==4):
        continue
    print(numerodez)
    if (numerodez==2):
        break

for x in range(0,5):
    pass #faz nada