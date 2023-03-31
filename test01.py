from turtle import *

def print_green(*obj, sep=' ', **kwargs): print("\033[32m%s\033[0m" % sep.join([str(e) for e in obj]), **kwargs)
def input_green(obj): print_green(obj, end=''); return input()

option = int(input_green("option(1-10) = "))


# 以下の関数はここには載せていない。
# begin_poly, end_poly, get_poly, clone, getturtle, getscreen, tracer, update
# getcanvas, getshapes, register_shape, addshape

# 関数の右側に付しているコメントはその関数の別名。どれを使用しても構わない。


# 【カメを動かす】
if option == 1:
    # 初期：原点 x軸正の方向

    # (相対) 前進・後進・正回転・負回転
    forward(100)    # fd
    back(100)       # bk backward
    left(45)        # lt
    right(90)       # rt

    # (絶対) 座標移動・x移動・y移動・原点に移動・向き設定
    goto(10, 20)    # setpos setposition (タプルを渡してもOK)
    setx(20); sety(40)
    home()
    setheading(90)  # seth (x軸正から反時計)

    # 円弧 (半径, extent=中心角, steps=多角形)
    circle(30); circle(-30)
    circle(50, 180)
    circle(100, 360, 6)
    # 点をプロット (size=直径, 色)
    dot(30, "red");     fd(50)

    # カメのスタンプ
    id = stamp();       fd(50);circle(30)
    clearstamp(id)
    for _ in range(5): stamp()
    clearstamps(2)  # 最初の2個を削除
    clearstamps(-3) # 最後の3個を削除

    # 取り消し
    circle(50); undo()
    # setundobuffer(size: int) でundoバッファサイズを設定
    # undobufferentries() はバッファに記録中のエントリー数を返す
    
    # 速度変更
    home();fd(400); speed(10); home();rt(180);fd(400);home()
    # 0.5 以上 10 以下を指定。それ以外は 0 (アニメーションなし) になる。
    # "fastest"=0  "fast"=10  "normal"=6  "slow"=3  "slowest"=1
    

# 【値に関する設定】
elif option == 2:
    
    # 角度を 360 等分ではない値に変更
    degrees(100); circle(30, 50)    # (50で半円になる)
    # 角度をラジアンにする
    import math
    radians(); circle(60, math.pi)  # (πで半円になる)
    
    # RGBで値を設定する際に 0〜255 で設定する（初期は 0〜1）
    colormode(255)
    
    # モード
    s = mode()      # ("standard" 初期東向き 反時計回りが正)
    mode("logo")    # (初期北向き 時計回りが正)
    mode("world")   # (ユーザー定義座標系(cf. option=5)を使用)
    

# 【現在のカメの状態を取得】
elif option == 3:
    
    # 位置・x座標・y座標・向き・速さ
    p = position()  # pos ((0.00, 0.00))
    x = xcor()      # (0.0)
    y = ycor()      # (0.0)
    θ = heading()   # (0.0) (0 以上 360 未満を返す)
    v = speed()     # (3)
    
    # ある座標への向き・距離
    φ = towards(10, 10)   # (45.0) (タプルを渡してもOK)
    d = distance(30, 40)  # (50.0)
    
    # ペンの太さ・下りてるか
    w = pensize()   # (1)
    b = isdown()    # (True)
    
    # ペンの色・塗りつぶし色・塗りつぶしモードか
    c = pencolor()  # ("black")
    c = fillcolor() # ("black")
    c = color()     # (("black", "black"))
    b = filling()   # (False)
    
    # カメの表示/非表示・見た目・その他 (詳しくは option=6 【カメの制御】 にて)
    b = isvisible()   # (True)
    b = shape()       # ("classic")
    b = resizemode()  # ("noresize")
    b = shapesize()   # ((1.0, 1.0, 1))
    b = shearfactor() # (0.0)
    φ = tiltangle()   # (0.0)
    
    # カメの矩形領域？
    rect = shapetransform()  # (1.0, 0.0, 0.0, 1.0)
    rect = get_shapepoly()   # ((0, 0), (-5, -9), (0, -7), (5, -9))
    
    # ペンの設定をタプルのリストで取得
    p = pen()
    # {       'shown': True,
    #       'pendown': True,
    #      'pencolor': 'black',
    #     'fillcolor': 'black',
    #       'pensize': 1,
    #         'speed': 3,
    #    'resizemode': 'noresize',
    # 'stretchfactor': (1.0, 1.0),
    #       'outline': 1,
    #   'shearfactor': 0.0,
    #          'tilt': 0.0         }


# 【ペンの制御】 
elif option == 4:
    
    # ペンを下ろす・上げる・太さ変更
    pendown()       # pd down
    penup()         # pu up
    pensize(2)      # width
    pen(pendown=True, pensize=1)
    # shown: bool           表示/非表示
    # pendown: bool         ペンが下りてるか
    # pencolor: str|tuple   色
    # fillcolor: str|tuple  塗りつぶし色
    # pensize: int          太さ
    # speed: int            速さ
    # resizemode: "auto"|"user"|"noresize"
    # stretchfactor: (float,float)
    # outline: int
    # tilt: float
    
    # ペンの色・塗りつぶしの色
    pencolor("red")       # ("#33cc8c"などもOK)
    pencolor(1, 1, 1)     # (白) (タプルを渡してもOK)
    fillcolor("red")
    fillcolor(1, 1, 1)
    color("red", "blue")  # (pencolor("red"); fillcolor("blue"))
    
    # 塗りつぶしモード
    begin_fill()
    circle(30)
    end_fill()
    
    
