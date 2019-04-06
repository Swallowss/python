
from pynput.mouse import Button, Controller

class myButtonObj:
    def __init__(self,blackMan,meteorite,yuanlibo,blackHole,dianxing,yindao,modeFlag):
        self.blackMan=self.mouseClickChange(blackMan)
        self.meteorite=self.mouseClickChange(meteorite)
        self.yuanlibo=self.mouseClickChange(yuanlibo)
        self.blackHole=self.mouseClickChange(blackHole)
        self.dianxing=self.mouseClickChange(dianxing)
        self.yindao=self.mouseClickChange(yindao)
        self.modeFlag=self.mouseClickChange(modeFlag)

    def mouseClickChange(self,str):
        if str=='left':
            return Button.left
        
        if str=='right':
            return Button.right
        return str