pay = float(input('Qual o seu salário? R$: '))
promo = ((15 / 100) * pay) + pay # 15% increase in payment
print(f'Seu novo salário é de {promo:.2f}')