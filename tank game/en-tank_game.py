import pygame
import math

pygame.init()



def red_bullet_blitRotate(surf, image, pos, originPos, angle):
    # offset from pivot to center
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = ((pos[0] - rotated_offset.x), (pos[1] - rotated_offset.y))

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle+90)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)


def blue_bullet_blitRotate(surf, image, pos, originPos, angle):
    # offset from pivot to center
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle+90)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)


def redblitRotate(surf, image, pos, originPos, angle):
    # offset from pivot to center
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)

def blueblitRotate(surf, image, pos, originPos, angle):
    # offset from pivot to center
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)

# load:
# tanks:
# red_tank:
red_tank = pygame.image.load("textures/tanks/tank-red-removebg-preview.png")
red_tank = pygame.transform.scale(red_tank, (47, 84))
red_tank = pygame.transform.rotate(red_tank, 270)
# blue_tank:
blue_tank = pygame.image.load("textures/tanks/tank-blue-removebg-preview.png")
blue_tank = pygame.transform.scale(blue_tank, (47, 84))
blue_tank = pygame.transform.rotate(blue_tank, 270)
# boom:
red_fire_tank = pygame.image.load("textures/tanks/boom/fire_tank.jpg")
red_bullet = pygame.image.load("textures/tanks/boom/bullet-removebg-preview.png")
red_bullet = pygame.transform.scale(red_bullet, (15, 28))
blue_fire_tank = pygame.image.load("textures/tanks/boom/fire_tank.jpg")
blue_bullet = pygame.image.load("textures/tanks/boom/bullet-removebg-preview.png")
blue_bullet = pygame.transform.scale(red_bullet, (15, 28))
# GUI:
play_GUI = pygame.image.load("textures/GUI/pixilart-drawing.png")
bg_GUI = pygame.image.load("textures/GUI/GUI bg.jpg")
play_GUI = pygame.transform.scale(play_GUI, (150, 150))
bg_GUI = pygame.transform.scale(bg_GUI, (1280, 720))
play_GUI_rect = play_GUI.get_rect()
play_GUI_rect.x = 950
play_GUI_rect.y = 500

# map:
map = pygame.image.load("textures/map/new_map.jpg")
map = pygame.transform.scale(map, (1280, 720))

# players:
red_w, red_h = red_tank.get_size()
blue_w, blue_h = blue_tank.get_size()
# bullet:
red_bw, red_bh = red_bullet.get_size()
blue_bw, blue_bh = red_bullet.get_size()

# blue:
blue_win = 0
blue_next_step = True
blue_rect = blue_tank.get_rect()
blue_bullet_BOOM , blueBOOML = False, 0
blue_x, blue_y, blue_d = 450, 530, 0
blue_sp_x, blue_sp_y, blue_sp_d = 450, 530, 0

# red:
red_win = 0
red_next_step = True
red_rect = red_tank.get_rect()
red_bullet_BOOM, redBOOML = False, 0
red_x, red_y, red_d = 1470, 530, 0
red_sp_x, red_sp_y, red_sp_d = 1470, 530, 0

# bullet:
red_bx, red_by, red_bd = red_x, red_y, red_d
blue_bx, blue_by, blue_bd = blue_x, blue_y, blue_d

# mouse:
mouse_pos = pygame.mouse.get_pos()
mouse_x = mouse_pos[0]
mouse_y = mouse_pos[1]


red_brect = red_bullet.get_rect()
blue_brect = blue_bullet.get_rect()

# text:
debug_text = False
debug_text_timer = 0

running = False
menu = True
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 20)
text_red = font.render(f'red_d: {int(red_d)} red_y: {int(red_y)} red_x: {int(red_x)}', True, (0, 0, 0), )
text_blue = font.render(f'blue_d: {int(blue_d)} blue_y: {int(blue_y)} blue_x: {int(blue_x)}', True, (0, 0, 0), )
text_mouse = font.render(f"x: {int(mouse_x)} y: {int(mouse_y)}", True, (0, 0, 0))


def def_red_next_step(rect):
    not_go = [[rect.x, 185], [rect.x, 885], [330, rect.y], [1630, rect.y]]
    for x in range(len(not_go)):
        if rect.x == not_go[0][0] and rect.y == not_go[0][1]:
            print("bad")
            red_next_step = False
        else:
            print("good")


red_d = 180
blue_d = 0

while menu:

    pygame.display.set_caption('tank game')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False

    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    mouse_clicked = pygame.mouse.get_pressed()

    print(mouse_x, mouse_y)

    if (play_GUI_rect.collidepoint(mouse_x, mouse_y)):
        print("1")
        if mouse_clicked[0]:
            print("2")
            menu = False
            running = True


    screen.blit(bg_GUI, (320, 180))
    screen.blit(play_GUI, (950, 500))

    pygame.display.flip()

