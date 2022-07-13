from cmath import pi
from turtle import position
import pygame
import os

WIDTH,HEIGHT  = 480,480
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Chess")

FPS = 60
ROW = 8
COLUMN = 8
TABLE_COLOR1 = (111,255,0)
TABLE_COLOR2 = (85,85,85)
X = 60


class Piece:
    instances = []
    moves = []
    bin = []
    def __init__(self,name,file_name,color,position_x,position_y):
        self.__class__.instances.append(self)
        self.name = name
        self.file_name = file_name
        self.color = color
        image = pygame.image.load(os.path.join('chess_assets',self.file_name))
        self.piece = pygame.transform.scale(image,(X,X))
        self.position_x = position_x
        self.position_y = position_y

    def succesful_move(self,color,piece,cordinate):
        self.__class__.moves.append([color,piece,cordinate])
        
    def knock(self,position_x,position_y,color):
        for piece in self.__class__.instances:
            if piece.position_x == position_x and piece.position_y == position_y and piece.color != color and piece.name != "King":
                self.__class__.bin.append(piece)
                self.__class__.instances.remove(piece)

    
    def __str__(self):
        return self.name+str(self.position_x)+str(self.position_y)

class King(Piece):
    def __init__(self,name,file_name,color,position_x,position_y):
        super().__init__(name,file_name,color,position_x,position_y)
    def movement(self,new_position_x,new_position_y):
        if abs(new_position_x-self.position_x) == 1 and abs(new_position_y-self.position_y) == 1 or abs(new_position_x-self.position_x) == 1 and abs(new_position_y-self.position_y) == 0 or abs(new_position_x-self.position_x) == 0 and abs(new_position_y-self.position_y) == 1:

            for piece in self.__class__.instances:
                if piece.position_y == new_position_y and piece.position_x == new_position_x:
                    if piece.color != self.color and piece.name != "King":
                        self.knock(new_position_x,new_position_y,self.color)
                    else:
                        return "Check"
            self.position_x = new_position_x
            self.position_y = new_position_y
            self.succesful_move(self.color,self.name,(self.position_x,self.position_y))
            return True

class Queen(Piece):
    def __init__(self,name,file_name,color,position_x,position_y):
        super().__init__(name,file_name,color,position_x,position_y)
    def movement(self,new_position_x,new_position_y):
        if new_position_x == self.position_x or new_position_y == self.position_y or abs(new_position_x-self.position_x) == abs(new_position_y-self.position_y):
            knock = False
            check = False
            for piece in self.__class__.instances:
                if abs(piece.position_y-self.position_y) == abs(piece.position_x-self.position_x):
                    if piece.position_y == self.position_y and piece.position_x == self.position_x:
                        continue
                    if piece.position_x == new_position_x and piece.position_y == new_position_y:
                        if piece.color != self.color and piece.name != "King":
                            knock = True
                        elif piece.color != self.color and piece.name == "King":
                            check = True
                        else:
                            return
                    elif new_position_y <= piece.position_y and self.position_y > piece.position_y:
                        if new_position_x < self.position_x and piece.position_x < self.position_x:
                            return
                        elif new_position_x > self.position_x and piece.position_x > self.position_x:
                            return

                    elif new_position_y >= piece.position_y and self.position_y < piece.position_y:
                        if new_position_x > self.position_x and piece.position_x > self.position_x:
                            return
                        elif new_position_x < self.position_x and piece.position_x < self.position_x:
                            return
                if new_position_x == self.position_x or new_position_y == self.position_y:
                    if piece.position_y == self.position_y and piece.position_x == self.position_x:
                        continue
                    if piece.position_y == self.position_y and (self.position_x < piece.position_x and piece.position_x < new_position_x):
                        return
                    elif piece.position_y == self.position_y and (self.position_x > piece.position_x and piece.position_x > new_position_x):
                        return
                    elif piece.position_x == self.position_x and (self.position_y > piece.position_y and piece.position_y > new_position_y) and new_position_y != self.position_y:
                        return
                    elif piece.position_x == self.position_x and (self.position_y < piece.position_y and piece.position_y < new_position_y) and new_position_y != self.position_y:
                        return
                    elif (new_position_x == piece.position_x and new_position_y == piece.position_y):
                        if piece.color != self.color and piece.name != "King":
                            knock = True
                        elif piece.color != self.color and piece.name == "King":
                            check = True
                        else:
                            return
            if check == True:
                return "Check"
            if knock == True:
                self.knock(new_position_x,new_position_y,self.color)

            self.position_x = new_position_x
            self.position_y = new_position_y
            self.succesful_move(self.color,self.name,(self.position_x,self.position_y))
            return True
