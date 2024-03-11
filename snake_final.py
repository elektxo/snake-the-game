import pygame

import random

# Inicialización de Pygame
pygame.init()

# Definición de colores
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

score = 0

# Tamaño de la pantalla
dis_width = 800
dis_height = 600

# Tamaño de los bloques del snake
block_size = 20

# Fuente y tamaño para el texto
font_style = pygame.font.SysFont("bahnschrift", 25)

# Función para mostrar texto en pantalla
def message(msg, color):
    global score
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

    msg2 = f"Tu puntuacion es de {score}"
    mesg2 = font_style.render(msg2, True, green)
    dis.blit(mesg2, [dis_width / 6, dis_height / 4])

# Función principal del juego
def gameLoop():
    global score
    # Variables para controlar el juego
    game_over = False
    game_close = False
    score = 0

    # Posición inicial del snake
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Velocidad inicial del snake
    x1_change = 0
    y1_change = 0

    # Lista para almacenar las posiciones del snake
    snake_List = []
    length_of_snake = 1

    # Posición aleatoria de la comida
    foodx = round(random.randrange(0, dis_width - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, dis_height - block_size) / 20.0) * 20.0

    # Bucle principal del juego
    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("¡Perdiste! Presiona Q-Quitar o C-Jugar de Nuevo", red)
            pygame.display.update()

            # Manejo de eventos del teclado
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Manejo de eventos del teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Verificación de bordes
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, block_size, block_size])

        # Añadir la nueva posición del snake a la lista
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > length_of_snake:
            del snake_List[0]

        # Verificar si el snake se ha chocado consigo mismo
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Dibujar el snake
        for segment in snake_List:
            pygame.draw.rect(dis, black, [segment[0], segment[1], block_size, block_size])

        # Actualizar la pantalla
        pygame.display.update()

        # Verificar si el snake ha comido la comida
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - block_size) / 20.0) * 20.0
            length_of_snake += 1
            score += 1

        # Control de velocidad del juego
        pygame.time.Clock().tick(15)

    pygame.quit()
    quit()


# Inicializar la pantalla del juego
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# Iniciar el juego
gameLoop()
