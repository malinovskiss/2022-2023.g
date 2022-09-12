class Transportlidzeklis():
    def _init_(self,modelis,krasa,motoraTilpums,atrumkarba):
        self.modelis = modelis
        self.krasa = krasa
        self.motoraTilpums = motoraTilpums
        self.atrumkarba = atrumkarba

    def dati(self):
        print(f"modelis: {self.modelis}")
        print(f"krasa: {self.krasa}")
        print(f"motora tilpums: {self.motoraTilpums}")
        print(f"atrumkarba: {self.atrumkarba}")

auto = Transportlidzeklis("Outlander", "melna", "10", "Manuāla")
auto.dati()