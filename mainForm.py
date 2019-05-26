# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from myButtonObj import *
from keyListener import *
import threading
###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 780,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"黑人", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer5.Add( self.m_staticText1, 0, wx.ALL, 5 )

		blackManChoices = [ u"1", u"2", u"3", u"4", u"left", u"right" ]
		self.blackMan = wx.ComboBox( self, wx.ID_ANY, u"left", wx.DefaultPosition, wx.Size( 80,-1 ), blackManChoices, wx.CB_READONLY )
		self.blackMan.SetSelection( 0 )
		bSizer5.Add( self.blackMan, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"陨石", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer5.Add( self.m_staticText2, 0, wx.ALL, 5 )

		meteoriteChoices = [ u"1", u"2", u"3", u"4", u"left", u"right" ]
		self.meteorite = wx.ComboBox( self, wx.ID_ANY, u"left", wx.DefaultPosition, wx.Size( 80,-1 ), meteoriteChoices, wx.CB_READONLY )
		self.meteorite.SetSelection( 1 )
		bSizer5.Add( self.meteorite, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"原力波", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer5.Add( self.m_staticText3, 0, wx.ALL, 5 )

		yuanliboChoices = [ u"1", u"2", u"3", u"4", u"left", u"right" ]
		self.yuanlibo = wx.ComboBox( self, wx.ID_ANY, u"left", wx.DefaultPosition, wx.Size( 80,-1 ), yuanliboChoices, wx.CB_READONLY )
		self.yuanlibo.SetSelection( 2 )
		bSizer5.Add( self.yuanlibo, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"黑洞", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer5.Add( self.m_staticText4, 0, wx.ALL, 5 )

		blackHoleChoices = [ u"1", u"2", u"3", u"4", u"left", u"right" ]
		self.blackHole = wx.ComboBox( self, wx.ID_ANY, u"left", wx.DefaultPosition, wx.Size( 80,-1 ), blackHoleChoices, wx.CB_READONLY )
		self.blackHole.SetSelection( 3 )
		bSizer5.Add( self.blackHole, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"电刑", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer5.Add( self.m_staticText5, 0, wx.ALL, 5 )

		dianxingChoices = [ u"1", u"2", u"3", u"4", u"left", u"right" ]
		self.dianxing = wx.ComboBox( self, wx.ID_ANY, u"left", wx.DefaultPosition, wx.Size( 80,-1 ), dianxingChoices, wx.CB_READONLY )
		self.dianxing.SetSelection( 4 )
		bSizer5.Add( self.dianxing, 0, wx.ALL, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"引导", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		bSizer5.Add( self.m_staticText51, 0, wx.ALL, 5 )

		yindaoChoices = [ u"1", u"2", u"3", u"4", u"left", u"right", wx.EmptyString ]
		self.yindao = wx.ComboBox( self, wx.ID_ANY, u"left", wx.DefaultPosition, wx.Size( 80,-1 ), yindaoChoices, wx.CB_READONLY )
		self.yindao.SetSelection( 5 )
		bSizer5.Add( self.yindao, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.modeFlag = wx.CheckBox( self, wx.ID_ANY, u"棒棒糖", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.modeFlag.SetValue(True)
		bSizer10.Add( self.modeFlag, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer10, 1, wx.EXPAND, 5 )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"启动", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button1, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer11, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.beginClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def beginClick( self, event ):
		event.Skip()
		btn=myButtonObj(self.blackMan.Value,self.meteorite.Value,self.yuanlibo.Value,self.blackHole.Value,self.dianxing.Value,self.yindao.Value,self.modeFlag.Value)
		kl=keyListener(btn)
		t = threading.Thread(target=kl.onListener(), args=())
		t.start()