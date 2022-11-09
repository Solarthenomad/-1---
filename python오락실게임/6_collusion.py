#초당 프레임수 설정
#프레임수가 높을수록 캐릭터 움직임이 부드러워짐 
#키보드를 누르면 캐릭터가 이동하는 것을 만들어보자 

import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen=pygame.display.set_mode(screen_width,screen_height)

pygame.display.set_caption("오락실 게임")

#FPS
clock = pygame.time.Clock()

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

#이동할 좌표
to_x = 0
to_y = 0

#이동 속도 
character_speed = 0.6


#적 enemy 캐릭터(빌런 우리가 깨야되는 대상)
enemy = pygame.image.load("") #적의 이미지 가져오기 
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
#적의 위치 
enemy_x_pos = screen_width-(enemy)


running = True
while running:
    dt = clock.tick(30) #게임화면의 초당 프레임수
    #이전에 비해서 느려진게 확인
    #캐릭터가 100만큼 이동해야 함
    #10 fps : 1초 동안에 10번 동작
    #20 fps : 1초 동안에 20번 동작 
    print("fps : "+str(clock.get_fps()))
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            running = False #게임이 진행중이 아니다.
            
        if event.type == pygame.KEYDOWN: #pygame의 keyboard를 누르는 이벤트가 발생하면
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                #pass
                #to_x -=5 #to_x = to_x-5
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT :
                #pass
                #to_x +=5 #to_x = to_x+5
                to_x +=character_speed
            elif event.key == pygame.K_UP:
                #pass
                #to_y -=5
                #to_y = to_y-5
                to_y -=character_speed
            elif event.key == pygame.K_DOWN:
                #pass
                #to_y+=5
                to_y+=character_speed
            
        if event.type == pygame.KEYUP: #방향키를 떼면 캐릭터는 먼춘다.
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x=0
            if event.key ==pygame.K_UP or event.key == pygame.K_DOWN :
                to_y =0
                
    #character_x_pos +=to_x
    #character_y_pos += to_y
    #위치 선택해주기 
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    
    #여기까지 문제가 다른 건 다 잘되는데 캐릭터 위치가 화면을 벗어나게 되면 그대로 벗어나게 됨. 아무리 방향키를 계속 눌러도 캐릭터는 화면 내에만 있어야 한다. 
    
    if character_x_pos <0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
        
    if character_y_pos<0:
        character_y_pos = 0
    elif character_y_pos > screen_height-character_height:
        character_y_pos = screen_height-character_height
        
        
    #충돌 처리 
    character_rect = character.get_rect
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    enemy_rect = enemy.get_rect
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    #충돌 체크 
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running : False
    
    screen.blit(backgroundimg,(0,0)) #배경그리기 screen에 background 이미지를(0,0) 위치에다가 그려줌(blit)
    #while 안에서 이벤트들이 발생하는 한 계속 그려준다 (running=True일 때)
    screen.blit(character, (character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos, enemy_y_pos))
    
    #screen.fill((0,0,255)) #screen에 색깔을 rgb값으로 주고 있다. (빨초파)
    pygame.display.update() #게임 화면 다시 그리기 pygame의 display 속성을 업로드해준다. 

    
pygame.quit()