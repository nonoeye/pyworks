import turtle as t

t.shape("turtle")
"""
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

# 삼각형
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)

t.right(180)

t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)

t.left(90)

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
"""
'''
# 
for i in range(4):
    t.forward(100)
    t.right(90)

# 삼각형
for i in range(3):
    t.forward(100)
    t.left(120)

t.right(180)

for i in range(3):
        t.forward(100)
        t.right(120)

for i in range(4):
    t.forward(100)
    t.left(90)
'''

# 변수 사용하기
n = 6
d = 100

for i in range(n):
    t.forward(d)
    t.left(360/n)

t.color("red")
t.pensize(3)
t.circle(50)



t.mainloop()