while running:

    text_red = font.render(f'red_d: {int(red_d)} red_y: {int(red_y)} red_x: {int(red_x)}', True, (0, 0, 0))
    text_blue = font.render(f'blue_d: {int(blue_d)} blue_y: {int(blue_y)} blue_x: {int(blue_x)}', True, (0, 0, 0))
    text_mouse = font.render(f"x: {int(mouse_x)} y: {int(mouse_y)}", True, (0, 0, 0))

    pygame.display.set_caption('tank game')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    red_rad = math.radians(red_d)
    blue_rad = math.radians(blue_d)

    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]

    if keys[pygame.K_l]:
        red_d += 1
    elif keys[pygame.K_j]:
        red_d -= 1
    elif keys[pygame.K_i]:
        if red_d >= 0 and red_d < 90:
            red_y -= math.sin(red_rad)
            red_x += math.cos(red_rad)
        elif red_d >= 90 and red_d < 180:
            red_y -= math.sin(red_rad)
            red_x += math.cos(-red_rad)
        elif red_d >= 180 and red_d < 270:
            red_y += math.sin(-red_rad)
            red_x += math.cos(-red_rad)
        elif red_d >= 270 and red_d < 360:
            red_y += math.sin(-red_rad)
            red_x += math.cos(red_rad)
    elif keys[pygame.K_k]:
        if red_d >= 0 and red_d < 90:
            red_y += math.sin(red_rad)
            red_x -= math.cos(red_rad)
        elif red_d >= 90 and red_d < 180:
            red_y += math.sin(red_rad)
            red_x -= math.cos(-red_rad)
        elif red_d >= 180 and red_d < 270:
            red_y -= math.sin(-red_rad)
            red_x -= math.cos(-red_rad)
        elif red_d >= 270 and red_d < 360:
            red_y -= math.sin(-red_rad)
            red_x -= math.cos(red_rad)

    if keys[pygame.K_f]:
        blue_bullet_BOOM = True
    if keys[pygame.K_d]:
        blue_d += 1
    elif keys[pygame.K_a]:
        blue_d -= 1
    elif keys[pygame.K_w]:
        if blue_d >= 0 and blue_d < 90:
            blue_y -= math.sin(blue_rad)
            blue_x += math.cos(blue_rad)
        elif blue_d >= 90 and blue_d < 180:
            blue_y -= math.sin(blue_rad)
            blue_x += math.cos(-blue_rad)
        elif blue_d >= 180 and blue_d < 270:
            blue_y += math.sin(-blue_rad)
            blue_x += math.cos(-blue_rad)
        elif blue_d >= 270 and blue_d < 360:
            blue_y += math.sin(-blue_rad)
            blue_x += math.cos(blue_rad)
    elif keys[pygame.K_s]:
        if blue_d >= 0 and blue_d < 90:
            blue_y += math.sin(blue_rad)
            blue_x -= math.cos(blue_rad)
        elif blue_d >= 90 and blue_d < 180:
            blue_y += math.sin(blue_rad)
            blue_x -= math.cos(-blue_rad)
        elif blue_d >= 180 and blue_d < 270:
            blue_y -= math.sin(-blue_rad)
            blue_x -= math.cos(-blue_rad)
        elif blue_d >= 270 and blue_d < 360:
            blue_y -= math.sin(-blue_rad)
            blue_x -= math.cos(blue_rad)

    screen.fill((255, 255, 255))

    red_pos = (red_x, red_y)
    red_rect.x = red_x
    red_rect.y = red_y
    red_brect.x = red_bx
    red_brect.y = red_by

    blue_pos = (blue_x, blue_y)
    blue_rect.x = blue_x
    blue_rect.y = blue_y
    blue_brect.x = blue_bx
    blue_brect.y = blue_by

    # bullet:
    if not red_bullet_BOOM:
        red_bx, red_by, red_bd = red_x, red_y, red_d
        red_bpos = (red_bx, red_by)

    if not blue_bullet_BOOM:
        blue_bx, blue_by, blue_bd = blue_x, blue_y, blue_d
        blue_bpos = (blue_bx, blue_by)

    screen.blit(map, (320, 180))
    redblitRotate(screen, red_tank, red_pos, (red_w / 2, red_h / 2), red_d)
    blueblitRotate(screen, blue_tank, blue_pos, (blue_w / 2, blue_h / 2), blue_d)

    if keys[pygame.K_o]:
        if red_bullet_BOOM == False:
            red_bullet_BOOM = True
            red_b_pos = (red_bx, red_by)
    if keys[pygame.K_f]:
        if blue_bullet_BOOM == False:
            blue_bullet_BOOM = True
            blue_bpos = (blue_bx, blue_by)

    if red_y >= 850:
        red_y -= 1
    elif red_y <= 230:
        red_y += 1
    elif red_x <= 375:
        red_x += 1
    elif red_x >= 1545:
        red_x -= 1

    if blue_y >= 850:
        blue_y -= 1
    elif blue_y <= 230:
        blue_y += 1
    elif blue_x <= 375:
        blue_x += 1
    elif blue_x >= 1545:
        blue_x -= 1

    """if redBOOM == True:
        screen.blit(red_fire_tank, (red_x, red_y))
        redBOOML += 1
        if redBOOML == 200:
            redBOOM = False
            redBOOML = 0"""
    if red_bullet_BOOM:
        red_bpos = (red_bx, red_by)
        red_bullet_blitRotate(screen, red_bullet, red_bpos, (red_bw / 2, red_bh / 2), red_bd)
        red_bd_rad = math.radians(red_bd)
        if red_bd >= 0 and red_bd < 90:
            red_by -= 2 * math.sin(red_bd_rad)
            red_bx += 2 * math.cos(red_bd_rad)
        elif red_bd >= 90 and red_bd < 180:
            red_by -= 2 * math.sin(red_bd_rad)
            red_bx += 2 * math.cos(-red_bd_rad)
        elif red_bd >= 180 and red_bd < 270:
            red_by += 2 * math.sin(-red_bd_rad)
            red_bx += 2 * math.cos(-red_bd_rad)
        elif red_bd >= 270 and red_bd < 360:
            red_by += 2 * math.sin(-red_bd_rad)
            red_bx += 2 * math.cos(red_bd_rad)

        if red_by >= 900:
            red_bullet_BOOM = False
        elif red_by <= 50:
            red_bullet_BOOM = False
        elif red_bx <= 300:
            red_bullet_BOOM = False
        elif red_bx >= 1600:
            red_bullet_BOOM = False

    if blue_bullet_BOOM:
        blue_bpos = (blue_bx, blue_by)
        blue_bullet_blitRotate(screen, blue_bullet, blue_bpos, (blue_bw / 2, blue_bh / 2), blue_bd)
        blue_bd_rad = math.radians(blue_bd)
        if blue_bd >= 0 and blue_bd < 90:
            blue_by -= 2 * math.sin(blue_bd_rad)
            blue_bx += 2 * math.cos(blue_bd_rad)
        elif blue_bd >= 90 and blue_bd < 180:
            blue_by -= 2 * math.sin(blue_bd_rad)
            blue_bx += 2 * math.cos(-blue_bd_rad)
        elif blue_bd >= 180 and blue_bd < 270:
            blue_by += 2 * math.sin(-blue_bd_rad)
            blue_bx += 2 * math.cos(-blue_bd_rad)
        elif blue_bd >= 270 and blue_bd < 360:
            blue_by += 2 * math.sin(-blue_bd_rad)
            blue_bx += 2 * math.cos(blue_bd_rad)

        if blue_by >= 900:
            blue_bullet_BOOM = False
        elif blue_by <= 50:
            blue_bullet_BOOM = False
        elif blue_bx <= 300:
            blue_bullet_BOOM = False
        elif blue_bx >= 1600:
            blue_bullet_BOOM = False

    if keys[pygame.K_y]:
        if not debug_text and debug_text_timer >= 200:
            debug_text = True
            debug_text_timer = 0
        elif debug_text and debug_text_timer >= 200:
            debug_text = False
            debug_text_timer = 0

    debug_text_timer += 1

    if debug_text:

        screen.blit(text_red, (900, 300))
        screen.blit(text_blue, (900, 400))
        screen.blit(text_mouse, (mouse_x, mouse_y))

    if red_d == 360:
        red_d = 0
    elif red_d < 0:
        red_d += 360

    if blue_d == 360:
        blue_d = 0
    elif blue_d < 0:
        blue_d += 360

    if red_rect.colliderect(blue_brect) and blue_bullet_BOOM:
        blue_win += 1
        blue_bullet_BOOM = False
        red_x = red_sp_x
        red_y = red_sp_y
        red_d = 180
    elif blue_rect.colliderect(red_brect) and red_bullet_BOOM:
        red_win += 1
        red_bullet_BOOM = False
        blue_x = blue_sp_x
        blue_y = blue_sp_y
        blue_d = 0

    if red_win == 3:
        print("Red Win!")
        exit()
    elif blue_win == 3:
        print("Blue Win!")
        exit()


    pygame.display.flip()
