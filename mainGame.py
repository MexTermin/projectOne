from board import *
from modulotabs import *
import os,sys
from exceptions import *

tablet = board("◎","◉")
tablet.makematriz()
tablet.teamsGenerate()


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)


def start():
    tablet.clearWindows()
    if len(tablet.position(tablet.matrice)["rojo"]) == 0 :
        tablet.clearWindows()
        input("           Congratulation player *Negro* you have won the  game, enter to continue...  ")
        return
    if len(tablet.position(tablet.matrice)["negro"]) == 0 :
        tablet.clearWindows()
        input("          Congratulation player *Rojo* you have won the  game, enter to continue...    ")
        return

    #----------------------Make the view to the tablet -----------------------------
    if tablet.turn == "rojo":
        poin = tablet.pteam1
    else:
        poin = tablet.pteam2
    print("Is turn of the team -",tablet.turn, "- you have {} points".format(poin))
    print(tablet.view())
    #-------------------------------------------------------------------------------
    searching = ["rojo"] if  (tablet.turn == "rojo") else ["negro"]
    pos = tablet.position(tablet.matrice)
    targets = []
    #-------------------------------------------------make dame-----------------------------------------------
    tablet.makedame()

    #------------------------------------------------Multi-target------------------------------------------------
    for element in searching:
        for tabs in pos[element]:
            if len(tabs.target(tablet.matrice,tablet.turn) ) > 0: 
                targets.append(tabs.target(tablet.matrice,tablet.turn) )
    #----------------------------------------------Single eat(obligatory)---s--------------------------------------------------------
    if len(targets) == 1:
        view = targets[0]
        view[0][1] =  tablet.translate(view[0][1])
        input("You should eat whit the tab, "+ str(view))
        view[0][1] =  tablet.translate(view[0][1])
        tablet.matrice,tablet.turn,poin = tablet.matrice[targets[0][0][0]] [targets[0][0][1]].eat(targets[0][1],tablet.matrice,poin)
        if tablet.turn == "rojo":
            tablet.pteam2 = poin
        else:
            tablet.pteam1 = poin
        tablet.makedame()
        start()
    #---------------------------------------------------------MultiEat---------------------------------------------------------------------
    elif len(targets) > 1:
        # -----------------------------------------------------Watching targets-------------------------------------------------------------------
        for i in range(len(targets)):
            view = targets[i]
            view[0][1] = tablet.translate(view[0][1])
            print(str(i)+":"+str(view)+"  ", end="")
            view[0][1] = tablet.translate(view[0][1])

        try:
            answer = int(input("  Select one target to eat:  "))
            if answer < 0 or answer > len(targets):
                raise Exception
        except :
            input( "You should type a number between 0 and  " + str(len(targets)-1) )
            start()
        tablet.matrice,tablet.turn,poin= tablet.matrice[targets[answer][0][0] ] [ targets[answer][0][1] ].eat(targets[answer][1],tablet.matrice,poin)
        #--addated point to each team--
        if tablet.turn == "rojo":
            tablet.pteam2 = poin
        else:
            tablet.pteam1 = poin
        start()
    # ------------------------------------------make the move--------------------------------------------------------------------------
    
    types = input("Type de tab and its directions: ").split(" ")

    try:
        #----------------------------------Controller the steps------------------------------------
        tab = (int(types[0][0]),int( tablet.translate(types[0][1])) )
        direction =  str(types[1])
        if direction.upper() != "RD" and direction.upper() != "LD":
            if direction.upper() != "LU" and direction.upper() != "RU":
                tablet.clearWindows()
                input("You should typing correctly direction")
                start()
        if tablet.matrice[tab[0]][tab[1]] ==  []:
            raise invalidmove("Select a correct tab")
        else:
            tablet.turn = tablet.matrice[tab[0]][tab[1]].move(direction,tablet.turn,tablet.matrice)
        #------------------------------------Controller the exceptions-----------------------------
    except invalidmove as e:
        tablet.clearWindows()
        input(str(e))

    except invalidtab as e:
        tablet.clearWindows()
        input(str(e))
    except:
        tablet.clearWindows()
        input("Type a correctly tab")
    #-------------- verify is there's a new dame---------
    tablet.makedame()
    start()

start()

while True:
    answer = input("Type 'Yes' if you wan play again, else type 'No': ")
    if answer.lower() == "yes":
        restart_program()
    elif answer.lower() == "no":
        exit(0)
