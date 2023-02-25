import pygame

pygame.init()
screen = pygame.display.set_mode((1600, 1000))
pygame.display.set_caption("Keyboard Test2")

clock = pygame.time.Clock()
run = True
key_status = ""
key = None

#게임 루프
while run:
      #1) 사용자 입력 처리
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  run = False
      #2) 누르고 있는 키 확인하기
      keys = pygame.key.get_pressed()
      if keys[pygame.K_LEFT]:
            print("LEFT")
      elif keys[pygame.K_RIGHT]:
            print("RIGHT")
      elif keys[pygame.K_UP]:
            print("abstrain : 기권하다")
      elif keys[pygame.K_DOWN]:
            print("DOWN")
      elif keys[pygame.K_SPACE]:
            print("SPACE")
      #2) 게임 상태 업데이트

      #3) 게임 상태 그리기
      screen.fill(pygame.color.Color(255, 255, 255))

      if key:
            pygame.display.set_caption(
                  pygame.key.name(key) + " " + key_status)

      pygame.display.flip()
      clock.tick(60)
pygame.quit()
