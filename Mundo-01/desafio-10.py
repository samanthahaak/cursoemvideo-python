cash = float(input('Quanto dinheiro tem na sua carteira? R$ '))
dol = cash / 5.03  # cotação em 04/05/23
eu = cash / 5.53  # cotação em 04/05/23
print(f'Você pode comprar {dol:.2f} dólares e {eu:.2f} euros')