import rekins
from rekins import Rekins

def datuIevade():
    klients = input("Ievadi vārdu: ")
    veltijums = input("Ievadi veltījumu: ")
    izmers = input("Ievadi izmēru (platums,garums,augstums): ")
    materials = input("Ievadi materiāla cenu EUR/m2: ")
    dati = Rekins(klients,veltijums,izmers,materials)
    dati.saglabat()
    dati.izdrukat()

while True:
    print('1 - Datu Ievade | 2 - Iziet')
    Izvele = input('Izvelaties darbibu: ')

    if Izvele == '1':
        datuIevade()
    elif Izvele == '2':
        break
    else:
        print('IEVADIET VELAMO IZVELES DARBIBAS NUMURU!')
        continue

import datetime
import csv

class Rekins():
    def __init__(self, klients, veltijums, izmers, materials):
        self.klients = klients
        self.veltijums = veltijums
        self.izmers = izmers.split(',')
        
        self.aprekins()
    
    def aprekins(self):
        darba_samaksa = 15
        PVN = 21
        produkta_cena = len(self.veltijums)*1.2+(int(self.izmers[0])/100*int(self.izmers[1])/100*int(self.izmers[2])/100)/3*self.materials
        PVN_summa = (produkta_cena+darba_samaksa)*PVN/100
        rekina_summa = (produkta_cena+darba_samaksa)+PVN_summa
        return rekina_summa

    def izdrukat(self):
        print(f'Klients: {self.klients}')
        print(f'Veltijums: {self.veltijums}')
        print(f'Izmers: {self.izmers}')
        print(f'Materials: {self.materials}')
        print(f'Laiks: {self.laiks}')
        print(f'Rekina Summa: {self.aprekins()}')

    def saglabat(self):
        with open('rekini.csv', 'a',encoding="utf-8",newline='') as fails:
            csvwrite = csv.writer(fails)
            csvwrite.writerow(['Klienta vārds','Veltījums','Izmēri','Materiāla cena','Laiks','Cena'])
            csvwrite.writerow([self.klients,self.veltijums,self.izmers,self.materials,self.laiks,self.aprekins()])