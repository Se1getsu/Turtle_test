from turtle import *

def print_green(*obj, sep=' ', **kwargs): print("\033[32m%s\033[0m" % sep.join([str(e) for e in obj]), **kwargs)
def input_green(obj): print_green(obj, end=''); return input()

stage = int(input_green("stage(1-10) = "))


# 【直線を描く】
if stage == 1:
    
    forward(200)
    done()


# 【四角描く】
elif stage == 2:
    
    forward(200)
    left(90)
    forward(200)
    left(90)
    forward(200)
    left(90)
    forward(200)
    left(90)
    done()


# 【forに書き換える】
elif stage == 3:
    
    for i in range(4):
        forward(200)
        left(90)
    done()


# 【任意のサイズの四角を描く】
elif stage == 4:
    
    a = numinput("数値を入力", "一辺の長さを入力してください。")
    for i in range(4):
        forward(a)
        left(90)
    done()


# 【渦巻きを描く】
elif stage == 5:
    
    speed(10)
    for i in range(50):
        forward((i + 1) * 10)
        left(90)
    done()
    

# 【四角を描く関数】
elif stage == 6:
    
    def shikaku():
        for i in range(4):
            forward(200)
            left(90)
    
    for i in range(6):
        shikaku()
        penup()
        goto(xcor()-30, ycor()-30)
        pendown()
    done()
    

# 【四角の色をifで変える】
elif stage == 7:
    
    def shikaku():
        for i in range(4):
            forward(200)
            left(90)
    
    for i in range(6):
        if i % 2 == 0:
            pencolor("red")
        else:
            pencolor("blue")
        
        shikaku()
        penup()
        goto(xcor()-30, ycor()-30)
        pendown()
    done()
    
    
# 【復習：五芒星を描く】
elif stage == 8:
    
    for i in range(5):
        forward(200)
        #left(180+36)
        right(180-36)
    done()


# 【すごい図形を書く】
elif stage == 9:
    
    penup()
    goto(-150, 150)
    pendown()
    
    d = 110
    
    for i in range(36):
        forward(300)
        right(d)
        
    done()


# 【whileに書き換える】
elif stage == 10:
    
    speed(0)
    penup()
    goto(-150, 150)
    pendown()
    
    d = numinput("数値を入力", "角度を入力してください。")
    forward(300)
    right(d)
    degree = d
    
    while degree % 360 != 0:
        forward(300)
        right(d)
        degree += d
    
    done()


# 後は やりたいようにやらせて、それをアシストする

