class TabelDispersie:
    def __init__(self, dimensiune):
        self.dimensiune = dimensiune
        self.tabla = [None] * dimensiune

    def functie_dispersie(self, cheie):
        return cheie % self.dimensiune

    def inserare(self, cheie, valoare):
        index = self.functie_dispersie(cheie)
        self.tabla[index] = valoare

    def cautare(self, cheie):
        index = self.functie_dispersie(cheie)
        return self.tabla[index]

# Utilizare
tabela = TabelDispersie(10)
tabela.inserare(27, "Exemplu")
valoare = tabela.cautare(27)
print(valoare)  # Output: Exemplu
