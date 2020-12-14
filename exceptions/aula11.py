lista = [1,10]
  
try:
  arquivo = open('teste.txt', 'r')
  texto=arquivo.read()
  div= 10/0
  numero=lista[1]
  x = a
except ZeroDivisionError:
  print('Divisão por 0')
except IndexError:
  print('Indice inválido')
except BaseException as ex:
  print(f'Erro desconhecido Erro {ex}')
  
finally:
  print('Sempre executa')
  arquivo.close()