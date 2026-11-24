import random

class Lotto:
    def __init__(self):
        self.numere_extrase = []

    def extract(self):
        while len(self.numere_extrase) < 6:
            numar_nou = random.randint(1, 49)
            if numar_nou not in self.numere_extrase:
                self.numere_extrase.append(numar_nou)

        return self.numere_extrase



if __name__ == "__main__":
    lotto1 = Lotto()
    lotto1.extract()
    print(lotto1.numere_extrase)

