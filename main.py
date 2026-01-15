import management
import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

spielfeld =[[" ","1","2","3"],["1","-","-","-"],["2","-","-","-"],["3","-","-","-"]]

#Namen eingeben
spielerX = input("Geben Sie den Namen von Spieler X ein: ")
spielerO = input("Geben Sie den Namen von Spieler O ein: ")
clear_screen() #Terminal clear
management.print_spielfeld(spielfeld)

#Spielablauf
while True:
    print(f"INFO: {spielerX} hat das Zeichen (X) und ist an der Reihe!")
    management.zug_setzen_spielerX(spielfeld)
    clear_screen() #Terminal clear
    management.print_spielfeld(spielfeld)
    gewinner = management.gewinner_prüfen(spielfeld)
    if gewinner == "X":
        print(f"Glückwunsch! {spielerX} hat das Spiel gewonnen!")
        break
    elif gewinner == "O":
        print (f"Glückwunsch! {spielerO} hat das Spiel gewonnen!")
        break

    print(f"INFO: {spielerO} hat das Zeichen (O) und ist an der Reihe!")
    management.zug_setzen_spielerO(spielfeld)
    clear_screen() #Terminal clear
    management.print_spielfeld(spielfeld)
    gewinner = management.gewinner_prüfen(spielfeld)
    if gewinner == "X":
        print(f"Glückwunsch! {spielerX} hat das Spiel gewonnen!")
        break
    elif gewinner == "O":
        print (f"Glückwunsch! {spielerO} hat das Spiel gewonnen!")
        break




