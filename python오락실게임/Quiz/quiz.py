#Quiz) 하늘에서 떨어지는 똥 피하기 게임을 만들시오

#게임 조건
#1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
#2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정함 
#3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
#4. 캐릭터가 똥과 충돌하면 게임 종료
#FPS는 30으로 고정해주기

#게임 이미지
#1. 배경 : 640*480
#2. 캐릭터 : 70*70 
#3. 똥 : 70*70

import pygame

pygame.init()

#화면 타이틀 만들어주기 

pygame.display.set_caption("하늘에서 떨어지는 똥피하기 게임")

#배경화면 불러오기
background = pygame.image.load("")

#캐릭터 불러오기
character =pygame.image.load("")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]


#enemy 불러오기 

#스크린 크기 설정 
screen_width = 500
screen_height = 500
pygame.display.set_mode(screen_width, screen_height)


#FPS 설정해주기 
cloock= pygame.time.Clock()


#캐릭터 크기, 위치, 속도 설정해주기 


character_width = 70
character_height = 70
character_y_pos = 0
character_x_pos = 0
character_speed = 70


####################이벤트 처리해주기 
running = True
while running : 
    for 


