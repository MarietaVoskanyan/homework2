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


#//


fhand=open('thetext.txt')
d=dict()
ls=list()
for line in fhand:
    line=line.rstrip()
    if not line.startswith("From "):
        continue
    
    words=line.split()
    ls.append(words[1])
new=list()
for i in range(len(ls)):
    ind=0
    a=list(ls[i])
    for j in a:
        if not j=='@':
            ind += 1
            continue
        else:
            
            new.append(a[ind+1:])
            
            new[i]="".join(new[i])
            
for c in new:
    if c not in d:
        d[c]=1
    else:
        d[c] += 1
print(d)


#//


import string
fhand=open('thetext.txt')
d=dict()
word=list()
for line in fhand:
    line=line.translate(str.maketrans('', '', string.punctuation))
    line=line.translate(str.maketrans('', '', string.digits))

    line=line.lower()
    words=line.split()
    for word in words:
        x=list(word)
        for i in x:
            if i not in d:
                d[i]=1
            else:
                d[i] +=1
    
    
for c in word:
    if c not in d:
        d[c]=1
    else:
        d[c] += 1
lst=list()
for key, val in d.items():
    lst.append((val, key))
lst.sort(reverse=True)
for key, val in lst:
    
    print(val)
