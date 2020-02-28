from exceptions import *

class tab:

    def __init__(self):
        self.pos    = []
        self.symbol = ""

    def counter(self,player):
        # return the counter to the players or tabs
        if player.lower() == "b":
            return "n"
        elif player.lower()== "n":
            return "b"
        else:
            return False

    def move(self,direction,turn,matrice):
         #-----------------------------------------------------------------------------------------------
        if direction.upper()  == "RU":
            if (turn == "n" and self.symbol =="n") or ( self.symbol == self.symbol.upper() and self.symbol == turn.upper() ):
                if matrice[self.pos[0]-1][self.pos[1]+1] == [] and self.pos[0] >1 and self.pos[1]<8:
                    y1,x1 = -1,1
                else:
                    raise invalidmove("you cant move here")
            else:
                raise invalidmove("you can't move this tab")
        #-----------------------------------------------------------------------------------------------
        if direction.upper()  == "LU":
            if (turn == "n" and self.symbol =="n" ) or ( self.symbol == self.symbol.upper() and self.symbol == turn.upper() ):
                if matrice[self.pos[0]-1][self.pos[1]-1] == []  and self.pos[0] >1 and self.pos[1]>1:
                    y1,x1 = -1,-1
                else:
                    raise invalidmove("you cant move here")
            else:
                raise invalidmove("you can't move this tab")
        #-----------------------------------------------------------------------------------------------
        if direction.upper()  == "LD":
            if (turn == "b" and self.symbol =="b") or ( self.symbol == self.symbol.upper() and self.symbol == turn.upper() ) :
                if matrice[self.pos[0]+1][self.pos[1]-1] == []  and self.pos[0] <8 and self.pos[1]>1:
                    y1,x1 = 1,-1
                else:
                    raise invalidmove("you cant move here")
            else:
                raise invalidmove("you can't mome this tab")         
        #-----------------------------------------------------------------------------------------------
        if direction.upper()  == "RD":
            if (turn == "b" and self.symbol =="b") or ( self.symbol == self.symbol.upper() and self.symbol == turn.upper() ) :
                if matrice[self.pos[0]+1][self.pos[1]+1] == []  and self.pos[0] <8 and self.pos[1]<8:
                    x1,y1 = 1,1

                else:
                    raise invalidmove("you cant move here")
        #-----------------------------------------------------------------------------------------------                
            else:
                raise invalidmove("you can't mome this tab")

        matrice[self.pos[0]+y1][self.pos[1]+x1] =  matrice[self.pos[0]][self.pos[1]]
        matrice[self.pos[0]][self.pos[1]] = []
        self.pos[0] = self.pos[0] + y1
        self.pos[1] = self.pos[1] + x1  
        return self.counter(turn)
        #-----------------------------------------------------------------------------------------------
    
    def target(self,matrice,player,*args):
        """[summary]
        
        Arguments:
            matrice {list} -- [receive an array where the location of all the chips is]
            player {string} -- [receive the player symbol that is n or b]
        
        returns:
            [tuple] -- [returns a tuple  with the card (only single tabs)  he can eat, the address, and in how many boxes is the enemy to eat ]
        """     
        targets = ()
        if len(args) >0:
            if args[0]== True:
                self.symbol = self.symbol.upper()
        if matrice[self.pos[0]] [self.pos[1]] != []:

            if  self.pos[0] < 7 and self.pos[1] < 7:
            #----------------------------------------------------------------------------------------------------------------
                if  matrice[self.pos[0]+1] [self.pos[1]+1] != []:
                    if self.symbol == "b" or self.symbol == self.symbol.upper():
                        if matrice[self.pos[0]+1][self.pos[1]+1].symbol.lower() == self.counter(player):
                            if  matrice[self.pos[0]+2][self.pos[1]+2] == []:
                                targets = (self.pos,"RD") 

            if  self.pos[0] >2  and self.pos[1] < 7 :
            #----------------------------------------------------------------------------------------------------------------                
                if matrice[self.pos[0]-1][self.pos[1]+1] != []:
                    if self.symbol == "n" or self.symbol == self.symbol.upper():
                        if matrice[self.pos[0]-1][self.pos[1]+1].symbol.lower()  == self.counter(player):
                            if  matrice[self.pos[0]-2][self.pos[1]+2]  == []:
                                targets = (self.pos,"RU") 

            if self.pos[0] > 2 and self.pos[1] > 2 :
            #----------------------------------------------------------------------------------------------------------------                
                if matrice[self.pos[0]-1][self.pos[1]-1] != []:
                    if self.symbol == "n" or self.symbol == self.symbol.upper():
                        if matrice[self.pos[0]-1][self.pos[1]-1].symbol.lower()  == self.counter(player):
                            if  matrice[self.pos[0]-2][self.pos[1]-2]  == []:
                                targets = (self.pos,"LU") 

            if self.pos[0] < 7 and self.pos[1] > 2 :
            #----------------------------------------------------------------------------------------------------------------                
                if matrice[self.pos[0]+1][self.pos[1]-1] != []:
                    if self.symbol == "b" or self.symbol == self.symbol.upper():
                        if matrice[self.pos[0]+1][self.pos[1]-1].symbol.lower()  == self.counter(player ):
                            if matrice[self.pos[0]+2][self.pos[1]-2]  == []:
                                targets = (self.pos,"LD") 

        self.symbol = self.symbol.lower()
        return targets

    def eat(self,direction,matrice,point,*args): 
        """[summary]
        
        this function make all way of eat for the simple tokens and the dames

        Arguments:
            direction {[string]} -- [must have as input the address in which the file must eat (ru, rd, lu, ld)]
            matrice {[list]} -- [it must be the matrix where all the object tabs are]
            point {[int]} -- [the points that each team carries]
        
        Raises:
            Exception: [generates an exception if one of the validated entries is incorrect]
        
        Returns:
            [list,string,int,bool] -- [the matrix returns with the modified elements, the player that corresponds
                                            to the next turn, the points it has and if there is an error or not]
        """ 
        if len(args) >0:
            if args[0]== True:
                self.symbol = self.symbol.upper()

        if direction.upper() == "RU" :
            if (self.symbol == "n" or self.symbol == self.symbol.upper()):
                y1,x1,y2,x2 = -1,1,-2,2

        if direction.upper() == "LU" :
            if   (self.symbol == "n" or self.symbol == self.symbol.upper()) :
                y1,x1,y2,x2 = -1,-1,-2,-2


        if direction.upper() == "RD" :
            if  (self.symbol == "b" or self.symbol == self.symbol.upper()):
                y1,x1,y2,x2 = 1,1,2,2
            
        if direction.upper() == "LD" :
            if (self.symbol == "b" or self.symbol == self.symbol.upper()):
                y1,x1,y2,x2 = 1,-1,2,-2
        #---------------- Make the eat----------------
        matrice[self.pos[0]+y2] [self.pos[1]+x2] = matrice[self.pos[0]] [self.pos[1]]
        matrice[self.pos[0]] [self.pos[1]] = []
        matrice[self.pos[0]+y1] [self.pos[1]+x1] = []
        self.pos[0] = self.pos[0] + y2
        self.pos[1] = self.pos[1] + x2
        targt = self.target(matrice,self.symbol,True)
        point += 5
        if len(targt)>0:

            for element in targt:
                if element[0] == self.pos[0] and  element[1] == self.pos[1] :
                    return  self.eat(targt[1],matrice,point,True)
        else:
            self.symbol = self.symbol.lower()
            return matrice,self.counter(self.symbol),point