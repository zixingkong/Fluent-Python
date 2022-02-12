# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     bingdundun
   Description :
   date：          2022/2/11
-------------------------------------------------
"""
import time
import turtle

turtle.title('PythonBingDwenDwen(冰墩墩)')
# 速度
turtle.speed(100)


class BingDwenDwen:
    def pen(self, dict):
        turtle.penup()
        turtle.goto(dict[0], dict[1])
        turtle.pencolor(dict[2])
        turtle.pensize(dict[3])
        turtle.fillcolor(dict[4])
        turtle.begin_fill()
        turtle.pendown()

    def pen1(self, dict_1):
        turtle.penup()
        turtle.goto(dict_1[0], dict_1[1])
        turtle.fillcolor(dict_1[2])
        turtle.begin_fill()
        turtle.setheading(dict_1[3])
        turtle.pendown()

    def left_hand(self, dict, hand):
        self.pen(dict)
        turtle.setheading(80)
        self.circle(hand)
        turtle.end_fill()

    def left_hand_fill(self, dict):
        self.pen(dict)
        turtle.setheading(95)
        self.circle(dict_left_hand[1])
        turtle.end_fill()

    def circle(self, dict):
        for i in dict:
            turtle.circle(i[0], i[1])

    def body(self, dict, dict1):
        turtle.penup()
        self.pen(dict)
        turtle.setheading(20)
        turtle.circle(-250, 35)
        # 左耳
        turtle.setheading(50)
        turtle.circle(-42, 180)
        # 左侧
        turtle.setheading(-50)
        turtle.circle(-190, 30)
        turtle.circle(-320, 45)
        # 左右腿
        self.circle(dict1)
        # 右手
        turtle.setheading(-120)
        self.circle(dict_right_hand[0])
        # 右侧
        turtle.setheading(86)
        turtle.circle(-300, 26)
        # 右耳
        turtle.setheading(122)
        turtle.circle(-53, 160)
        turtle.end_fill()

    def right_ear_fill(self, dict):
        self.pen(dict)
        turtle.setheading(120)
        turtle.circle(-28, 160)
        turtle.setheading(210)
        turtle.circle(150, 20)
        turtle.end_fill()

    def left_ear_fill(self):
        turtle.penup()
        turtle.goto(90, 230)
        turtle.setheading(40)
        turtle.begin_fill()
        turtle.pendown()
        turtle.circle(-30, 170)
        turtle.setheading(125)
        turtle.circle(150, 23)
        turtle.end_fill()

    def right_hand_fill(self, dict):
        self.pen1(dict)
        self.circle(dict_right_hand[1])
        turtle.setheading(-90)
        turtle.circle(300, 14)
        turtle.end_fill()

    def left_leg_fill(self, dict, dict1):
        self.pen1(dict1)
        self.circle(dict)
        turtle.setheading(42)
        turtle.circle(-200, 29)
        turtle.end_fill()

    def right_leg_fill(self, dict, dict1):
        self.pen1(dict1)
        self.circle(dict)
        turtle.setheading(-14)
        turtle.circle(-200, 27)
        turtle.end_fill()

    def eyes(self, dict, dict1):
        self.pen1(dict)
        self.circle(dict1)
        turtle.end_fill()

    def eyes_fill(self, dict):
        for i in dict:
            turtle.penup()
            turtle.goto(i[0], i[1])
            turtle.pencolor(i[2])
            turtle.fillcolor(i[2])
            turtle.begin_fill()
            turtle.pendown()
            turtle.setheading(0)
            turtle.circle(i[3], i[4])
            turtle.end_fill()

    def nose(self, dict):
        turtle.penup()
        turtle.goto(37, 80)
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.pendown()
        self.circle(dict)
        turtle.end_fill()

    def mouse(self):
        turtle.penup()
        turtle.goto(-15, 48)
        turtle.setheading(-36)
        turtle.begin_fill()
        turtle.pendown()
        turtle.circle(60, 70)
        turtle.setheading(-132)
        turtle.circle(-45, 100)
        turtle.end_fill()

    def rainbow(self, dict):
        turtle.penup()
        for i in dict:
            turtle.goto(i[0][0], i[0][1])
            turtle.pensize(5)
            turtle.pencolor(i[0][2])
            turtle.pendown()
            turtle.setheading(60)
            self.circle(i[1])

    def heart(self, dict):
        self.pen(dict)
        turtle.setheading(36)
        turtle.circle(-8, 180)
        turtle.circle(-60, 24)
        turtle.setheading(110)
        turtle.circle(-60, 24)
        turtle.circle(-8, 180)
        turtle.end_fill()

    def rings(self, dict):
        for i in dict:
            turtle.penup()
            turtle.goto(i[0], i[1])
            turtle.pendown()
            turtle.pencolor(i[2])
            turtle.circle(6)

        turtle.penup()
        turtle.pencolor("black")
        turtle.goto(-16, -160)
        turtle.write("BEIJING 2022", font=('Arial', 10, 'bold italic'))
        turtle.hideturtle()
        turtle.done()


if __name__ == '__main__':
    dict = [(177, 112, "lightgray", 3, "white"),
            (182, 95, "black", 1, "black"),
            (-73, 230, "lightgray", 3, "white"),
            (-130, 180, "black", 1, "black"),
            (220, 115, "brown", 1, "brown")]
    dict_1 = [(-180, -55, "black", -120),
              (108, -168, "black", -115),
              (-38, -210, "black", -155),
              (-64, 120, "black", 40),
              (51, 82, "black", 120)]
    # 左手
    dict_left_hand = [[(-45, 200), (-300, 23)],
                      [(-37, 160), (-20, 50), (-200, 30)]]
    # 右手
    dict_right_hand = [[(50, 30), (-35, 200), (-300, 23)],
                       [(50, 30), (-27, 200), (-300, 20)]]
    # 左右腿
    dict1 = [(120, 30),
             (200, 12),
             (-18, 85),
             (-180, 23),
             (-20, 110),
             (15, 115),
             (100, 12),
             (15, 120),
             (-15, 110),
             (-150, 30),
             (-15, 70),
             (-150, 10),
             (200, 35),
             (-150, 20)]
    # 左右腿填充
    dict2 = [[(110, 15), (200, 10), (-18, 80), (-180, 13), (-20, 90), (15, 60)],
             [(15, 100), (-10, 110), (-100, 30), (-15, 65), (-100, 10), (200, 15)]]
    # 左右眼圈
    dict4 = [[(-35, 152), (-100, 50), (-35, 130), (-100, 50)],
             [(-32, 152), (-100, 55), (-25, 120), (-120, 45)]]
    # 左右眼珠
    dict5 = [
        [(-47, 55, "white", 25, 360),
         (-45, 62, "darkslategray", 19, 360),
         (-45, 68, "black", 10, 360),
         (-47, 86, "white", 5, 360)],
        [(79, 60, "white", 24, 360),
         (79, 64, "darkslategray", 19, 360),
         (79, 70, "black", 10, 360),
         (79, 88, "white", 5, 360)]
    ]
    # 鼻子
    dict6 = [(-8, 130), (-22, 100), (-8, 130)]
    # 彩虹圈
    dict7 = [[(-135, 120, "cyan"), [(-165, 150), (-130, 78), (-250, 30), (-138, 105)]],
             [(-131, 116, "slateblue"), [(-160, 144), (-120, 78), (-242, 30), (-135, 105)]],
             [(-127, 112, "orangered"), [(-155, 136), (-116, 86), (-220, 30), (-134, 103)]],
             [(-123, 108, "gold"), [(-150, 136), (-104, 86), (-220, 30), (-126, 102)]],
             [(-120, 104, "greenyellow"), [(-145, 136), (-90, 83), (-220, 30), (-120, 100)]]]
    # 五环
    dict8 = [(-5, -170, "blue"),
             (10, -170, "black"),
             (25, -170, "brown"),
             (2, -175, "lightgoldenrod"),
             (16, -175, "green")]
    BingDwenDwen = BingDwenDwen()
    BingDwenDwen.left_hand(dict[0], dict_left_hand[0])
    BingDwenDwen.left_hand_fill(dict[1])
    BingDwenDwen.body(dict[2], dict1)
    BingDwenDwen.right_ear_fill(dict[3])
    BingDwenDwen.left_ear_fill()
    BingDwenDwen.right_hand_fill(dict_1[0])
    BingDwenDwen.left_leg_fill(dict2[0], dict_1[1])
    BingDwenDwen.right_leg_fill(dict2[1], dict_1[2])
    BingDwenDwen.eyes(dict_1[3], dict4[0])
    BingDwenDwen.eyes_fill(dict5[0])
    BingDwenDwen.eyes(dict_1[4], dict4[1])
    BingDwenDwen.eyes_fill(dict5[1])
    BingDwenDwen.nose(dict6)
    BingDwenDwen.mouse()
    BingDwenDwen.rainbow(dict7)
    BingDwenDwen.heart(dict[4])
    BingDwenDwen.rings(dict8)
