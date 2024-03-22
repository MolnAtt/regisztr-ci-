from app_tesi.models import Felhasznalo as Tuser, Osztaly as Tosztaly
from app_foglalkozasvalaszto.models import Foglalkozasvalaszto_Felhasznalo as Fuser, Foglalkozasvalaszto_Osztaly as Fosztaly

def transport_osztaly_tesi_foglalkozasvalaszto():
    for tosztaly in Tosztaly.objects.all():
        Fosztaly.objects.get_or_create(
            nev = tosztaly.nev,
            slug = tosztaly.kod,
            sorszam = tosztaly.sorszam,
        )
        

def transport_user_tesi_foglalkozasvalaszto():
    for tuser in Tuser.objects.all():
        Fuser.objects.get_or_create(
            user = tuser.user,
            osztaly = Fosztaly.objects.get(slug=tuser.osztaly.kod),
        )
