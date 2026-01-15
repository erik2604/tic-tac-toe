import management

spielfeld =[[" ","1","2","3"],["1","-","-","-"],["2","-","-","-"],["3","-","-","-"]]

#Namen eingeben
spielerX = input("Geben Sie den Namen von Spieler X ein: ")
spielerO = input("Geben Sie den Namen von Spieler O ein: ")
management.clear_screen() #Terminal clear
management.print_spielfeld(spielfeld)

#Spielablauf
while True:
    print(f"INFO: {spielerX} hat das Zeichen (X) und ist an der Reihe!")
    management.zug_setzen_spieler(spielfeld, "X")
    management.clear_screen() #Terminal clear
    management.print_spielfeld(spielfeld)

    if management.unentschieden_prüfen(spielfeld):
        print("Unentschieden! Niemand hat gewonnen!")
        break
    
    gewinner = management.gewinner_prüfen(spielfeld)
    if gewinner == "X":
        print(f"Glückwunsch! {spielerX} hat das Spiel gewonnen!")
        break
    elif gewinner == "O":
        print (f"Glückwunsch! {spielerO} hat das Spiel gewonnen!")
        break

    print(f"INFO: {spielerO} hat das Zeichen (O) und ist an der Reihe!")
    management.zug_setzen_spieler(spielfeld, "O")
    management.clear_screen() #Terminal clear
    management.print_spielfeld(spielfeld)

    if management.unentschieden_prüfen(spielfeld):
        print("Unentschieden! Niemand hat gewonnen!")
        break

    gewinner = management.gewinner_prüfen(spielfeld)
    if gewinner == "X":
        print(f"Glückwunsch! {spielerX} hat das Spiel gewonnen!")
        break
    elif gewinner == "O":
        print (f"Glückwunsch! {spielerO} hat das Spiel gewonnen!")
        break




