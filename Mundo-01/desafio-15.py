# Diária do carro: R$ 60.00 |valor por km rodado: R$ 0.15
km = float(input('Quantos km foram percorridos? '))
days = int(input('Quantos dias alugados? '))
day_cost = 60
km_cost = 0.15
tc = (km * km_cost) + (days * day_cost)
print(f'Diária no valor de: R$ {day_cost:.2f}')
print(f'Valor por km: R$ {km_cost}')
print(f'O total a pagar por {days} diárias e {km} kms rodados é de R$ {tc:.2f}')