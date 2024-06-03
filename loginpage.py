import pygame as pyg
import sys

pyg.init()

window_width = 300
window_height = 500

color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_active = pyg.Color('dodgerblue2')
color_passive = pyg.Color('lightskyblue3')

window = pyg.display.set_mode((window_width, window_height))
clock = pyg.time.Clock()
logic_running = True

def display_child_text(text, colortext, coordinatex, coordinatey):
    if colortext == False:
        colortext = color_black
    else:
        colortext = color_white

    text_font = pyg.font.SysFont("Arial", 16, True, True)
    text_to_render = text_font.render(text, True, colortext)
    text_to_render_rect = text_to_render.get_rect()
    text_to_render_rect.center = (window_width / coordinatex, window_height / coordinatey)
    window.blit(text_to_render, text_to_render_rect)

def display_parent_text(text, colortext, coordinatex, coordinatey):
    if colortext == False:
        colortext = color_black
    else:
        colortext = color_white

    text_font = pyg.font.SysFont("Arial", 24)
    text_to_render = text_font.render(text, True, colortext)
    text_to_render_rect = text_to_render.get_rect()
    text_to_render_rect.center = (window_width / coordinatex, window_height / coordinatey)
    window.blit(text_to_render, text_to_render_rect)

base_font = pyg.font.Font(None, 32)

username_text = ''
password_text = ''
password_hidden_text = ''
input_rect_username = pyg.Rect(30, 150, 200, 32)
input_rect_password = pyg.Rect(30, 220, 200, 32)
active_username = False
active_password = False
color_username = color_passive
color_password = color_passive

while logic_running:
    window.fill(color_white)

    display_parent_text(text="Login Page", colortext=False, coordinatex=2, coordinatey=8)
    display_child_text(text="Username", colortext=False, coordinatex=4, coordinatey=4)
    display_child_text(text="Password", colortext=False, coordinatex=4, coordinatey=2.5)

    exit_pressed_button = pyg.key.get_pressed()
    if exit_pressed_button[pyg.K_ESCAPE]:
        logic_running = False

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
            sys.exit()
        if event.type == pyg.MOUSEBUTTONDOWN:
            if input_rect_username.collidepoint(event.pos):
                active_username = True
                active_password = False
            elif input_rect_password.collidepoint(event.pos):
                active_password = True
                active_username = False
            else:
                active_username = False
                active_password = False
        if event.type == pyg.KEYDOWN:
            if active_username:
                if event.key == pyg.K_BACKSPACE:
                    username_text = username_text[:-1]
                else:
                    username_text += event.unicode
            if active_password:
                if event.key == pyg.K_BACKSPACE:
                    password_text = password_text[:-1]
                    password_hidden_text = password_hidden_text[:-1]
                else:
                    password_text += event.unicode
                    password_hidden_text += "*"

    color_username = color_active if active_username else color_passive
    color_password = color_active if active_password else color_passive

    pyg.draw.rect(window, color_username, input_rect_username)
    pyg.draw.rect(window, color_password, input_rect_password)

    text_surface_username = base_font.render(username_text, True, (0, 0, 0))
    window.blit(text_surface_username, (input_rect_username.x + 5, input_rect_username.y + 5))
    input_rect_username.w = max(200, text_surface_username.get_width() + 10)

    text_surface_password = base_font.render(password_hidden_text, True, (0, 0, 0))
    window.blit(text_surface_password, (input_rect_password.x + 5, input_rect_password.y + 5))
    input_rect_password.w = max(200, text_surface_password.get_width() + 10)

    pyg.display.flip()
    dt = clock.tick(60) / 1000

pyg.quit()
