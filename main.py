def inicializar_cache(tamanho_cache):
    enderecos = {}
    for key in range(tamanho_cache):
        enderecos[key] = -1
    
    return enderecos

def imprimir_cache(cache):
    print(f"Tamanho cache: {len(cache)}")
    print("Pos Cache  |    Posição Memória")
    for key, value in cache.items():
        print(f"{key:>10} |{value:>20}")
    
    print("\n")

def mapeamento_direto(tamanho_cache, pos_memoria):
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
                    print(f"Status: Hit")
                    imprimir_cache(enderecos)
                else:
                    value = pos_memoria[i]
                    enderecos[posicao_cache] = value
                    miss += 1
                    print(f"Status: Miss")
                    imprimir_cache(enderecos)

    
    taxa_acertos = ((hit * 100) / (hit + miss))

    print(f"\nMemórias acessadas: {len(pos_memoria)}\nNúmero de hits: {hit}\nNúmero de misses: {miss}\nTaxa de acertos (hits): {taxa_acertos:.2f}%")    

tamanho_cache = 5
pos_memoria = [0, 1, 2, 3, 1, 4, 5, 6]
mapeamento_direto(tamanho_cache, pos_memoria)
