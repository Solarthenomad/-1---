import os 
import pygame

pygame.init()
os.init()
def __main__ = "__name__"

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("PANG 오락실 게임")

#FPS
clock = pygame.time.Clock()
#사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트)


current_path = os.path.dirname(__file__) #현재 파일의 위치를 변환해주는 것 

image_path = os.path.join(current_path, "images") #이미지 폴더 위치 반환 
#이렇게 하면 전체 파일의 주소를 다 적어줄 필요는 없음

#배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))


#스테이지 만들기
stage = pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size = stage.get_rect().size
stage_width = stage_size[0]
stage_height = stage_size[1]

#캐릭터 만들기
character = pygame.image.load(os.path.join(image_path , "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
charactr_height = character_size[1]
character_x_pos = (screen_width/2)-(character_width/2)
character_y_pos = (screen_height/2) - (charactr_height/2)-stage_height
character_speed = 30


running = True 
while running : 
    dt = clock.tick(30)
    
    for event in pygame.event.get():
        if event.type = pygame.QUIT:
            running = False
            
            
#5. 화면에 그리기
screen.blit(background,(0,0))
screen.blit(stage,(0, screen_height-stage_height) )    
screen.blit(character, (character_x_pos,character_y_pos))        
 
 
pygame.display.update()
 
pygame.quit()

        