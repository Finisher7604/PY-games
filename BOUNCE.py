
from tkinter import *
import random
import time
tk=Tk()

tk.title("BOUNCE!")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=500,height=500,bd=0,highlightthickness=0)
canvas.pack()
tk.update()

class Ball:
    def __init__(self,canvas,paddle,color):
        self.canvas=canvas
        self.paddle=paddle
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,250,200)
        start=[-5,-4,-3,-2,-1,0,1,2,3]
        
        self.x=start[0]
        self.y=-5  #here we used -3 so tha ball moves upward first 
        self.canvas_height=self.canvas.winfo_height()  #function winfo_height give sthe height of the canvas
        self.canvas_width=self.canvas.winfo_width()
        self.hit_bottom=False

    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)   #[x1,y1,x2,y2]
        if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
            if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                return True
            return False
        

    def draw(self):
        self.canvas.move(self.id,self.x,self.y) #(self.id,horizontal,vertical)
        pos=self.canvas.coords(self.id)    #it creates array [x1,y1,x2,y2]
        #print(pos)   #optional thing to add
        if pos[1]<=0:   #[1] is y1
            self.y=3
        if pos[3]>=self.canvas_height:   #[3] is y2
            self.hit_bottom=True
            canvas.create_text(245,100,text="GAME OVER")
        if pos[0]<=0:   #[0] is x1
            self.x=3
        if pos[2]>=self.canvas_width:   #[2] si x2
            self.x=-3
        if self.hit_paddle(pos)==True:
            self.y=-3

#the upper border of the canvas is 0 (y1 is 0) and bottom is 500 (y2 is 500)

class Paddle():
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.x=0
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Right>',self.turnright)
        self.canvas.bind_all('<KeyPress-Left>',self.turnleft)
        

    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=0
        if pos[2]>=self.canvas_width:
            self.x=0
        
    def turnleft(self,event):
        self.x=-3
    def turnright(self,event):
        self.x=3
    

paddle=Paddle(canvas,'black')        
ball=Ball(canvas,paddle,'red')



while 1:  #infinte loop
    if ball.hit_bottom==False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

    

