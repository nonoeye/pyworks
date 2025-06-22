# 입력과 출력
# 입력 - Entry(), 출력 - Text()
"""
import tkinter as tk

def click():
    # Enty에 입력된 문자 가져오기
    text = Entry.get()
    # 0(첫째행), 0(시작문자) 에서 끝까지 삭제
    output.delete(0.0, tk.END)
    # Text에 문자 삽입하기 (END- 끝까지 삭제후 문자 삽입)
    output.insert(tk.END,text)

root = tk.Tk()
root.title("입력과 출력")
root.geometry("250x200+200+300")
#전체 글꼴 적용
root.option_add(*"font", "System 13")


# 이름 입력받기
tk.Label(root, text="이름: ", height=3, font=("System", 12)).grid(row=0, column=0)
Entry = tk.Entry(root)
Entry.grid(row=0, column=1)

#버튼을 눌러 출력하기 - columnspan=2 (병합)
tk.Button(root,text="확인", width=10, height=2).grid(row=1, columnspan=2)
tk.Label(root,text="").grid(row=2, column=0) # 빈 레이블 추가
output = tk.Text(root, width=20, height=3)
output.grid(row=30, columnspan=2)

root.mainloop()
"""

#컴퓨터 용어 사전 만들기
from tkinter import *

dic = {
    "이진수": "2진법으로 나타낸 숫자,0과 1로 구성함",
    "이진수": "특정한 기능을 수행하는 프로그램으로 재사용 가능한 코드 조각",
    "알고리즘": "컴퓨터로 작업을 수행하기 위해 컴퓨터가 이해할 수 있도록 \
단계별로 설명해 놓은 것"
}

def submit():
    #찾는 단어가 어쩌구저쩌구
    try:
        WORD = Entry.get() # 입력된 단어
        definition = dic[WORD] # 단어 검색
        output.delete(0.0, END) #입력상자 초기화
        output.insert(END) # 단어 삽입
    except KeyError:
        output.delete(0.0, END)
        Output.Insert(END, "단어를 찾을수 없습니다")

root = Tk()
root.title("컴퓨터 용어 사전")

Label(root, text="검색할 단어를 입력하세요").grid(row=0, column=0)
Entry = Entry(root, width=20, bg="skyblue")
Entry.grid(row=1, column=0)

# 제출
Button(root, text="제출").grid(row=2, column=0, sticky=W)
Label(root,text="정의").grid(row=3, column=0, sticky=W)
output = Text(root, width=60, height=10, bg="yellowgreen")
output.grid(row=4, column=0, sticky=W)

root.mainloop()
    