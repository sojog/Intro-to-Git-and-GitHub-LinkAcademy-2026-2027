class Ticket:
    def __init__(self):
        self.numere = []

    def adauga_numere(self):
        while len(self.numere) < 6:
            nr = int(input("Introdu un nou numar"))
            if nr not in self.numere and nr in range(1, 50):
                self.numere.append(nr)