# trazendo a biblioteca capaz de realizar requisições 
import requests
import random

# uma variável chamada url que armazena o endereço com as infos que desejo buscar
url = 'https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json'
# faço a requisição e armazeno em uma variável chamada resposta
resposta = requests.get(url)
# transforma a resposta em JSON
data =resposta.json()
# exibindo as informações com o comando print
print(data)
# acessando as informações
data[0]
#variável chamada valor secreto que armazena uma tecnologia aleatória da lista
valor_secreto = random.choice(data)
# variável para armazenar apenas a palavra
palavra_secreta = valor_secreto['palavra']
# variável para armazenar apenas a dica
dica = valor_secreto['dica']
# mostra na tela quantas letras a palavra secreta possui e a dica
# o f é capaz de juntar/combinar palavras e variáveis
print(f'A palavrar secreta tem {len(palavra_secreta)} letras')
print(f'A dica é -> {dica}')
chute = input('O uqe você acha que é ')
if chute == palavra_secreta:
  print('Acertou')
else:
 print(f'Errou.. a palavra secreta era {palavra_secreta}')
