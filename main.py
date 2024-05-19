import pygame
import sys
import random
pygame.font.init()
per=False
sz=(600,450)
sc=pygame.display.set_mode(sz)
clock=pygame.time.Clock()
fps=60
score=0

x=random.randint(20,580)
y=random.randint(20,430)
x_new=x
y_new=y

while True:
    sc.fill(("yellow"))

    f2 = pygame.font.SysFont('serif', 48)
    text2 = f2.render(str(score), False,
                      (0, 180, 0))


    sc.blit(text2, (10, 20))
    pygame.draw.circle(sc,(0,0,0),(x,y),20)
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            sys.exit()


        if i.type==pygame.MOUSEBUTTONDOWN :
            per=True
            x_new,y_new=i.pos[0],i.pos[1]
            score=score+1
    if x>x_new:
         x=x-1
    elif x<x_new:
        x=x+1
    if y<y_new:
        y=y+1
    elif y>y_new:
        y=y-1
    pygame.display.update()
    clock.tick(fps)
