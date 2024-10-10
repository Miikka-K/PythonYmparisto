# LUOKKA HENKILÖTUNNUSTEN KÄSITTELYYN
# ===================================

# KIRJASTOT JA MODUULIT
# ---------------------
from datetime import datetime
# LUOKAT
# ------

# Henkilötunnuksen käsittely
class NationalSSN:
    """Various methods to access and validate Finnish Social Security Number properties"""

    def __init__(self, ssn: str) -> None:

        """Generates a Finnish SSN object

        Args:
            ssn (str): 11 char SSN to process
        """

        self.ssn = ssn

        # Laskemalla selviävät ominaisuudet
        self.dateOfBirth = ''
        self.number = 0
        self.gender = ''
        self.checkSum = ''

    # Luokan metodi eri osien laskentaan ja järkevyystarkistuksiin

    # Tarkistetaan, että HeTu:n pituus on 11 merkkiä pitkä
    def checkSsnLengthOk(self) -> bool:
        """Checks the length of SSN

        Returns:
            bool: True if 11 else False
        """
        ssnLength = len(self.ssn)
        if ssnLength != 11:
            return False
            # TODO: Mieti pitäisikö tässä generoida virheilmoitus (raise)
        else:
            return True
            
        
    # Pilkotaan henkilötunnus osiin
    def splitSsn(self) -> dict:
        """Splits SSN into day,month,year,century,birthnumber,and sum

        Returns:
            dict: splitted SSN for validation and age calculation
        """
        # Tehdään pilkkominen vain jos pituus on oikein (11)
        if self.checkSsnLengthOk(): # Jos True, pilkotaan HeTu osiin tarkistusta varten, huom. self.metodinNimi
            dayPart = self.ssn[0:2]             # Pilkotaan Päiväosuus
            monthPart = self.ssn[2:4]           # Pilkotaan kuukausiosuus
            yearPart = self.ssn[4:6]            # Pilkotaan vuosiosuus
            centuryPart = self.ssn [6:7]        # Pilkotaan vuosisataosuus
            birthNumberPart = self.ssn [7:10]   # Pilkotaan loppuosa
            checksumPart = self.ssn [10]        # Pilkotaan viimeinenosa
            if dayPart.isdigit() and monthPart.isdigit() and yearPart.isdigit():
                return {
            "day": dayPart,
            "month": monthPart,
            "year": yearPart,
            "century": centuryPart,
            "birthnumber": birthNumberPart,
            "checksum": checksumPart}
            else:
                # TODO: Mieti pitäisikö tässä generoida virheilmoitus (raise)
                return {'status': 'error'}

    # Muutetaan syntymäaikaosa ja vuosisata päivämääräksi
    def getDateOfBirth(self) -> datetime:
        ssnParts = self.splitSsn()
        if 'status' in ssnParts:
            raise ValueError("Invalid SSN format") # Raise jos SSN on väärä
        # Haetaan vuosi, kuukausi ja päivä integerinä
        day = int(ssnParts["day"])
        month = int(ssnParts["month"])
        year = int(ssnParts["year"])
        century = ssnParts["century"]
         # Vuosisatakoodien sanakirja
        centuryCodes = {
        "+": 1800,
        "-": 1900,
        "A": 2000
        }
        # Muutetaan vuosi koko vuodeksi
        if century in centuryCodes:
            fullYear = centuryCodes[century] + year
        else:
            raise ValueError("Invalid century code") # Nostetaan virhe jos century code on väärä

        dateOfBirth = datetime(fullYear,month,day)
        return dateOfBirth

    # Lasketaan ikä nyt täysinä vuosina
    def calculateAge(self, arg):
        pass
    
    # Tarkistetaan onko ssn oikein
    def isValid(self, arg):
        pass

# MAIN KOKEILUJA VARTEN (Poista kun ei käyttöä)
# ---------------------

if __name__ == "__main__":
    hetu1 = NationalSSN('111256-8101')
    print(hetu1.checkSsnLengthOk())
    print(hetu1.splitSsn())
    print(hetu1.getDateOfBirth())