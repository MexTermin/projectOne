from modulotabs import *
from coloreshell import *
import os
class board:

    def __init__(self,symbol,dameSymbol):

        self.matrice = []
        self.turn = "negro"
        self.dameSymbol = dameSymbol
        self.symbol = symbol
        self.pteam1 = 0
        self.pteam2 = 0

    def makematriz(self):
        # this method make the principal matrice
        for ypos in range(0,9):
            self.matrice.append([])
            for xpos in range (0,9):
                self.matrice[ypos].append([])

    def CreateTeam(self,team,start,row):
        """[summary]
            this function generate the teams
        Arguments:
            simbol {[string]} -- [a letter that represents the teams]
            start {[int]} -- [is the initial column of the board where the team will be place]
            row {[int]} -- [is the initial row of the board where the team will be place]
        """       
        start = start
        for ypos in range(row,row+3):
            for xpos in range(1,9,2):
                f = tab()
                f.team = team
                f.symbol = self.symbol
                if start == 2:
                    f.pos =[ypos,xpos+1]
                    self.matrice[ypos][xpos+1]=f
                else:
                    f.pos =[ypos,xpos]
                    self.matrice[ypos][xpos]=f
            start = 1 if (start == 2) else 2
    def teamsGenerate(self):
        self.CreateTeam("negro",1,1)
        self.CreateTeam("rojo",2,6)

    def view(self):
        #--------------------------------this method render de principal view of the program--------------------
        indicator = 0
        colour = 0
        pos = ""
        tabla = "  a  b  c  d  e  f  g  h "
        for vertical in range(1,len(self.matrice)):
            colour = 0 if  (indicator == 1) else 1
            tabla+="\n" + str(vertical)
            for i in range(1,9):
                c = Colour.BLACK if (colour ==0) else Colour.WHITE1
                pos =   "   "  if (self.matrice[vertical][i] == [])  else " "   +   str(self.matrice[vertical][i].symbol)  +   " "
                if self.matrice[vertical][i] != []:
                    if self.matrice[vertical][i].team.lower() == "rojo" :
                        c = Colour.WHITE3 
                tabla += c +  pos +  Colour.END
                colour = 1  if (colour == 0) else  0 
            indicator = 1 if  (indicator == 0) else 0
        return tabla
            
    def position(self, matrice):
        # save all position for any tabs

        allPos = { "rojo": [], "negro":[] }
        for element in matrice:
            for ovject in element:
                if ovject != []:
                    if  ovject.team == "rojo":
                        allPos["rojo"].append(ovject)
                    elif  ovject.team == "negro":
                        allPos["negro"].append(ovject)

        return allPos

    def translate(self,string):
        # this method translate the input
        if not isinstance(string,int):
            string = string.lower()
        listing = {
             "a":1,
             "b":2,
             "c":3,
             "d":4,
             "e":5,
             "f":6,
             "g":7,
             "h":8,

             1:"a",
             2:"b",
             3:"c",
             4:"d",
             5:"e",
             6:"f",
             7:"g",
             8:"h"

        }
        return listing[string]

    def makedame(self):
        # this method verify is there's any new dame in the tablet
        for element in range(1,9,7 ):
            for tabs in range(1,9):
                if element == 1:
                    if self.matrice[element][tabs] != []:
                        if self.matrice[element][tabs].team == "rojo": 
                            self.matrice[element][tabs].symbol = self.dameSymbol
                            self.matrice[element][tabs].isDame = True
                if element == 8:
                    if self.matrice[element][tabs] != []:
                        if self.matrice[element][tabs].team == "negro": 
                            self.matrice[element][tabs].symbol = self.dameSymbol
                            self.matrice[element][tabs].isDame = True
    def clearWindows(self):
        if os.name == "posix":
            os.system ("clear")
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system ("cls")
    

