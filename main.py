lista = [4, 10, 12, 9, 5]
potegi = [(x, x **2, x**3, x**4)for x in lista]
print(potegi)
#zad 1.1
potegi2 = list(map(lambda x: ((x, x **2, x**3, x**4), lista)))
#zad 1.2
lista_dat = ['20241101', '20231223', '20220711', '20230503']
lista_dat_potegi = list(map(lambda x: {'rok': int(x[:4]), 'miesiac': int(x[4:6]), 'dzien': int(x[6:])}, lista_dat))