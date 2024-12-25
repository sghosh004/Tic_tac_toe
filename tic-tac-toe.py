import pygame
from sys import exit
pygame.init()

WIDTH,HEIGHT=500,500
surface=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
clock=pygame.time.Clock()
board=[[None for i in range(3)] for j in range(3)]
cross=pygame.image.load('Cross_tic_tac_toe.png')
circle=pygame.image.load('Circle_tic_tac_toe.png')
turn='O'
font=pygame.font.Font(None, 50)

def reset_game():
    global board, turn
    pygame.time.wait(3000)
    turn='O'
    board=[[None for i in range(3)] for j in range(3)]

def check_winner(board):
    for row in range(3):
        if all(board[row][col] == 'X' for col in range(3)):
            return 'X'
        if all(board[row][col] == 'O' for col in range(3)):
            return 'O'

    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)):
            return 'X'
        if all(board[row][col] == 'O' for row in range(3)):
            return 'O'

    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != None:
        return board[0][0]
    if (board[0][2] == board[1][1] == board[2][0]) and board[0][2] != None:
        return board[0][2]

    if all(cell != None for row in board for cell in row):
        return 'Draw'

    return None

while True:
    surface.fill((242, 230, 217))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            print(f'Mouse clicked at {x}, {y}')
            if x>100 and x < 400 and y>100 and y<400:
                x, y = (x//100)-1, (y//100)-1
                if board[x][y]==None:
                    board[x][y]=turn
                    turn='X' if turn == 'O' else 'O'

    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == 'O':
                surface.blit(circle,(100*(i+1),100*(j+1)))
            elif board[i][j] == 'X':
                surface.blit(cross,(100*(i+1),100*(j+1)))

    pygame.draw.rect(surface, (191, 128, 64), pygame.Rect(100,100,301,301), 5)
    pygame.draw.line(surface, (191, 128, 64),(200,100),(200,400),5)
    pygame.draw.line(surface, (191, 128, 64),(300,100),(300,400),5)
    pygame.draw.line(surface, (191, 128, 64),(100,200),(400,200),5)
    pygame.draw.line(surface, (191, 128, 64),(100,300),(400,300),5)

    winner=check_winner(board)
    if winner is not None:
        pygame.draw.rect(surface, (191,128,64), pygame.Rect(0,200,500,100))
        if winner == 'Draw':
            result=font.render('It\'s a Draw', False, (0,0,0))
        else:
            result=font.render('Winner is '+ winner, False, (0,0,0))
        surface.blit(result, result.get_rect(center=(250,250)))
        pygame.display.flip()
        pygame.time.delay(1000)
        reset_game()
    
    pygame.display.flip()
    clock.tick(60)