import pygame
import sys

pygame.init()

background_color =(255,255,255)
line_color = (0,0,0)
red = (255,0,0)
green = (0,100,0)

screen = pygame.display.set_mode([600,600])

grid = [[0 for i in range(100)] for j in range(100)]
blocked_list = []
distance_list = [sys.maxsize for i in range(100)]
visited_list = [False for i in range(100)]

start_row = 0
start_col = 0

def print_sol():
    print("Node \tDistance from Source")
    for node in range(100):
        if node not in blocked_list:
            print(node, "\t", distance_list[node])


def populate_grid():
    global grid
    for i in range(100):
        if i-10 >= 0:
            grid[i][i-10] = 1
        if i+10 <= 99:
            grid[i][i+10] = 1
        if i-1 >= 0 and i%10 != 0:
            grid[i][i-1] = 1
        if i+1 <= 99 and (i+1)%10 != 0:
            grid[i][i+1] = 1
        
def min_dist():
    global distance_list,visited_list
    min = sys.maxsize
    min_index = source_node
    for u in range(100):
        if distance_list[u] < min and visited_list[u] == False:
            min = distance_list[u]
            min_index = u
    return min_index

def dijkstra():

    global grid,visited_list,distance_list,source_node

    for i in range(100):
        x = min_dist()
        visited_list[x] = True
        for y in range(100):
            if grid[x][y] > 0 and visited_list[y] == False and \
                distance_list[y] > distance_list[x] + grid[x][y]:
                distance_list[y] = distance_list[x] + grid[x][y]
    
def node(row,col):
    global start_row,start_col
    start_row,start_col = col,row
    pygame.draw.rect(screen,red,(row*50 + 2,col*50 + 2,50 - 2,50 - 2))
       
    pygame.display.update()

def block(row,col):
    global grid,blocked_list
    for i in range(100):
        grid[i][10*(col-1)+(row-1)] = 0
    blocked_list.append(10*(col-1)+(row-1))

    pygame.draw.rect(screen,line_color,(row*50 + 2,col*50 + 2,50 - 2,50 - 2))
    pygame.display.update()

def display_grid():
    pygame.display.set_caption("SHORTEST PATH FINDER")
    screen.fill(background_color)

    for i in range(11):
        pygame.draw.line(screen,line_color,(50 + 50*i,50),(50 +50*i,550),2)
        pygame.draw.line(screen,line_color,(50,50 + 50*i),(550,50 +50*i),2)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONUP:
                row,col = pygame.mouse.get_pos()
                row = row//50
                col = col//50
                if row > 0 and col > 0:
                    if event.button == 1:
                        block(row,col)
                    if event.button == 3:
                        node(row,col)
                            

populate_grid()
display_grid()

source_node = 10*(start_row-1)+(start_col-1)
distance_list[source_node] = 0
visited_list[source_node] = True

dijkstra()

print_sol()

pygame.quit()









    


    

