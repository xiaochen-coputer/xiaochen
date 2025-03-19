import tkinter as tk


root = tk.Tk()

e1 = tk.Entry(root)
e1.grid(row=0,column=1,columnspan=2,pady=10)
e2 = tk.Entry(root)
e2.grid(row=1,column=1,columnspan=2,pady=10)


v = tk.IntVar()
r1 = tk.Radiobutton(root,text="+",variable=v,value=1)
r1.grid(row=2,column=0,pady=20)
r2 = tk.Radiobutton(root,text="-",variable=v,value=2)
r2.grid(row=2,column=1)
r3 = tk.Radiobutton(root,text="×",variable=v,value=3)
r3.grid(row=2,column=2)
r4 = tk.Radiobutton(root,text="÷",variable=v,value=4)
r4.grid(row=2,column=30,pady=20)


def cal():
    x = int(e1.get())
    y = int(e2.get())
    n = v.get()
    print(x,y,n)
    if n == 1:
        res = x + y
    elif n == 2:
        res = x - y
    elif n == 3:
        res = x * y
    elif n == 4:
        res = x / y
    l1.config(text=res)



l1 = tk.Label(root,text="结果区域")
l1.grid(row=3,column=1,columnspan=2,pady=10)
b1 = tk.Button(root,text="计算",command=cal)
b1.grid(row=4,column=1,columnspan=2,pady=10)


root.mainloop()
