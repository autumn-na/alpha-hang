
import login
import random
import pygame
from alpha_hang import *


# Colors

BLACK = (70, 70, 70)
WHITE = (200, 200, 200)
BLUE = (50, 50, 255)
RED = (255, 50, 50)
GREEN = (50, 250, 50)
YELLOW = (255,228,0)
Real_WHITE=(255,255,255)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
global stage
stage = 0



class Start_Button(pygame.sprite.Sprite):

    def __init__(self, color, x, y, width, height):
        super().__init__()

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
        start_img0 = pygame.transform.scale(start_img,(width,height))
        self.image.blit(start_img0, [0, 0])
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def update(self):
        pass


class Level_Button(pygame.sprite.Sprite):

    def __init__(self, color, x, y, width, height):
        super().__init__()

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def update(self):
        pass

class Input_Button(pygame.sprite.Sprite):

    def __init__(self, color, x, y, width, height):
        super().__init__()

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def update(self):
        pass

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()


        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)


        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


def makeWall(x,y,wid,hei):
    wall = Wall(x, y, wid, hei)
    Two_sprite_List.add(wall)

class GuessBox(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()


        self.image = pygame.Surface([width, height])
        self.image.fill(Real_WHITE)


        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

def makeBox(x,y,wid,hei):
    global list
    Box = GuessBox(x,y,wid,hei)
    Box_list.add(Box)
    list.append(Box)
    Two_sprite_List.add(Box)

def guess():
    global GuessWord
    global GuessList
    global button_text
    global count
    global list
    Guess_list = set(GuessList)
    str = ""
    cnt = 0

    for i in GuessWord:
        if i in Guess_list:
            str += i
        else:
            str += ' '
    count = len(GuessWord)
    for st in str:
        if st != ' ':
           cnt += 1
        else:
            pass

    count -= cnt


    for number, Box in enumerate(list):
        number = number % len(GuessWord)
        text = guess_font.render(str[number], True, (0, 0, 0))
        Box.image.fill(Real_WHITE)
        Box.image.blit(text, [10, -5])



pygame.init()
pic = pygame.image.load("Hangman.jpg")
start_img = pygame.image.load("start.jpg")
game_img = pygame.image.load("game.gif")
end_img = pygame.image.load("end.jpg")

font = pygame.font.SysFont("notosanscjkkr",60)
guess_font = pygame.font.SysFont("notosanscjkkr",40)
name_font = pygame.font.SysFont("notosanscjkkr",20)


screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the title of the window
pygame.display.set_caption('Test')

# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()
button_list = pygame.sprite.Group()
Box_list = pygame.sprite.Group()
Two_sprite_List = pygame.sprite.Group()
Three_sprite_list = pygame.sprite.Group()
#------------------------------------------------------------------------
#map1

start_button = Start_Button(RED, 700, 450, 100, 100)
button_list.add(start_button)
all_sprite_list.add(start_button)

level1_button = Level_Button(BLACK, 130,400,80,80)
button_list.add(level1_button)
all_sprite_list.add(level1_button)

level2_button = Level_Button(BLACK, 330,400,80,80)
button_list.add(level2_button)
all_sprite_list.add(level2_button)

level3_button = Level_Button(BLACK, 530,400,80,80)
button_list.add(level3_button)
all_sprite_list.add(level3_button)

#------------------------------------------------------------------------
#map2

input_button = Input_Button(WHITE, 400, 350, 100, 100)
button_list.add(input_button)
Two_sprite_List.add(input_button)

#---------------------------------------------------------------
#map3

back_button = Level_Button(WHITE, 300,250,80,80)
button_list.add(back_button)
Three_sprite_list.add(back_button)

clock = pygame.time.Clock()

global done
global button_text
global GuessList
global bool
global count
global name
global list
global level


name = font.render("Select Level! ", True, (255, 255, 255))
list = []
done = False
button_text = ""
GuessList = ""
bool = True
level = 1



one_text = name_font.render("lvl1", True, (255, 255, 255))
two_text = name_font.render("lvl2", True, (255, 255, 255))
three_text = name_font.render("lvl3", True, (255, 255, 255))
def map1():
    global done
    global stage
    global name
    global level
    st_font = pygame.font.SysFont("notosanscjkkr", 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            if level1_button.rect.collidepoint(x, y):
                level1_button.image.fill(GREEN)
                level2_button.image.fill(BLACK)
                level3_button.image.fill(BLACK)
                level = 1

                name = st_font.render("Challenge Level 1! ", True, (255, 70, 70))

            elif level2_button.rect.collidepoint(x, y):
                level1_button.image.fill(BLACK)
                level2_button.image.fill(GREEN)
                level3_button.image.fill(BLACK)
                level = 2

                name = st_font.render("Challenge Level 2! ", True, (255, 70, 70))

            elif level3_button.rect.collidepoint(x, y):
                level1_button.image.fill(BLACK)
                level2_button.image.fill(BLACK)
                level3_button.image.fill(GREEN)
                level = 3
                name = st_font.render("Challenge Level 3! ", True, (255, 70, 70))

            elif start_button.rect.collidepoint(x, y):
                print('start')
                stage += 1

    screen.fill(BLACK)
    screen.blit(pygame.transform.scale(pic, (1000, 600)), (0, 0))
    level1_button.image.blit(one_text, [25, 25])
    level2_button.image.blit(two_text, [25, 25])
    level3_button.image.blit(three_text, [25, 25])
    screen.blit(name, (10, 60))
    all_sprite_list.draw(screen)

lst = ["perpetrate", "perpetrate", "perpetrate"]
GuessWord = lst[random.randint(0,2)]
count = len(GuessWord)
jujak_list = ['_']*len(GuessWord)

alpha = AlphaHang(len(GuessWord))
curWord = '_' * len(GuessWord)
failWord = []

def map2():
    global done
    global stage
    global button_text
    global GuessWord
    global GuessList
    global bool
    global count
    global start
    global list
    global jujak_list
    global curWord
    global failWord

    if bool:
        for i in range(len(GuessWord)):
            makeWall(200 + (60*i),520,50,10)
            makeBox(200 + (60*i),465,50,50)

            makeWall(200 + (60*i),220,50,10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            buttons = [pygame.key.name(k) for k, v in enumerate(pressed) if v] #['s']'

            if buttons:
                if buttons[0] == "return":
                    GuessList += button_text
                    guess()
                    print(count)
                    button_text = ''

                    alpha.readGene('../genes/gene_master_')
                    alpha.perceive(curWord, failWord)
                    alpha.evaluate()
                    guessed_char = alpha.guess()

                    for i in range(len(GuessWord)):
                        if GuessWord[i] == guessed_char:
                            curWord = curWord[:i] + guessed_char + curWord[i+1:]
                    if guessed_char not in GuessWord:
                        failWord.append(guessed_char)

                    for i in range(len(curWord)):
                        if curWord[i] != '_':
                            jujak_list[i] = '*'
                    #if random.randint(0,100)>50-10*level:
                    #    jujak_list[random.randint(0,len(GuessWord))] = '*'

                    print(jujak_list)


                button_text = buttons[0]
                if len(button_text) > 1:
                    button_text = ''

    bool = False

    text = font.render(button_text, True, (0, 0, 0))  # 텍스트가 표시된 Surface 를 만듬
    screen.blit(pygame.transform.scale(game_img, (1000, 600)), (0, 0))
    Two_sprite_List.update()
    Two_sprite_List.draw(screen)
    input_button.image.fill(WHITE)
    input_button.image.blit(text,[30,0])

    score = round(100/len(GuessWord)*(len(GuessWord)-count),2)
    alpha_score = round(100/len(GuessWord)*(len(GuessWord)-jujak_list.count("_")),2)
    name = name_font.render("Kim / {}".format(score), True, (28, 0, 0))
    screen.blit(name, (800, 300))
    time = name_font.render("AlphaHang / {}".format(alpha_score), True, (28, 0, 0))
    screen.blit(time, (800, 20))


    for n,i in enumerate(jujak_list):
        jujak_1 = guess_font.render(str(i), True, (0, 0, 0))
        screen.blit(jujak_1, (210+60*n, 160))



    if GuessList:
        used = name_font.render("used Char : {}".format(set(GuessList)), True, (28, 0, 0))
        screen.blit(used, (550, 370))

    if count == 0:
        stage += 1

    if jujak_list.count("*") == len(GuessWord):
        stage += 1

def map3():
    global done
    global stage
    global count

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            if back_button.rect.collidepoint(x, y):
                stage = 0
                done = True

    screen.blit(pygame.transform.scale(end_img, (1000, 600)), (0, 0))
    score = 100/len(GuessWord)*(len(GuessWord)-count)
    alpha_score = round(100 / len(GuessWord) * (len(GuessWord) - jujak_list.count("_")), 2)
    score_name = name_font.render("Kim / {}".format(score), True, (255, 255, 255))
    screen.blit(score_name, (450, 250))
    score_alpha = name_font.render("AlphaHang / {}".format(alpha_score), True, (255, 255, 255))
    screen.blit(score_alpha, (450, 350))

    back = name_font.render("re?", True, (0, 0, 0))
    back_button.image.blit(back, [30,20])


    Three_sprite_list.draw(screen)



while not done:

    if stage == 0:
        map1()
    elif stage == 1:
        map2()
    elif stage == 2:
        map3()


    pygame.display.flip()
    clock.tick(100)


pygame.quit()