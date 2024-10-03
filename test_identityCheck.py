# YKSIKKÖTESTIT MODUULILLE identityCheck.py
import identityCheck

# TESTATAAN ONKO NUMERO 5-6 NUMEROA PITKÄ TAI ONKO NUMERON JOUKOSSA VÄÄRÄ MERKKI
# ------------------------------------------------------------------------------
def test_opiskelijanumeroOk_5():
    assert identityCheck.opiskelijanumeroOk("12345") == True

def test_opiskelijanumeroOk_6():
    assert identityCheck.opiskelijanumeroOk("123456") == True

def test_opiskelijanumeroOk_4():
    assert identityCheck.opiskelijanumeroOk("1234") == False

def test_opiskelijanumeroOk_7():
    assert identityCheck.opiskelijanumeroOk("1234567") == False

def test_opiskelijanumeroOk_kirjain():
    assert identityCheck.opiskelijanumeroOk("12X45") == False
    
# TDD-TESTAUSTA
# -------------

# Henkilötunnus on oikein muodostettu, ei virheitä
def test_checkHetuOK():
    assert identityCheck.checkHetu("130728-478N") == (0, "OK")

# Henkilötunnuksessa pitää olla 11 merkkiä, merkkejä puuttuu
def test_checkHetuShort():
    assert identityCheck.checkHetu("13028-478N") == (1, "Henkilötunnus liian lyhyt")

# Henkilötunnuksessa liikaa merkkejä
def test_checkHetuLong():
    assert identityCheck.checkHetu("1307288-478N") == (2, "Henkilötunnus liian pitkä")

# Henkilötunnuksessa virheellinen päivä
def test_checkHetuDays():
    assert identityCheck.checkHetu("440728-478N") == (3, "Päivä virheellinen")

# Henkilötunnuksessa virheellinen kuukausi
def test_checkHetuMonths():
    assert identityCheck.checkHetu("132728-478N") == (4, "Kuukausi virheellinen")

# Henkilötunnuksessa virheellinen vuosi
def test_checkHetuYears():
    assert identityCheck.checkHetu("1307N8-478N") == (5, "Vuosi virheellinen")

# Henkilötunnuksessa vuosisata virheellinen
def test_checkHetuCenturyCode():
    assert identityCheck.checkHetu("130728sxxxx") == (6, "Vuosisatakoodi virheellinen")

# Henkilötunnuksessa
def test_checkHetuModulo():
    assert identityCheck.checkHetu("130728-478M") == (7, "Varmistussumma ei täsmää")
