#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Author: Oicebot

This file published under GPLv3. 

All Weapon Data came from Weapon reroll calculator at: 
http://us.battle.net/d3/en/forum/topic/15699487088
'''

import os, sys
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title(u'武器附魔计算器 v0.12  - Build by Oicebot')
        self.master.geometry(u'391x446')
        self.master.resizable(0,0)
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('TFrame2.TLabelframe', font=(u'宋体',9))
        self.style.configure('TFrame2.TLabelframe.Label', font=(u'宋体',9))
        self.Frame2 = LabelFrame(self.top, text=u'武器白字估算值', style='TFrame2.TLabelframe')
        self.Frame2.place(relx=0.02, rely=0.377, relwidth=0.964, relheight=0.182)

        self.style.configure('TFrame1.TLabelframe', font=(u'宋体',9))
        self.style.configure('TFrame1.TLabelframe.Label', font=(u'宋体',9))
        self.Frame1 = LabelFrame(self.top, text=u'可能洗出的结果', style='TFrame1.TLabelframe')
        self.Frame1.place(relx=0.02, rely=0.592, relwidth=0.964, relheight=0.397)

        #---------------------------------------

        self.Combo2List = ['0','5','6','7',]
        self.Combo2Var = StringVar(value='0')
        self.Combo2 = Combobox(self.top, state='readonly', text='0',
                               textvariable=self.Combo2Var, values=self.Combo2List, font=(u'宋体',9))
        self.Combo2.place(relx=0.716, rely=0.305, relwidth=0.207, relheight=0.045)
        self.Combo2.bind("<<ComboboxSelected>>",self.Caculate)

        self.Combo3List = ['0','6','7','8','9','10',]
        self.Combo3Var = StringVar(value='0')
        self.Combo3 = Combobox(self.top, state='readonly', text='0',
                               textvariable=self.Combo3Var, values=self.Combo3List, font=(u'宋体',9))
        self.Combo3.place(relx=0.491, rely=0.305, relwidth=0.207, relheight=0.045)
        self.Combo3.bind("<<ComboboxSelected>>",self.Caculate)

        #self.Text6Var = StringVar(value='0')
        #self.Text6 = Entry(self.top, textvariable=self.Text6Var, font=(u'宋体',9))
        #self.Text6.place(relx=0.491, rely=0.305, relwidth=0.207, relheight=0.045)
        #self.Text6.bind('<Return>',self.Caculate)

        self.Text5Var = StringVar(value='1639')
        self.Text5 = Entry(self.top, textvariable=self.Text5Var, font=(u'宋体',9))
        self.Text5.place(relx=0.266, rely=0.305, relwidth=0.207, relheight=0.045)
        self.Text5.bind('<Return>',self.Caculate)

        self.Text4Var = StringVar(value='1385')
        self.Text4 = Entry(self.top, textvariable=self.Text4Var, font=(u'宋体',9))
        self.Text4.place(relx=0.02, rely=0.305, relwidth=0.228, relheight=0.045)
        self.Text4.bind('<Return>',self.Caculate)

        self.Combo1List = [u'单手钉锤',u'武杖',u'双手钉锤',u'双手斧',u'双手剑',
                           u'拳套武器',u'单手连枷',u'双手连枷',u'弩枪',u'弓',
                           u'弩',u'魔杖',u'单手斧',u'单手剑',u'匕首',u'矛',
                           u'祭祀刀',u'长柄武器',u'双手法杖',u'单手重武器',u'双手重武器',]
        self.Combo1Var = StringVar(value=u'单手钉锤')
        self.Combo1 = Combobox(self.top, state='readonly', text=u'单手钉锤',
                               textvariable=self.Combo1Var, values=self.Combo1List, font=(u'宋体',9))
        self.Combo1.place(relx=0.02, rely=0.126, relwidth=0.228, relheight=0.045)
        self.Combo1.bind("<<ComboboxSelected>>",self.UpdateInfo)

        self.Check1Var = IntVar(value=0)
        self.style.configure('TCheck1.TCheckbutton', font=(u'宋体',9))
        self.Check1 = Checkbutton(self.top, text=u'我这是远古的', variable=self.Check1Var,
                                  style='TCheck1.TCheckbutton',  command=self.UpdateInfo)
        self.Check1.place(relx=0.716, rely=0.062, relwidth=0.248, relheight=0.056,)

        #-----------------------------------

        self.style.configure('TLabel3.TLabel', anchor='w', foreground='#B4B4B4', font=(u'宋体',9))
        self.Label3 = Label(self.top, text=u'Data From:/u/might_be_a_terrorist', style='TLabel3.TLabel')
        self.Label3.place(relx=0.432, rely=0.018, relwidth=0.553, relheight=0.038)

        self.style.configure('TTLabel.TLabel', anchor='w', font=(u'宋体',9))
        self.TLabel = Label(self.top, text=u'武器攻速词缀', style='TTLabel.TLabel')
        self.TLabel.place(relx=0.716, rely=0.251, relwidth=0.2, relheight=0.038)

        self.style.configure('TTLabel.TLabel', anchor='w', font=(u'宋体',9))
        self.TLabel = Label(self.top, text=u'增伤（ed）% ', style='TTLabel.TLabel')
        self.TLabel.place(relx=0.491, rely=0.251, relwidth=0.2, relheight=0.038)

        self.style.configure('TTLabel.TLabel', anchor='w', font=(u'宋体',9))
        self.TLabel = Label(self.top, text=u'最高', style='TTLabel.TLabel')
        self.TLabel.place(relx=0.266, rely=0.251, relwidth=0.1, relheight=0.038)

        self.style.configure('TTLabel.TLabel', anchor='w', font=(u'宋体',9))
        self.TLabel = Label(self.top, text=u'最低', style='TTLabel.TLabel')
        self.TLabel.place(relx=0.02, rely=0.251, relwidth=0.1, relheight=0.038)

        self.style.configure('TLabel1.TLabel', anchor='w', font=(u'宋体',9))
        self.Label1 = Label(self.top, text=u'第二步，输入武器元素伤害、ED、攻速词缀等，按回车生效', style='TLabel1.TLabel')
        self.Label1.place(relx=0.02, rely=0.197, relwidth=0.95, relheight=0.038)

        self.style.configure('TTLabel.TLabel', anchor='w', font=(u'宋体',9))
        self.TLabel = Label(self.top, text=u'武器基础攻速', style='TTLabel.TLabel')
        self.TLabel.place(relx=0.491, rely=0.072, relwidth=0.2, relheight=0.038)

        self.style.configure('TLabel1.TLabel', anchor='w', font=(u'宋体',9))
        self.Label1 = Label(self.top, text=u'第一步，选择武器类型：', style='TLabel1.TLabel')
        self.Label1.place(relx=0.02, rely=0.018, relwidth=0.338, relheight=0.038)

        self.style.configure('TTLabel.TLabel', anchor='w', font=(u'宋体',9))
        self.TLabel = Label(self.top, text=u'平均基础伤害', style='TTLabel.TLabel')
        self.TLabel.place(relx=0.266, rely=0.072, relwidth=0.2, relheight=0.038)

        self.style.configure('TTLabel.TLabel', anchor='w', font=(u'宋体',9))
        self.TLabel = Label(self.top, text=u'武器类型', style='TTLabel.TLabel')
        self.TLabel.place(relx=0.02, rely=0.072, relwidth=0.15, relheight=0.038)

        #----------------------- LabelDMG LabelSPD Label5

        self.LabelDMG_Var = StringVar(value='450.5')
        self.style.configure('TLabelDMG.TLabel', )
        self.LabelDMG = Label(self.top, textvariable=self.LabelDMG_Var, style='TLabelDMG.TLabel')
        self.LabelDMG.place(relx=0.266, rely=0.126, relwidth=0.207, relheight=0.04)

        self.LabelSPD_Var = StringVar(value='1.20')
        self.style.configure('LabelSPD.TLabel', )
        self.LabelSPD = Label(self.top, textvariable=self.LabelSPD_Var, style='LabelSPD.TLabel')
        self.LabelSPD.place(relx=0.491, rely=0.126, relwidth=0.207, relheight=0.04)

        self.Label5_Var = StringVar(value='1344.5')
        self.style.configure('TLabel5.TLabel', )
        self.Label5 = Label(self.top, textvariable=self.Label5_Var, style='TLabel5.TLabel')
        self.Label5.place(relx=0.716, rely=0.126, relwidth=0.207, relheight=0.04)

        #-----------------------Label_DMG_result Label_Reroll_Result1-3

        self.Label_DMG_result_Var = StringVar(value='0')
        self.style.configure('TLabel_DMG_result.TLabel', anchor='center', font=(u'微软雅黑',26))
        self.Label_DMG_result = Label(self.Frame2, textvariable=self.Label_DMG_result_Var, style='TLabel_DMG_result.TLabel')
        self.Label_DMG_result.place(relx=0.021, rely=0.198, relwidth=0.936, relheight=0.704)

        self.Label_Reroll_Result3_Var = StringVar(value='0')
        self.style.configure('TLabel_Reroll_Result.TLabel', anchor='center', font=(u'微软雅黑',26))
        self.Label_Reroll_Result3 = Label(self.Frame1, textvariable=self.Label_Reroll_Result3_Var, style='TLabel_Reroll_Result.TLabel')
        self.Label_Reroll_Result3.place(relx=0.276, rely=0.633, relwidth=0.707, relheight=0.277)

        self.Label_Reroll_Result2_Var = StringVar(value='0')
        self.style.configure('TLabel_Reroll_Result.TLabel', anchor='center', font=(u'微软雅黑',26))
        self.Label_Reroll_Result2 = Label(self.Frame1, textvariable=self.Label_Reroll_Result2_Var, style='TLabel_Reroll_Result.TLabel')
        self.Label_Reroll_Result2.place(relx=0.276, rely=0.362, relwidth=0.707, relheight=0.277)

        self.Label_Reroll_Result1_Var = StringVar(value='0')
        self.style.configure('TLabel_Reroll_Result.TLabel', anchor='center', font=(u'微软雅黑',26))
        self.Label_Reroll_Result1 = Label(self.Frame1, textvariable=self.Label_Reroll_Result1_Var, style='TLabel_Reroll_Result.TLabel')
        self.Label_Reroll_Result1.place(relx=0.276, rely=0.09, relwidth=0.707, relheight=0.277)

        #-----------------------

        self.style.configure('TLabel2.TLabel', anchor='e', font=(u'宋体',9))
        self.Label2 = Label(self.Frame1, text=u'洗出7速时', style='TLabel2.TLabel')
        self.Label2.place(relx=0.085, rely=0.723, relwidth=0.25, relheight=0.186)

        self.style.configure('TLabel2.TLabel', anchor='e', font=(u'宋体',9))
        self.Label2 = Label(self.Frame1, text=u'洗出10ed时', style='TLabel2.TLabel')
        self.Label2.place(relx=0.085, rely=0.452, relwidth=0.25, relheight=0.186)

        self.style.configure('TLabel2.TLabel', anchor='e', font=(u'宋体',9))
        self.Label2 = Label(self.Frame1, text=u'白字洗到满时', style='TLabel2.TLabel')
        self.Label2.place(relx=0.085, rely=0.181, relwidth=0.25, relheight=0.186)

class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        #Entire Weapon Caculate Info
        self.WeaponTable = { u'单手钉锤': [1.20, 450.5,  1344.5, 1750],
                             u'武杖':    [1.15, 1419.5, 1613.5, 2098],
                             u'双手钉锤': [1,    1824.5, 1613.5, 2098],
                             u'双手斧':  [1.1,   1534.5, 1613.5, 2098],
                             u'双手剑':  [1.15,  1419.5, 1613.5, 2098],
                             u'拳套武器':[1.4,      280, 1344.5, 1750],
                             u'单手连枷':[1.4,    273.5, 1344.5, 1750],
                             u'双手连枷':[1.15,  1418.5, 1613.5, 2098],
                             u'弩枪':   [1.6,      420, 1176.5, 1750],
                             u'弓':     [1.4,     479, 1344.5, 1750],
                             u'弩':     [1.1,     862, 1344.5, 1750],
                             u'魔杖':   [1.4,      275, 1344.5, 1750],
                             u'单手斧':  [1.3,     355, 1344.5, 1750],
                             u'单手剑':  [1.4,     280, 1344.5, 1750],
                             u'匕首':   [1.5,      214, 1344.5, 1533],
                             u'矛':     [1.2,    439.5, 1344.5, 1750],
                             u'祭祀刀':  [1.4,      293, 1344.5, 1750],
                             u'长柄武器':[1.05,    1660, 1613.5, 2098],
                             u'双手法杖':[1.1,     1534, 1613.5, 2098],
                             u'双手重武器':[1.1,    1535.5, 1613.5, 2098],
                             u'单手重武器':[1.3,    355, 1344.5, 1750],
                }


    def UpdateInfo(self, event=None):
        WeaponInfo   = self.WeaponTable[self.Combo1Var.get()]
        W_BaseDMG    = WeaponInfo[1]
        W_BaseSPD    = WeaponInfo[0]
        IsAncient    = self.Check1Var.get() # Default 0 = unchecked
        if IsAncient:
            W_Max_Bonus = WeaponInfo[-1]
        else:
            W_Max_Bonus = WeaponInfo[-2]

        self.LabelDMG_Var.set('%.2f' % W_BaseDMG)
        self.LabelSPD_Var.set('%.2f' % W_BaseSPD)
        self.Label5_Var.set('%.2f' % W_Max_Bonus)

        self.Caculate()

    def Caculate(self, event=None):
        W_BaseDMG   = float(self.LabelDMG.cget("text"))
        W_BaseSPD   = float(self.LabelSPD.cget("text"))
        W_Low_DMG   = float(self.Text4Var.get())
        W_Hig_DMG   = float(self.Text5Var.get())
        W_ED        = float(self.Combo3Var.get())
        W_SPD       = float(self.Combo2Var.get())
        W_Max_Bonus = float(self.Label5.cget("text"))

        WeaponDMG = W_BaseSPD * (W_BaseDMG + (W_Low_DMG + W_Hig_DMG) / 2) * (1 + W_ED / 100) * (1 + W_SPD / 100)
        self.Label_DMG_result_Var.set('%.1f' % WeaponDMG)

        Result1 = (W_Max_Bonus + W_BaseDMG) * W_BaseSPD * (1 + W_ED / 100) * (1 + W_SPD / 100)
        Result2 = W_BaseSPD * (W_BaseDMG + (W_Low_DMG + W_Hig_DMG) / 2) * 1.1 * (1 + W_SPD / 100)
        Result3 = W_BaseSPD * (W_BaseDMG + (W_Low_DMG + W_Hig_DMG) / 2) * (1 + W_ED / 100) * 1.07

        self.Label_Reroll_Result1_Var.set('%.1f' % Result1)
        self.Label_Reroll_Result2_Var.set('%.1f' % Result2)
        self.Label_Reroll_Result3_Var.set('%.1f' % Result3)


if __name__ == "__main__":

    #print WeaponTable[u'双手剑'][3]

    top = Tk()
    Application(top).mainloop()

