class Funcionario:
def__init__(self,nome,email):
  self.nome=nome
  self.email=email
  self.horas= {}
  self.salario_hora= {}
defcadastro_hora(self,mes,horas):
  if(mesnotinself.horas):
  self.horas[mes]=horas
defcadastro_salario_hora(self,mes,valor):
  if(mesnotinself.salario_hora):
  self.salario_hora[mes]=valor
defcalcula_salario(self,mes):
  if(mesnotinself.horas)or(mesnotinself.salario_hora):
  print(‘Mês Inexistente!!’)
  else:
return self.horas[mes]*self.salario_hora[mes]
def__repr__(self):
return f’Funcionário:{self.nome}, \nEmail: {self.email},\nhoras/mês: {self.horas}, \nsalário-hora: {self.salario_hora}’

