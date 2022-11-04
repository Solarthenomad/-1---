import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen=pygame.display.set_mode(screen_width,screen_height)

pygame.display.set_caption("오락실 게임")

#배경 이미지 불러오기
backgroundimg = pygame.image.load("C:/Users/trixy/OneDrive/바탕 화면/python오락실게임/backgroundimg.png")

running = True
while running:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            running = False #게임이 진행중이 아니다.
            
    screen.fill(())
    
    screen.blit(backgroundimg,(0,0)) #배경그리기 screen에 background 이미지를(0,0) 위치에다가 그려줌(blit)
    #while 안에서 이벤트들이 발생하는 한 계속 그려준다 (running=True일 때)
    
    #screen.fill((0,0,255)) #screen에 색깔을 rgb값으로 주고 있다. (빨초파)
    pygame.display.update() #게임 화면 다시 그리기 pygame의 display 속성을 업로드해준다. 

    
pygame.quit()

