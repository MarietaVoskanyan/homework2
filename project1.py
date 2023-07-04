k=0
t=1
while True:
    try:
        line = input('> ')
        if line == 'done':
            break
        k = k + int(line)
        t = t * int(line)
    except:
        print('Bad data')
print(k, t)
