# MODUULI VIDEOKUVAN KÄSITTELYYN
# ==============================

# KIRJASTOT JA MODUULIT
# ---------------------

# Ulkoinen kirjasto opencv-python tallentuu nimellä CV2
import cv2

# FUNKTIO, JOKA KÄYNNISTÄÄ WEB-KAMERAN JA NÄYTTÄÄ KUVAA IKKUNASSA
# ---------------------------------------------------------------

def webstream(camIx):
    """Opens a video stream and shows frames in a window

    Args:
        camIx (int): Index of the camera used starting from 0
    """
    # Ikkunan nimi ja video striimi kamera indeksillä
    ikkuna = "Kamera" + str(camIx)

    # Objekti joka tallentaa videota striimiin
    capture = cv2.VideoCapture(camIx)

    # IKUINEN SILMUKKA KAMERALLE
    # ==========================

    # while loop joka pitää ohjelman käynnissä
    while capture.isOpened():
        ret, frame = capture.read()

        # jos ei striimiä tule, lopetetaan ohjelma
        if not ret:
            print("Ei voi saada videokuvaa, lopetetaan...")
            break

        # päätetään nappi jolla voi lopettaa ohjelman
        cv2.imshow(ikkuna, frame)
        if cv2.waitKey(1) == ord('q'):
            break

    # Vapautetaan lopuksi muisti ja tuhotaan ikkuna
    capture.release()
    cv2.destroyAllWindows()

# TESTIT
# ------
if __name__ == "__main__":
    webstream(0)
