import management

spielfeld =[[" ","1","2","3"],["1","-","-","-"],["2","-","-","-"],["3","-","-","-"]]

#Namen eingeben
spielerX = input("Geben Sie den Namen von Spieler X ein: ")
spielerO = input("Geben Sie den Namen von Spieler O ein: ")
management.print_spielfeld(spielfeld)

while True:
    management.zug_setzen_spielerX(spielfeld)
    management.print_spielfeld(spielfeld)
    gewinner = management.gewinner_prüfen(spielfeld)
    if gewinner == "X":
        print(f"Glückwunsch! {spielerX} hat das Spiel gewonnen!")
        break
    elif gewinner == "O":
        print (f"Glückwunsch! {spielerO} hat das Spiel gewonnen!")
        break
    management.zug_setzen_spielerO(spielfeld)
    management.print_spielfeld(spielfeld)
    gewinner = management.gewinner_prüfen(spielfeld)
    if gewinner == "X":
        print(f"Glückwunsch! {spielerX} hat das Spiel gewonnen!")
        break
    elif gewinner == "O":
        print (f"Glückwunsch! {spielerO} hat das Spiel gewonnen!")
        break




