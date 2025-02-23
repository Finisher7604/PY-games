from tkinter import *
import random
import time

counter_1=0
counter_2=0

tk=Tk()
tk.title("Pong!")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.config(bg="black")
canvas.pack()
tk.update()


canvas.create_line(250,0,250,400,fill="white")

class Ball:
    def __init__(self,canvas,color,paddle1,paddle2):
        self.canvas=canvas
        self.paddle1=paddle1
        self.paddle2=paddle2
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,234,200)
        starts=[3,-3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=-3
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()

    def hit_paddle1(self,pos):
        paddle_pos=self.canvas.coords(self.paddle1.id)   
        if pos[1]>=paddle_pos[1] and pos[1]<=paddle_pos[3]:
            if pos[0]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
                return True
            return False


    def hit_paddle2(self,pos):
        paddle_pos=self.canvas.coords(self.paddle2.id)   #[x1,y1,x2,y2]
        if pos[1]>=paddle_pos[1] and pos[1]<=paddle_pos[3]:
            if pos[2]>=paddle_pos[0] and pos[2]<=paddle_pos[2]:
                return True
            return False

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:   
            self.y=3
        if pos[3]>=self.canvas_height:
            self.y=-3
        if pos[0]<=0:
            self.x=3
            self.score(True)
        if pos[2]>=self.canvas_width:
            self.x=-3
            self.score(False)
        if self.hit_paddle1(pos)==True:
            self.x=3
        if self.hit_paddle2(pos)==True:
            self.x=-3

    def score(self,val):
        global counter_1
        global counter_2

        if val==True:
            a=self.canvas.create_text(125,40,text=counter_1,font=('Arial',60),fill='white')
            canvas.itemconfig(a,fill='black')
            counter_1 +=1
            a=self.canvas.create_text(125,40,text=counter_1,font=('Arial',60),fill='white')

        if val==False:
            a=self.canvas.create_text(375,40,text=counter_2,font=('Arial',60),fill='white')
            canvas.itemconfig(a,fill='black')
            counter_2 +=1
            a=self.canvas.create_text(375,40,text=counter_2,font=('Arial',60),fill='white')
            



class Paddle1:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,150,30,250,fill=color)
        self.y=0
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all('a',self.go_up)
        self.canvas.bind_all('d',self.go_down)

    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=0
        if pos[3]>=400:
            self.y=0

    def go_up(self,event):
        self.y=-3

    def go_down(self,event):
        self.y=3

            
            
class Paddle2:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(470,150,500,250,fill=color)
        self.y=0
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.go_up)
        self.canvas.bind_all('<KeyPress-Right>',self.go_down)

    
    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=0
        if pos[3]>=400:
            self.y=0

    def go_up(self,event):
        self.y=-3

    def go_down(self,event):
        self.y=3
        
    
paddle1=Paddle1(canvas,"blue")
paddle2=Paddle2(canvas,"blue")
ball=Ball(canvas,"orange",paddle1,paddle2)


while 1:
    ball.draw()
    paddle1.draw()
    paddle2.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    if counter1==10:
        ball.x=0
        ball.y=0
        paddle1.y=0
        paddle2.y=0
        canvas.create_text(250,200,text="Player 1 won",font=32,fill='red')
        canvas.create_text(250,215,text="Score:" + str(counter1) + "-" str(counter2),font=32,fill='red')
    if counter1==10:
        ball.x=0
        ball.y=0
        paddle1.y=0
        paddle2.y=0
        canvas.create_text(250,200,text="Player 2 won",font=32,fill='red')
        canvas.create_text(250,215,text="Score:"+str(counter1)+" -" str(counter2),font=32,fill='red')
    

