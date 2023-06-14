val = float(input('Qual o preço do produto R$: '))
total_desc = val - ((5 / 100) * val)
print(f'O valor do produto com 5% de desconto é R$ {total_desc:.2f}')