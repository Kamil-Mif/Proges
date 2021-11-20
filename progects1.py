import pgzrun
import pygame

pygame.init()





        
            



TITLE = "Лабиринт Духов" # Заголовок окна игры
FPS = 60 # Количество кадров в секунд

start = Actor('start')
#inf = Actor('beta', (850, 600))
#op = Actor('beta', (850, 400))
idole = Actor('z2', (249, 50))
play = Actor("play", (850, 300))
cell = Actor ("bloks2")
cell1 = Actor ("bloks1")
cell2 = Actor ('bloks3')
cell3 = Actor ('bloks4')
cell4 = Actor ('bons')
cell5 = Actor ('bloks5')
size_w = 17 # Ширина поля в клетках
size_h = 10 # Высота поля в клетках
WIDTH = cell.width * size_w
HEIGHT = cell.height * size_h
level = 1
count = 0


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
        
        
        
    elif mode == "end":
        screen.draw.text("GAME OVER", center=(150, 150), color = 'white', fontsize = 26)
        mode = 'menu'
        
    elif mode == "options":
        start.draw()
        
    
    elif mode == "infa":
        start.draw()
        
 

def update(dt):
    global mode
    if mode == 'game':
        if keyboard.w:
            idole.y -= 5
            idole.image = 's2'
    
        elif keyboard.a:
            idole.x -= 5
            idole.image = 'x2'
        
        elif keyboard.d:
            idole.x += 5
            idole.image = 'y2'
        
        elif keyboard.s:
            idole.y += 5
            idole.image = 'z2'
        
        elif keyboard.z:
            mode = 'menu'
            
        pygame.mixer.music.stop()
        
        pygame.mixer.music.load('sounds/m11.mp3')
        pygame.mixer.music.play()
       
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
