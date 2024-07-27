## Lista de Supermercado Simples

Este é um programa Python simples que implementa uma lista de supermercado em modo texto. 

![GIF](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWNuNDh1djg5YWVuZmtlazR2dGt6cDRzbjRieGEwaTdnb3lscjBhZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/e6lyxcRngMS1jbTyXS/200.webp)

### Funcionalidades

- **Adicionar Produtos:** Permite adicionar novos produtos à lista, incluindo nome, unidade de medida, quantidade, descrição e um ID gerado automaticamente.
- **Remover Produtos:** Remove um produto da lista usando seu ID único.
- **Pesquisar Produtos:** Busca por produtos na lista pelo nome.
- **Listar Produtos:** Exibe todos os produtos adicionados à lista, mostrando seu nome e ID.
- **Cria um arquivo com a Lista de Produtos:** Cria um arquivo .txt com a lista de produtos e lê toda vez que for executado.

### Como Usar

1. **Clonar o repositório:** 
   ```bash
   git clone https://github.com/seu-usuario/lista-supermercado-simples.git 
   ```

2. **Executar o programa:**
   ```bash
   python lista_supermercado.py
   ```

3. **Navegar pelo menu:**
   - Digite o número correspondente à opção desejada.

### Detalhes da Implementação

- O programa utiliza uma lista chamada `lista_produtos` para armazenar os produtos adicionados.
- Cada produto é representado por um dicionário com as seguintes chaves: `nome`, `unidade`, `quantidade`, `descrição` e `id`.
- Um ID único é gerado para cada produto usando uma combinação da primeira letra do nome, a quantidade e um número aleatório.
- As funções `adiciona_produto`, `remover_prduto` e `pesquisar_produto` implementam as funcionalidades principais do programa.
- O programa utiliza a biblioteca `os` para limpar a tela e oferecer uma interface mais amigável.
- Um bloco `try-except` é utilizado para tratamento básico de exceções, como entrada inválida do usuário.
