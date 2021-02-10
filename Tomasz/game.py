import pygame
from math import sin, cos, pi
from random import choice, uniform, randint

OKNO_SZER = 800
OKNO_WYS = 600
FPS = 60

PALETKA_WYS = 80
PALETKA_SZER = 20
PIŁKA_R = 10
SPEED = 4

STOP_PLAY = 20
MAX_LICZBA_PILEK = 3

PALETKA = (255, 255, 255)
PIŁKA = (255, 255, 255)
TŁO = (0, 0, 0)
TEKST = (127, 127, 127)
WINNER = (127, 255, 127)
LOOSER = (255, 127, 127)

pygame.init()
okienko = pygame.display.set_mode((OKNO_SZER, OKNO_WYS), 0, 32)
pygame.display.set_caption("Przykład Ponga")
zegarek = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 64)

gracz1 = pygame.Rect(0, OKNO_WYS // 2 - PALETKA_WYS // 2, PALETKA_SZER, PALETKA_WYS)
gracz2 = pygame.Rect(OKNO_SZER - PALETKA_SZER, OKNO_WYS // 2 - PALETKA_WYS // 2, PALETKA_SZER, PALETKA_WYS)

gracz1_speed = 0
gracz2_speed = 0


def nowa_piłka(nowa=True):
    global lista_pilek
    phi = uniform(-pi / 3, pi / 3)
    piłka_x = OKNO_SZER // 2
    piłka_y = OKNO_WYS // 2
    piłka_dx = SPEED * choice([-1, 1]) * cos(phi)
    piłka_dy = SPEED * sin(phi)
    a = {}
    color = (randint(100, 255), randint(100, 255), randint(100, 255))

    a['piłka_x'] = piłka_x
    a['piłka_y'] = piłka_y
    a['piłka_dx'] = piłka_dx
    a['piłka_dy'] = piłka_dy
    a['color'] = color
    if nowa:
        lista_pilek.append(a)
    else:
        return a




gracz1_wynik = 0
gracz2_wynik = 0
gracz1_text = font.render("0", True, TEKST)
gracz2_text = font.render("0", True, TEKST)

lista_pilek = []
nowa_piłka()

graj = True


while graj:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            graj = False
        elif zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_w:
                gracz1_speed -= SPEED
            elif zdarzenie.key == pygame.K_s:
                gracz1_speed += SPEED
            elif zdarzenie.key == pygame.K_UP:
                gracz2_speed -= SPEED
            elif zdarzenie.key == pygame.K_DOWN:
                gracz2_speed += SPEED
        elif zdarzenie.type == pygame.KEYUP:
            if zdarzenie.key == pygame.K_w:
                gracz1_speed += SPEED
            elif zdarzenie.key == pygame.K_s:
                gracz1_speed -= SPEED
            elif zdarzenie.key == pygame.K_UP:
                gracz2_speed += SPEED
            elif zdarzenie.key == pygame.K_DOWN:
                gracz2_speed -= SPEED

    gracz1.y += gracz1_speed
    if gracz1.y < 0:
        gracz1.y = 0
    elif gracz1.y > OKNO_WYS - PALETKA_WYS:
        gracz1.y = OKNO_WYS - PALETKA_WYS
    gracz2.y += gracz2_speed
    if gracz2.y < 0:
        gracz2.y = 0
    elif gracz2.y > OKNO_WYS - PALETKA_WYS:
        gracz2.y = OKNO_WYS - PALETKA_WYS


    for index, pilka in enumerate(lista_pilek, start=0) : #[{},{}]
        pilka["piłka_x"] += pilka["piłka_dx"]
        pilka["piłka_y"] += pilka["piłka_dy"]

        if pilka["piłka_y"] < PIŁKA_R:
            wystaje = PIŁKA_R - pilka["piłka_y"]
            pilka["piłka_y"] = PIŁKA_R + wystaje
            pilka["piłka_dy"] *= -1
        elif pilka["piłka_y"] > OKNO_WYS - PIŁKA_R:
            wystaje = pilka["piłka_y"] - (OKNO_WYS - PIŁKA_R)
            pilka["piłka_y"] = OKNO_WYS - PIŁKA_R - wystaje
            pilka["piłka_dy"] *= -1
        if pilka["piłka_x"] < PIŁKA_R + PALETKA_SZER:
            if gracz1.y <= pilka["piłka_y"] <= gracz1.y + PALETKA_WYS:
                wystaje = PIŁKA_R + PALETKA_SZER - pilka["piłka_x"]
                pilka["piłka_x"] = PIŁKA_R + PALETKA_SZER + wystaje
                pilka["piłka_dx"] *= -1
            else:
                if gracz1_wynik < STOP_PLAY and gracz2_wynik < STOP_PLAY:
                    gracz2_wynik += 1

                if gracz2_wynik >= STOP_PLAY:
                    gracz1_text = font.render(str(gracz1_wynik), True, LOOSER)
                    gracz2_text = font.render(str(gracz2_wynik), True, WINNER)
                    SPEED = 0
                    gracz1_speed = 0
                    gracz2_speed = 0
                else:
                    gracz2_text = font.render(str(gracz2_wynik), True, TEKST)
                lista_pilek.pop(index)
                liczba_pilek = choice([1,2])
                print(id(lista_pilek),lista_pilek)
                for liczba in range(liczba_pilek):
                    if len(lista_pilek) > MAX_LICZBA_PILEK:
                        break
                    nowa_piłka()
        elif pilka["piłka_x"] > OKNO_SZER - PALETKA_SZER - PIŁKA_R:
            if gracz2.y <= pilka["piłka_y"] <= gracz2.y + PALETKA_WYS:
                wystaje = pilka["piłka_x"] - (OKNO_SZER - PALETKA_SZER - PIŁKA_R)
                pilka["piłka_x"] = OKNO_SZER - PALETKA_SZER - PIŁKA_R - wystaje
                pilka["piłka_dx"] *= -1
            else:
                if gracz1_wynik < STOP_PLAY and gracz2_wynik < STOP_PLAY:
                    gracz1_wynik += 1

                if gracz1_wynik >= STOP_PLAY:
                    gracz1_text = font.render(str(gracz1_wynik), True, WINNER)
                    gracz2_text = font.render(str(gracz2_wynik), True, LOOSER)
                    SPEED = 0
                    gracz1_speed = 0
                    gracz2_speed = 0
                else:
                    gracz1_text = font.render(str(gracz1_wynik), True, TEKST)
                lista_pilek.pop(index)
                liczba_pilek = choice([1,2])
                print(id(lista_pilek), lista_pilek)
                for liczba in range(liczba_pilek):
                    if len(lista_pilek) >= MAX_LICZBA_PILEK:
                        break
                    nowa_piłka()


    okienko.fill(TŁO)
    okienko.blit(gracz1_text, (40, 40))
    okienko.blit(gracz2_text, (OKNO_SZER - 40 - gracz2_text.get_rect().width, 40))
    pygame.draw.rect(okienko, PALETKA, gracz1)
    pygame.draw.rect(okienko, PALETKA, gracz2)

    for pilka in lista_pilek: # {piłka_x= 20 ...} {}
        pygame.draw.circle(okienko, pilka['color'], (pilka['piłka_x'], pilka['piłka_y']), PIŁKA_R)


    pygame.display.update()
    zegarek.tick(FPS)

pygame.quit()