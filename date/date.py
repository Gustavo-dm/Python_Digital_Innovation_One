from datetime import date

def trabalhando_com_date():
  data_atual= date.today()
  #%D=dia  %A=dia de semana  %B=mês  %Y=ano
  data_atual_str = data_atual.strftime('%D %A ' '%B ' '%Y ')
  print(data_atual_str)

trabalhando_com_date()