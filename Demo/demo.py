# –*–coding:utf-8 –*–
# time:2021-01-19 14:32
import pygame
print(pygame.version)


#  定义三个常量函数，用来标识白棋、黑棋、以及空
EMPTY = 0
BLACK = 1
WHITE = 2
# 定义黑色
black_color = [0, 0, 0]
# 定义白色
white_color = [255, 255, 255]

# 定义棋盘
class RenjuBoard(object):
    def __init__(self):
        self._board = [[]] * 15
        self.reset()
    # reset 重置棋盘
    def reset(self):
        for row in range(len(self._board)):
            self._board[row] = [EMPTY] * 15
    # 定义棋盘上的下棋函数，row表示行，col 表示列， is_black表示当前点位该下黑棋，还是白棋
    def move(self, row, col, is_black):
        if self._board[row][col] == EMPTY:
            self._board[row][col] = BLACK if is_black else WHITE
            return True
        return False
    # 给棋盘定义一个函数将自己在screen上面画出来，使用pygame.draw（）函数，并且将顺便下了的棋子也画出来
    def draw(self, screen):
        for h in range(1, 16):
            pygame.draw.line(screen, black_color, [40, h * 40], [600, h * 40], 1)
            # pygame.draw.line(screen, black_color)
        # 给棋盘加一个外框，使美观
        pygame.draw.circle(screen, black_color, [320, 320], 5, 0)
        pygame.draw.circle(screen, black_color, [160, 160], 3, 0)
        pygame.draw.circle(screen, black_color, [160, 480], 3, 0)
        pygame.draw.circle(screen, black_color, [480, 160], 3, 0)
        pygame.draw.circle(screen, black_color, [480, 480], 3, 0)
        for row in range(len(self._board)):
            for col in range(len(self._board[row])):
                # 将下在棋盘上的棋子画出来
                if self._board[row][col] != EMPTY:
                    ccolor = black_color \
                        if self._board[row][col] == BLACK else white_color
                    # 取得这个交叉点下的棋子的颜色，并将棋子画出来
                    pos = [40 * (col + 1), 40 * (row + 1)]
                    # 画出棋子
                    pygame.draw.circle(screen, ccolor, pos, 18, 0)

def is_win(board):
    for n in range(15):
        flag = 0
        for b in board._board:
            if b[n] == 1:
                flag += 1
                if flag == 5:
                    print('黑棋胜！')
                    return False
            else:
                flag = 0
    flag = 0
    for b in board._board:
        if b[n] == 2:
            flag += 1
            if flag == 5:
                print('白棋胜！')
                return False
        else:
            flag = 0

    flag = 0
    for b in board._board[n]:
        if b == 1:
            flag += 1
            if flag == 5:
                print('黑棋胜！')
                return False
        else:
            flag = 0

    flag = 0
    for b in  board._board[n]:
        if b == 2:
            flag += 1
            if flag == 5:
                print('白棋胜！')
                return False
        else:
            flag = 0

    # 判断正斜方向胜利
    for x in range(4, 25):
        flag = 0
        for i, b in range(board._board):
            if 14 >= x - i >= 0 and b[x - i] == 1:
                flag += 1
                if flag == 5:
                    print('黑棋胜！')
                    return False
            else:
                flag = 0
    # 判断斜方向胜利
    for x in range(11, -11, -1):
        flag = 0
        for i, b in enumerate(board._board):
            if 0 <= x + 1 <= 14 and b[x + i] == 1:
                flag = 0
                if flag == 5:
                    print('白棋胜！')
                    return False
            else:
                flag = 0
    return True

def main():
    board = RenjuBoard()
    is_black = True
    pygame.init() #初始化
    pygame.display.set_caption('五子棋')
    screen = pygame.display.set_mode((640, 640))
    screen.fill([125, 95, 24])
    board.draw(screen)
    pygame.display.flip() #刷新窗口显示
    running = True


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                pass
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                row = round((y - 40) / 40)
                col = round((x - 40) / 40)
                if board.move(row, col, is_black):
                    is_black = not is_black
                    screen.fill([125, 95, 24])
                    board.draw(screen)
                    pygame.display.flip() # 刷新显示
                    if not is_win(board):
                        running = False
    pygame.quit()

if __name__=='__main__':
    main()