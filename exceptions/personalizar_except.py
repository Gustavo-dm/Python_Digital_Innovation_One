class Error(Exception): #herda do built in exception
  pass

class InputError(Error): #herda de erro
  def __init__ (self,message):
    self.message= message


while True:
  try:
    x=int(input('Entre com uma nota de 0 a 10: '))
    print(x)
    if x > 10 or x < 0:
      raise InputError('Digite um valor maior que 0 e menor que 10')
    break;
  except ValueError:
    print('Valor invalido, digite um número')  
  
  except InputError as ex:
    print(ex)