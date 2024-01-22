
import pygame
from pygame.locals import *
from sys import exit
from random import randint, choice, shuffle
from time import sleep
from math import atan2, degrees, pi, cos, sin, sqrt


pygame.init() #inicando a biblioteca

#Musica de fundo
pygame.mixer.music.set_volume(0.1)
background_music = pygame.mixer.music.load('BoxCat_Games_CPU Talk.mp3')
pygame.mixer.music.play(-1)

#Musica bonus


#Barulho moeda/maça
collision_noise = pygame.mixer.Sound('smw_coin.mp3')

som_morte = pygame.mixer.Sound('smw_game_over.wav')

som_vitoria = pygame.mixer.Sound('vitoria.mp3')

pygame.display.set_caption('Snake Game')



width = 1280
height = 720

key_right = K_d
key_left = K_a
key_down = K_s
key_up = K_w

vel = 8
x_control = vel
y_control = 0
life = 0
vida_apple = 0
escolha = 0
life_drop = False
apple_tamanho = 0
answer = 0
maca_verde_born = False

paused = 0

#Posicao inicial da cobra
x_snake = int(width/2)
y_snake = int(height/2)

#fonte do contador
font = pygame.font.SysFont('arial', 40, True, True)
font2 = pygame.font.SysFont('arial', 25, True, True)




#valor inicial do contador
points = 15
quiz_feito = False
fazendo_quiz = False
testando = False



#posiçao inicial da maça
x_apple = randint(40, 1200)
y_apple = randint(50,700)


x_troll_apple = randint(40, 1200)
y_troll_apple = randint(50,700)

x_life_apple = randint(40, 1200)
y_life_apple = randint(50, 700)


snake_lista = []

#controla a velocidade de frames por segundo(line:81)
clock = pygame.time.Clock()

#tela do game
screen_inicio = pygame.display.set_mode((width,height))
screen = pygame.display.set_mode((width,height))
screen_1 = pygame.display.set_mode((width,height))

first_length = 5

inicio = True
dead = False
finish = False

quizes = [
    ['Quem é o maior campeão da Copa do Mundo?', ['Brasil', 'França', 'Alemanha', 'Itália']],
    ['Qual a primeira Lei de Newton?', ['Inércia', 'Princípio Fundamental da Dinâmica', 'Lei da Ação e Reação', 'Lei da Gravidade']],
    ['Dois espelhos planos são alinhados, o ângulo que se forma é de 90°. Quantas imagens foram formadas?', ['3', '4', '2', '7']],
    ['A que temperatura a água ferve?', ['100 ºC', '-10ºC ', '180 ºC', '0ºC']],
    ['No período pré-colonial a atividade econômica que teve maior destaque foi:', ['Pau-Brasil', 'Mineração', 'Cana-de-açúcar', 'Café']],
    ['Qual o nome dos dois filhos do Neymar?', ['Davi e Mavie', 'Rafa e Marcos', 'Eduardo e Jair Renan', 'Luan e Ylana']],
    ['Qual dos seguintes não é considerado um recurso renovável?', ['Petróleo', 'Biomassa', 'Solar', 'Eólica']]

]


def x_y_apple():
    global x_apple, y_apple, x_apple_green, y_apple_green, x_troll_apple, y_troll_apple, x_life_apple, y_life_apple
    x_apple = randint(40 , 1200)
    y_apple = randint(50 , 700)
    x_troll_apple = randint(40, 1200)
    y_troll_apple = randint(50, 700)
    


