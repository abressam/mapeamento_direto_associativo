import random

def inicializar_cache(tamanho_cache):
    enderecos = {}
    for key in range(tamanho_cache):
        enderecos[key] = -1
    
    return enderecos

def inicializar_frequencia(tamanho_cache):
    frequencia = {}
    for key in range(tamanho_cache):
        frequencia[key] = 0
    
    return frequencia

def imprimir_cache(cache):
    print(f"Tamanho cache: {len(cache)}")
    print(f"Pos Cache{'':<2}|{'':>2}Posição Memória")
    for key, value in cache.items():
        print(f"{key:>9}{'':<2}|{value:>17}")
    
    print("\n")

def mapeamento_direto(pos_memoria):
    tamanho_cache = int(input("Digite o tamanho da cache:\n"))

    hit = 0
    miss = 0
    enderecos = inicializar_cache(tamanho_cache)

    for i in range(len(pos_memoria)):
        posicao_cache = pos_memoria[i] % tamanho_cache
        for key, value in enderecos.items():
            if key == posicao_cache:
                print(f"Linha {i} | posição de memória desejada {pos_memoria[i]}")
                if value == pos_memoria[i]:
                    hit += 1
                    print("Status: Hit")
                    imprimir_cache(enderecos)
                else:
                    value = pos_memoria[i]
                    enderecos[posicao_cache] = value
                    miss += 1
                    print("Status: Miss")
                    imprimir_cache(enderecos)

    taxa_acertos = ((hit * 100) / (hit + miss))

    print(f"Memórias acessadas: {len(pos_memoria)}\nNúmero de hits: {hit}\nNúmero de misses: {miss}\nTaxa de acertos (hits): {taxa_acertos:.2f}%")    

def menu_mapeamento():
    op = 0
    menu = """
        1 - mapeamento direto
        2 - mapeamento associativo
        3 - sair
        """
    while op not in [1,2,3]:
      op = int(input(menu))

    return op

def menu_algoritmo_subs():
    op = 0
    menu = """
    1 - LRU
    2 - LFU
    3 - FIFO
    """
    while op not in [1,2,3]:
      op = int(input(menu))

    return op

def existe_bloco_vazio_cache(cache, start, keys_range,):    
    for key in range(start, keys_range):
        if cache[key] == -1:
            return key    
    return -1

def procura_cache(cache, start, keys_range, pos_memoria):
    for key in range(start, keys_range):
        if cache[key] == pos_memoria:
            return key 
    return -1

def hit_lru(cache, keys_range, pos_cache):
    temp = cache[keys_range-1]
    cache[keys_range - 1] = cache[pos_cache]

    for key in range(pos_cache + 1, keys_range):
        if key == keys_range - 1:
            cache[key - 1] = temp
            break
        cache[key - 1] = cache[key]      

def substitui_cache(cache, start , keys_range, pos_memoria, algoritmo_subs, frequencia):
    if algoritmo_subs == 3:
      for key in range(start, keys_range):
          if key == keys_range - 1:
              cache[key] = pos_memoria
              break
          cache[key] = cache[key+1]
    elif algoritmo_subs == 1:
        cache[start] = pos_memoria
    else:
        menor_frequencia = {}
        for key in range(start, keys_range):
              if frequencia[key] in menor_frequencia:
                  menor_frequencia[frequencia[key]].append(key)
              else:
                  menor_frequencia[frequencia[key]] = [key]

        menor = list(menor_frequencia.keys())
        menor.sort()
        posicoes_cache = menor_frequencia[menor[0]]
        cache[random.choice(posicoes_cache)] = pos_memoria       

def mapeamento_associativo_conjunto(pos_memoria):
    tamanho_cache = int(input("Informe o tamanho da cache: "))
    num_conj = int(input("Informe o numero de conjuntos: "))
    while tamanho_cache % num_conj != 0:
        tamanho_cache = int(input("Informe o tamanho da cache: "))
        num_conj = int(input("Informe o numero de conjuntos: "))

    hit = 0
    miss = 0

    algoritmo_subs = menu_algoritmo_subs()
    
    num_blocos = int(tamanho_cache / num_conj)
    cache = inicializar_cache(tamanho_cache)
    frequencia = inicializar_frequencia(tamanho_cache)

    for i in range(len(pos_memoria)):
        print(f"Linha {i} | posição de memória desejada {pos_memoria[i]}")
        conj_cache = pos_memoria[i] % num_conj
        keys_range = (conj_cache + 1) * num_blocos
        start = 0

        if conj_cache != 0:
          start += conj_cache * num_blocos

        pos_cache = procura_cache(cache, start, keys_range, pos_memoria[i])
        if pos_cache != -1:
            hit += 1
            if algoritmo_subs == 1:
              hit_lru(cache, keys_range, pos_cache)
            elif algoritmo_subs == 2:
              frequencia[pos_cache] += 1
      
            print("Status: Hit")
            imprimir_cache(cache)
        else:
          print("Status: Miss") 
          pos_cache = existe_bloco_vazio_cache(cache, start, keys_range)
          if pos_cache != -1:
            cache[pos_cache] = pos_memoria[i]
            miss += 1
            imprimir_cache(cache)
          else:
            miss += 1
            substitui_cache(cache, start, keys_range, pos_memoria[i], algoritmo_subs, frequencia)
            imprimir_cache(cache)


    taxa_acertos = ((hit * 100) / (hit + miss))

    print(f"Memórias acessadas: {len(pos_memoria)}\nNúmero de hits: {hit}\nNúmero de misses: {miss}\nTaxa de acertos (hits): {taxa_acertos:.2f}%") 


