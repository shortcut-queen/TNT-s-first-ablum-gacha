import tkinter as tk
import random
root=tk.Tk()
width = 400
height = 300
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
root.geometry(alignstr)
root.resizable(width=False,height=False)
def tnt():
    l1=['风年','风盆','晚风','爱风','西风','风影','年盆','晚年','爱年','戏年','年影','碗盆','爱盆','洗盆','盆影','碗爱','文严文','晚樱','戏爱','爱影','戏影']
    len_l1=len(l1)-1
    res1 = random.sample(range(0,len_l1 ),6)
    res2  = random.randint(0,len_l1)
    ll1=[]
    for i in res1:
        #print(l1[i])
        ll1.append(l1[i])
    ll1.append(l1[res2])
    w=tk.Label(root,text=ll1)
    w.pack()


b1=tk.Button(root,text='我命由天不由我',activebackground='#ff5456',width=15,height=5,command=lambda :tnt())
b1.pack()
root.title('下辈子再买团专')
root.mainloop()