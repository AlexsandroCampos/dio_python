valor = int(input("Digite um numero: \n"))

if valor < 5:
    print("Menor que 5")
elif valor >= 5 and valor < 10:
    print("Maior ou igual a 5 e menor que 10")
else:
    print("Maior ou igual a 10")

# estruturas aninhadas são ifs dentro de ifs
# veja ternária abaixo

saldo = 10
saque = 9
status = "Sucesso" if saldo >= saque else "Falha"
print(f"\n{status}")