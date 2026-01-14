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



#Spielerzüge setzen
def zug_setzen_spielerX(spielfeld):
    eingabe_i = int(input("In welcher Zeile wollen Sie Ihr Kreuz setzen? (1-3) "))
    eingabe_j = int(input("In welcher Spalte wollen Sie Ihr Kreuz setzen? (1-3) "))
    spielfeld[eingabe_i][eingabe_j] = "X"

def zug_setzen_spielerO(spielfeld):
    eingabe_i = int(input("In welcher Zeile wollen Sie Ihr Kreuz setzen? (1-3) "))
    eingabe_j = int(input("In welcher Spalte wollen Sie Ihr Kreuz setzen? (1-3) "))
    spielfeld[eingabe_i][eingabe_j] = "O"



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


