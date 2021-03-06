import requests

cep_input=input('Digite seu cep: ')
if len(cep_input) !=8:
  print('quantidade de digitos invalida')
  exit()
request=requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

adress_data=request.json()
if 'erro' not in adress_data:
  print('CEP: {}'.format(adress_data['cep']))
  print('Rua: {}'.format(adress_data['logradouro']))
  print('Bairro: {}'.format(adress_data['bairro']))
  print('Uf: {}'.format(adress_data['uf']))
else:
  print('O Cep {} não foi encontrado, tente novamente'.format(cep_input))

def retorna_pokemon(pokemon):
  response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
  dados_pokemon=response.json()
  return dados_pokemon

dados_pokemon=retorna_pokemon('pikachu')
print(dados_pokemon['sprites']['front_shiny'])