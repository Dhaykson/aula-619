banco_de_dados = [
{
  'codigo': 1,
  'nome': 'mouse',
  'preco': 150.50,
  'disponivel': True
}
]

codigo_atual = 1

def cadastrar_produto(nome: str, preco: float) -> None:
  global codigo_atual
  codigo_atual += 1
  produto = {
    "codigo": codigo_atual,
    "nome": nome,
    "preco": preco,
    "disponivel": True
  }
  banco_de_dados.append(produto)
  print('Produto adicionado com sucesso')

def listar_produtos():
  print('---PRODUTOS CADASTRADOS---')
  for produto in banco_de_dados:
    print(f"Código': {produto['codigo']}")
    print(f"Nome: {produto['nome']}")
    print(f"Preço: {produto['preco']}")
    print(f"Disponivel': {produto['disponivel']}")
    print('-'*50)
  
def buscar_produto(codigo: int):
  for produto in banco_de_dados:
    if produto ['codigo'] == codigo:
      return produto
  return None

def deletar_produto(codigo: int):
  produto = buscar_produto(codigo)
  if produto:
    banco_de_dados.remove(produto)
    print('Produto removido com sucesso!')
    return  
  print('Produto não encontrado!')
  

def editar_produto(codigo: int, nome: str, preco: float):
  produto = buscar_produto(codigo)
  if produto:
    produto['nome'] = nome
    produto['preco'] = preco
    print('produto editado com sucesso!')
    return
  print('Produto não encontrado!')

def menu():
  print('--- BEM VINDO AO MENU ---')
  while True:
    print('1 - Adicionar produto')
    print('2 - Editar produto')
    print('3 - Listar produtos')
    print('4 - Buscar produto')
    print('5 - Deletar produto')
    print('0 - Sair')
    opcao = input('Selecione a opção: ')
    if opcao == '1':
      nome = input('Digite o nome do produto: ')
      preco = float(input('Digite o valor do produto: '))
      cadastrar_produto(nome, preco)
    elif opcao == '2':
      codigo = int(input('Digite o código do produto: '))  
      nome = input('Digite o nome do produto: ')
      preco = float(input('Digite o preço do produto: '))
      editar_produto(codigo, nome, preco)
    elif opcao == '3':
      listar_produtos()
    elif opcao == '4':
      codigo = int(input('Digite o codigo do produto: '))
      print(buscar_produto(codigo))  
    elif opcao == '5':
      codigo = int(input('Digite o codigo do produto: '))
      deletar_produto(codigo)
    elif opcao == '0':
      print('você saiu do programa!')
      break    
    else:
      print('opção Inválida')


menu()
