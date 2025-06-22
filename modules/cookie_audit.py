import requests

SENSITIVE = ['session', 'token', 'auth', 'uid', 'user']

def run():
    print("\n🍪 Audit pédagogique des cookies\n")
    url = input("🔗 URL cible : ").strip()

    try:
        r = requests.get(url)
        cookies = r.cookies

        if not cookies:
            print("❌ Aucun cookie trouvé.")
            return

        for c in cookies:
            print(f"\n🍪 {c.name} = {c.value}")
            print(f"Secure    : {'✅' if c.secure else '❌'}")
            print(f"HttpOnly  : {'✅' if c._rest.get('HttpOnly') else '❌'}")
            risk = 0
            for k in SENSITIVE:
                if k in c.name.lower():
                    print(f"🚩 Nom sensible détecté : '{k}'")
                    risk += 1
            if not c.secure: risk += 1
            if not c._rest.get('HttpOnly'): risk += 1
            print(f"🔐 Score de risque : {risk}/3")
    except Exception as e:
        print(f"❌ Erreur : {e}")
