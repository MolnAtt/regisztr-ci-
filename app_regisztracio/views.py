from django.shortcuts import render
from django.contrib.auth.models import Group, User
from validate_email import validate_email 
from seged import tagja

def regisztracio(request):
    if request.user.is_authenticated:
        return render(request, 'regisztracio/visszajelzes.html', {
                    'hosszu': f'Sőt, be is van jelentkezve, {request.user.last_name} {request.user.first_name}.',
                    'rovid': 'Már regisztrált az oldalra.',
                })

    if request.method == "GET":
        return render(request, 'regisztracio/regisztracio.html')
    
    if request.method == "POST":
        a_username = request.POST['email']

        if not validate_email(a_username):
            return render(request, 'regisztracio/visszajelzes.html', {
                        'rovid': 'Sikertelen regisztráció',
                        'hosszu': 'Ez az email-cím nem helyes. Nézze meg, nem gépelte-e el!'
                    })

        if User.objects.filter(username=a_username).exists():
            return render(request, 'regisztracio/visszajelzes.html', {
                        'rovid': 'Sikertelen regisztráció',
                        'hosszu': 'Ezzel az email-címmel már korábban regisztráltak fiókot ezen az oldalon. Próbálkozzon más email-címmel vagy használja a jelszó-emlékeztető funkciót!'
                    })
        
        
        a_user = User.objects.create_user(
            username = a_username,
            password = request.POST['password'],
            email = a_username,
            last_name = request.POST['last_name'],
            first_name = request.POST['first_name'],
        )

        idegen_regisztralok_csoportja, _ = Group.objects.get_or_create(name='idegen_regisztralo')
        a_user.groups.add(idegen_regisztralok_csoportja)

        return render(request, 'regisztracio/visszajelzes.html', {
                    'rovid': 'Sikeres regisztráció',
                    'hosszu': 'Sikeresen regisztrált fiókot a Kőbányai Szent László Gimnázium applikációs oldalán.'
                })


def valaszto(request):
    context = {
        'linkek': [
            # {'url': 'felveteli', 'nev': 'Felvételi', },
            # {'url': 'kar', 'nev': 'Kárbejelentő', },
            { 'url': 'fogadoora', 'nev': 'Fogadóóra', },
            { 'url': 'polo', 'nev': 'Pólórendelés', },
            { 'url': 'nyiltnap', 'nev': 'Nyílt napok', },
            { 'url': 'szuloitajekoztato', 'nev': 'Nyílt napi szülői tájékoztatók', },
            { 'url': 'tesi', 'nev': 'Testnevelés +2 óra', },
            { 'url': 'matekverseny', 'nev': 'Matematikaverseny', },
            { 'url': 'foglalkozasvalaszto/palyaorientacio_2024', 'nev': 'Pályaorientáció 2024', },
        ]
        }
    
    if request.user.is_authenticated:
        if tagja(request.user, 'admin'):
            context['linkek'].append(
                {'url': 'admin', 'nev': 'Adminisztráció', }
                )
        context['linkek'].append(
            {'url': 'accounts/logout', 'nev': 'Kijelentkezés', },
        )
    else:
        context['linkek'] += [
            {'url': 'regisztracio', 'nev': 'Regisztráció', },
            {'url': 'accounts/login', 'nev': 'Bejelentkezés', },
        ]

    return render(request, "regisztracio/valaszto.html", context)
