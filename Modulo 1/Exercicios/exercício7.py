# Peça ao usuário para digitar "M" para manhã ou qualquer outra tecla para tarde. Se for "M", exiba "Bom dia!, senão exiba "Boa tarde!".

horário = input('Digite "M" para manhã ou "T" para tarde: ')
if horário == "M":
    print("Bom dia!")
elif horário == "T":
    print("Boa tarde!")