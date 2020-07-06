from board import *
from tkinter import *
from tkinter.font import *
import colorsys
import time
import math

cell_size = 50
WIDTH = 3

timer_start = False
time_start = 0
time_end = 0

def color(fraction):
    new_color = [int(255/2 + i * 255/2) for i in colorsys.hsv_to_rgb(fraction,1,1)]
    return '#{:02x}{:02x}{:02x}'.format(new_color[0],new_color[1],new_color[2])

def create():
    global main_board, timer_start, time_start, time_end
    timer_start = False
    time_start = time.time()
    time_end = time.time()
    
    main_board = Board((int(width_v.get()), int(height_v.get())), int(position_v.get()))
    main_board.scramble()
    tick()

def tick():
    global main_board, timer_start, time_start, time_end, cell_size
    main_canvas.delete('all')
    cell_size = int(cell_v.get())
    
    for i in range(main_board.size[0]):
        for j in range(main_board.size[1]):
            main_canvas.create_rectangle(WIDTH+i*cell_size, WIDTH+j*cell_size,
                                    WIDTH+i*cell_size+cell_size, WIDTH+j*cell_size+cell_size,
                                    width=WIDTH,
                                    fill=color(main_board.board[i][j] / main_board.positions))
            main_canvas.create_text(WIDTH+i*cell_size+cell_size/2,
                                    WIDTH+j*cell_size+cell_size/2,
                                    font=FONT,
                                    text=str(int(main_board.board[i][j])))
    
    if timer_start:
        time_end = time.time()
    
    time_d = time_end - time_start
    m = math.floor(time_d/60)
    s = time_d - m*60
    
    if time_d < 60:
        time_str = "{:.3f}".format(s)
    else:
        time_str = "{}:{:06.3f}".format(m,s)
    
    time_v.set(time_str)
    
    master.after(30, tick)

def click(event):
    global main_board, timer_start, time_start, cell_size
    if not timer_start:
        timer_start = True
        time_start = time.time()
        time_end = time.time()
    
    coords = (int(event.y/cell_size),int(event.x/cell_size))
    if coords[0] < main_board.size[0] and coords[1] < main_board.size[1]:
        main_board.move(coords)
    
    if main_board.check_solved():
        timer_start = False

master = Tk()
FONT = Font(master, family='Helvetica', size=24, weight='bold')

Label(master, text="Width").grid(row=0,column=0)
width_v = StringVar()
width_e = Entry(master,textvariable=width_v)
width_e.grid(row=0,column=1)
width_v.set("3")

Label(master, text="Height").grid(row=0,column=2)
height_v = StringVar()
height_e = Entry(master,textvariable=height_v)
height_e.grid(row=0,column=3)
height_v.set("3")

Label(master, text="Positions").grid(row=0,column=4)
position_v = StringVar()
position_e = Entry(master,textvariable=position_v)
position_e.grid(row=0,column=5)
position_v.set("3")

create_b = Button(master, text="Create", command=create)
create_b.grid(row=1,column=0,columnspan=6)

main_canvas = Canvas(master, width=750, height=500)
main_canvas.grid(row=2,column=0,columnspan=6)
main_canvas.bind("<Button-1>", click)

time_v = StringVar()
time_l = Label(master, textvariable=time_v, font=FONT)
time_l.grid(row=3,column=0,columnspan=6)

Label(master, text="Cell Size").grid(row=4,column=0)
cell_v = StringVar()
cell_v.set("50")
cell_e = Entry(master,textvariable=cell_v)
cell_e.grid(row=4,column=1)

mainloop()