import pygame

pygame.init()
screen = pygame.display.set_mode((1600, 1000))
pygame.display.set_caption("Keyboard Test")

clock = pygame.time.Clock()
run = True
key_status = ""
key = None

#게임 루프
while run :
      #1) 사용자 입력 처리
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  run = False
            elif event.type == pygame.KEYDOWN:
                  key_status = "Key Down"
                  key = event.key
            elif event.type == pygame.KEYUP:
                  key_status = "Key Up"
                  key = event.key
      #2) 게임 상태 업데이트

      #3) 게임 상태 그리기
      screen.fill(pygame.color.Color(255, 255, 255))

      if key:
            pygame.display.set_caption(
                  pygame.key.name(key) + "우왕" + key_status)
      pygame.display.flip()
      clock.tick(60)
pygame.quit()
