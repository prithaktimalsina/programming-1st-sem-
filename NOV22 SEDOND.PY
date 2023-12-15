import math
from tkinter import*

width, height = 640, 480
max_speed = 5
time = velocity = speed = 0
jump_released = True
left_engaged = right_engaged = False


platforms = []
pf_data = [[150, 250, 250, 600, 'Green'],
         [100, 325, 500, 600]]

p_start = [320, 300, 340, 320]
player_y = p_start[3] - 10


root = Tk()
root.geometry(f'{width}x{height}')
root.title ("Platformer by Rhodes")

canvas = Canvas(root)
canvas.configure(bg='Blue')
canvas.pack(fill=BOTH, expand=True)


def create_platforms():
    for ds in pf_data:
        platforms.append(canvas.create_rectangle(ds[1], ds[2], ds[3], fill=ds[4]))
        
def get_coord_pairs(cid):
    return{'x1': canvas.coords(cid)[0],          'y1': canvas.coords(cid)[1],
           'x2': canvas.coords(cid)[2],          'y2': canvas.coords(cid)[3]}               
        
def check_grounded():
    p =get_coord_pairs(player)
    for platform in platforms:
        pf = get_coord_pairs(platform)
        if p['x2'] > pf['x1'] and p['x1'] < pf['x2']:            
            if p['y1'] < pf['y1'] < p['y2']:
                return pf['y1']   
            
            
def jump():
    global velocity
    velocity = 45 + math.fabs(speed)
    
    
def key_press(event):
    global jump_released, left_engaged, right_engaged
    if event.keycode == 32 and jump_released:
        jump()
        jump_released = False
    elif event.keycode == 37:
        left_engaged = True
    elif event.keycode == 39:
        right_engaged = True
        
        
        
def key_release(event):
    global jump_released, left_engaged, right_engaged
    if event.keycode == 32 and jump_released:
        jump()
        jump_released = True
        
        
def action():
    global player_y, time, velocity, speed,left_engaged, right_engaged, platforms, player
    
    time += .1
    y = velocity * math.sin(math.pi / 2) * time - .5 * -9.8 * time**2
    canvas.coords(player, p_start[0], player_y + y - 10, p_start[2], player_y + y + 10)
    
    
    #vertex
    ascent_time = velocity * math.sin(math.pi / 2) / 9.8
    
    if time > ascent_time and check_grounded():
        player_y = check_grounded() - 10
        time = 0
        velocity = 0
        
    if left_engaged and speed < max_speed
        speed += 0.25
    elif right_engaged and math.fabs(speed) < max_speed:
        speed -= 0.25
    else:
        if speed > 0:
            speed -= .25
        elif speed < 0:
            speed += .25
    for platform in platforms:
        canvas.move(platform, speed, 0)
        
        root.after(10, action)
        
                 
create_platforms()
player = canvas.create_rectangle(p_start[0], p_start[1], p_start[2], p_start[3], fill='Red')


root.blind("<KeyPress>", key_press)
root.bind("KeyRelease>", key_release)
action()


root.mainloop()

def check_complete():
    p = get_coord_pairs(player)
    for platform in platforms:
        if canvas.itemcget(platform, 'fill') == 'Black':
            pf = get_coord_pairs(platform)
            if p['x2'] < pf['x1'] or p['x1'] > pf['x2'] or p['y2'] < pf['y1'] or p['y1'] > pf['y2']:
                return False
            else:
                canvas.delete("all")
                canvas.configure(bg='Black')
                message = "Thank you, but our princess is in another castle!"
                canvas.create_text(320, 220, text=message, fill="White", font='Arial 18 bold')
                canvas.pack()
                return True