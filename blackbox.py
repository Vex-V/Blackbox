import pygame
from sys import exit
import random

initdirec=[0,0,""]

finalrow=0
finalcoloumn=0

Revealed = False

state =1

win = False
loss = False

winner=False

Guess = False

atoms=3
tries= 5
points=0

redirect_rules = {
        "right": {
            "topleft": "up",
            "bottomleft": "down"
        },
        "left": {
            "topright": "up",
            "bottomright": "down"
        },
        "down": {
            "topleft": "left",
            "topright": "right"
        },
        "up": {
            "bottomleft": "left",
            "bottomright": "right"
        }
    }

try_dict = {
    1: 2,
    2: 3,
    3: 6,
    4: 8,
    5: 12
}


topleft=[[]]
bottomleft=[[]]
bottomright=[[]]
topright=[[]]

center=[[]]
found=[[]]

group_map = {
    "topleft": topleft,
    "topright": topright,
    "bottomleft": bottomleft,
    "bottomright": bottomright
}

movement = {
        "right": (0, 1),
        "left": (0, -1),
        "down": (1, 0),
        "up": (-1, 0)
    }

def direction(row,coloumn):
    if coloumn == 0:
        direc = "right"
    elif coloumn == 9:
        direc = "left"
    elif row == 0:
        direc= "down"
    elif row == 9:
        direc = "up"

    return direc


def generate(central):
    topleft.append([central[0]-1,central[1]-1])
    topright.append([central[0]-1,central[1]+1])
    bottomright.append([central[0]+1,central[1]+1])
    bottomleft.append([central[0]+1,central[1]-1])


def checkcorner(row,coloumn):
    corner=[0,9]
    if row in corner and coloumn in corner:
        return 1
    else:
        return 0 
    
def checkgrid(row,coloumn):
    grid=[i for i in range(1,9)]
    if row in grid and coloumn in grid:
        return 1
    else:
        return 0

def checkedge(row,coloumn):
    edges=[0,9]
    if row in edges or coloumn in edges:
         return 1
    else:
         return 0


def initial(row,coloumn,direc):
    if [row,coloumn,direc] == initdirec:
       return 0
    
    else:
       return 1
    
    
def move(row, coloumn, direc):
    global finalrow, finalcoloumn

    if checkedge(row, coloumn) == 1 and initial(row, coloumn, direc) == 1:
        print("yes", coloumn)
        finalrow, finalcoloumn = row, coloumn
        return

    if [row, coloumn] in center:
        finalrow, finalcoloumn = 0, 0
        return


    for group_name, new_direc in redirect_rules.get(direc, {}).items():
        print(group_name, new_direc)
        if [row, coloumn] in group_map[group_name]:
            return move(row, coloumn, new_direc)


    dr, dc = movement.get(direc, (0, 0))
    move(row + dr, coloumn + dc, direc)

         
def gennew(num):

    global atoms,tries,points,center,topleft,topright,bottomleft,bottomright
    atoms=num
    all_pairs = [[x, y] for x in range(1, 8) for y in range(1, 8)]
    random.shuffle(all_pairs)
    tries = try_dict.get(atoms)
    points=0
    center = all_pairs[:atoms]
    topleft.clear()
    bottomleft.clear()
    bottomright.clear()
    topright.clear()
    for point in center:
        generate(point)
    print(center)

pygame.init()
screen=pygame.display.set_mode((1200,720))
pygame.display.set_caption("TRY")
clock=pygame.time.Clock()
base_sur=pygame.Surface((1200,720))
base_sur.fill('antiquewhite1')

sec_sur=pygame.Surface((1200,720))
sec_sur.fill('antiquewhite1')

smallfont = pygame.font.SysFont('Corbel',35,bold = pygame.font.Font.bold) 

