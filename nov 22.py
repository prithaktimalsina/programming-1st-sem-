from tkinter import*


root = Tk()
root.title('Drawing on Canvas')
canvas = Canvas(root)
canvas.configure(bg='#1E1E1E')
canvas.pack(fill=BOTH, expand=True)

canvas.create_rectangle(50, 50, 200, 100, fill= '#0000FF', outline='#FFFF00')

canvas.create_oval(50, 50, 200, 100, fill= '#00FF00', outline='#FFFF00')

canvas.create_arc(0, 0, 50, start=45 , extent=90 , fill='#FF00FF') 

canvas.create_line(7, 12, 43, 102, fill='#FF0000', width=5)

canvas.create_text(150, 160, text='Hello world!', fill='#FFFFFF', font=('Comic Sans MS', 15, 'bold'))

canvas.create_polygon([1, 10, 20, 20, 14, 50, ], fill='#00FFAA')

x1 = y2 = 0
ball_w = ball_h = 20
x_pos  = y.pos True

ball =canvas, oval(x1, y1, x1  + ball_w, y1 + ball_h, file )
ball_x = canvas.coords(ball)[0]
ball_y = canvas.cpprds(ball)[1]

x_pos = True if(x_pos and ball_x)




def animation():
    global x1, y1, ball_w, bakk_h, X_pos, Y_pos, ball
    canvas.move(ball, x1, y1)
    
    x1 = 1 if x_pos else -1
    y1 = 1 if y_pos else -1
    ball


root.mainloop()

