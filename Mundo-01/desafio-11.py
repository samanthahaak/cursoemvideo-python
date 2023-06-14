height = float(input('Qual é a altura da parede em metros: '))
length = float(input('Qual é a largura da parede em metros: '))
area = height * length
ink_litter = 2 # every 2 square meters need 1 litter of ink
print(f'Sua parede tem dimensão {height}x{length} e sua área é de {area}m²')
print(f'Para pintar essa parede você vai precisar de {area/ink_litter} litros de tinta')