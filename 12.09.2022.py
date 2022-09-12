#class - definē klasi

class Auto():
    def _init_(self,modelis,krasa):
        self.modelis = modelis
        self.krasa = modelis

bmw = Auto(modelis = "XS", krasa = "Sarkana")

print(bmw.modelis)

class Auto():
    def _init_(self,modelis,krasa):
        self.modelis = krasa
        self.krasa = krasa

    def dati(self):
        print(f"modelis ir{self.modelis}, krāsa - {self.krasa}")

    def krasas_maina(self, jaunaKrasa):
        print(f"Iepriekšējā auto krāsa - {self.krasa}")
        print(f"Jaunā auto krāsa - {jaunaKrasa}")

audi = Auto(modelis="Q6",krasa="zila")

audi.dati()
audi.krasas_maina("melns")