def death():
    global inicio, dead
    dead_msg = f'GAME OVER! Press "R" to play again!'
    text2 = font.render(dead_msg, True, (0,0,0))
    ret_text = text2.get_rect()
    som_morte.play()
    pygame.mixer.music.set_volume(0)


    dead = True
    while dead:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    restart_game()
                if event.key == K_m:
                    inicio = True

        ret_text.center = (width//2, height//2)
        screen.blit(text2, ret_text)
        pygame.display.update()


#Aumentando o comprimento da cobra
def increases_snake(snake_lista):
    for XeY in snake_lista:
        #XeY = [x,y]
        #XeY[0] = x
        #XeY[1] = y
        pygame.draw.rect(screen, (0,255,0), (XeY[0], XeY[1], 20, 20))
        

def restart_game():
    global points, first_length, x_snake, y_apple, y_snake, x_apple, snake_lista, head_list, dead, vel, x_apple_green, y_apple_green, vol, key_right, key_left, key_down, key_up, apple_tamanho, quiz_feito, fazendo_quiz, life, vida_apple, escolha, answer, finish, maca_verde_born
    points = 15
    vel = 8
    first_length = 5
    x_snake = int(width/2)
    y_snake = int(height/2) 
    x_apple = randint(40,1200) 
    y_apple = randint(50,700) 
    x_apple_green = randint(40,1200)
    y_apple_green = randint(40,700)
    snake_lista = []
    head_list = []
    dead = False
    finish = False
    vol = pygame.mixer.music.set_volume(0.1)
    key_right = K_d
    key_left = K_a
    key_down = K_s
    key_up = K_w
    apple_tamanho = 0
    quiz_feito = False
    fazendo_quiz = False
    life = 0
    vida_apple = 0
    escolha = 0
    answer = 0
    maca_verde_born =False

font3 = pygame.font.SysFont('arial', 30, True, True)
msg_inicio = "WELCOME to the snake game! Press any key to continue!"
text_inicio = font3.render(msg_inicio, True, (0,0,0))
ret_text2 = text_inicio.get_rect()



while inicio:
    screen_inicio.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            inicio = False
            sleep(0.5)
            pygame.display.update()
    ret_text2.center = (width//2, height//2)
    screen_inicio.blit(text_inicio, ret_text2)
    pygame.display.update()


def apple_1(resposta):
    global paused, apple_tamanho, x_snake, y_snake, head_list, snake_lista,quiz_feito
    if resposta == 1:
        apple_tamanho = 1
    elif resposta == 2:
       apple_tamanho = 2    
    paused = 0
    x_snake = int(width/2)
    y_snake = int(height/2)
    snake_lista = []
    head_list = []
    pygame.display.update()
    quiz_feito = True

def vel_snake(resposta):
    global paused, x_snake, y_snake, snake_lista, head_list, quiz_feito, vel
    if resposta == 1:
        if points > 0 and points % 5 == 0:
            vel += 0.5
            if vel >= 16:
                vel = 16 
    if resposta == 2:
        if points > 0 and points % 2 == 0:
            vel += 2.5
            if vel >= 20:
                vel = 20
    paused = 0
    x_snake = int(width/2)
    y_snake = int(height/2)
    snake_lista = []
    head_list = []
    pygame.display.update()
    quiz_feito = True
    
def colors_double(resposta):
    global quiz_feito, points, first_length, paused, x_snake, y_snake, snake_lista, head_list
    if resposta == 1:
        x_y_apple()
        points += 2
        quiz_feito = False
        collision_noise.play() 
        first_length += 1      
    if resposta == 2:
        x_y_apple()
        points += 0.5
        quiz_feito = False
        collision_noise.play() 
        first_length += 1
    if resposta == 3:
        x_y_apple()
        points += 1
        quiz_feito = False
        collision_noise.play()
        first_length += 1
    
def finish():
    global final_msg, inicio, finish 
    final_msg = f'Parabéns você zerou meu humilde jogo!'
    text2 = font.render(final_msg, True, (0,0,0))
    ret_text = text2.get_rect()
    som_vitoria.play()
    pygame.mixer.music.set_volume(0)

    finish = True
    while finish:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    restart_game()
                if event.key == K_m:
                    inicio = True

        ret_text.center = (width//2, height//2)
        screen.blit(text2, ret_text)
        pygame.display.update()



while True:
    clock.tick(30)
    screen.fill((255,255,255))
    msg =  f"Pontos: {int(points)}"
    text = font.render(msg, True, (0,0,0))
    if life > 0:
        msg_2 = f"Vidas: {life}"
        text_2 = font.render(msg_2, True,(0,0,0))
        screen.blit(text_2, (width - 224, 80))

    if paused == 1:
        if not fazendo_quiz:
            quiz = choice(quizes)
            pergunta = quiz[0]
            respostas = [*quiz[1]]
            resposta_certa = respostas[0]
            shuffle(respostas)
            fazendo_quiz = True
        
        text = font2.render(pergunta, True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (width//2, height//2 - 200)
        screen.blit(text, text_rect)

        text_resposta_1 = font2.render(f'1) {respostas[0]}', True, (0,0,0))
        text_resposta_2 = font2.render(f'2) {respostas[1]}', True, (0,0,0))
        text_resposta_3 = font2.render(f'3) {respostas[2]}', True, (0,0,0))
        text_resposta_4 = font2.render(f'4) {respostas[3]}', True, (0,0,0))
        text_respostas_rect_1 = text_resposta_1.get_rect()
        text_respostas_rect_2 = text_resposta_2.get_rect()
        text_respostas_rect_3 = text_resposta_3.get_rect()
        text_respostas_rect_4 = text_resposta_4.get_rect()
        text_respostas_rect_1.center = (width//2, height//2 - 100)
        text_respostas_rect_2.center = (width//2, height//2 - 50)
        text_respostas_rect_3.center = (width//2, height//2)
        text_respostas_rect_4.center = (width//2, height//2 + 50)
        screen.blit(text_resposta_1, text_respostas_rect_1)
        screen.blit(text_resposta_2, text_respostas_rect_2)
        screen.blit(text_resposta_3, text_respostas_rect_3)
        screen.blit(text_resposta_4, text_respostas_rect_4)


        for event in pygame.event.get():
            if points == 5:
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_1:
                        if resposta_certa == respostas[0]:
                            apple_1(1)
                        else:
                            apple_1(2)
                    elif event.key == K_2:
                        if resposta_certa == respostas[1]:
                            apple_1(1)
                        else:
                            apple_1(2)
                    elif event.key == K_3:
                        if resposta_certa == respostas[2]:
                            apple_1(1)
                        else:
                            apple_1(2)
                    elif event.key == K_4:
                        if resposta_certa == respostas[3]:
                            apple_1(1)
                        else:
                            apple_1(2)
                    else:
                        paused = 1
            elif points == 10:
                if event.type == QUIT:
                    pygame.quit()            
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_1:
                        if resposta_certa == respostas[0]:
                            vel_snake(1)
                        else:
                            vel_snake(2)
                    elif event.key == K_2:
                        if resposta_certa == respostas[1]:
                            vel_snake(1)
                        else:
                            vel_snake(2)
                    elif event.key == K_3:
                        if resposta_certa == respostas[2]:
                            vel_snake(1)
                        else:
                            vel_snake(2)
                    elif event.key == K_4:
                        if resposta_certa == respostas[3]:
                            vel_snake(1)
                        else:
                            vel_snake(2)
                    else:
                        paused = 1
            elif points == 15:
                if event.type == QUIT:
                    pygame.quit()            
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_1:
                        if resposta_certa == respostas[0]:
                            answer = 1
                            paused = 0
                            x_snake = int(width/2)
                            y_snake = int(height/2)
                            snake_lista = []
                            head_list = []
                            pygame.display.update()
                            quiz_feito = True
                        else:
                            answer = 2
                            paused = 0
                            x_snake = int(width/2)
                            y_snake = int(height/2)
                            snake_lista = []
                            head_list = []
                            pygame.display.update()
                            quiz_feito = True

                    elif event.key == K_2:
                        if resposta_certa == respostas[1]:
                            answer = 1
                            paused = 0
                            x_snake = int(width/2)
                            y_snake = int(height/2)
                            snake_lista = []
                            head_list = []
                            pygame.display.update()
                            quiz_feito = True
                        else:
                            answer = 2
                            paused = 0
                            x_snake = int(width/2)
                            y_snake = int(height/2)
                            snake_lista = []
                            head_list = []
                            pygame.display.update()
                            quiz_feito = True
                    elif event.key == K_3:
                        if resposta_certa == respostas[2]:
                            answer = 1
                            paused = 0
                            x_snake = int(width/2)
                            y_snake = int(height/2)
                            snake_lista = []
                            head_list = []
                            pygame.display.update()
                            quiz_feito = True
                        else:
                            answer = 2
                            paused = 0
                            x_snake = int(width/2)
                            y_snake = int(height/2)
                            snake_lista = []
                            head_list = []
                            pygame.display.update()
                            quiz_feito = True
                    elif event.key == K_4:
                        if resposta_certa == respostas[3]:
                            answer = 1
                            paused = 0
                            x_snake = int(width/2)
                            y_snake = int(height/2)
                            snake_lista = []
                            head_list = []
                            pygame.display.update()
                            quiz_feito = True
                        else:
                            answer = 2
                            paused = 0
                            x_snake = int(width/2)
                            y_snake = int(height/2)
                            snake_lista = []
                            head_list = []
                            pygame.display.update()
                            quiz_feito = True
                    else:
                        paused = 1
            elif points == 20:
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                
                pygame.display.update()
                
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        #Dando funçao as teclas
        if event.type == KEYDOWN:
            if event.key == key_left:
                if x_control == vel: 
                    pass
                else:
                    x_control = - vel
                    y_control = 0 
                
            if event.key == key_right:
                if x_control == - vel:
                    pass
                else:
                    x_control = + vel
                    y_control = 0

            if event.key == key_up:
                if y_control == + vel:
                    pass
                else:
                    y_control = - vel
                    x_control = 0
            if event.key == key_down:
                if y_control == - vel:
                    pass
                else:
                    y_control = + vel
                    x_control = 0
    
    #jogo pausado para resolução de um quiz
    if paused == 1:
        pygame.display.flip()
        continue
    
   
    if points % 5 == 0 and 20 >  points > 0  and not quiz_feito:
        if paused != 1:
            paused = 1
        else:  
            paused = 0
        fazendo_quiz = False
        

    x_snake += x_control
    y_snake += y_control

    #desenhando elementos:
    #cobra/maça
    snake = pygame.draw.rect(screen, (0,255,0), (x_snake , y_snake , 20 , 20))
    if apple_tamanho == 0:
        apple = pygame.draw.circle(screen, (255,0,0), (x_apple, y_apple), 15, 0)
    elif apple_tamanho == 1:
        apple = pygame.draw.circle(screen, (255,0,0), (x_apple, y_apple), 20, 0)
    elif apple_tamanho == 2:
        apple = pygame.draw.circle(screen, (255,0,0), (x_apple, y_apple), 10, 0)

    #criando colisao
    if snake.colliderect(apple):
        if points <= 14:
         colors_double(3)
        elif points >= 25:
            colors_double(3) 
        else:
            if answer == 1:
                colors_double(1)
            elif answer == 2:
                colors_double(2)
        
    if 25 > points >= 15 and answer == 1:
        msg_2 = f"Multiplicador: 2x"
        text_2 = font.render(msg_2, True,(0,0,0))
        screen.blit(text_2, (width - 355, 80))
    elif 25 > points >= 15 and answer == 2:
        msg_2 = f"Multiplicador: 1/2x"
        text_2 = font.render(msg_2, True,(0,0,0))
        screen.blit(text_2, (width - 355, 80))
            
    if points >= 15:
        if not maca_verde_born:
            d = 0
            while d < 400:
                x_apple_green = randint(40, 1200)
                y_apple_green = randint(50, 700)
                dx = x_snake - x_apple_green
                dy = y_snake - y_apple_green
                d = sqrt(dx**2 + dy**2)
            maca_verde_born = True   
        apple_green = pygame.draw.circle(screen,(0,200,0), (x_apple_green, y_apple_green), points*1.5, 0)
        if apple_green.colliderect(apple):
            x_y_apple()
        if apple_green.colliderect(snake):
            x_y_apple()
        if snake.colliderect(apple_green):
            if life == 0:
                death()
            elif life > 0:
                life -= 1
                x_y_apple()
        if x_apple_green == x_snake and y_apple_green == y_snake:
            x_y_apple()
        dx = x_snake - x_apple_green
        dy = y_snake - y_apple_green
        rads = atan2(-dy,dx)
        rads %= 2*pi
        vel_apple_green = 5
        x_apple_green += cos(rads) * vel_apple_green 
        y_apple_green -= sin(rads) * vel_apple_green 

    if points >= 30:
        troll_apple = pygame.draw.circle(screen, (70, 41, 90), (x_troll_apple, y_troll_apple), 15, 0)
        if troll_apple.colliderect(apple_green):
            x_y_apple()
        elif troll_apple.colliderect(apple):
            x_y_apple()
        if snake.colliderect(troll_apple):
            key_left, key_right = key_right, key_left
            key_up, key_down = key_down, key_up
            x_y_apple()
    
        if not testando:
            if points > 30 and points % 5 == 0:
                escolha = randint(1,10)
                testando = True
                print(escolha)
            if escolha == 1:
                vida_apple = 1
                if vida_apple == 1:
                    life_apple = pygame.draw.circle(screen, (0,0,255), (x_life_apple, y_life_apple), 15, 0)
                    vida_apple = 0
            else:
                vida_apple = 0

        if points == 35:
            life_drop = True
            vida_apple = 1
            if vida_apple == 1:
                life_apple = pygame.draw.circle(screen, (0,0,255), (x_life_apple, y_life_apple), 15, 0)
            
    
            

            if life_apple.colliderect(apple):
                x_y_apple()
            elif life_apple.colliderect(apple_green):
                x_y_apple()
            elif life_apple.colliderect(troll_apple):
                x_y_apple()
            if snake.colliderect(life_apple):
                life += 1
                x_y_apple()
                x_life_apple = -10
                y_life_apple = -10
                vida_apple = 0

        if points == 50:
            finish()
    #armazenando os valores X e Y da "cobra"
    head_list = []
    head_list.append(x_snake)
    head_list.append(y_snake)

    if len(snake_lista) > first_length:
        del snake_lista[0]
    
    #aramazenado o valor que a "head_list" adiquirir
    snake_lista.append(head_list)
    
    #tela de morte
    if snake_lista.count(head_list) > 1 or x_snake > width or x_snake < 0 or y_snake > height or y_snake < 0: #se tiver duas coodernadas iguais uma da cabeça e outra do corpo a cobra encostou em si mesma
        if life == 0:
            death()
        elif life > 0:
            life -= 1
            x_snake = int(width/2)
            y_snake = int(height/2)

    #funçao que faz a cobra crescer
    increases_snake(snake_lista)

    #escrevendo o contador de pontos
    screen.blit(text, (width - 224,40))

    pygame.display.flip()

