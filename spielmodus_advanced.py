import management

def spiel_starten():
    while True:
        spielfeld = [
            [" ", "1", "2", "3"],
            ["1", "-", "-", "-"],
            ["2", "-", "-", "-"],
            ["3", "-", "-", "-"]
        ]

        #Namen eingeben
        spielerX = input("Geben Sie den Namen von Spieler X ein: ")
        spielerO = input("Geben Sie den Namen von Spieler O ein: ")

        #Listen für gesetzte Symbole
        positionen_X = []
        positionen_O = []

        management.clear_screen()
        management.print_spielfeld(spielfeld)

        symbole = [
            (spielerX, "X", positionen_X),
            (spielerO, "O", positionen_O)
        ]

        spiel_laeuft = True

        while spiel_laeuft:
            for name, symbol, liste in symbole:
                print(f"INFO: {name} hat das Zeichen ({symbol}) und ist an der Reihe!")
                
                #Spieler setzt Symbol
                i, j = management.zug_setzen_spieler(spielfeld, symbol, return_coords=True)

                #Neue Position speichern
                liste.append((i, j))

                #Wenn mehr als 3 Steine → ältesten entfernen
                if len(liste) > 3:
                    alt_i, alt_j = liste.pop(0)
                    spielfeld[alt_i][alt_j] = "-"

                management.clear_screen()
                management.print_spielfeld(spielfeld)

                #Gewinner prüfen
                gewinner = management.gewinner_prüfen(spielfeld)
                if gewinner == symbol:
                    print(f"Glückwunsch! {name} hat gewonnen!")
                    spiel_laeuft = False
                    break

                #Unentschieden prüfen
                if management.unentschieden_prüfen(spielfeld):
                    print("Unentschieden!")
                    spiel_laeuft = False
                    break

        #Wiederholung des Spiels
        repeat = input("Wollen Sie noch einmal spielen? (y/n)")
        if repeat == "y":
            management.clear_screen()
            continue
        else:
            break