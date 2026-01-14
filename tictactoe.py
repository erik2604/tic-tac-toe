spielfeld =[[" ","1","2","3"],["1","-","-","-"],["2","-","-","-"],["3","-","-","-"]]

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

#Namen eingeben
spielerX = input("Geben Sie den Namen von Spieler X ein: ")
spielerO = input("Geben Sie den Namen von Spieler O ein: ")
print_spielfeld(spielfeld)


#Gewinnstatus überprüfen
ergebnis = 0
for i in spielfeld:
    ergebnis = spielfeld[i][ergebnis] + ergebnis
print(ergebnis)