
from tkinter import*

root = Tk()
root.title("Tic Tac Toe")
Label(root, text='Welcome To Tictactoe').pack()
ttt_grid =[]
index = 0
x_turn = True

def click(event, button_id):
    if ttt_grid[button_id] != '0' and ttt_grid[button_id] != 'X':
        if x_turn:
            ttt_grid[button_id]['text'] = 'X'
        else:
            ttt_grid[button_id]['text'] = '0'
        x_turn = not x_turn


ttt_frame = LabelFrame(root)

for r in range(3):
    for c in range(3):
        Button(ttt_frame, width=3)
        Button.grid(row=r, column=c)
        Button.bind('<Button-1>', lambda event, i= index: click(event,i))
        index +=1
        ttt_grid.append(Button)

ttt_frame.pack()
score_frame = LabelFrame(root, borderwidth=0, highlightthickness=0)
Label(score_frame,text='Score:').grid(row=0, column=0)
Label(score_frame,Text='100').grid(row=0, column=1)
score_frame.pack()










root.mainloop()