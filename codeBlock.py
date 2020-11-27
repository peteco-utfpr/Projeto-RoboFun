
def generate():
  plano = []
  cont = 0
  while cont < 3:
   plano.append('GA')
   cont += 1
  cont = 0
  while cont < 7:
   plano.append('M')
   cont += 1
  return plano
plano=generate()