import pygame

pygame.init() #pygame을 초기화해준다. init():초기화함수.반드시 해줘야 함 

#화면 크기 설정해주기
screen_width = 480 #screen_width라는 변수 안에 480넣기
screen_height = 640 #scree_height라는 변수 안에 640 넣기 
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("오락실 게임") #오락실 게임은 내가 정한 이 플젝의 타이틀

#이벤트 루프  #게임 진행 중일 때의 상황과 게임이 진행중이지 않을 때의 상황을 넣어두기 
#게임이 종료되지 않도록 대기하는 것을 이벤트 루프라고 함 
running = True #게임이 진행중인 것을 디폴트 값으로 두기 
while running: #running이 계속해서 True일 때는 ㅇㅋ해주기 
    pass
    for event in pygame.event.get(): #관용문으로 외우기 #어떤 이벤트가 발생했나 찾아보자 pygame의 event를 get() 해준 것중 event
        if event.type == pygame.QUIT: #이벤트 타입 = 창이 닫히는 것
            running = False #게임이 진행중이 아님
#pygame 종료 
pygame.quit()