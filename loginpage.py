import pygame as pyg 
import sys as sys

pyg.init()

window_width = 500
window_height = 300

color_white = (255, 255, 255)
color_black = (0, 0, 0)

window = pyg.display.set_mode((window_width, window_height))
clock = pyg.time.Clock()
logic_running = True

def display_child_text(text, colortext, coordinatex, coordinatey):
    
    if colortext == True:
        colortext = color_black
    else:
        colortext = color_white
    
    text_font = pyg.font.SysFont("Arial", 16)
    text_toRender = text_font.render(text, True, colortext)
    text_toRender_rect = text_toRender.get_rect()
    text_toRender_rect.center = (window_width/coordinatex, window_height/coordinatey)
    window.blit(text_toRender, text_toRender_rect)
    
    

while logic_running:
    
    window.fill("white")
    
    
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            logic_running = False


    pyg.display.flip()
    dt = clock.tick(60)/1000

pyg.quit()