class Rook(Piece):
    def __init__(self,name,file_name,color,position_x,position_y):
        super().__init__(name,file_name,color,position_x,position_y)
    def movement(self,new_position_x,new_position_y):
        if new_position_x == self.position_x or new_position_y == self.position_y:
            knock = False
            check = False
            for piece in self.__class__.instances:
                if piece.position_y == self.position_y and piece.position_x == self.position_x:
                    continue

                if piece.position_y == self.position_y and (self.position_x < piece.position_x and piece.position_x < new_position_x):
                    return
                elif piece.position_y == self.position_y and (self.position_x > piece.position_x and piece.position_x > new_position_x):
                    return
                elif piece.position_x == self.position_x and (self.position_y > piece.position_y and piece.position_y > new_position_y) and new_position_y != self.position_y:
                    return
                elif piece.position_x == self.position_x and (self.position_y < piece.position_y and piece.position_y < new_position_y) and new_position_y != self.position_y:
                    return
                elif (new_position_x == piece.position_x and new_position_y == piece.position_y):
                    if piece.color != self.color and piece.name != "King":
                        knock = True
                    elif piece.color != self.color and piece.name == "King":
                        check = True
                    else:
                        return
            
            if check == True:
                return "Check"
            if knock == True:
                self.knock(new_position_x,new_position_y,self.color)
            self.position_x = new_position_x
            self.position_y = new_position_y
            self.succesful_move(self.color,self.name,(self.position_x,self.position_y))
            return True
class Bishop(Piece):
    def __init__(self,name,file_name,color,position_x,position_y):
        super().__init__(name,file_name,color,position_x,position_y)
    def movement(self,new_position_x,new_position_y):
        if abs(new_position_x-self.position_x) == abs(new_position_y-self.position_y):
            knock = False
            check = False
            for piece in self.__class__.instances:
                if abs(piece.position_y-self.position_y) == abs(piece.position_x-self.position_x):
                    if piece.position_y == self.position_y and piece.position_x == self.position_x:
                        continue
                    if piece.position_x == new_position_x and piece.position_y == new_position_y:
                        if piece.color != self.color and piece.name != "King":
                                knock = True
                        elif piece.color != self.color and piece.name == "King":
                                check = True
                        else:
                            return
                    elif new_position_y <= piece.position_y and self.position_y > piece.position_y:
                        if new_position_x < self.position_x and piece.position_x < self.position_x:
                            return
                        elif new_position_x > self.position_x and piece.position_x > self.position_x:
                            return

                    elif new_position_y >= piece.position_y and self.position_y < piece.position_y:
                        if new_position_x > self.position_x and piece.position_x > self.position_x:
                            return
                        elif new_position_x < self.position_x and piece.position_x < self.position_x:
                            return
            if check == True:
                return "Check"
            if knock == True:
                self.knock(new_position_x,new_position_y,self.color)
            self.position_x = new_position_x
            self.position_y = new_position_y
            self.succesful_move(self.color,self.name,(self.position_x,self.position_y))
            return True
class Knight(Piece):
    def __init__(self,name,file_name,color,position_x,position_y):
        super().__init__(name,file_name,color,position_x,position_y)
    def movement(self,new_position_x,new_position_y):
        if abs(new_position_x-self.position_x) == 1 and abs(new_position_y-self.position_y) ==2 or abs(new_position_y-self.position_y) == 1 and abs(new_position_x-self.position_x) == 2:
            for piece in self.__class__.instances:
                if piece.position_x == new_position_x and piece.position_y == new_position_y:
                    if piece.color != self.color and piece.name != "King":
                            self.knock(new_position_x,new_position_y,self.color)
                    else:
                        return "Check"

            self.position_x = new_position_x
            self.position_y = new_position_y
            self.succesful_move(self.color,self.name,(self.position_x,self.position_y))
            return True
class Pawn(Piece):
    def __init__(self,name,file_name,color,position_x,position_y):
        super().__init__(name,file_name,color,position_x,position_y)
    def movement(self,new_position_x,new_position_y):
        if abs(new_position_y-self.position_y) == 1 and abs(new_position_x-self.position_x) <=1:
            if self.color == "black" and new_position_y > self.position_y or self.color == "white" and new_position_y < self.position_y:
                for index,piece in enumerate(self.__class__.instances):

                    if self.position_x != new_position_x and (piece.position_x != new_position_x or piece.position_y != new_position_y):
                        if index == len(self.__class__.instances)-1:
                            return
                    elif self.position_x == new_position_x and piece.position_x == new_position_x and piece.position_y == new_position_y:
                        return
                    elif self.position_x != new_position_x and piece.position_x == new_position_x and piece.position_y == new_position_y: 
                        if piece.color != self.color and piece.name != "King":
                            self.knock(new_position_x,new_position_y,self.color)
                            break
                        else:
                            return "Check"
                    
                    

                self.position_x = new_position_x
                self.position_y = new_position_y
                self.succesful_move(self.color,self.name,(self.position_x,self.position_y))
                return True
        elif abs(new_position_y-self.position_y) == 2 and abs(new_position_x-self.position_x) <=1 and new_position_x == self.position_x:
            if self.color == "black" and self.position_y == 1 or self.color == "white" and self.position_y == 6:
                for piece in self.__class__.instances:
                    if piece.position_y >= new_position_y and piece.position_y < self.position_y and piece.position_x == new_position_x:
                        return
                    elif piece.position_y <= new_position_y and piece.position_y > self.position_y and piece.position_x == new_position_x:
                        return
                self.position_x = new_position_x
                self.position_y = new_position_y
                self.succesful_move(self.color,self.name,(self.position_x,self.position_y))
                return True


