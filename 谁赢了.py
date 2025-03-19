import tkinter as tk
import random
root = tk.Tk()

dice_list = []
for i in range(1,7):
    dice_list.append(tk.PhotoImage(file=f'./png/{i}.png'))
print(dice_list)


class Window:
    def __init__(self,root):
        self.root = root
        self.root.title('谁输了')
        self.root.geometry('400x300')
        self.create_widget()
        self.count = 0


    def create_widget(self):
        self.lb1 = tk.Label(self.root,image=random.choice(dice_list))
        self.lb1.grid(row=0,column=0,padx=20,pady=20)
        self.lb2 = tk.Label(self.root,image=random.choice(dice_list))
        self.lb2.grid (row=0,column=2,padx=20,pady=20)
        self.lb3 = tk.Label(self.root,text='比赛开始!')
        self.lb3.grid(row=1,column=1,padx=20,pady=20)

        b1 = tk.Button(self.root,text='roll', command=self.roll1)
        b1.grid(row=2,column=0)
        b2 =tk.Button(self.root,text='roll', command=self.roll2)
        b2.grid(row=2,column=2)
        b3 =tk.Button(self.root,text='谁赢了', command=self.compare)
        b3.grid(row=3,column=1)


    def roll1(self):
        self.count += 1
        self.p1 = random.randint(0,5)
        self.lb1.config(image=dice_list[self.p1])
        if self.count<=15:
            self.root.after(100,self.roll1)
        else:
            self.couut = 0

    def roll2(self):
        self.count += 1
        self.p2 = random.randint(0,5)
        self.lb2.config(image=dice_list[self.p2])
        if self.count<=15:
            self.root.after(100,self.roll2)
        else:
            self.couut = 0

    def compare(self):
        if self.p1 > self.p2:
            self.lb3.config(text='左边赢了')
        elif self.p1 < self.p2:
            self.lb3.config(text='右边赢了')
        else:
            self.lb3.config(text='都输了!')


Window(root)
root.mainloop()
            
        



    
