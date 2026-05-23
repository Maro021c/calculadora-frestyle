numero1 = int(input("fala um numero ai"))
numero2 = int(input("fala outro"))

print ("1:soma")
print ("2:subtração")
print ("3:multiplicação")
print ("4:divisão")
print ("5:hipoteca")

seleção = int (input("escolha ai macho"))

if seleção == 1:
    operador = "+"

elif seleção == 2:
    operador = "-"
    

elif seleção == 3:
    operador = "*"

elif seleção == 4:
    operador = "/"

else: print("Pobre KKKKKKKKK")


resultado = eval(f"{numero1} {operador} {numero2}")

print (f"{resultado}")
