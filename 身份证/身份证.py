from tkinter import *
import datetime,time
class ID:
    def __init__(self):
        #布局
        self.frame=Tk()
        self.frame.title('身份证验证')
        self.frame.geometry('700x480+550+250')
        self.frame['bg']='lightblue'


        #图片
        self.image=PhotoImage(file='QQ截图20191015174539.png')
        self.Label_image=Label(self.frame,image=self.image)
        self.Label_image.place(x=10,y=60)
        #请输入身份证
        self.Label_shenfen=Label(self.frame,text='请输入身份证号码：',font=('微软雅黑',15,'bold'),bg='navy',fg='lightblue')
        self.Label_shenfen.place(x=300,y=20)
        #身份证输入框
        self.Enery=Entry(self.frame,font=('微软雅黑',14,'bold'))
        self.Enery.place(x=300,y=60,width=250,height=30)
        #校验按钮
        self.button=Button(self.frame,text='校验',fg='navy',font=('微软雅黑',14,'bold'),command=self.jiaoyan)
        self.button.place(x=590,y=61,width=80,height=30)
        #是否有效文字
        self.Label_shifou=Label(self.frame,text='是否有效:',font=('微软雅黑',14,'bold'),bg='lightblue',fg='navy')
        self.Label_shifou.place(x=300,y=140)

        #是否有效文本框和显示
        self.result=StringVar()
        self.result.set('')
        self.Enery_shifou=Entry(self.frame,state=DISABLED,textvariable=self.result,font=('微软雅黑',14,'bold'))
        self.Enery_shifou.place(x=400,y=140,width=120,height=30)
        #性别
        self.Label_sex=Label(self.frame,text=('性别：'),font=('微软雅黑',14,'bold'),bg='lightblue',fg='navy')
        self.Label_sex.place(x=335,y=200,)
        #性别文本框和显示
        self.result1=StringVar()
        self.result.set('')
        self.Enery_sex=Entry(self.frame,state=DISABLED,textvariable=self.result1,font=('微软雅黑',14,'bold'))
        self.Enery_sex.place(x=400,y=200,width=120,height=30)
        #出生日期
        self.Label_birthday=Label(self.frame,text='出生日期：',font=('微软雅黑',14,'bold'),bg='lightblue',fg='navy')
        self.Label_birthday.place(x=297,y=260)
        #出生日期显示和文本框
        self.result2=StringVar()
        self.result2.set('')
        self.Enery_birthday=Entry(self.frame,state=DISABLED,textvariable=self.result2,font=('微软雅黑',14,'bold'))
        self.Enery_birthday.place(x=400,y=260,width=200,height=30)

        #所在地
        self.Label_dizhi=Label(self.frame,text='所在地：',font=('微软雅黑',14,'bold'),bg='lightblue',fg='navy')
        self.Label_dizhi.place(x=315,y=320)
        #所在地显示和文本框
        self.result3 = StringVar()
        self.result3.set('')
        self.Enery_dizhi=Entry(self.frame,state=DISABLED,textvariable=self.result3,font=('微软雅黑',14,'bold'))
        self.Enery_dizhi.place(x=400,y=320,width=200,height=30)
        #关闭按钮
        self.button1=Button(self.frame,text='关闭',font=('微软雅黑',14,'bold'),fg='navy',command=self.guanbi)
        self.button1.place(x=550,y=400,width=80,height=30)


    #校验函数
    def jiaoyan(self):
        list=['1','2','3','4','5','6','7','8','9','0','x']
        list1 = ['1', '3', '5', '7', '9']
        list2 = ['2', '4', '6', '8']
        num = self.Enery.get()

        for i in num:
            #是否有效
            if i in list and len(num)==18:
                self.result.set('有效')
            else:
                self.result.set('无效')
            #判断男女
            if num[-2] in list1 and len(num) == 18:
                self.result1.set('男')
            elif num[-2] in list2 and len(num) == 18:
                self.result1.set('女')
            else:
                self.result1.set('无效')
            #判断出生年月
            birthday = num[6:14]
            year = birthday[0:4]
            month = birthday[4:6]
            day = birthday[6:8]
            if len(num) == 18:
                self.result2.set(year + '-' + month + '-' + day)
            else:
                self.result2.set('无效')

            #身份证所在地
            f = open(file="身份证归属地.txt", mode='r', encoding="utf-8")
            area = f.readlines()
            res_area=''
            if len(num)==18:
                for item in area:
                    if num[:6] == item[:6]:
                        res_area = item[6:-1]
                    if res_area=='':
                        self.result3.set('')
                    else:
                        self.result3.set(res_area)
            else:
                self.result3.set('无效')


    #关闭功能
    def guanbi(self):
        self.frame.destroy()
    #显示功能
    def show(self):
        self.frame.mainloop()


    # def tanchuanry('150x100+840+440')
    #     #     self.xx.Lable=Label(self.xx,text='请输入有效号码')
    #     #     self.xx.Lable.place(x=30,y=35)
    #     #     self.xx.mainloop()g(self):
    #     self.xx=Tk()
    #     self.xx.title('我只是一个窗口')
    #     self.xx.geomet
a=ID()

a.show()
