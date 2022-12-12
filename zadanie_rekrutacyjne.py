wejscie = 'slo2ocen.in'




#Wczytywanie pliku
import linecache
n = (linecache.getline(wejscie, 1))
n = int(n)
m = (linecache.getline(wejscie, 2))
m = list(int(x) for x in m.split()) 
a = linecache.getline(wejscie, 3)
a = list(int(x) for x in a.split()) 
b = linecache.getline(wejscie, 4)
b = list(int(x) for x in b.split()) 

n_origin = (linecache.getline(wejscie, 1))
n_origin = int(n_origin)
m_origin = (linecache.getline(wejscie, 2))
m_origin = list(int(x) for x in m_origin.split()) 
a_origin = linecache.getline(wejscie, 3)
a_origin = list(int(x) for x in a_origin.split()) 
b_origin = linecache.getline(wejscie, 4)
b_origin = list(int(x) for x in b_origin.split()) 


#Funkcja
def slonie(n,m,a,b):
    licznik_prawd = 0
    licznik_zamian = 0
    Suma_wszystkieC = 0

    while licznik_prawd < n:

        #1. najlższejszy słoń- wybieramy
        #waga
        najlzejszy = min(m)
        #numer najlzszejszego (+1)
        najlzejszy_numer = m.index(najlzejszy)+1
        #gdzie stoi (+1)
        najlzejszy_indeks = a.index(najlzejszy_numer)
        #gdzie powinien stać (+1)
        najlzejszy_indeks_docel = b.index(najlzejszy_numer)

        #2. Kto powinien stać na tym miejscu
        na_miejscu_najlzejszego = b[najlzejszy_indeks]
        #a gdzie stoi (+1)
        gdzie_stoi_cel = a.index(na_miejscu_najlzejszego)

        #jeśli najlższejszy jest na swoim miejscu:
        if na_miejscu_najlzejszego == najlzejszy_numer:
            #to wybieramy następnego najlższejszego
            licznik_prawd = licznik_prawd + 1
            m[najlzejszy_numer-1] = 1000000

        else:    
            #3. Zamiana
            #przestawiamy tego co ma być tam gdzie najlższejszy
            a[najlzejszy_indeks] = na_miejscu_najlzejszego
            a[gdzie_stoi_cel] = najlzejszy_numer
            licznik_zamian += 1

            #Obliczanie masy
            masa_najlzejszy = m[najlzejszy_numer-1]
            masa_zamienianego = m[na_miejscu_najlzejszego-1]
            sumaC = masa_najlzejszy + masa_zamienianego
            Suma_wszystkieC = Suma_wszystkieC + sumaC

    return Suma_wszystkieC


wyjscie = slonie(n,m,a,b)
print(n_origin,'\n',m_origin,'\n',a_origin,'\n',b_origin,'\n',wyjscie)