from core.engine import run_module
import questionary

def main():
    print("Intrusor - Pédagogie & Pentest\n")

    while True:
        choix = questionary.select(
            " Que veux-tu faire ?",
            choices=[
                " Scan réseau",
                "Audit cookies sensibles",
                "Quitter"
            ]
        ).ask()

        if choix == "Scan réseau":
            run_module("scan")
        elif choix == "Audit cookies sensibles":
            run_module("cookie_audit")
        elif choix == "Quitter":
            print("À bientôt sur Intrusor !")
            break

if __name__ == "__main__":
    main()
