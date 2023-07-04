while True:
  k=0 t=1
  line = input('> ')
  if line == 'done':
        break
  k += line
  t *= line
print(k, t)
