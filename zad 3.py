#zad 3.1
dane = [x.split() for x in open('dane3.txt').readlines()]
temperatura = [float(x[2]) for x in dane]
temperatura.sort(reverse= True)
print(temperatura)
