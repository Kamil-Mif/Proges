import pgzrun
import pygame

pygame.init()





        
            



TITLE = "Лабиринт Духов" # Заголовок окна игры
FPS = 60 # Количество кадров в секунд

start = Actor('start')
#inf = Actor('beta', (850, 600))

idole = Actor('z2', (249, 50))
play = Actor("play", (850, 300))
cell = Actor ("bloks2")
cell1 = Actor ("bloks1")
cell2 = Actor ('bloks3')
cell3 = Actor ('bloks4')
cell4 = Actor ('bons')
cell5 = Actor ('bloks5')
cell6 = Actor ('bloks')
cell7 = Actor ('bloks6')
cell8 = Actor ('bloks7')
size_w = 17 # Ширина поля в клетках
size_h = 10 # Высота поля в клетках
WIDTH = cell.width * size_w
HEIGHT = cell.height * size_h
level = 1
count = 0

hit = 0
ist = 0
str(hit)
str(ist)
mode = 'menu'

if mode == 'menu':
    pygame.mixer.music.load('sounds/m2.mp3')
    pygame.mixer.music.play()

    

map = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0],
       [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0], 
       [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0], 
       [0, 1, 0, 1, 1, 1, 0, 1, 0, 2, 1, 1, 0, 1, 0, 1, 0], 
       [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0], 
       [0, 1, 1, 1, 0, 1, 1, 1, 0, 4, 2, 4, 0, 2, 0, 1, 0], 
       [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 3, 0, 1, 0, 1, 0],
       [0, 0, 1, 1, 0, 1, 1, 1, 2, 3, 1, 1, 0, 1, 0, 1, 0], 
       [0, 2, 1, 1, 0, 3, 1, 1, 0, 2, 3, 1, 1, 1, 1, 1, 0],  
       [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]]
        
        
        
def map_draw():
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 0:
                cell.left = cell.width*j
                cell.top = cell.height*i
                cell.draw()
            elif map[i][j] == 1:
                cell1.left = cell.width*j
                cell1.top = cell.height*i
                cell1.draw()
            elif map[i][j] == 2:
                cell2.left = cell.width*j
                cell2.top = cell.height*i
                cell2.draw()
            elif map[i][j] == 3:
                cell3.left = cell.width*j
                cell3.top = cell.height*i
                cell3.draw()
            
            elif map[i][j] == 4:
                cell4.left = cell.width*j
                cell4.top = cell.height*i
                cell4.draw()
            
            elif map[i][j] == 5:
                cell5.left = cell.width*j
                cell5.top = cell.height*i
                cell5.draw()
                

            
def draw():
    global mode
    if mode == 'menu':
        start.draw()
        play.draw()
        screen.draw.text("Насторойки(бета)", center=(850, 450), color = 'white', fontsize = 26)
        screen.draw.text("Информация(бета)", center=(850, 650), color = 'white', fontsize = 26)
    if mode == "game": 
        map_draw()
        idole.draw()
        screen.draw.text( 'Испуг:' , center=(1500, 900), color = 'orange', fontsize = 36)
        screen.draw.text('Щит:'  , center=(1600, 900), color = 'orange', fontsize = 36)
        screen.draw.text( ist , center=(1520, 900), color = 'orange', fontsize = 36)
        screen.draw.text( hit , center=(1620, 900), color = 'orange', fontsize = 36)
        
        
    elif mode == "end":
        screen.draw.text("GAME OVER", center=(150, 150), color = 'white', fontsize = 26)
        mode = 'menu'
        
    elif mode == "options":
        start.draw()
        
    
    elif mode == "infa":
        start.draw()
        
play_game = False


def update(dt):
    
    
    
    global mode, play_game
    if mode == 'game':
        if keyboard.w :
            tx = int(idole.x // cell.width)
            ty = int((idole.y - 25) // cell.height)

            if  ty >= size_h or map[ty][tx] == 0:
                print('Stop')
            else:
                idole.y -= 5
                idole.image = 's2'
    
        elif keyboard.a:
            tx = int((idole.x - 25)// cell.width)
            ty = int(idole.y   // cell.height)

            if  map[ty][tx] == 0:
                print('Stop')
            else:
                idole.x -= 5
                idole.image = 'x2'
        
        elif keyboard.d:
            tx = int((idole.x + 25)// cell.width)
            ty = int(idole.y   // cell.height)

            if map[ty][tx] == 0:
                print('Stop')
            else:
                idole.x += 5
                idole.image = 'y2'
        
        elif keyboard.s:
            tx = int(idole.x // cell.width)
            ty = int((idole.y + 35) // cell.height)

            if ty >= size_h or map[ty][tx] == 0:
                print('Stop')
            else:    
                idole.y += 5
                idole.image = 'z2'
        
        elif keyboard.z:
            mode = 'menu'
            
        tx = int(idole.x // cell.width)
        ty = int(idole.y // cell.height)
        if map[ty][tx] == 3:
            print('opps')
            
        if map[ty][tx] == 4:
            print('bonus')
            
        if map[ty][tx] == 2:
            print('bones')
            ist + 1
        
        if play_game == False:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('sounds/m11.mp3')
            pygame.mixer.music.play()
            play_game = True
       
def on_mouse_down(button, pos):
    global mode
    if mode == 'menu':
        if play.collidepoint(pos):
            mode = 'game'
            
        #elif op.collidepoint(pos):
            #mode = 'options'
            
        #elif inf.collidepoint(pos):
            #mode = 'infa'
            
pgzrun.go()