# pos_memoria = [0, 1, 2, 3, 1, 4, 5, 6]
#pos_memoria = [1, 0, 3, 2, 1, 0, 3, 2]
# pos_memoria = [1, 0, 3, 2, 4, 6, 5, 7, 1, 4]
#pos_memoria = [0,2,4,6,0,2,4,6,0,2,4,6,0,2,4,6,0,2,4,6,0,8]
pos_memoria = [8,7,12,7,13,8,11,14,8,1,11,9,4,6,8,13,10,11,9,11,14,2,11,1,14,6,11,14,12,10,11,14,4,7,8,3,5,14,6,1,12,1,12,12,1,14,1,5,13,3,14,2,2,13,11,5,1,13,5,12,8,8,13,2,10,3,8,7,6,13,13,14,8,13,6,2,10,7,10,2,10,4,13,8,13,3,2,3,5,14,10,4,4,12,6,5,5,2,12,8,6,3,3,13,7,13,6,6,7,3,9,10,9,10,13,14,9,14,3,7,5,5,3,5,1,5,7,14,2,5,13,6,2,10,1,12,5,8,11,2,5,7,13,2,9,11,8,9,12,14,3,7,3,14,7,1,14,9,6,12,10,4,12,5,4,5,6,5,4,5,3,9,5,12,2,4,2,9,6,14,11,10,8,6,10,12,7,13,10,5,1,12,7,8,6,6,8,5,14,12,3,3,4,1,5,7,6,4,8,8,11,5,11,6,7,3,4,2,6,14,3,4,9,3,8,3,6,11,12,2,12,2,8,12,5,1,13,4,11,8,1,4,2,3,9,9,10,2,3,3,1,8,11,3,10,6,13,12,7,5,10,1,10,10,9,2,12,2,4,8,5,1,5,11,5,11,3,6,9,13,12,13,1,1,8,1,13,11,13,13,11,12,2,12,11,5,8,8,7,5,8,7,6,14,1,2,6,5,5,14,12,4,12,2,10,1,9,14,13,4,4,8,1,14,2,7,5,5,5,14,13,4,11,5,5,9,1,1,4,14,11,4,1,13,7,4,13,12,2,8,13,5,6,3,2,9,3,7,8,13,8,1,3,12,2,7,6,13,2,2,1,5,6,10,8,12,12,4,3,9,7,9,8,14,11,11,7,3,3,10,8,8,10,11,12,10,4,6,2,8,8,10,6,4,4,8,7,9,12,4,7,3,6,12,10,4,9,9,12,9,11,11,10,10,5,2,14,5,12,8,1,7,14,7,2,14,3,6,4,7,13,2,8,14,3,3,12,14,12,14,1,5,5,8,12,7,14,6,3,2,6,10,3,10,13,12,6,2,6,5,1,10,7,2,9,4,14,5,1,5,13,14,4,6,6,11,2,3,2,9,1,2,14,14,12,11,11,4,2,11,3,12,4,8,8,6,5,6,9,2,10,2,5,3,12,14,6,7,2,13,3,9,4,9,4,2,6,7,2,1,2,1,11,10,10,8,3,4,13,8,12,5,3,3,12,2,14,11,8,13,1,6,5,7,4,12,6,10,2,9,11,7,5,7,12,3,4,4,8,4,1,7,13,8,14,11,11,6,1,11,1,1,5,11,2,5,1,5,6,2,13,8,7,14,4,11,13,11,14,6,9,13,13,1,13,6,6,8,2,13,7,5,4,3,6,3,8,4,5,14,13,11,9,8,4,2,4,14,3,13,7,14,9,12,11,5,3,9,10,13,13,9,14,12,3,14,4,1,4,7,3,6,10,3,7,7,7,14,11,11,4,8,2,12,10,6,7,6,11,1,4,9,1,11,6,5,8,10,6,7,1,1,14,13,13,5,6,6,12,2,3,4,2,2,8,7,9,2,9,3,2,4,13,11,9,9,3,6,8,5,13,9,12,6,12,3,11,1,3,5,9,3,9,12,11,12,8,6,10,11,14,2,4,8,12,9,11,12,5,5,6,8,3,12,5,6,5,10,7,10,3,9,9,14,14,6,1,10,6,3,6,14,5,11,6,10,1,8,5,3,4,5,7,10,3,9,1,14,4,6,12,5,14,8,6,14,11,1,5,14,13,8,6,13,12,4,1,3,6,5,4,13,1,14,4,9,7,10,9,9,13,10,2,12,5,2,14,1,8,4,3,2,11,14,13,10,3,1,3,12,9,9,5,4,1,12,11,6,2,5,13,5,10,13,12,1,8,8,5,9,11,13,8,6,14,12,10,3,10,1,7,13,5,14,12,10,12,13,4,13,8,9,8,14,5,14,10,1,9,11,9,14,10,11,4,11,8,11,11,11,11,8,2,13,4,12,14,3,2,5,14,8,4,8,2,13,14,6,1,13,4,6,6,14,13,6,7,4,8,7,10,7,3,2,14,14,3,4,6,11,8,12,3,4,12,10,14,2,14,9,7,1,12,7,7,11,4,12,5,4,14,5,7,8,13,3,12,1,9,1,2,12,14,12,3,8,3,1,3,11,10,9,4,5,8,11,8,12,11,13,11,14,10,13,8,4,3,3,12,4,4,11,5,11,12,6,8,7,5,14]

op = 0
while op != 3:
    op = menu_mapeamento()
    if op == 1:
        mapeamento_direto(pos_memoria)
    elif op == 2:
        mapeamento_associativo_conjunto(pos_memoria)