import management
import spielmodus_standard
import spielmodus_advanced

#Hauptmenü
while True:
    management.clear_screen()
    print("-Willkommen zu Tic-Tac-Toe!-")
    print("1) Neues Spiel starten")
    print("2) Regeln anzeigen")
    print("3) Beenden")

    auswahl = input("\nBitte wählen Sie: ")

    if auswahl == "1":
        management.clear_screen()
        print("Wählen Sie einen der folgenden Spielmodi aus: ")
        print("1) Spielmodus Standard")
        print("2) Spielmodus Advanced")
        spielmodus_wählen = input("\nBitte wählen Sie: ")
        if spielmodus_wählen == "1":
            management.clear_screen()
            spielmodus_standard.spiel_starten()
        elif spielmodus_wählen == "2":
            management.clear_screen()
            spielmodus_advanced.spiel_starten()
    elif auswahl == "2":
        management.clear_screen()
        print("---REGELN---")
        print("\nSpielmodus Standard: \nSetzen Sie abwechselnd ein X oder ein O. Wer zuerst drei Zeichen ein einer Spalte, Zeile oder Diagonale hat, hat gewonnen!\n")
        print("\nSpielmodus Advanced: \nBeim Spielmodus Advanced dürfen pro Spieler nur maximal drei Zeichen auf dem Spielfeld existieren. \nWird ein viertes Symbol gesetzt, so wird das am längsten bestehende Symbol wieder entfernt.\n")
        input("Weiter mit Enter")
    elif auswahl == "3":
        break
    else:
        print("Ungültige Eingabe!")
        input("Weiter mit Enter")





