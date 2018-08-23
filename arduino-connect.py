import serial
import time
import pygame
from pygame.locals import *
import sys


ser = serial.Serial('/dev/ttyACM0',9600)
time.sleep(2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((500,300))
    pygame.display.set_caption("Humidity & Temperrature")
    font = pygame.font.Font(None,55)
    while(1):
        screen.fill((0,0,0))
        #Humidity
        ser.write(b'H')
        h = ser.readline()
        h = h[:-1]
        #print('Humidity:' + h)
        text = font.render('Humidity:' + h + ' %',True,(255,255,255))
        screen.blit(text,[50,50])

        time.sleep(1)

        #temperature
        ser.write(b'T')
        t = ser.readline()
        t = t[:-1]
        #print('Temperature:' + t)
        text = font.render('Temperature:' + t+ ' C',True,(255,255,255))
        screen.blit(text,[50,100])


        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                ser.close()
                pygame.quit()
                sys.exit()

if __name__=="__main__":
    main()



