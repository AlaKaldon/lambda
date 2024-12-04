class galeria:
    def __init__(self, kraj, miasto, lokale_handlowe):
        self.kraj = kraj
        self.miasto = miasto
        self.lokale_handlowe = lokale_handlowe
    def __str__(self):
        return '{}{}{}'.format(self.kraj, self.miasto, self.lokale_handlowe)
g = galeria('PL', 'gdansk', [(3, 4), (6, 7), (9,2)])

#zad 2.2
dane = [w.split() for w in open('galerie.txt').readlines()]
galeria= list(map(lambda x: [x[0], x[1], [(int(a), int(b))for a , b in zip(x[2::2], x[3::2])]], dane))
print(dane)
for g in galeria:
    print(g)
for g in galeria:
    if g.miasto == 'Essen':
        print(g.lokale_handlowe[4][1])

#zad 2.3
galerie_sort_miasta = list(sorted(galeria, key=lambda x: x.miasto))
print(g)

#zad 2.4
galerie_sort_powierzchnia = list(sorted(galeria, key=lambda x: sum([a * b for a, b in x.lokale_handlowe if a > 0])))
for g in galerie_sort_powierzchnia:
    print(g)

