import turtle as t
t.shape("turtle")
def polygon(n):
    for x in range(n):
        t.forward(50)
        t.left(360/n)

def polygon2(n, d):
    for x in range(n):
        t.forward(d)
        t.left(360/n)


polygon(3)  #다각형 함수 호출
polygon(5)

t.up()
t.forward(100)
t.down()
polygon2(3, 100)

t.mainloop


