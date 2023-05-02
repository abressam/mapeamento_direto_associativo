def inicializar_cache(tamanho_cache):
    enderecos = {}
    for key in range(tamanho_cache):
        enderecos[key] = -1
    
    return enderecos

def imprimir_cache(cache):
    print(f"Tamanho cache: {len(cache)}")
    print("Pos Cache   |    Posição Memória")
    for key, value in cache.items():
        print(f"          {key} |                 {value}")

def mapeamento_direto(tamanho_cache, pos_memoria):
    # posicao_cache = pos_memoria % tamanho_cache
    enderecos = inicializar_cache(tamanho_cache)

    # print(len(pos_memoria))

    # for i in range(len(pos_memoria)):
    imprimir_cache(enderecos)



    # if enderecos[pos_memoria] == posicao_cache:
    #     hit += 1
    # else:
    #     miss += 1


    

tamanho_cache = int(input("Informe o tamanho da cache: "))
pos_memoria = [33, 3, 11, 5]
mapeamento_direto(tamanho_cache, pos_memoria)
# int(input(f"Informe a(s) posição de memória que deseja acessar (de 0 a {tamanho_cache - 1}): "))
