# from keyListener import *

# if __name__=='__main__':
#     kl=keyListener();
#     kl.onListener();


import wx
import mainForm
 
class YPiao(mainForm.MyFrame1):
    #这里开始继承后对Virtual event handlers进行override,这个示例是对关于我们的菜单选择后进行了重载。
    def m_abooutOnMenuSelection( self, event ):
        wx.MessageBox("这是一款免费软件","关于软件",wx.YES_NO|wx.ICON_QUESTION)
         
# init the programe
app = wx.App() #实例化APP，因为wxformbuilder只提供界面布局，所以需要我们自己对代码进行构架
frame = YPiao(None) #frame的实例
frame.Show()
 
app.MainLoop() #wxpython的启动函数