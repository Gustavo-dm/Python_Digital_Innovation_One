import shutil 
def escrever_arquivo(aluno):
  arquivo = open('notas,txt','w')
  arquivo.write(aluno)
  arquivo.close()

def atualizar_arquivo(nome_arquivo,aluno):

  arquivo = open(nome_arquivo,'a')
  arquivo.write(aluno)
  arquivo.close()

def ler_arquivo(nome_arquivo):
  arquivo = open(nome_arquivo,'r') 
  aluno = arquivo.read()
  #print(aluno)

def copia_arquivo(nome_arquivo):
  shutil.copy(nome_arquivo,'notas2.txt')

#def move_arquivo(nome_arquivo):
  #shutil.move(nome_arquivo,'notas2.txt')


def media_notas(nome_arquivo):
  arquivo = open(nome_arquivo,'r')
  aluno_nota =arquivo.read()
  #print(aluno_nota)
  aluno_nota = aluno_nota.split('\n')

  lista_media= []
  for x in aluno_nota:

    lista_notas=x.split(',')
    aluno=lista_notas[0]
    lista_notas.pop(0)

    
    media=lambda notas:sum([int (i) for i in notas]) / 4
    print(media(lista_notas))
    lista_media.append({aluno:media(lista_notas)})
  return lista_media



#if name == '__main__':
#escrever_arquivo('Primeira linha\n')
lista_media = media_notas('notas.txt')
#aluno='Não lusca,10,10,10\n'
#atualizar_arquivo('notas.txt',aluno)
ler_arquivo('notas.txt')
copia_arquivo('notas.txt')