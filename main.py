import management
import spielmodus_standard

#Hauptmenü
while True:
    management.clear_screen()
    print("-Willkommen zu Tic-Tac-Toe!-")
    print("1) Neues Spiel starten")
    print("2) Regeln anzeigen")
    print("3) Beenden")

    auswahl = input("Bitte wählen Sie: ")

    if auswahl == "1":
        management.clear_screen()
        print("Wählen Sie einen der folgenden Spielmodi aus: ")
        print("1) Spielmodus Standard")
        spielmodus_wählen = input("Bitte wählen Sie: ")
        if spielmodus_wählen == "1":
            management.clear_screen()
            spielmodus_standard.spiel_starten()
    elif auswahl == "2":
        print("Regeln: \n\nSpielmodus Standard: \nSetzen Sie abwechselnd ein X oder ein O. Wer zuerst drei Zeichen ein einer Spalte, Zeile oder Diagonale hat, hat gewonnen!\n")
        input("Weiter mit Enter")
    elif auswahl == "3":
        break
    else:
        print("Ungültige Eingabe!")
        input("Weiter mit Enter")





