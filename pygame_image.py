import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")#練習２
    kk_img = pg.transform.flip(kk_img, True, False)#練習２
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300,200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        kouka_speed = [-1,0]
        if key_lst[pg.K_UP]:
           kouka_speed[1] += -1
        if key_lst[pg.K_DOWN]:
            kouka_speed[1] += 1
        if key_lst[pg.K_LEFT]:
            kouka_speed[0]  += -1
        if key_lst[pg.K_RIGHT]:
            kouka_speed[0] += 2
        kk_rct.move_ip(kouka_speed)
        x = -(tmr % 3200)
        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img2,[x+1600,0])
        screen.blit(bg_img,[x+3200,0])
        screen.blit(bg_img2,[x+4800,0])
        #screen.blit(kk_img, [300,200])#練習４
        screen.blit(kk_img, kk_rct)

        pg.display.update()
        tmr += 1          
        clock.tick(400)
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()