def draw_window(pos,can_move):
    WIN.fill(TABLE_COLOR2)
    row = 0
    while row < ROW:
        column = 0
        while column < COLUMN:
            if row%2:
                if column % 2:
                    pygame.draw.rect(WIN,TABLE_COLOR1 ,pygame.Rect(column*X,row*X,X,X),)
                else:
                    pygame.draw.rect(WIN,TABLE_COLOR2,pygame.Rect(column*X,row*X,X,X),2)
            
            else:
                if column % 2:
                    pygame.draw.rect(WIN,TABLE_COLOR2,pygame.Rect(column*X,row*X,X,X),2)
                else:
                    pygame.draw.rect(WIN,TABLE_COLOR1 ,pygame.Rect(column*X,row*X,X,X))
            column +=1 
        row +=1 
    
    for instance in Piece.instances:
        WIN.blit(instance.piece,(instance.position_x*X,instance.position_y*X))
        if pos != None:
            if pos[0] == instance.position_x and pos[1] == instance.position_y and instance.color == can_move:
                pygame.draw.rect(WIN,(0,0,255),pygame.Rect(pos[0]*X,pos[1]*X,X,X),2)

    pygame.display.update()
        
def call_pieces(color):
    x = 0
    while x < 3:
        if color == "black":
            custom_y = 0
        else:
            custom_y = 7
        if x == 1:
            Queen("Queen","{0}_queen.png".format(color),color,3,custom_y)
            King("King","{0}_king.png".format(color),color,4,custom_y)
        elif x == 0:
            Rook("Rook","{0}_rook.png".format(color),color,0,custom_y)
            Knight("Knight","{0}_knight.png".format(color),color,1,custom_y)
            Bishop("Bishop","{0}_bishop.png".format(color),color,2,custom_y)
        elif x == 2:
            Rook("Rook","{0}_rook.png".format(color),color,7,custom_y)
            Knight("Knight","{0}_knight.png".format(color),color,6,custom_y)
            Bishop("Bishop","{0}_bishop.png".format(color),color,5,custom_y)
        
        x+=1
    y = 0
    while y <8:
        if color == "black":
            Pawn("Pawn","{0}_pawn.png".format(color),color,y,1)
        else:
            Pawn("Pawn","{0}_pawn.png".format(color),color,y,6)
        y+=1

def move(pos,moveable_piece,can_move):

    if moveable_piece != None and moveable_piece.color == can_move:
        if moveable_piece.position_x != pos[0] or moveable_piece.position_y != pos[1]:
            result = moveable_piece.movement(pos[0],pos[1])
            if result == True:
                if can_move == "white":
                    can_move = "black"
                else:
                    can_move = "white"
        return can_move
    elif moveable_piece == None:
        for piece in Piece.instances:
            if piece.position_x == pos[0] and piece.position_y == pos[1] and piece.color == can_move:
                return piece
        return None

def check_if_check(can_move):
    current_king = None
    for instance in Piece.instances:
        if instance.name =="King" and instance.color == can_move:
            current_king = instance
            break
    
    if current_king != None:
        for instance in Piece.instances:
            if instance.color != can_move:
                asd = instance.movement(current_king.position_x,current_king.position_y)
                if asd == "Check":
                    return current_king

def check_if_good_move(can_move,selected,pos):
    original_x = selected.position_x
    original_y = selected.position_y
    before = len(Piece.instances)
    selected.movement(pos[0],pos[1])
    check = check_if_check(can_move)
    selected.position_x = original_x
    selected.position_y = original_y
    after = len(Piece.instances)
    if check != None:
        return False
    else:
        try:
            if before > after:
                Piece.instances.append(Piece.bin[-1])
        except:
            pass
        return True
    
        
def main():
    run = True
    clock = pygame.time.Clock()
    call_pieces("black")
    call_pieces("white")
    pos = None
    select = None
    can_move = "white"
    while(run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                tuple_pos = pygame.mouse.get_pos()
                pos = []
                pos.append(int(tuple_pos[0]/X))
                pos.append(int(tuple_pos[1]/X))

                current_king = check_if_check(can_move)
       
                if select == None:
                    select = move(pos,None,can_move)
                else:  
                    move_result = check_if_good_move(can_move,select,pos)
                    if move_result != False:
                        can_move = move(pos,select,can_move)
                    select= None
                    pos = None                              #HA NEM JO EZT VEDD KI !!!!!!!!!!
        draw_window(pos,can_move)
    main()

if __name__ == "__main__":
    main()