
import qrcode
import time
from colorama import init
from colorama import Fore, Back, Style
init()

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

print(Fore.WHITE)
veri = input("Lütfen Kare Kodun içine girecek veriyi yazın ->")
print(Fore.GREEN)
print("Veri qrcode'a yazıldı!")
time.sleep(0.5)
print(Fore.WHITE)

qr.add_data(veri)
qr.make(fit=True)


görüntü = qr.make_image()


kayitbicim = input("Lütfen kayıt biçimini yazın -> -Örn : .png --->")
print(Fore.GREEN)
print("Kayıt biçimi Başarılı")
time.sleep(0.5)
print(Fore.WHITE)

isim = input("QR code ismi ne olsun -->")
print(Fore.GREEN)
print("İsim koyma başarılı!")
time.sleep(0.5)
print(Fore.WHITE)

görüntü.save(isim+kayitbicim)
print(Fore.CYAN)
print(Style.DIM)
print("QR CODE BAŞARIYLA OLUŞTURULDU!")
time.sleep(5)
print("QR CODE BULUNDUĞUNUZ KLASÖRE KAYDEDİLDİ! İyi günler..")
time.sleep(1)
