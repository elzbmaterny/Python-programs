def funkcja1_suma(x,y):
    suma = x + y
    return suma

print(funkcja1_suma(1,3))

def liczby_150():
    for i in range(1,51):
        if i%2==0:
            print('kot')
        elif i%3==0:
            print('pies')
        else:
            print(i)
    
liczby_150()    