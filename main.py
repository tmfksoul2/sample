import pygame

pygame.init()

# ウィンドウの作成
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('〇×ゲーム')

# 色の設定
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# フォントの設定
font = pygame.font.SysFont(None, 100)
text_img = font.render('Test', True, BLACK, GREEN)

# 画像の読み込み
winner_img = pygame.image.load('sayachi.jpg')
#winner_img = pygame.transform.scale(winner_img, (300, 300))

# ボード（0:空白、1:〇、-1:×）===================================================================================================
board = [[0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0]]

number = 1

for row_index, row in enumerate(board):
    for col_index, col in enumerate(row):
        if col == 1:
            pygame.draw.circle(screen, RED, (col_index * 200 + 100, row_index * 200 + 100), 80, width=5)
# ==========================================================================================================================


# 関数======================================================================================================================
def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (0, i * 200), (screen_width, i * 200), width = 5)
        pygame.draw.line(screen, BLACK, (i * 200, 0), (i * 200, screen_height), width = 5)

def draw_board():
    # 〇、×の描画
    for row_index, row in enumerate(board):
        for col_index, col in enumerate(row):
            if col == 1:
                pygame.draw.circle(screen, RED, (col_index * 200 + 100, row_index * 200 + 100), 80, width=5)
            elif col == -1:
                pygame.draw.line(screen, BLUE, (col_index * 200 + 20, row_index * 200 + 20), (col_index * 200 + 180, row_index * 200 + 180), width = 5)
                pygame.draw.line(screen, BLUE, (col_index * 200 + 20, row_index * 200 + 180), (col_index * 200 + 180, row_index * 200 + 20), width = 5)

def check_winner():
    # 勝利の確認
    winner = None
    game_over = False
    for row_index, row in enumerate(board):
        if sum(row) == 3:
            winner = 'o'
        if sum(row) == -3:
            winner = 'x'
        if board[0][row_index] + board[1][row_index] + board[2][row_index] == 3:
            winner = 'o'
        if board[0][row_index] + board[1][row_index] + board[2][row_index] == -3:
            winner = 'x'
        if board[0][0] + board[1][1] + board[2][2] == 3 or board[0][2] + board[1][1] + board[2][0] == 3:
            winner = 'o'
        if board[0][0] + board[1][1] + board[2][2] == -3 or board[0][2] + board[1][1] + board[2][0] == -3:
            winner = 'x'

    # 勝者の描画
    if winner == 'o' or winner == 'x':
        winner_text_img = font.render(winner + ' Win!', True, BLACK, GREEN)
        screen.blit(winner_text_img, (200, 50))
        screen.blit(winner_img, (200, 150))
        reset_text_img = font.render('Click to Reset', True, BLACK, GREEN)
        screen.blit(reset_text_img, (80, 420))
        game_over = True
    return game_over

# ==========================================================================================================================

# メインループ===============================================================================================================
run = True
while run:

    # ウィンドウの塗りつぶし
    screen.fill(WHITE)

    # マウスの位置の取得
    mx, my = pygame.mouse.get_pos()
    x = mx // 200
    y = my // 200

    # グリッド線の描画
    draw_grid()

    # 〇×の描画
    draw_board()

    # 勝者の確認
    game_over = check_winner()
    print(game_over)
    
    pygame.display.update()

    # イベントの取得
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if board[y][x] == 0 and game_over == False:
                board[y][x] = number
                number *= -1
            if game_over:
                board = [[0, 0, 0], 
                         [0, 0, 0], 
                        [0, 0, 0]]
                number = 1
# ==========================================================================================================================
pygame.quit()