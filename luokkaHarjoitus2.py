class Hemmo:
    """yliluokka jossa ei ole yhtään pakollista parametria"""
    def __init__(self,etunimi,sukunimi):
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.harrastukset = []

class Stara(Hemmo):
    """Aliluokka, joka perii Hemmo-luokan ominaisuudet"""
    def __init__(self, etunimi, sukunimi, soitin):
        super().__init__(etunimi, sukunimi)

        self.soitin = soitin

if __name__ == '__main__':
    hemmo1 = Hemmo('Ilkka', 'Lipsanen')
    hemmo2 = Hemmo('Martti', 'Syrjä')
    stara1 = Stara('Heikki','Kuula','vokalisti')

    hemmo1.etunimi = 'Harri'
    hemmo1.sukunimi = 'Harma'
    hemmo1.harrastukset =['keilailua','juoksua']

    print ('Ja tämä hemmo on',hemmo1.etunimi,hemmo1.sukunimi,'joka harrastaa', hemmo1.harrastukset)
    print(stara1.etunimi,stara1.sukunimi,'oli suosittu 1970-luvulla')
    
    