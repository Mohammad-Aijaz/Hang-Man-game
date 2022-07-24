import pygame
import random

pygame.init()
WIDTH,HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman GAME")

# this is for example creating a variable
xy = 2

#image loop
images = []
for i in range(7):
    image = pygame.image.load("Hangman" + str(i) + ".png")
    images.append(image)



#hang_man words
words = ["HELLO", "CAT", "TABLE", "CHAIR", "BOAT", "AIJAZZZ", "SONA", "SHIREEN", "NOMAAN", "NAWAZ"]
word = random.choice(words)
guessed = []



#button making
GAP = 15
RAIDUS = 20
START_GAP = 20
letters = []
A = 65                                              # the value of A is 65 by default in programing language, so B=66, C=67......
start_x = round(WIDTH - (START_GAP) - ((RAIDUS * 2 + GAP) * 13))
start_y = 400
for i in range(26):
    x = start_x +  ((RAIDUS * 2 + GAP) *(i % 13))  # % is used to get the remainder of devision
    y = start_y + (i // 13 * (RAIDUS * 2 + GAP))
    letters.append([x, y, chr(A + i), True])


    
#RGB colours
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)



#character image
Hangman_image = 0



#font
LETTER_FONT = pygame.font.SysFont("comicsanc", 30, False, True)
WORD_FONT = pygame.font.SysFont("comicsanc", 50) 
RESULT_FONT = pygame.font.SysFont("comicsanc", 70, True, True)
TITLE_FONT = pygame.font.SysFont("comicsanc", 70,)



#win/loos result
def result_dicleration(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = RESULT_FONT.render(message, 1, BLACK)
    win.blit(text,(round(WIDTH/2 - (text.get_width()/2)), round(HEIGHT/2)))
    pygame.display.update()
    pygame.time.delay(3000)



#drawing on screen
def draw():
    
    win.fill(WHITE)
    win.blit(images[Hangman_image],(150, 100))
    text = TITLE_FONT.render("HANGMAN" , 1, BLACK)
    win.blit(text, (round(WIDTH/2 - (text.get_width()/2)), 20))

    #word making
    displayed_word = ""

    for alphabet in word:
        if alphabet in guessed:
            displayed_word += alphabet + " "

        else:
            displayed_word += "_ "
        word_text = WORD_FONT.render(displayed_word, 1, BLACK)
        win.blit(word_text, (400, 200))


    #letters in circle       
    for letter in letters:
        x, y, ltr, visible = letter
        if visible :
            pygame.draw.circle(win, BLACK, (x, y), RAIDUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (round(x - text.get_width()/2), round(y - text.get_height()/2)))
    pygame.display.update()





#game loop
FPS = 60
clock = pygame.time.Clock()
run = True
restarting = 0

while run:
    clock.tick(FPS)
    draw()
    
    while restarting < 1 :     
        won = True
        for alphabet in word:
            if alphabet not in guessed:           
                won = False

        if won:
            result_dicleration("you won")
            word = random.choice(words)
            guessed = []
            Hangman_image = 0
            x = start_x +  ((RAIDUS * 2 + GAP) )
            y = start_y
            pygame.draw.circle(win, BLACK, (x, y), RAIDUS, 3)
            letter[3] = True
            #break

        if Hangman_image == 6:
            result_dicleration("you lose")
            restarting += 1
            run = False
           # question =input("yes/ no: ")
            break
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    if m_y < letter[1]+ RAIDUS and m_y > letter[1] - RAIDUS:
                        if m_x < letter[0] + RAIDUS and m_x > letter[0] - RAIDUS:
                            guessed.append(ltr)
                            if ltr not in word:
                                if Hangman_image < 7:
                                    Hangman_image += 1
                            letter[3] = False

        
pygame.quit()
