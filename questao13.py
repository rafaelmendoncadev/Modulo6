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