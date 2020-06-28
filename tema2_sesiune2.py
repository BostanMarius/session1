def solution(a='gddfcv'):
    b=[]
    if len(a)%2==0:
        lungimepara=len(a)
        print(lungimepara)
        n=0
        while n < lungimepara:
                b.append(a[n]+a[n+1])
                n+=2
    else:
        lungimeimpara=len(a)
        print(lungimeimpara)
        n = 0
        while n < lungimeimpara:
            if n  == lungimeimpara-1:
                b.append(a[n] + '_')
            else:
                b.append(a[n] + a[n + 1])
            n += 2

    print(b)

def words(d='This is an example!'):
    d=d.split()
    g=d[0]
    c=g[::-1]+' '
    n=1
    while n < len(d):
        f=d[n]
        if n==len(d)-1:
            c+= f[::-1]
        else:
            c+=f[::-1]+' '
        n+=1
    print(c)

class Human():
    def __init__(self,name):
        self.name=name
    def create(self,name1,name2):
        c=[]
        c.append(name1)
        c.append(name2)
        return c

class Man(Human):
    pass
class Women(Human):
    pass

solution('abcdefghj')
words()
adam=Man("Adam")
eve=Women("Eve")
god=Human("God")
array=god.create(adam.name,eve.name)

print(array)