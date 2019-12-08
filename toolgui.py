#coding:utf-8
#python 3.4
__AUTHOR__ = '王勇'
version = 0.1

from tkinter import *

class ToolGUI:

    def __init__(self, root):
        '''
        初始化数据
        '''
        #self.frame = Frame(root)        #tkinter模块对象与Class类承接
        #self.frame.pack()
        #self.design()
        self.me()       #GUI默认显示界面

    def design(self):
        '''
        布局text控件、文本、输入控件；text控件中添加滚条
        :return:
        '''
        GUImenu = Menu(root)

        nmon = Menu(GUImenu,tearoff=0)
        nmon.add_command(label='批量部署', command = self.bushu)
        nmon.add_command(label='批量监控', command = self.jiankong)
        nmon.add_command(label='批量下载', command = self.xiazai)
        nmon.add_separator()    #分割线
        nmon.add_command(label='批量分析', command = self.fenxi)

        data = Menu(GUImenu,tearoff=0)
        data.add_command(label='造数', command = self.fenxi)

        baowen = Menu(GUImenu,tearoff=0)
        baowen.add_command(label='8583报文分析', command = self.fenxi)

        http = Menu(GUImenu, tearoff=0)
        http.add_command(label='GET请求', command = self.fenxi)
        http.add_command(label='POST请求', command = self.fenxi)


        help = Menu(GUImenu,tearoff=0)
        help.add_command(label='关于', command = self.me)

        GUImenu.add_cascade(label='nmon工具', menu=nmon)
        GUImenu.add_cascade(label='批量造数', menu=data)
        GUImenu.add_cascade(label='报文分析', menu=baowen)
        GUImenu.add_cascade(label='HTTP请求', menu=http)
        GUImenu.add_cascade(label='帮助', menu=help)

        root.config(menu=GUImenu)

    def bushu(self):
        frame = Frame(root, width=600, height=200, bg='green')
        lb = Label(frame, text='部署模块开发中......',font=('宋体', 11),
                              bg='#FFFEEE', fg='green')
        frame.place(x=10, y=10)
        lb.place(x=20, y=40)

    def jiankong(self):
        frame = Frame(root, width=600, height=200, bg='green')
        lb = Label(frame, text='监控模块开发中......',font=('宋体', 11),
                              bg='#FFFEEE', fg='green')
        frame.place(x=10, y=10)
        lb.place(x=20, y=40)

    def xiazai(self):
        frame = Frame(root, width=600, height=200, bg='green')
        lb = Label(frame, text='下载模块开发中......',font=('宋体', 11),
                              bg='#FFFEEE', fg='green')
        frame.place(x=10, y=10)
        lb.place(x=20, y=40)

    def fenxi(self):
        frame = Frame(root, width=600, height=200, bg='green')
        lb = Label(frame, text='分析模块开发中......',font=('宋体', 11),
                              bg='#FFFEEE', fg='green')
        frame.place(x=10, y=10)
        lb.place(x=20, y=40)

    def me(self):
        frame = Frame(root, width=600, height=200, bg='green')
        lb = Label(frame, text='关于模块开发中......',font=('宋体', 11),
                              bg='#FFFEEE', fg='green')
        frame.place(x=10, y=10)
        lb.place(x=20, y=40)


if __name__ == '__main__':

    root = Tk()
    root.title('GUI')
    root.geometry('800x600+400+0')   #宽*高+左边界长度+上边界长度
    root.resizable(False, False)
    root.iconbitmap('test.ico')

    ToolGUI(root).design()
    root.mainloop()