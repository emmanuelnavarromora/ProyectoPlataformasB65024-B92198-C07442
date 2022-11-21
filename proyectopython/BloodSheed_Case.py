#!/usr/bin/python3
# Universidad de Costa Rica
# Programación Bajo Plataformas Abiertas
# Proyecto de Python: Juego Tipo Point and Click
# Profesor: Julian Gairaud
# Estudiantes:  Andrés Chaves Vargas (B92198), Emmanuel Nvarro (B65024),
# Steven Segura Ulloa (C07442)
# Nombre del Juego: Bloodsheed Case

import pygame
import time
# import sys
# from pygame.locals import *
pygame.init()
# Variables de Ventana Inicial y Menú de Inicio
if __name__ == '__main__':
    WIDTH, HEIGHT = 800, 400
    BLACK = (0, 0, 0)
    FPS = 60
    COL_TEXT = (255, 255, 255)
    run = True
    initial_game = False
    fullscreen = False
    WHITE = (255, 255, 255)
    azul_claro = (0, 128, 255)

    monitor_size = [pygame.display.Info().current_w,
                    pygame.display.Info().current_h]
    WINDOW = pygame.display.set_mode(
            monitor_size, pygame.HWSURFACE |
            pygame.DOUBLEBUF |
            pygame.RESIZABLE)
    pygame.display.set_caption('BloodSheed Case')
    FONT = pygame.font.SysFont('arialblack', 40)

    # Imagenes del Juego
    inicial_Background = pygame.image.load(
                    'bloodsheedcase.png').convert_alpha()
    inicial_Background2 = pygame.image.load(
                    'Bloodsheed Case (1).png').convert_alpha()
    scene_1 = pygame.image.load('Oficina.png').convert_alpha()
    scene_2 = pygame.image.load('Edificio.png').convert_alpha()
    Sam = pygame.image.load('Sam.png').convert_alpha()
    Sam2 = pygame.image.load('Sam2.png').convert_alpha()
    Ryan = pygame.image.load('Ryan.png').convert_alpha()
    Ryan2 = pygame.image.load('Ryan2.png').convert_alpha()
    Shawn = pygame.image.load('Shawn.jpeg').convert_alpha()
    Shawn2 = pygame.image.load('Shawn2.png').convert_alpha()
    manager = pygame.image.load('Guarda.png').convert_alpha()
    neighbor = pygame.image.load('Vecina.png').convert_alpha()
    crime_Scene = pygame.image.load('fondo.jpeg').convert_alpha()
    trial_Scene = pygame.image.load('juicio.jpeg').convert_alpha()
    winner_Scene = pygame.image.load('Ganador.png').convert_alpha()
    no_Evidence = pygame.image.load('No_evidencia.png').convert_alpha()
    game_Over = pygame.image.load('Fin_Juego.png').convert_alpha()
    # Imagenes de Botones
    img_initial = pygame.image.load('boton_iniciar.png').convert_alpha()
    img_out = pygame.image.load('boton_salir.png').convert_alpha()
    img_resume = pygame.image.load('boton_reanudar.png').convert_alpha()
    img_back = pygame.image.load('boton_regresar.png').convert_alpha()
    img_sinfondo = pygame.image.load('sinfondo.png').convert_alpha()
    img_shawn = pygame.image.load('Button_Shawn.png').convert_alpha()
    img_ryan = pygame.image.load('Button_Ryan.png').convert_alpha()
    img_sam = pygame.image.load('Button_Sam.png').convert_alpha()
    # Textos utilizados en el juego
    # Parte 1
    initial_text = 'Presione ESPACIO para Iniciar'
    text1 = '''Detective:  Aló!, en que puedo servirle.

    Policia: Buenas noches dectective tenemos un nuevo caso de homicidio

    y necesitamos su ayuda para hallar al culpable.

    Ensegida le envio la dirección del lugar del suceso!!'''

    text2 = '''Policia: Buenas noches detective...

    El suceso se dio en la habitacion 319, donde la victima llamada Sarah vivia

    , se sabe que era una estudiante de teatro y que le encantaba cocinar,  asi

    como la tecnologia y la vida fitness.'''

    text3 = '''Policia: Entre los principales sospechosos se encuentra Sam que

    era su mejor amiga y companera de cuarto, tambien se tiene a Shawn que era

    otro de sus amigos, este la fue a visitar enterandose que habia fallecido y

    el ultimo sospecho  es Ryan un trabajador de una tienda de telefonos fue

    visto por lo vecinos entrar al apartemento unas horas antes'''

    text4 = '''Informacion de Sam:

    Los policias notaron que se encontraba ansiosa, ademas tenia sangre en su

    ropa, tenia una una quebrada y durante su declaracion se fotaba sus manos

    constantemente. Ella menciono que era la companera de cuarto de Sarah pero

    no se encontraba en el lugar de los echos cuando y enrealidad se entero por

    una llamada, adicionalmente tenia la ropa seca.'''

    text5 = '''Informacion de Ryan: Los policias indican que Ryan menciona poca

    informacion ya que no pudo observar casi nada durante su paso por el lugar

    debido a que perdio sus lentes, al ser requisado se encontro una factura a

    nombre de la victima, por la compra de un celular y dijo que cuando fue a

    entregarle el celular Sarah se encontraba bien, como dato adicional este se

    encontraba totalmente empapado por la fuerte lluvia de hace unas horas.'''

    text6 = '''Informacion de Shawn: Durante su entrevista los policias

    observaron tenia rasgunos en sus manos, tambien mencionaron que este se
    
    mostraba muy triste e indignado por la noticia. Shawn comento que venia de
    
    estar con su novia y cuando se le pregunto por que estaba seco alego que
    
    vino en taxi. Ademas se supo que es un peleador profesional de artes
    
    marciales y en su bolsillo se encontro un lapisero con el nombre Sarah'''
    # Parte 2


    class Buttons():
        # Constructor
        def __init__(self, x, y, image, scale):
            width = image.get_width()
            height = image.get_height()
            self.image = pygame.transform.scale(
                    image, (int(width * scale), int(height * scale)))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw_buttons(self, surface):
            # Encontrar la posicion del mouse
            mouse_pos = pygame.mouse.get_pos()
            action_mouse = False

            # Funcionamiento de los clicks con el mouse_pos
            if self.rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action_mouse = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            # Dibujar los botones en la pantalla
            surface.blit(self.image, (self.rect.x, self.rect.y))
            return action_mouse
        def draw_buttons_one_use(self, surface):
            # Encontrar la posicion del mouse
            mouse_pos = pygame.mouse.get_pos()
            action_mouse = False

            # Funcionamiento de los clicks con el mouse_pos
            if self.rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action_mouse = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            # Dibujar los botones en la pantalla
            surface.blit(self.image, (self.rect.x, self.rect.y))
            return action_mouse

    # Crear las instancias de los botones
    button_initial = Buttons(
                    (WINDOW.get_width()//4.6),
                    WINDOW.get_height()//1.24,
                    img_initial, 0.5)
    button_out = Buttons(
                    WINDOW.get_width()//1.7,
                    WINDOW.get_height()//1.25,
                    img_out, 0.5)
    button_resume = Buttons(
                    WINDOW.get_width()//13.333,
                    WINDOW.get_height()//3.2,
                    img_resume, 0.5)
    button_back = Buttons(
                    WINDOW.get_width()//1.5686,
                    WINDOW.get_height()//3.2,
                    img_back, 0.5)
    button_bed = Buttons(
                    WINDOW.get_width()//15,
                    WINDOW.get_height()//1.5,
                    img_sinfondo, 0.6)
    button_wardrobe = Buttons(
                    WINDOW.get_width()//6.6,
                    WINDOW.get_height()//2.9,
                    img_sinfondo, 0.7)
    button_chair = Buttons(
                    WINDOW.get_width()//3.5,
                    WINDOW.get_height()//1.8,
                    img_sinfondo, 0.25)
    button_desk = Buttons(
                    WINDOW.get_width()//2.7,
                    WINDOW.get_height()//2.4,
                    img_sinfondo, 0.6)

    button_lamp = Buttons(
                    WINDOW.get_width()//1.55,
                    WINDOW.get_height()//18,
                    img_sinfondo, 0.5)

    button_shelf = Buttons(
                    WINDOW.get_width()//1.57,
                    WINDOW.get_height()//3.35,
                    img_sinfondo, 0.7)

    button_door = Buttons(
                    WINDOW.get_width()//1.13,
                    WINDOW.get_height()//2.4,
                    img_sinfondo, 0.4)

    button_wardrobe_key = Buttons(
                    WINDOW.get_width()//1.5686,
                    WINDOW.get_height()//3.2,
                    img_sinfondo, 0.5)
    button_lockbox_code = Buttons(
                    WINDOW.get_width()//1.5686,
                    WINDOW.get_height()//3.2,
                    img_sinfondo, 0.5)

    button_sam = Buttons(
                    WINDOW.get_width()//13.333,
                    WINDOW.get_height()//3.2,
                    img_sam, 0.5)
    button_shawn = Buttons(
                    WINDOW.get_width()//2.9629,
                    WINDOW.get_height()//3.2,
                    img_shawn, 0.5)
    button_ryan = Buttons(
                    WINDOW.get_width()//1.5686,
                    WINDOW.get_height()//3.2,
                    img_ryan, 0.5)
    def texts(text, font, col_text, x, y):  # Muestra los textos en pantalla
        img = font.render(text, True, col_text)
        WINDOW.blit(img, (x, y))

    def scenes(scene_img):
        WINDOW.blit(pygame.transform.scale(
                    scene_img, (WINDOW.get_width()-60, WINDOW.get_height()-60)),
                    (0, 0))

    def render_multi_line(text, x, y, fsize):
        lines = text.splitlines()
        for i, l in enumerate(lines):
            font = pygame.font.SysFont('timesnewroman', 2*fsize)
            WINDOW.blit(font.render(l, 0, WHITE), (x, y+1 + fsize*i))

    def sounds(sound):
        pygame.mixer.init()
        pygame.mixer.music.load(sound)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()

    # Estados necesarios
    game_articles = False
    game_pause = False
    game_state = 'main'
    button_state = False
    button_Bed = False
    button_Wardrobe = False
    button_Chair = False
    button_Desk = False
    button_Lamp = False
    button_Shelf = False
    button_Door = False
    button_Wardrobe_Key = False
    button_Lockbox_Code = False
    button_Winner = False
    button_gameover = False
    articles = []
    while run:
        clock = pygame.time.Clock()
        WINDOW.blit(pygame.transform.scale(
                    inicial_Background,
                    (WINDOW.get_width(), WINDOW.get_height())),
                    (0, 0))
        clock.tick(FPS)

        if initial_game == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.VIDEORESIZE:
                    if not fullscreen:
                        WINDOW = pygame.display.set_mode(
                                (event.w, event.h),
                                pygame.HWSURFACE |
                                pygame.DOUBLEBUF |
                                pygame.RESIZABLE)

                    if fullscreen:
                        WINDOW = pygame.display.set_mode(
                            monitor_size, pygame.FULLSCREEN)
                    else:
                        WINDOW = pygame.display.set_mode(
                            (WINDOW.get_width(), WINDOW.get_height()),
                            pygame.HWSURFACE |
                            pygame.DOUBLEBUF |
                            pygame.RESIZABLE)
            WINDOW.blit(pygame.transform.scale(
                        inicial_Background,
                        (WINDOW.get_width(), WINDOW.get_height())),
                        (0, 0))
            # Revisa el estado en que se encuentra el menu

            if game_state == 'main':
                game_pause = False
                # Lo que sucede al presionar cada boton
                if button_initial.draw_buttons(WINDOW):
                    game_state = 'Escena_1.1'
                    #sounds('Phone.mp3')
                if button_out.draw_buttons(WINDOW):
                    run = False
            if game_pause == False:
                # Parte 1: Introduccion
                if game_state == 'Escena_1.1':
                    scenes(scene_1)
                    render_multi_line(initial_text, 10, 10, 15)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                game_state = 'Escena_1.2'
                            if event.key == pygame.K_p:
                                game_pause = True

                if game_state == 'Escena_1.2':
                    scenes(scene_1)
                    # change_scenes(texto1)
                    render_multi_line(text1, 10, 10, 15)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                game_state = 'Escena_1.3'
                                # sounds('Sirena Policia.mp3')
                            if event.key == pygame.K_p:
                                game_pause = True

                if game_state == 'Escena_1.3':
                    scenes(scene_2)
                    # sounds('Sirena Policia.mp3')
                    render_multi_line(text2, 10, 10, 15)
                    for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                game_state = 'Escena_1.3.1'
                            if event.key == pygame.K_p:
                                game_pause = True

                if game_state == 'Escena_1.3.1':
                    scenes(scene_2)
                    render_multi_line(text3, 10, 10, 15)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                game_state = 'Escena_1.4'
                                #sounds('SonidoAmbiente.mp3')
                            if event.key == pygame.K_p:
                                game_pause = True

                if game_state == 'Escena_1.4':
                    scenes(Sam2)
                    render_multi_line(text4, 10, 10, 15)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                game_state = 'Escena_1.5'
                            if event.key == pygame.K_p:
                                game_pause = True
                if game_state == 'Escena_1.5':
                    scenes(Ryan2)
                    render_multi_line(text5, 10, 10, 15)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                game_state = 'Escena_1.6'
                            if event.key == pygame.K_p:
                                game_pause = True
                if game_state == 'Escena_1.6':
                    scenes(Shawn2)
                    render_multi_line(text6, 10, 10, 15)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                game_state = 'Escena_2.1'
                            if event.key == pygame.K_p:
                                game_pause = True

                # Parte 2: Seleccion de Elementos

            if button_state == False:
                if game_state == 'Escena_2.1':
                    scenes(crime_Scene)
                    render_multi_line('''Investigue la escena del crimen y encuentre

                    todo lo necesario para el juicio. Toque la puerta cuando quiera

                    iniciar el juicio''', 10, 10, 15)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                game_state = 'Escena_2.2'
                            if event.key == pygame.K_p:
                                game_pause = True

                if game_state == 'Escena_2.2':
                    scenes(crime_Scene)
                    if 'salida' in articles:
                        game_state = 'Escena_3.1'
                    else:
                        button_state = True

                if game_state == 'Escena_3.1':
                    scenes(trial_Scene)
                    render_multi_line('''Se va a iniciar por el asesinato de Samantha

                                , por favor detective presente los hallazgos de

                                su investigación''', 10, 10, 15)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                game_state = 'Escena_3.2'
                            if event.key == pygame.K_p:
                                game_pause = True

                if game_state == 'Escena_3.2':
                    scenes(trial_Scene)
                    render_multi_line('Juez: \n' +
                            'Presente el motivo del asesinato:', 10, 10, 15)
                    if 'segunda pista' in articles:
                        scenes(trial_Scene)
                        render_multi_line('Juez: \n' +
                                '''Sara estaba a punto de recibir una
                                
                                enorme herencia familiar''', 10, 10, 15)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    game_state = 'Escena_3.3'
                                if event.key == pygame.K_p:
                                    game_pause = True
                    else:
                        scenes(trial_Scene)
                        render_multi_line('Detective: \n' + '''No encontre el motivo del asesinato.
                                
                                Tuve que haber hecho un mejor trabajo.'''
                                , 10, 10, 15)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    game_state = 'Game_Over'

                if game_state == 'Escena_3.3':
                    scenes(trial_Scene)
                    render_multi_line('Juez: \n' +
                            'Presente evidencia clave:', 10, 10, 15)
                    if 'tercera pista' in articles:
                        scenes(trial_Scene)
                        render_multi_line('Detective: \n' +
                                '''Un anillo de compromiso con la fecha
                                
                                05/02/19.''', 10, 10, 15)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    game_state = 'Escena_3.4'
                                if event.key == pygame.K_p:
                                    game_pause = True
                    else:
                        scenes(trial_Scene)
                        render_multi_line('Detective: \n' + '''No encontre evidencia clave.
                                
                                Tuve que haber hecho un mejor trabajo.'''
                                , 10, 10, 15)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    game_state = 'Game_Over'

                if game_state == 'Escena_3.4':
                    scenes(trial_Scene)
                    render_multi_line('''Presente el arma homicida''', 10, 10, 15)
                    if 'arma homicida' in articles:
                        scenes(trial_Scene)
                        render_multi_line('''El arma homicida fue encontrada
                                
                                en la caja fuerte de un armario. Es un cuchillo.'''
                                , 10, 10, 15)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    game_state = 'Escena_3.5'
                                if event.key == pygame.K_p:
                                    game_pause = True
                    else:
                        scenes(trial_Scene)
                        render_multi_line('''No encontre el arma homicida.
                                
                                No se puede saber quien es el asesino.
                                
                                Tuve que haber hecho un mejor trabajo.'''
                                , 10, 10, 15)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    game_state = 'Game_Over'

                if game_state == 'Escena_3.5':
                    scenes(trial_Scene)
                    render_multi_line('Juez: \n' +
                            '''Con la evidencia mostrada, a quien determina como
                            
                            el culpable?:''', 10, 10, 15)
                    if 'primera pista' in articles:
                        scenes(trial_Scene)
                        render_multi_line('Detective: \n' +  '''El arma fue

                            encontrada en una caja fuerte con la contraseña

                            050219 misma que el anillo. Esto significa que el

                            asesino conocia la contraseña, luego de algunas

                            interrogaciones, se determino que la otra unica

                            persona que conocia esta fecha era:'''
                             , 10, 10, 15)
                        if button_shawn.draw_buttons(WINDOW):
                            #shawn
                            game_state = 'button_Shawn'

                        if button_ryan.draw_buttons(WINDOW):
                            #ryan
                            game_state = 'button_Ryan'
                        if button_sam.draw_buttons(WINDOW):
                            #sam
                            game_state = 'button_Sam'
                    else:
                        scenes(trial_Scene)
                        render_multi_line('Detective: \n' + '''No encontre suficiente
                                    
                    evidencia para encontrar un culpable.
                                
                    Tuve que haber hecho un mejor trabajo.'''
                                , 10, 10, 15)
                if game_state == 'button_Shawn':
                    scenes(trial_Scene)
                    render_multi_line('Detective: \n' + '''Su novio Shawn''', 10, 10, 15)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                game_state = 'Escena_3.6'
                            if event.key == pygame.K_p:
                                game_pause = True
                if game_state == 'button_Ryan':
                    scenes(trial_Scene)
                    render_multi_line('Detective: \n' + '''Ryan ''', 10, 10, 15)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                game_state = 'Game_Over'
                            if event.key == pygame.K_p:
                                game_pause = True
                if game_state == 'button_Sam':
                    scenes(trial_Scene)
                    render_multi_line('Detective: \n' + '''Su mejor amiga Sam ''', 10, 10, 15)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                game_state = 'Game_Over'
                            if event.key == pygame.K_p:
                                game_pause = True
                if game_state == 'Escena_3.6':
                    scenes(trial_Scene)
                    render_multi_line('Juez: \n' +
                            '''Buen trabajo detective, consiguio resolver el caso:''', 10, 10, 15)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                game_state = 'Escena_Win'
                            if event.key == pygame.K_p:
                                game_pause = True

                if game_state == 'Game_Over':
                    button_gameover = True
                    scenes(game_Over)
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                button_gameover = False
                                game_state = 'main'
                                articles.clear()
                if game_state == 'Escena_Win':
                    button_Winner = True
                    scenes(winner_Scene)
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                button_Winner = False
                                game_state = 'main'
                                articles.clear()
            if button_gameover == True:
                scenes(game_Over)
            if button_Winner == True:
                scenes(winner_Scene)
            if button_state == True:
                scenes(crime_Scene)

                if button_bed.draw_buttons(WINDOW):
                    button_Bed = True
                if button_wardrobe.draw_buttons(WINDOW):
                    button_Wardrobe = True
                if button_chair.draw_buttons(WINDOW):
                    button_Chair = True
                if button_desk.draw_buttons(WINDOW):
                    button_Desk = True
                if button_lamp.draw_buttons(WINDOW):
                    button_Lamp = True
                if button_shelf.draw_buttons(WINDOW):
                    button_Shelf = True
                if button_door.draw_buttons(WINDOW):
                    button_Door = True

            if button_Wardrobe == True:
                scenes(crime_Scene)
                # render_multi_line(text_Wardrobe, 10, 10, 15)
                if 'llave armario' in articles:

                    render_multi_line('Se abrio el armario', 10, 10, 15)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            game_pause = True
                        else:
                            scenes(crime_Scene)
                            render_multi_line('''Se encontro una caja fuerte al fondo del armario, se necesita una
                            
                            contraseña de cuatro digitos para abrirla''', 10, 10, 15)
                            articles.append('caja fuerte')
                            button_Lockbox_Code = True
                else:
                    render_multi_line('Es necesaria una llave para abrir el armario', 10, 10, 15)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_p:
                                game_pause = True
                            else:
                                button_Wardrobe = False

            if button_Lockbox_Code == True:
                if 'caja fuerte' in articles:
                    scenes(crime_Scene)
                    render_multi_line('''Digite la clave de la caja fuerte:''', 10, 10, 15)
                    if 'primera pista' in articles:
                        if 'segunda pista' in articles:
                            if 'tercera pista' in articles:
                                scenes(crime_Scene)
                                render_multi_line('''Se encontro el arma homicida''', 10, 10, 15)
                                articles.append('arma homicida')
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        run = False
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_p:
                                            game_pause = True
                                        else:
                                            button_Lockbox_Code = False
                                            button_Wardrobe = False
                            else:
                                scenes(crime_Scene)
                                render_multi_line('''Se necesitan mas pistas''', 10, 10, 15)
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        run = False
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_p:
                                            game_pause = True
                                        else:
                                            button_Lockbox_Code = False
                                            button_Wardrobe = False
                        else:
                            scenes(crime_Scene)
                            render_multi_line('''Se necesitan mas pistas''', 10, 10, 15)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    run = False
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_p:
                                        game_pause = True
                                    else:
                                        button_Lockbox_Code = False
                                        button_Wardrobe = False
                    else:
                        scenes(crime_Scene)
                        render_multi_line('''Se necesitan mas pistas''', 10, 10, 15)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_p:
                                    game_pause = True
                                else:
                                    button_Lockbox_Code = False
                                    button_Wardrobe = False

            # Pistas variables
            if button_Chair == True:
                scenes(crime_Scene)
                if 'chair enable' in articles:
                    render_multi_line('Presione S para mover la silla y alcanzar la lampara', 10, 10, 15)
                    articles.append('moved chair')
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_p:
                                game_pause = True
                            if event.key == pygame.K_s:
                                button_Lamp = True
                            else:
                                button_Chair = False
                else:
                    render_multi_line('Es solamente una silla', 10, 10, 15)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_p:
                                game_pause = True
                            else:
                                button_Chair = False
            if button_Shelf == True:
                scenes(crime_Scene)
                render_multi_line('''Una nota que indica que Sara solicito
                                
                cambiar la contraseña su caja fuerte por algo que
                                
                                no iba a olvidar''', 10, 10, 15)
                articles.append('segunda pista')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            button_Shelf = False
                    if event.key == pygame.K_p:
                        game_pause = True
            if button_Desk == True:
                scenes(crime_Scene)
                render_multi_line('''Sara recibio una carta de que iba a recibir
                            
                            una gran herencia de su familia''', 10, 10, 15)
                articles.append('primera pista')
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            button_Desk = False
                        if event.key == pygame.K_p:
                            game_pause = True

            if button_Lamp == True:
                scenes(crime_Scene)
                render_multi_line('Deberia utilizar una silla para alcanzar la lampara', 10, 10, 15)
                articles.append('chair enable')
                if 'moved chair' in articles:
                    scenes(crime_Scene)
                    render_multi_line('Dentro de la lampara encuentra la llave del armario', 10, 10, 15)
                    articles.append('llave armario')
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            button_Lamp = False

                        if event.key == pygame.K_p:
                            game_pause = True
            if button_Bed == True:
                scenes(crime_Scene)
                render_multi_line('''En la cama se encuentra un anillo
                                    
                con la fecha 05/02/19'''
                                , 10, 10, 15)
                articles.append('tercera pista')
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            button_Bed = False
                        if event.key == pygame.K_p:
                            game_pause = True
            if button_Door == True:
                scenes(crime_Scene)
                render_multi_line('''Le gustaria iniciar el juicio? Presione s para
                                    
                                    continuar''', 10, 10, 15)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            game_pause = True
                        if event.key == pygame.K_s:
                            button_Door = False
                            button_state = False
                            articles.append('salida')
                        else:
                            button_Door = False
            elif game_pause == True:
                WINDOW.blit(pygame.transform.scale(
                            inicial_Background2,
                            (WINDOW.get_width(), WINDOW.get_height())),
                            (0, 0))
                if button_resume.draw_buttons(WINDOW):
                    game_pause = False
                if button_back.draw_buttons(WINDOW):
                    game_state = 'main'

                if game_articles == True:
                    WINDOW.blit(pygame.transform.scale(
                                inicial_Background2,
                                (WINDOW.get_width(), WINDOW.get_height())),
                                (0, 0))
                    if button_video.draw_buttons(WINDOW):
                        pass
                    if button_back2.draw_buttons(WINDOW):
                        game_pause = True
                pygame.display.update()
        else:
            texts(
                initial_text,
                FONT, COL_TEXT,
                WINDOW.get_width()//3,
                WINDOW.get_height()//1.2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.VIDEORESIZE:
                if not fullscreen:
                    WINDOW = pygame.display.set_mode(
                            (event.w, event.h),
                            pygame.HWSURFACE |
                            pygame.DOUBLEBUF |
                            pygame.RESIZABLE)
                if fullscreen:
                    WINDOW = pygame.display.set_mode(
                        monitor_size, pygame.FULLSCREEN)
                else:
                    WINDOW = pygame.display.set_mode(
                        (WINDOW.get_width(), WINDOW.get_height()),
                        pygame.HWSURFACE |
                        pygame.DOUBLEBUF |
                        pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Para parar el juego
                    initial_game = True
        pygame.display.update()
    pygame.quit()
