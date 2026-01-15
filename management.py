import os

#Terminal clear
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

#Spielfeld anzeigen
def print_spielfeld(spielfeld):
    i=0
    while i < 4:
        j=0
        while j < 4:
            print(spielfeld[i][j],"  ",end="")
            j = j+1
        print("\n")
        i = i+1



#Spielerzug setzen
def zug_setzen_spieler(spielfeld, symbol, return_coords=False):
    while True:
        try:
            i = int(input("In welcher Zeile wollen Sie Ihr Kreuz setzen? (1-3) "))
            j = int(input("In welcher Spalte wollen Sie Ihr Kreuz setzen? (1-3) "))

            if spielfeld[i][j] != "-":
                print("Dieses Feld ist bereits besetzt!")
                continue

            spielfeld[i][j] = symbol

            if return_coords:
                return i, j
            else:
                return

        except ValueError:
            print("Bitte geben Sie eine gültige Zahl zwischen 1-3 ein!")


#Gewinnstatus überprüfen
def gewinner_prüfen(spielfeld):
#Horizontale Prüfung
    i=1
    while i < 4:
        ergebnis=""
        j=1
        while j < 4:
            ergebnis += spielfeld[i][j]
            j = j+1
        if ergebnis == "XXX":
            return "X"
        elif ergebnis == "OOO":
            return "O"
        i = i+1
#Vertikale Prüfung       
    j=1
    while j < 4:
        ergebnis=""
        i=1
        while i < 4:
            ergebnis += spielfeld[i][j]
            i = i+1
        if ergebnis == "XXX":
            return "X"
        elif ergebnis == "OOO":
            return "O"
        j = j+1  
#Diagonale Prüfung  
    #Diagonale (links-oben/rechts-unten)
    ergebnis = spielfeld[1][1] + spielfeld[2][2] + spielfeld[3][3]
    if ergebnis == "XXX":
        return "X"
    elif ergebnis =="OOO":
        return "O"
    #Diagonale (rechts-oben/links-unten)
    ergebnis = spielfeld[1][3] + spielfeld[2][2] + spielfeld[3][1]
    if ergebnis == "XXX":
        return "X"
    elif ergebnis == "OOO":
        return "O"
    
    return None   


#Unentschieden prüfen
def unentschieden_prüfen(spielfeld):
    i=1
    while i < 4:
        j=1
        while j < 4:
            if spielfeld[i][j] == "-":
                return None
            j = j+1
        i = i+1
    return True