#Gtext=smallfont.render('Guess',True,'black')
instrucs = [
    "- Click on any edge square to shoot a ray going inward.",
    "- The square you clicked on will change color and turn green.",
    "- If another square also turns green, the ray hit a corner.",
    "  of an atom and deflected and exited there.",
    "- If the clicked square turns dark green, the ray exited ",
    "  on the same square.",
    "- If nothing changes, the ray hit an atom directly and ",
    "  stopped there.",
    " ",
    "- Click Guess to Click inside the box and to try to find",
    "  The location of the atoms",
    "- You lose if you guess wrong too many times, and win if",
    "  you find all atoms"
]


WIDTH=50
HEIGHT=50
MARGIN=1
BUFFERH=102
BUFFERW=357

gridP = [[0 for x in range(100)] for y in range(100)]
gridG = [[0 for x in range(100)] for y in range(100)]


gennew(1)



while True:
    
    if state == 1:

        if tries == 0:
            Revealed=True
            loss=True
            
        
        if points == atoms:
            Revealed=True
            win = True


        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:

                
                pos = pygame.mouse.get_pos()

                if 980 <= pos[0] <= 980+140 and 180 <= pos[1] <= 180+40:
                        pygame.quit()
                        exit()

                if 125 <= pos[0] <= 125+180 and 500 <= pos[1] <= 500+40:
                        state=2

                if win == False and loss == False:
                    if 125 <= pos[0] <= 125+140 and 180 <= pos[1] <= 180+40:
                        if Guess == True:
                            Guess=False
                        else:

                            Guess=True
                    print(Guess)

                    if Guess == False:
                        coloumn = pos[0] // (WIDTH + MARGIN) 
                        row = pos[1] // (HEIGHT + MARGIN)
                        coloumn=coloumn-7
                        row=row-2

                        if checkedge(row,coloumn) == 1 and checkcorner(row,coloumn) == 0:
                            gridP = [[0 for x in range(100)] for y in range(100)] 
                            gridP[row][coloumn] = 1
                            direc = direction(row,coloumn)
                            
                            initdirec=[row,coloumn,direc]
                            move(row,coloumn,direc)
                            row1=finalrow
                            coloumn1=finalcoloumn
                            #print(coloumn1)
                            if row1 == 0 and coloumn1 == 0:
                                pass
                            elif row == row1 and coloumn == coloumn1:
                                gridP[row1][coloumn1]=2
                            else:
                                
                                gridP[row1][coloumn1]=1

                            print("Click ", pos, "Row: ", row, "Coloumn: ", coloumn)

                    else:
                        coloumn = pos[0] // (WIDTH + MARGIN) 
                        row = pos[1] // (HEIGHT + MARGIN)
                        coloumn=coloumn-7
                        row=row-2
                        print("Click ", pos, "Row: ", row, "Coloumn: ", coloumn)
                        if checkedge(row,coloumn) == 0 and checkcorner(row,coloumn) == 0:
                            gridG = [[0 for x in range(100)] for y in range(100)] 
                            gridG[row][coloumn] = 1
                            if [row,coloumn] in center and [row,coloumn] not in found:
                                points=points+1
                                found.append([row,coloumn])
                            elif checkgrid(row,coloumn) == 1: 
                            
                                tries=tries-1
                            else:
                                pass
                        
                elif loss==True:
                
                    if 980 <= pos[0] <= 980+140 and 230 <= pos[1] <= 230+40:
                        loss=False
                        Guess=False
                        Revealed=False
                        gridP = [[0 for x in range(100)] for y in range(100)] 
                        gennew(atoms)

                elif win == True:
                    
                    if 980 <= pos[0] <= 980+140 and 230 <= pos[1] <= 230+40:
                        win=False
                        Guess=False
                        Revealed=False
                        gridP = [[0 for x in range(100)] for y in range(100)] 
                        gennew(atoms+1)
                    
                if atoms == 6:
                    winner = True
                    
                    loss=True
                    print("win")

        if Guess == False:
            word="Play"
            color1="chartreuse4"
            attempts=""
        
            
        else:
            word="Guess"
            color1="darkred"
            attempts= "Tries: " + str(tries)
            

        
        Gtext=smallfont.render("Quit",True,'black')
        pygame.draw.rect(base_sur,"red",[980,180,140,40],0,10) 
        base_sur.blit(Gtext , (980+35,184))


        Gtext=smallfont.render("How To Play",True,'black')
        pygame.draw.rect(base_sur,"White",[125,500,180,40],0,10) 
        base_sur.blit(Gtext , (125+5,504))


        if loss == True:
            Gtext=smallfont.render("Try again",True,'black')
            pygame.draw.rect(base_sur,"blue",[980,230,140,40],0,10) 
            base_sur.blit(Gtext , (980+10,235))

            Gtext=smallfont.render("Round Lost",True,'black')
            base_sur.blit(Gtext , (570,50))

        elif win == True:
            Gtext=smallfont.render("Continue",True,'black')
            pygame.draw.rect(base_sur,"green",[980,230,140,40],0,10) 
            base_sur.blit(Gtext , (980+10,235))

            Gtext=smallfont.render("Round Won",True,'black')
            base_sur.blit(Gtext , (570,50))
        else:
            pygame.draw.rect(base_sur,"antiquewhite1",[980,230,140,40],0,10) 
            pygame.draw.rect(base_sur,"antiquewhite1",[570,50,200,40],0,10)


        if winner == True:
            pygame.draw.rect(base_sur,"antiquewhite1",[570,50,200,40],0,10)
            Gtext=smallfont.render("You win",True,'black')
            base_sur.blit(Gtext , (570,50))

        pygame.draw.rect(base_sur,"antiquewhite1",[125,224,150,40],0,10)
        Ttext=smallfont.render(attempts,True,'black')
        base_sur.blit(Ttext , (125+35,224))

        Points= "Points: " + str(points)
        pygame.draw.rect(base_sur,"antiquewhite1",[127,264,160,40],0,10)
        Ptext=smallfont.render(Points,True,'black')
        base_sur.blit(Ptext , (125+35,264))

        Gtext=smallfont.render(word,True,'black')
        pygame.draw.rect(base_sur,color1,[125,180,140,40],0,10) 
        base_sur.blit(Gtext , (125+35,184))

        for row2 in range(10):
            for coloumn2 in range(10):
                            
                            if checkcorner(row2,coloumn2)==1:
                                color="antiquewhite1"
                            elif checkedge(row2,coloumn2) == 1:
                                color ="red"
                            else:
                                color="black"
                            if Revealed == True:
                                if [row2,coloumn2] in center:
                                    color="yellow"
                                elif [row2,coloumn2] in topleft or [row2,coloumn2] in topright or [row2,coloumn2] in bottomleft or [row2,coloumn2] in bottomright:
                                    color="orange"
                            
                            if Guess == False:
                                if gridP[row2][coloumn2] == 1:
                                    color = "green"
                                elif gridP[row2][coloumn2] == 2:
                                    color = "forestgreen"
                            else:
                                if gridG[row2][coloumn2] == 1:
                                    color = "darkred"
                                
                            pygame.draw.rect(base_sur,color,[(MARGIN + WIDTH) * coloumn2 + MARGIN + BUFFERW ,(MARGIN + HEIGHT) * row2 + MARGIN+ BUFFERH,WIDTH, HEIGHT])
        screen.blit(base_sur,(0,0))
        pygame.display.update()


    elif state == 2:

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:

                
                pos = pygame.mouse.get_pos()

                if 550 <= pos[0] <= 550+140 and 600 <= pos[1] <= 600+40:
                    state = 1

        Gtext=smallfont.render("Return",True,'black')
        pygame.draw.rect(sec_sur,"White",[550,600,140,40],0,10) 
        sec_sur.blit(Gtext , (550+20,600+4))
        x=0
        pygame.draw.rect(sec_sur,"Grey",[195,30,850,550])
        for text in instrucs:
            Gtext=smallfont.render(text,True,'black')
            sec_sur.blit(Gtext , (195+20,30+10+x))
            x=x+40
        

        screen.blit(sec_sur,(0,0))
        pygame.display.update()


    clock.tick(30)