# 【キャンバスの制御】
elif option == 5:
    
    # 背景色
    bgcolor("orange")
    bgcolor(1, 0.5, 1)
    # bgpic("ファイルパス") で背景画像を設定できる
    
    # リセット (設定は全て保持される)
    circle(30,180); clear()
    # リセット (設定も全て初期状態に戻り、カメは原点へ)
    circle(30,180); reset()
    # リセット (全てのカメをリセット)
    circle(30,180); resetscreen()
    # リセット (背景色・背景画像・イベントを含めた全てを初期状態に)
    circle(30,180); clearscreen()
    
    # 文字を出す
    write("これはサンプルの文章です。", True, align="left"); circle(-30)
    # arg: object               文字（strにキャストされる）    
    # move: bool = False        Trueなら出した文字の右下に移動する
    # align: str = "left"       カメの右に:"left" カメを中心に:"center" カメの左に: "left"
    # font: (str, int, str) = ("Arial", 8, "normal")    フォント
    
    # ユーザー定義座標系（角度が歪む場合がある）
    setworldcoordinates(-50,-80,50,80); circle(30)
    

# 【カメの制御】
elif option == 6:    
    
    pu();speed(0);goto(100,400)
    def m(): pu();speed(0);rt(169);fd(305);seth(0);pd(); speed(1);fd(300) 
    
    # カメの非表示/表示・見た目
    hideturtle()       ;m()# ht
    showturtle()           # st
    shape("classic")   ;m()# (矢印（デフォルト）)
    shape("arrow")     ;m()# (少し大きい矢印)
    shape("triangle")  ;m()# (大きい矢印)
    shape("turtle")    ;m()# (カメ)
    shape("circle")    ;m()# (丸)
    shape("square")    ;m()# (四角)
    
    # リサイズモード
    resizemode("noresize")
    # "noresize": 大きさ不変（デフォルト）
    # "auto": ペンの太さによって変える
    # "user": shapesize関数で設定する
    shapesize(1.0, 1.0, 1) # ((幅, 厚み, アウトライン) この設定はデフォルト値)
    
    # せん断因子mを設定（傾き 1/m で斜めらせることができる）
    shearfactor(1); m()
    
    # 回転・回転角設定
    tilt(45); m()   # (45度 半時計回転)
    tiltangle(0)    # (元に戻す)
    

# 【イベント】
elif option == 7:
    
    # 画面をクリック・カメをクリック・離す・ドラッグ
    onscreenclick(lambda x, y: print("画面がクリックされた"))
    onclick(lambda x, y: print("カメがクリックされた"))
    onrelease(lambda x, y: print("カメがリリースされた"))
    ondrag( goto )
    # fun: (float, float) -> object コールバック
    # btn: int = 1                  マウスボタンの番号（デフォルト 1 は 左クリック）
    # add: True|False|None = None   Trueなら新しい束縛として、そうでなければ上書き
    
    # キーが押された・離された
    onkeypress(lambda: print("上"), "Up")
    onkeyrelease(lambda: print("上リリース"), "Up")   # onkey
    
    # t[ms]後に呼び出す
    ontimer(lambda: print("3秒経過"), 3000)


# 【アニメーションの設定】
elif option == 8:
    
    # アニメーションの描画間隔[ms]（長いと遅くなる）
    dt = delay()    # (5)
    delay(100); fd(100); lt(180)
    

# 【ウィンドウの制御】
elif option == 9:
    
    # ウィンドウのタイトルを設定
    title("9.ウィンドウの制御")
    
    # ウィンドウの高さ・幅を取得
    h = window_height()     # (876 (環境依存))
    w = window_width()      # (900 (環境依存))
    
    # ウィンドウの位置と大きさをセット
    setup(0.5, 0.75, None, None)    # (初期値  幅:ディスプレイの50% 高さ:ディスプレイの75%  x:中央 y:中央)
    setup(500, 400, 300, 200)    # (幅:500px 高さ:400px  x:300px y:200px)
    # 第 3,4 引数は省略可
    
    # ウィンドウフォーカスを獲得 (引数の xdummy, ydummy は onclick に渡す時用)
    listen()
    
    # 入力ダイアログ
    name = textinput("テスト", "名前: "); print_green("name = %r" % name)       # Cancel を押したら None
    height = numinput("テスト", "身長: "); print_green("height = %r" % height)  # Cancel を押したら None
    
    # ウィンドウを閉じる
    bye()
    # exitonclick() でスクリーン上のマウスクリックに bye を束縛できる。


# 【クラス】
elif option == 10:
    
    # カメをインスタンス化
    t = Turtle()
    t.fd(200)
    
    reset(); del t
    
    # 複数のカメを作って動かす
    ts = [Turtle() for _ in range(5)]
    for i, t in enumerate(ts):
        t.penup(); t.goto(-150, i*50-100); t.pendown(); t.speed(0);
    for _ in range(60):
        for i, t in enumerate(ts):
            t.forward(5)
    
    # ベクトル演算
    a = Vec2D(30, 40)
    b = Vec2D(20, -20)
    
    c = a + b        # ((50.00,20.00))
    d = a - b        # ((10.00,60.00))
    e = a * b        # (-200 内積)
    f = 2 * a        # ((60.00,80.00))
    g = abs(a)       # (50.0 絶対値)
    h = b.rotate(90) # ((20.00,20.00))



if option != 9:
    
    # 終了（これがないと実行が終了してウィンドウが閉じる）
    done()     # mainloop