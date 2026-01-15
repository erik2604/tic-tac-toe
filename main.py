import management

while True:
    spielfeld =[[" ","1","2","3"],
                ["1","-","-","-"],
                ["2","-","-","-"],
                ["3","-","-","-"]]

    #Namen eingeben
    spielerX = input("Geben Sie den Namen von Spieler X ein: ")
    spielerO = input("Geben Sie den Namen von Spieler O ein: ")
    management.clear_screen() #Terminal clear
    management.print_spielfeld(spielfeld)

    #Symbole der Spieler
    symbole = [(spielerX, "X"),(spielerO, "O")]

    #Spielabbruch bei Unentschieden oder Sieg
    spiel_läuft = True

    #Spielablauf
    while spiel_läuft:
        for name, symbol in symbole:
            print(f"INFO: {name} hat das Zeichen ({symbol}) und ist an der Reihe!")
            management.zug_setzen_spieler(spielfeld, symbol)

            management.clear_screen()
            management.print_spielfeld(spielfeld)

            gewinner = management.gewinner_prüfen(spielfeld)
            if gewinner == symbol:
                print(f"Glückwunsch! {name} hat das Spiel gewonnen!")
                spiel_läuft = False
                break
            
            if management.unentschieden_prüfen(spielfeld):
                print("Unentschieden! Niemand hat gewonnen!")
                spiel_läuft = False
                break

    #Wiederholung des Spiels
    repeat = input("Wollen Sie noch einmal spielen? (y/n)")
    if repeat == "y":
        management.clear_screen()
        continue
    else:
        break



