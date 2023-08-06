import pygame
from sys import exit
from random import randint,choice
class Enemy(pygame.sprite.Sprite):
    def __init__(self,nam):
        super().__init__()
        
        self.name = nam
        
        if self.name  == "Meta":
            self.image = pygame.image.load("graphics/meta.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,(70,70))
            self.image = pygame.transform.flip(self.image,True,False)
            self.rect = self.image.get_rect(topleft = (randint(900,1100),200))
        
        elif self.name == "Koopa":
            self.image = pygame.image.load("graphics/koopa.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,(50,50))
            self.image = pygame.transform.flip(self.image,True,False)
            self.rect = self.image.get_rect(topleft = (randint(900,1100),300))
        elif self.name == "Pirannah":
            self.image = pygame.image.load("graphics/pirannah.png").convert_alpha()
            self.image  = pygame.transform.scale(self.image,(50,50))
            self.rect = self.image.get_rect(topleft  = (randint(900,1100),300))
            
        else:
            self.image = pygame.image.load("graphics/goomba.png")
            self.image = pygame.transform.scale(self.image,(50,50))
            self.rect = self.image.get_rect(topleft = (randint(900,1100),300))
        
    def update(self):
        self.rect.x -= 5
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
        

    
class Mario(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/Mario.png').convert_alpha() 
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect(topleft = (0,300))
        self.going_left = False
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound('audio/Mario_Jump.mp3')
        
    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.top >= 300:
            self.gravity = -20
            self.jump_sound.play()
        if keys[pygame.K_LEFT] and self.going_left == False:
            self.image = pygame.transform.flip(self.image,True,False)
            print("hi")
            self.rect.x -= 5
            self.going_left = True
            
        elif keys[pygame.K_LEFT]:
            print("kow")
            self.rect.x -= 5

      
        if keys[pygame.K_RIGHT] and self.going_left == True:
            self.image = pygame.transform.flip(self.image,True,False)
            self.rect.x += 5
            self.going_left = False
            
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 5
        

    
    def apply_gravity(self):
        self.gravity += 1 
        self.rect.y += self.gravity
        if(self.rect.top>=300):
            self.rect.top = 300
    def update(self):
        self.jump()
        self.apply_gravity()

'''

class Goomba:
    
    def __init__(self):
        self.surface = pygame.image.load('graphics/goomba.png').convert_alpha()
        
        DFLT_IMG_SZ = (50,50)
        self.surface = pygame.transform.scale(self.surface,DFLT_IMG_SZ)
        self.rect = self.surface.get_rect(topleft = (600,300))
        
    def move(self):
        self.rect.left -=1

    def reset(self):
        self.rect.x = 800
    def spawn(self):
        
        screen.blit(self.surface,self.rect)
    def hit(self, rect):
        return  rect.colliderect(self.rect)
'''
    
'''



    
def movement(list):
    if list:
        for enemy in list:
            if enemy.name == "Pirannah":
                enemy.rect.x -= 2
            else:
                enemy.rect.x -= 5
            screen.blit(enemy.surface,enemy.rect)
        list = [goomba for goomba in list if goomba.rect.x> -100]    
        return list
    else:
        return []
''' 


'''
def collisions(player, obstacles):
    if obstacles:
        for rect in obstacles:
            if player.colliderect(rect):
    
                return False
    return True
'''
 
def collision_sprite():
    if pygame.sprite.spritecollide(mario.sprite,enemies,False):
        enemies.empty()
        return False
    else:
        return True


def display_score():
    time = int (pygame.time.get_ticks()//1000) - start_time
    score_surf = test_font.render(f'{time}', False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)



pygame.init()
screen = pygame.display.set_mode((800,400)) #(width, height)
pygame.display.set_caption("Baby Sean")
clock  = pygame.time.Clock()
start_time = 0 
'''

test_surface = pygame.Surface((100,200)) # rectangle surface
test_surface.fill ('Red')

'''

test_surface = pygame.image.load("graphics/ground.png").convert_alpha() # image surface
DFLT_IMG_SZ = (800, 400)
test_surface = pygame.transform.scale(test_surface, DFLT_IMG_SZ)
test_font = pygame.font.Font(None,50)
text_surface = test_font.render("Sean", False,"Orange") #(text,AA,Color)
text_rect = text_surface.get_rect(center = (0,50 )) 
bg_music = pygame.mixer.Sound('audio/smash.mp3')
bg_music.set_volume(0.5)
bg_music.play(loops = -1)
'''
goomba_surface = pygame.image.load('graphics/goomba.png').convert_alpha()
DFLT_IMG_SZ = (50,50)
goomba_x = 600
goomba_surface = pygame.transform.scale(goomba_surface,DFLT_IMG_SZ)
goomba_rect = goomba_surface.get_rect(topleft = (600,300))



'''

# surface and rectangles for images

game_active = False
end_time = 0




going_left = False
going_right = True
mario_loading = pygame.image.load("graphics/Mario.png").convert_alpha()
mario_loading  = pygame.transform.scale(mario_loading,(100,200))
mario_loading_rect = mario_loading.get_rect(center = (400,200))
mario = pygame.sprite.GroupSingle()
mario.add(Mario())
enemies = pygame.sprite.Group()



#timer

obstsacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstsacle_timer,900)
while True:
    #draw all our elements and update everything
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit() 
            exit()
        
        if event.type == pygame.KEYDOWN:
            '''
            
        
            if event.key == pygame.K_RIGHT:
                mario_rect.left += 50
                if(going_right == False):
                    mario_surface = pygame.transform.flip(mario_surface,True,False)
                   
                    going_right = True
                    going_left = False
            if event.key == pygame.K_LEFT:

                if(going_left == False):
                    mario_surface = pygame.transform.flip(mario_surface,True,False)
                    mario_rect.left -= 50
                    going_left = True
                    going_right = False
                else:
                    mario_rect.left -= 50
            '''

          
            
        
        
        if game_active == False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    
                    
                    start_time = int(pygame.time.get_ticks()//1000)
        
        
        if event.type == obstsacle_timer and game_active:
            enemies.add(Enemy(choice(["Meta","goomba", "Pirannah","Koopa"])))

            
            '''
            random = randint(0,3)
            if(random == 0):
                enemy_list.append(Enemy("Goomba",goomba.surface))
                #enemy_list.append(goomba.surface.get_rect(topleft = (randint(900,1100),300)))
            elif(random == 1):
                enemy_list.append(Enemy("Koopa",koopa_surface))
                #enemy_list.append(koopa_surface.get_rect(topleft = (randint(900,1000),300)))
            elif(random == 2):
                enemy_list.append(Enemy("Pirannah",pirannah_surface))
            else:
                enemy_list.append(Enemy("Meta",meta_surface))
                #enemy_list.append(meta_surface.get_rect(topleft = (randint(900,1100),200)))
            '''



    if game_active: 
      
       
        
        screen.blit(test_surface,(0,0))
        pygame.draw.rect(screen,"black",text_rect)
        screen.blit(text_surface,text_rect)
        display_score()
       
        
      

        
        end_time  = int (pygame.time.get_ticks()//1000) - start_time
        mario.draw(screen)
        mario.update()
        enemies.draw(screen)
        enemies.update()
        game_active = collision_sprite()

    else:
    
        
        mario.sprite.rect.x = 0
        screen.fill("Black")
        screen.blit(mario_loading,mario_loading_rect)
        ntext_surface = test_font.render( "Your Score: " + str(end_time), False,"Orange") #(text,AA,Color)
        
     
        ntext_rect = ntext_surface.get_rect(center = (400,50 )) 
        pygame.draw.rect(screen,"white",ntext_rect)
        screen.blit(ntext_surface,ntext_rect)
        

    '''
      
        if goomba_2.rect.x< -50:
            goomba_2.reset()   
         
        
        if goomba.rect.x < -50:
            goomba.reset()
        if mario_rect.x > 850:
            mario_rect.x= -50
        screen.blit(goomba.surface,goomba.rect)
        if goomba.rect.x < 100:
            bool = True

        if bool:
            goomba_2.spawn()
    '''

 

    '''
        mouse_pos = pygame.mouse.get_pos()
        if mario_rect.collidepoint(mouse_pos):
            print("collision")
        
        
    '''
       

        
    

        




    pygame.display.update() #update everytime loop runs
    clock.tick(60) # this code tells it to not run faster than 60 fps
     