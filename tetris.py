import sys, pygame
import array as arr
import time

pygame.init()

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

columns = 8
rows = 15


static = [[bool for i in range(rows)] for j in range(columns)]
for i in range(rows):
    for j in range(columns):
        static[j][i] = False

# Camera Stuff ..
block_pixel_size = 20
width = block_pixel_size * columns
height = block_pixel_size * rows

screen = pygame.display.set_mode([width, height])

for s in static:
    print s

def main():

    posX = 0
    posY = 0

    #Formations
    active = [[False, False, False], [False, True, False], [True, True, True]]

    while 1:
        screen.fill((0,0,0))

        for a in active:
            print a

        #logic
        for j in range(3):
            for i in range(3):
                if active[i][j]:
                    if posY + j + 1 == rows:
                        placeActiveOnStatic(posX, posY, active)
                        posY = 0
                        print "ah"
                    elif static[posX + i][posY + j]:
                        placeActiveOnStatic(posX, posY, active)
                        posY = 0
        print "aa: ", posY

        #draw
        for i in range(rows):
            for j in range(columns):
                if static[j][i]:
                    pygame.draw.rect(screen, BLUE, (j * block_pixel_size, i * block_pixel_size, block_pixel_size, block_pixel_size), 0)

        for j in range(3):
            for i in range(3):
                if active[i][j]:
                    pygame.draw.rect(screen, RED,((j + posX) * block_pixel_size, (i + posY) * block_pixel_size, block_pixel_size, block_pixel_size),0)
        pygame.display.flip()

        time.sleep(0.5)

        posY += 1

        # input
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if posX >= 1:
                        posX -= 1
                if event.key == pygame.K_RIGHT:
                    if posX < columns:
                        posX += 1
                if event.key == pygame.K_UP:
                    active = rotate(active)

        #print posY

def rotate(active):
    new_active = [[False, False, False], [False, False, False], [False, False, False]]

    for i in range(3):
        for j in range(3):
            new_active[j][i] = active[i][j]
    return new_active


def placeActiveOnStatic(posX, posY, active):
    for j in range(3):
        for i in range(3):
            if active[j][i]:
                static[posX + i][posY + j] = True






if __name__ == "__main__":
    main()