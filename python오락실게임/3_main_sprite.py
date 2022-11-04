import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen=pygame.display.set_mode(screen_width,screen_height)

pygame.display.set_caption("오락실 게임")

#배경 이미지 불러오기
backgroundimg = pygame.image.load("C:/Users/trixy/OneDrive/바탕 화면/python오락실게임/backgroundimg.png")

#스프라이트(캐릭터) 불러오기 
character = pygame.image.load("C:/Users/trixy/OneDrive/바탕 화면/python오락실게임/character.png")
#캐릭터는 항상 움직임 => 움직일수있도록 하려면?
#캐릭터의 크기 설정해주기 
character_size = character.get_rect().size #이미지의 크기를 구할 수 있음 
#이미지 크기의 가로 길이
character_width = character_size[0] #캐릭터의 가로 길이
character_height = character_size[1]
#캐릭터의 세로 길이 
#사이즈를 불러왔으니 이제는 캐릭터의 위치를 설정해주자
#처음 게임 시작할 때 캐릭터의 위치
character_x_pos = screen_width /2
#게임하면서의 캐릭터 가로위치
character_x_pos=screen_width/2 - (character_width/2)

#화면 가로의 절반에 해당되는 곳에 위치함
character_y_pos = screen_height/2
#게임하면서의 캐릭터 세로위치
character_y_pos = screen_height/2 - (character_height/2)
#화면 세로의 절반에 해당되는 곳에 위치함

running = True
while running:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            running = False #게임이 진행중이 아니다.
            
    screen.fill(())
    
    screen.blit(backgroundimg,(0,0)) #배경그리기 screen에 background 이미지를(0,0) 위치에다가 그려줌(blit)
    #while 안에서 이벤트들이 발생하는 한 계속 그려준다 (running=True일 때)
    screen.blit(character, (character_x_pos,character_y_pos))
    
    #screen.fill((0,0,255)) #screen에 색깔을 rgb값으로 주고 있다. (빨초파)
    pygame.display.update() #게임 화면 다시 그리기 pygame의 display 속성을 업로드해준다. 

    
pygame.quit()