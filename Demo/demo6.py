# –*–coding:utf-8 –*–
# time:2021-03-05 16:04
import pygame, sys, random
from pygame.locals import *
from tkinter import messagebox

redColor = pygame.Color(255, 0, 0)
blackColor = pygame.Color(0, 0, 0)
whiteColor = pygame.Color(255, 255, 255)

def Gameover():
	'''
	GameOver 游戏结束
	'''
	messagebox.showinfo("提示：","GameOver")
	pygame.quit()
	sys.exit()

def main():
    # 初始化pygame
    pygame.init()
    # 定义一个变量 控制速度
    fpsClock = pygame.time.Clock()
    # 创建一个窗口界面
    playSurface = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('贪吃蛇')

    # 初始化目标方块的位置
    targetPosition = [300, 300]
    # 目标方块标记 判断贪吃蛇是否吃掉目标方块 1为没吃掉 0为吃掉
    targetFlag = 1


    # 初始化贪吃蛇的位置 （100,100）为基准
    # 初始化贪吃蛇长度 列表中有几个元素 就有几个身体
    snake_head = [100, 100]
    snake_body = [[80, 100], [60, 100]]


    # 初始化方向 默认为右
    direction = 'right'
    # 定义一个认为控制的方向的变量
    changedirection = direction

    # pygame 所有事件全部放到一个实时循环中
    while True:
        # 从队列中获取事件
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    changedirection = 'right'
                if event.key == K_LEFT:
                    changedirection = 'left'
                if event.key == K_UP:
                    changedirection = 'up'
                if event.key == K_DOWN:
                    changedirection = 'down'
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
        # 确定方向
        if changedirection == 'left' and not direction == 'right':
            direction = changedirection
        if changedirection == 'right' and not direction == 'left':
            direction = changedirection
        if changedirection == 'up' and not direction == 'down':
            direction = changedirection
        if changedirection == 'down' and not direction == 'up':
            direction = changedirection

        # 根据方向移动蛇头
        if direction == 'right':
            snake_head[0] += 20
        if direction == 'left':
            snake_head[0] -= 20
        if direction == 'up':
            snake_head[1] -= 20
        if direction == 'down':
            snake_head[1] += 20

        # 增加蛇的长度
        snake_body.insert(0, list(snake_head))

        # 如果贪吃蛇位置和目标方块位置重合
        if snake_head[0] == targetPosition[0] and snake_head[1] == targetPosition[1]:
            targetFlag = 0

        else:
            snake_body.pop()

        if targetFlag == 0:
            x = random.randrange(1, 32)
            y = random.randrange(1, 24)
            targetPosition = [int(x * 20), int(y * 20)]
            targetFlag = 1

        # 填充背景颜色
        playSurface.fill(blackColor)

        for position in snake_body:
            # rect函数内
            # 第一个参数surface  指定一个surface编辑区
            # 第二个参数color    指定颜色
            # 第三个参数rect     返回一个矩形包含位置信息（x,y）,(width，height)
            # 第四个参数width    表示线条的粗细 width=0 实心  width=1 空心
            # 画蛇
            pygame.draw.rect(playSurface, whiteColor, Rect(position[0], position[1], 20, 20))
            # 画目标方块儿
            pygame.draw.rect(playSurface, redColor, Rect(targetPosition[0], targetPosition[1], 20, 20))

        # 更新显示到屏幕
        pygame.display.flip()

        # 判断游戏结束
        if snake_head[0] > 620 or snake_head[0] < 0:
            Gameover()
        if snake_head[1] > 460 or snake_head[1] < 0:
            Gameover()
        # 控制游戏速度
        fpsClock.tick(3)


# 启动入口 main函数
if __name__ == '__main__':
    main()