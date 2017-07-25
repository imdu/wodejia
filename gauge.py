from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import os
import fnmatch
def sosuo():
    str1 = ent1.get()
    str2 = ent2.get()
    if not (str1 and str2):
        tkinter.messagebox.showinfo('提示', "请输入关键字和文件类型")
        return
    fn = tkinter.filedialog.askdirectory()
    if not fn:
        return
    listbox.delete(0,END)
    fnlist = os.walk(fn)
    for root,dirs,files in fnlist:
        for i in fnmatch.filter(files,str2):
            f = open (root + "/" + i).read()
            if str1 in f:
                listbox.insert(END,root + "/" + i)




root = Tk()#主窗口名字
root.title("文件搜索")
root.resizable(False,False)



root.geometry("550x200+600+200")
Label(root,text="搜索词").grid()#grid网格布局
ent1 = Entry()
ent1.grid(row=0,column=1)
Label(root,text="文件类型").grid(row=0,column=2)
ent2 = Entry()
ent2.grid(row=0,column=3)
btn =Button(root,text="选择文件",command=sosuo)
#btn['fg']='red'#按钮背景色
btn.grid(row=0,column=4)
listbox = Listbox(root,width=78)#box宽度
listbox.grid(row=1,column=0,columnspan=5)#colunnspan纵向对其

#
root.mainloop()