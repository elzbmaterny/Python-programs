import math

# n = 6
# m = [2400, 2000, 1200, 2400, 1600, 4000]
# a = [1, 4, 5, 3, 6, 2]
# b = [5, 3, 2, 4, 6, 1]

n= 11
m = [4735, 5525, 4720, 3648, 3280, 3726, 4684, 5959, 3797, 3181, 3585]
a = [4, 11, 6, 5, 2, 3, 10, 7, 9, 8, 1]
b = [11, 8, 6, 1, 5, 4, 9, 2, 3, 10, 7]


licznik_prawd = 0
licznik_zamian = 0
Suma_wszystkieC = 0

while licznik_prawd < n:

    #1. najlższejszy słoń- wybieramy
    #waga
    najlzejszy = min(m)
    #print('waga najlzejszego = ',najlzejszy)
    #numer najlzszejszego (+1)
    najlzejszy_numer = m.index(najlzejszy)+1
    #print('numer najlzejszego ',najlzejszy_numer)
    #gdzie stoi (+1)
    najlzejszy_indeks = a.index(najlzejszy_numer)
    #print('indeks najlzejszego - gdzie stoi = ', najlzejszy_indeks)
    #gdzie powinien stać (+1)
    najlzejszy_indeks_docel = b.index(najlzejszy_numer)
    #print('gdzie powinien stać najlzszejszy = ',najlzejszy_indeks_docel)

    #2. Kto powinien stać na tym miejscu
    na_miejscu_najlzejszego = b[najlzejszy_indeks]
    #print('Kto powinien stać na jego miejscu (nr) = ',na_miejscu_najlzejszego)
    #a gdzie stoi (+1)
    gdzie_stoi_cel = a.index(na_miejscu_najlzejszego)
    #print('gdzie stoi cel = ', gdzie_stoi_cel)

    #jeśli najlższejszy jest na swoim miejscu:
    if na_miejscu_najlzejszego == najlzejszy_numer:
        #print('ten słoń stoi na swoim miejscu')
        #to wybieramy następnego najlższejszego
        licznik_prawd = licznik_prawd + 1
        #print('waga teraz: ',najlzejszy)
        m[najlzejszy_numer-1] = 1000000
        #print('teraz m =',m)

    else:    
        #3. Zamiana
        #przestawiamy tego co ma być tam gdzie najlższejszy
        a[najlzejszy_indeks] = na_miejscu_najlzejszego
        #i odwrotnie
        a[gdzie_stoi_cel] = najlzejszy_numer
        #print('lista po zamianie = ', a)
        licznik_zamian += 1

        #Obliczanie masy
        masa_najlzejszy = m[najlzejszy_numer-1]
        masa_zamienianego = m[na_miejscu_najlzejszego-1]
        sumaC = masa_najlzejszy + masa_zamienianego
        Suma_wszystkieC = Suma_wszystkieC + sumaC
        print('To jest zamiana nr ',licznik_zamian)
        print('Masy słoni = ',sumaC)
        print('Lista po zamianie: ',a)

    #print(' To była iteracja nr', licznik_prawd)
print('\nOstateczny układ = ',a)
print('Całkowita masa = ',Suma_wszystkieC)