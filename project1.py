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


#//

fruit = 'banana'
index = -1
while (-index) < (len(fruit)+1):
    letter = fruit[index]
    print(letter)
    index = index - 1
