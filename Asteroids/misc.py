import pygame
from leaderboard import load_leaderboard, update_leaderboard
from constants import gameDisplay, white, black, display_height, display_width, custom_font, red

# Create funtion to chek for collision
def isColliding(x, y, xTo, yTo, size):
    if x > xTo - size and x < xTo + size and y > yTo - size and y < yTo + size:
        return True
    return False


def drawText(msg, color, x, y, center=True):
    screen_text = custom_font.render(msg, True, color)
    if center:
        rect = screen_text.get_rect(center=(x, y))
        gameDisplay.blit(screen_text, rect)
    else:
        gameDisplay.blit(screen_text, (x, y))

def show_leaderboard():
    gameDisplay.fill(black)
    drawText("LEADERBOARD", white, display_width / 2, 50, 50)

    leaderboard = load_leaderboard()
    y_offset = 100
    for i, entry in enumerate(leaderboard):
        drawText(f"{i + 1}. {entry['name']} - {entry['score']}", white, display_width / 2, y_offset, 30)
        y_offset += 40

    drawText("Press any key to return to menu", white, display_width / 2, display_height - 50, 20)
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                waiting = False

def navigable_menu():
    menu_options = ["Start", "Leaderboard", "Quit"]
    selected_option = 0  # Índice de la opción seleccionada

    running = True
    while running:
        gameDisplay.fill(black)

        # Dibujar las opciones del menú
        for i, option in enumerate(menu_options):
            color = white if i == selected_option else red
            drawText(option, color, display_width / 2, display_height / 2 + i * 50, 40)

        pygame.display.update()

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:  # Seleccionar opción
                    if menu_options[selected_option] == "Start":
                        return "Playing"  # Inicia el juego
                    elif menu_options[selected_option] == "Leaderboard":
                        show_leaderboard()  # Muestra el Leaderboard
                    elif menu_options[selected_option] == "Quit":
                        pygame.quit()
                        quit()


def get_player_name():
    name = ""
    active = True
    while active:
        gameDisplay.fill(black)
        drawText("Enter your name:", white, display_width / 2, display_height / 2 - 50, 50)
        drawText(name, white, display_width / 2, display_height / 2, 50)
        drawText("Press Enter to save", white, display_width / 2, display_height / 2 + 50, 20)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode
    return name