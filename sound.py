# MODUULI ÄÄNIMERKKIEN ANTAMISEEN
# ===============================

# KIRJASTOT JA MODUULIT
# ---------------------

# Windows-äänet
import winsound

# Ajankäsittely
import time

# WAIT FUNKTIO
# ------------

def waitMs(ms):
    """Waits for X milliseconds

    Args:
        ms (int): time in milliseconds
    """
    seconds = ms / 1000
    time.sleep(seconds)

# ÄÄNIFUNKTIOT
# ------------

def shortBeep():
    """Creates a 1 kHz sound for 250 milliseconds"""
    winsound.Beep(1000, 250) # suluissa herzit ja äänen kesto

def longBeep():
    """Creates a 1 kHz sound for 1 seconds"""
    winsound.Beep(1000, 1000)


# Säädettävät äänet 1. korkeus ja kesto parametreina
def parametricBeep(frequency, duration):
    """produces a sound at given frequency and duration

    Args:
        frequency (int): in hertz
        duration (int): in milliseconds
    """
    winsound.Beep(frequency, duration)

# Säädettävät äänet 2. toistuva äänimerkki korkeus, kesto ja määrä
def repeatingBeep(frequency: int, duration: int, count: int) -> None:
    """Creates a repeating buzzer sound

    Args:
        frequency (int): Tone frequency in Hz
        duration (int): Duration of the single tone in ms
        count (int): How many times sound repeats
    """
    for i in range(count):
        winsound.Beep(frequency, duration)
        waitMs(250)


# Ääni tulee halutusta tiedostosta, parametrina äänen nimi
def playWav(fileName: str) -> None:
    """Plays a wav sound file

    Args:
        fileName (str): Name of the audiofile
    """
    winsound.PlaySound(fileName, winsound.SND_FILENAME)

# TESTIT
# ======
if __name__ == "__main__":
    repeatingBeep(1000,250,5)