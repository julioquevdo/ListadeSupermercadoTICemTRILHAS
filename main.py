import os
import random

lista_produtos = []


def main():
    os.system("cls")
    print("Lista de Supermercado Simples\n\n")
    for indice, i in enumerate(lista_produtos):
        print(f"{indice+1} - Nome: {i["nome"]} --- ID: {i["id"]}")

    print("1 - Adicionar Produto")
    print("2 - Remover Produto")
    print("3 - Pesquisar Produto")
    print("4 - Sair do Programa")
    
    try:
        escolha = int(input("\nDigite sua opção: "))
        if escolha == 1:
            os.system("cls")
            adiciona_produto()
        elif escolha == 2:
            os.system("cls")
            remover_prduto()
        elif escolha == 3:
            os.system("cls")
            pesquisar_produto()
        elif escolha == 4:
            os.system("cls")
            print("Obrigado por testar a Lista de Supermercado Simples!")
    except:
        print("não rolou")

def adiciona_produto():
    print("ADICIONAR UM PRODUTO")
    nome_produto = input("Escreva o nome do produto: ")
    print("""\nQuilograma (KG)  
Grama (G)  
Litro (L)  
Mililitro (ML)  
Unidade  
Metro (M)  
Centímetro (CM)""")
    unidade_medida = input("\nDigite a unidade de medida: ")
    quantidade = input("Digite a quantidade desse produto: ")
    descrição = input("Digite a descrição desse produto (opcional): ")
    novo_produto = {
        "nome": nome_produto,
        "unidade": unidade_medida,
        "quantidade": quantidade,
        "descrição" : descrição,
        "id": (nome_produto[0] + quantidade + str(round(random.random()* 100)))
    }
    lista_produtos.append(novo_produto)
    input("Aperte ENTER para voltar ao menu inicial: ")
    main()



def remover_prduto():
    if len(lista_produtos) == 0:
        print("Não tem nenhum item na lista para você remover")
        input("Aperte ENTER para voltar ao menu inicial: ")
        main()
    else:
        for i in lista_produtos:
            print(f"Nome: {i["nome"]} --- ID: {i["id"]}")
            print("\nDigite '0' para sair")
        resposta = input("Digite o ID do item que você deseja remover: ")
        if resposta == "0":
            main()
        else:
            for i in lista_produtos:
                if i["id"] == resposta:
                    lista_produtos.remove(i)
                    print("O produto foi removido de sua lista")
                    input("Aperte ENTER para voltar ao menu inicial: ")
                    main()
                else:
                    print("produto não encontrado")
                    input("Aperte ENTER para voltar ao menu inicial: ")
                    main()


def pesquisar_produto():
    if len(lista_produtos) == 0:
        print("Não tem nenhum item na lista")
        input("Aperte ENTER para voltar ao menu inicial: ")
        main()
    else:
        resposta = input("Digite o nome do Item que você deseja procurar: ")
        for i in lista_produtos:
            if resposta in i["nome"]:
                print(f"""PRODUTOS ENCONTRADO:
Nome e ID: {i["nome"]} - {i["id"]}, Quantidade: {i["quantidade"]}, Unidade: {i["unidade"]}, Descrição: {i["descrição"]} """)
                input("Aperte ENTER para voltar ao menu inicial: ") 
                main()
            else:
                print("Nenhum produto foi encontrado")
                input("Aperte ENTER para voltar ao menu inicial: ") 
                main()


if __name__ == "__main__":
    main()