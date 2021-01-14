
def generate():
  plano = []
  x = 0
  x = 1
  while x < 5:
   cont = 0
   while cont < 1:
    plano.append('GA')
    cont += 1
   cont = 0
   while cont < 2:
    plano.append('M')
    cont += 1
   x = x + 1
  return plano
plano=generate()
print(plano)
