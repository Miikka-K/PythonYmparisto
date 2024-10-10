# LUOKKA HENKILÖTUNNUSTEN KÄSITTELYYN
# ===================================

# KIRJASTOT JA MODUULIT
# ---------------------

# LUOKAT
# ------

# Henkilötunnuksen käsittely
class NationalSSN:
    def __init__(self, ssn) -> None:
        self.ssn = ssn

        # Laskemalla selviävät ominaisuudet
        self.dateOfBirth = ''
        self.number = 0
        self.gender = ''
        self.checkSum = ''

    # Luokan metodi eri osien laskentaan ja järkevyystarkistuksiin
    def mname(self, arg):
        pass