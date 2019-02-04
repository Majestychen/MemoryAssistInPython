# -*- coding:utf-8 -*-

from src.Conf.config import *
from src.MissionSystem import missionSystem
from src.View.MainFrame.TabFrame.FirstTabFrame import messageFrame


class AddWindow():
    def __init__(self):
        self.missionSystemTools = missionSystem.MissionSystem()
        self.addWindow = None
        pass

    def window(self):
        self.addWindow = tkinter.Toplevel()
        self.addWindow.title('添加任务')
        self.addWindow.iconbitmap('../images/icon.ico')
        screenWidth = self.addWindow.winfo_screenwidth()
        screenHeight = self.addWindow.winfo_screenheight()
        self.addWindow.geometry(
            '300x230+' + str(int((screenWidth - 300) / 2)) + '+' + str(int((screenHeight - 230) / 2)))
        self.addWindow.resizable(width=False, height=False)

        nameLabel = tkinter.Label(self.addWindow, text='书名', font=('Arial', 12), width=15, height=2)
        nameLabel.place(x=-30, y=50, anchor='nw')

        nameEntry = tkinter.Entry(self.addWindow, font=('Arial', 12), width=15, bd=5, relief='flat')
        nameEntry.place(x=80, y=55, anchor='nw')

        missionRangeLabel = tkinter.Label(self.addWindow, text='任务范围', font=('Arial', 12), width=15, height=2)
        missionRangeLabel.place(x=-30, y=100, anchor='nw')

        missionRangeEntry = tkinter.Entry(self.addWindow, font=('Arial', 12), width=15, bd=5, relief='flat')
        missionRangeEntry.place(x=80, y=105, anchor='nw')

        def addMission():
            """
            确认添加按钮的事件
            :return:
            """
            bookName = nameEntry.get()
            missionRange = missionRangeEntry.get()
            self.missionSystemTools.addMission(bookName=bookName, missionRange=missionRange)
            self.addWindow.after(300, self.addWindow.destroy)
            messageFrame.MessageFrame().updataData()
            if DEBUG and VIEW_DEBUG:
                print('{USR}{MESSAGE_FRAME} now user click add mission button and system save it')
            pass

        addButton = tkinter.Button(self.addWindow, text='确认添加', command=addMission)
        addButton.place(x=200, y=155, anchor='nw')
        pass