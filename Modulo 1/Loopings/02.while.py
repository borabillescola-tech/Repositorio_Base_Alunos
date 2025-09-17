bombons = 10

while bombons > 0: # Enquanto bombons > 0 o while continua executando
    print(f"Eu tenho {bombons} bombons.")
    bombons -= 1 # diminui um bombom
    print(f"Comi 1 e fiquei com {bombons} bombons.") # Informa a quantidade de bombons após a subtração

    if bombons == 0: # Se bombons for igual a 0
        print("Acabaram os bombons!") # Informa que acabaram os bombons