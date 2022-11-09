#텍스트 설정
#초당 프레임수 설정
#프레임수가 높을수록 캐릭터 움직임이 부드러워짐 
#키보드를 누르면 캐릭터가 이동하는 것을 만들어보자 

import pygame
###################################

#기본 초기화는 프레임워크.init() 반드시해야함
pygame.init()

screen_width = 480
screen_height = 640
screen=pygame.display.set_mode(screen_width,screen_height)

#화면 타이틀 이름
pygame.display.set_caption("오락실 게임")

#FPS
#time을 불러오기 
clock = pygame.time.Clock()

#여기까지 무조건 처음에 써줘야 됨
##########################################

#1. 사용자 게임 초기화(qorudghkaus, 게임이미지, 좌표, 속도, 폰트 설정해주기 )

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

enemy_x_pos = screen_width-(enemy_width/2)
enemy_y_pos = screen_height-(enemy_height/2)

#폰트 가져오기 
#폰트 객체 생성(폰트, 크기)
game_font = pygame.font.Font(None,40)

#총 시간 
total_time = 10

#시간 계산
start_ticks = pygame.time.get_ticks()

#2. 이벤트 처리해주기
running = True
while running:
    dt = clock.tick(60) #게임화면의 초당 프레임수
    #위에서 불러운 clock 설정해주기
    #이전에 비해서 느려진게 확인
    #캐릭터가 60만큼 이동해야 함
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
    #3. 게임 캐릭터 위치 정의해주기
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
        
        
    #4. 이미지간 충돌 처리 
    #4-1. 벽에 충돌할 때 
    character_rect = character.get_rect
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    enemy_rect = enemy.get_rect
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    #4-2, 적끼리 충돌 체크 
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running : False
    
    screen.blit(backgroundimg,(0,0)) #5. 화면 그리기  
    #배경그리기 screen에 background 이미지를(0,0) 위치에다가 그려줌(blit)
    #while 안에서 이벤트들이 발생하는 한 계속 그려준다 (running=True일 때)
    screen.blit(character, (character_x_pos,character_y_pos))
    #캐릭터 그리기
    screen.blit(enemy,(enemy_x_pos, enemy_y_pos))#적 그리기 
    
    #타이머 집어 넣기 
    #경과 시간 계산(elapsed_time = 흘러간 시간 )
    #pygame.time.get_ticks()에서ㅓ 처음 시간인 start_ticks를 빼줘서 순수 경과시간을 구해줌
    #1000으로 나누는 시간은 밀리세컨이기 때문에 세컨으로 바꿔줌
    elapsed_time =(pygame.time.get_ticks() - start_ticks)/1000
    
    #이거 다시 한번 들어보기 
    timer = game_font.render((int(total_time-elapsed_time)),True,(255,255,255))
    
    #render은 화면에 보여주는 것이다.
    # 위의 코드를 해석해보면, 
    # timer라는 친구는 game_font의 rendering된 친구인데 
    #출력할 글자, True, 글자색상 순으로 표현
    screen.blit(timer, (10,10))
    #만약 시간이 0이하이면 게임 종료이다. 
    if total_time - elapsed_time<=0:
        print("타임아웃")
        running = False
    
    
    #screen.fill((0,0,255)) #screen에 색깔을 rgb값으로 주고 있다. (빨초파)
    pygame.display.update() #게임 화면 다시 그리기 pygame의 display 속성을 업로드해준다. 

    
pygame.quit()

#잠시 대기 
pygame.time.delay(2000) #2초 정도 대기g하다가 게임을 종료시켜줌(ms)