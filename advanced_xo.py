import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True

cells=[
    {'start_coord':(0, 0), 'end_coord':(190, 190),'x_checked':False, 'o_checked':False},
    {'start_coord':(200, 0), 'end_coord':(390, 190),'x_checked':False, 'o_checked':False},
    {'start_coord':(400, 0), 'end_coord':(490, 190),'x_checked':False, 'o_checked':False},
    {'start_coord':(0, 200), 'end_coord':(190, 390),'x_checked':False, 'o_checked':False},
    {'start_coord':(200, 200), 'end_coord':(390, 390),'x_checked':False, 'o_checked':False},
    {'start_coord':(400, 200), 'end_coord':(490, 390),'x_checked':False, 'o_checked':False},
    {'start_coord':(0, 400), 'end_coord':(190, 590),'x_checked':False, 'o_checked':False},
    {'start_coord':(200, 400), 'end_coord':(390, 590),'x_checked':False, 'o_checked':False},
    {'start_coord':(400, 400), 'end_coord':(490, 590),'x_checked':False, 'o_checked':False},
]

mouse_pos=(0, 0)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    for cell in cells:
        pygame.draw.rect(screen, 'white',(cell['start_coord'][0], cell['start_coord'][1], 190, 190))
        if cell['start_coord'][0]<mouse_pos[0]<cell['end_coord'][0] and cell['start_coord'][1]<mouse_pos[1]<cell['end_coord'][1]:
            cell['o_checked']=True
            print(cell)
            mouse_pos=(0,0)

        if cell['o_checked']:
            pygame.draw.circle(screen, 'blue',(cell['start_coord'][0]+95,cell['start_coord'][1]+95,), 60)
            pygame.draw.circle(screen, 'white',(cell['start_coord'][0]+95,cell['start_coord'][1]+95,), 50)
        if cell['x_checked']:
            pygame.draw.circle(screen, 'blue',(cell['start_coord'][0]+95,cell['start_coord'][1]+95,), 60)
            pygame.draw.circle(screen, 'white',(cell['start_coord'][0]+95,cell['start_coord'][1]+95,), 50)
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()