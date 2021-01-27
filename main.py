import pygame
pygame.init()
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('track6.png')   #here use any image from track1 to track 6 ...for fun ....(ō｡ŏ)
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car,(30,60))
car_x =150  #inittalising the initaial co-ordinates of car
car_y =300   #inittalising the initaial co-ordinates of car
drive =True
direction ='Up'
focal_distance = 25   #adding camera for tracking  (This will act as a camera for the car to detect the road)
cam_x_offset = 0
cam_y_offset = 0
clock = pygame.time.Clock()  
while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive =False

    clock.tick(60)
    cam_x =car_x + cam_x_offset +15  # Camera offset is used to move camera to the upper part of the car
    cam_y = car_y + cam_y_offset + 15  #this is used to put a camera on car to track movement // here cam_y_offset is used to move camera to front of the car after taking the second turn
    up_px = window.get_at((cam_x, cam_y - focal_distance))[0]  #this will make car move only in  white colour upward
    down_px = window.get_at((cam_x, cam_y + focal_distance))[0]  #this will make car move only in  white colour downward
    right_px = window.get_at((cam_x + focal_distance, cam_y))[0]  #this will help car to make a right turn
    # print(up_px, right_px, down_px)
    #Change Direction
    if direction =='Up' and up_px != 255 and right_px ==255:
        direction = 'right'
        cam_x_offset =30  # This will make camera turn
        car = pygame.transform.rotate(car, -90)
    elif direction == 'right' and right_px != 255 and down_px ==255:
        direction ='down'
        car_x = car_x + 30
        cam_x_offset =0
        cam_y_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction =='down' and down_px!= 255 and right_px ==255:
        direction= 'right'
        car = pygame.transform.rotate(car, 90)
        car_y =car_y +30
        cam_x_offset = 30
        cam_y_offset = 0
    elif direction =='right' and right_px!= 255 and up_px == 255:
        direction ='Up'
        car = pygame.transform.rotate(car, 90)
        car_x = car_x + 30
        cam_x_offset = 0


    #Driving
    if direction == 'Up' and up_px == 255:  #white colour (Colour of the Road) for going upward
        car_y = car_y - 2
    elif direction == 'right' and right_px ==255: # if there is white colour on right side car will move in that direction
         car_x = car_x + 2
    elif direction == 'down' and down_px ==255:  #if there is white colour on down side car will move in that direction
        car_y = car_y + 2
    window.blit(track,(0, 0))
    window.blit(car,(car_x,car_y))
    pygame.draw.circle(window,(0, 225,255), (cam_x, cam_y), 5,5)
    pygame.display.update()
