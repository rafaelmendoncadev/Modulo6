#### 1. Faça um Programa que mostre a mensagem (print) "Alo mundo" na tela.
import math
print("Alo mundo")

#### 2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
numero = int(input("Digite um numero: "))
print(f"O numero informado foi {numero}")

# 3. Faça um Programa que peça dois números e imprima a soma.
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
soma = numero1 + numero2
print(f"A soma dos numeros {numero1} e {numero2} é {soma}")

# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"A média das notas {nota1}, {nota2}, {nota3} e {nota4} é {media:.2f}")

#### 5. Faça um Programa que converta metros para centímetros. Você pode pedir o comprimento em metros para o usuário (input).
metros = float(input("Digite o comprimento em metros: "))
centimetros = metros * 100
print(f"{metros} metros é igual a {centimetros} centímetros.")

#### 6. Faça um Programa que calcule a área de uma sala de um apartamento. Para isso, o seu programa precisa pedir a largura da sala, o comprimento da sala e imprimir a área em m² da sala.
largura = float(input("Digite a largura da sala em metros: "))
comprimento = float(input("Digite o comprimento da sala em metros: "))
area = largura * comprimento
print(f"A área da sala é {area} m².")

#### 7. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
ganho_por_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salario = ganho_por_hora * horas_trabalhadas
print(f"Seu salário no mês é R$ {salario:.2f}.")

#### 8. Vamos criar um conversor de temperatura. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#$C = \frac{5}{9}(F-32)$
fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"A temperatura em graus Celsius é {celsius:.2f}°C.")

#### 9. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
#$F = \frac{9}{5}C + 32$
celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"A temperatura em graus Fahrenheit é {fahrenheit:.2f}°F.")

#### 10. Tendo como dados de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
#$P = 72,7h - 58$
altura = float(input("Digite sua altura em metros: "))
peso_ideal = (72.7 * altura) - 58
print(f"Seu peso ideal é {peso_ideal:.2f} kg.")

#### 11. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
##### a. Para homens: $P = 72,7h - 58$
##### b. Para mulheres: $P = 62,1h - 44,7$
altura = float(input("Digite sua altura em metros: "))
genero = input("Digite seu gênero (M para masculino, F para feminino): ").upper()

if genero == 'M':
    peso_ideal = (72.7 * altura) - 58
    print(f"Seu peso ideal é {peso_ideal:.2f} kg.")
elif genero == 'F':
        peso_ideal = (62.1 * altura) - 44.7
        print(f"Seu peso ideal é {peso_ideal:.2f} kg.")
else:
            print("Gênero inválido. Por favor, digite 'M' para masculino ou 'F' para feminino.")

#### 12. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#####  Calcule o salário bruto (horas * salario por hora)
##### Calcule o desconto do IR (11% do salário bruto)
##### Calcule o desconto do INSS (8% do salário bruto)
# Calcule o desconto do sindicato (5% do salário bruto)
# Calcule o salário líquido (salário bruto - descontos)

ganho_por_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salario_bruto = ganho_por_hora * horas_trabalhadas
desconto_ir = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (desconto_ir + desconto_inss + desconto_sindicato)    
print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Desconto do IR: R$ {desconto_ir:.2f}")
print(f"Desconto do INSS: R$ {desconto_inss:.2f}")
print(f"Desconto do Sindicato: R$ {desconto_sindicato:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")

#### 13. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados 
#da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que
# a tinta é vendida em latas de 18 litros, que custam R\$ 80,00. Informe ao usuário a quantidades de latas 
# de tinta a serem compradas e o preço total.
area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
litros_necessarios = area / 3
latas_necessarias = math.ceil(litros_necessarios / 18)
preco_total = latas_necessarias * 80
print(f"Quantidade de latas necessárias: {latas_necessarias}")
print(f"Preço total: R$ {preco_total:.2f}")


 
 




