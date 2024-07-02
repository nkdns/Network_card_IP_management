from tkinter import *
from tkinter.ttk import *
class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_frame_lxyufdav = self.__tk_label_frame_lxyufdav(self)
        self.tk_table_lxyugkyn = self.__tk_table_lxyugkyn( self.tk_label_frame_lxyufdav) 
        self.tk_label_frame_lxyukfe7 = self.__tk_label_frame_lxyukfe7(self)
        self.tk_list_box_lxyukxkh = self.__tk_list_box_lxyukxkh( self.tk_label_frame_lxyukfe7) 
        self.tk_label_frame_lxyv0okg = self.__tk_label_frame_lxyv0okg(self)
        self.tk_label_frame_lxyv1618 = self.__tk_label_frame_lxyv1618( self.tk_label_frame_lxyv0okg) 
        self.tk_input_lxyv1hm1 = self.__tk_input_lxyv1hm1( self.tk_label_frame_lxyv1618) 
        self.tk_label_frame_lxyv16wy = self.__tk_label_frame_lxyv16wy( self.tk_label_frame_lxyv0okg) 
        self.tk_label_lxyv2g52 = self.__tk_label_lxyv2g52( self.tk_label_frame_lxyv16wy) 
        self.tk_label_frame_lxyv17zk = self.__tk_label_frame_lxyv17zk( self.tk_label_frame_lxyv0okg) 
        self.tk_input_lxyv4183 = self.__tk_input_lxyv4183( self.tk_label_frame_lxyv17zk) 
        self.tk_label_frame_lxyv7ih4 = self.__tk_label_frame_lxyv7ih4( self.tk_label_frame_lxyv0okg) 
        self.tk_input_lxyv8q02 = self.__tk_input_lxyv8q02( self.tk_label_frame_lxyv7ih4) 
        self.tk_button_lxyvak75 = self.__tk_button_lxyvak75( self.tk_label_frame_lxyv0okg) 
        self.tk_button_lxyvatz0 = self.__tk_button_lxyvatz0( self.tk_label_frame_lxyv0okg) 
        self.tk_button_lxyvcfa0 = self.__tk_button_lxyvcfa0( self.tk_label_frame_lxyv0okg) 
    def __win(self):
        self.title("网络切换器")
        # 设置窗口大小、居中
        width = 787
        height = 434
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.resizable(width=False, height=False)
        
    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def __tk_label_frame_lxyufdav(self,parent):
        frame = LabelFrame(parent,text="预置IP列表",)
        frame.place(x=10, y=10, width=538, height=242)
        return frame
    def __tk_table_lxyugkyn(self,parent):
        # 表头字段 表头宽度
        columns = {"ID":25,"IP":119,"子网掩码":119,"备注":249}
        tk_table = Treeview(parent, show="headings", columns=list(columns),)
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸
        
        tk_table.place(x=9, y=0, width=520, height=216)
        self.create_bar(parent, tk_table,True, False,9, 0, 520,216,538,242)
        return tk_table
    def __tk_label_frame_lxyukfe7(self,parent):
        frame = LabelFrame(parent,text="网卡列表",)
        frame.place(x=570, y=10, width=200, height=242)
        return frame
    def __tk_list_box_lxyukxkh(self,parent):
        lb = Listbox(parent)
        lb.place(x=8, y=1, width=183, height=216)
        self.create_bar(parent, lb, True, False,8, 1, 183,216,200,242)
        return lb
    def __tk_label_frame_lxyv0okg(self,parent):
        frame = LabelFrame(parent,text="详细信息",)
        frame.place(x=10, y=258, width=760, height=163)
        return frame
    def __tk_label_frame_lxyv1618(self,parent):
        frame = LabelFrame(parent,text="IP",)
        frame.place(x=274, y=2, width=220, height=57)
        return frame
    def __tk_input_lxyv1hm1(self,parent):
        '''
        IP Input
        '''
        ipt = Entry(parent, )
        ipt.place(x=10, y=0, width=200, height=30)
        return ipt
    def __tk_label_frame_lxyv16wy(self,parent):
        frame = LabelFrame(parent,text="当前网卡",)
        frame.place(x=15, y=2, width=220, height=57)
        return frame
    def __tk_label_lxyv2g52(self,parent):
        label = Label(parent,text="NET CARD",anchor="center", )
        label.place(x=10, y=0, width=200, height=30)
        return label
    def __tk_label_frame_lxyv17zk(self,parent):
        frame = LabelFrame(parent,text="子网掩码",)
        frame.place(x=520, y=2, width=220, height=57)
        return frame
    def __tk_input_lxyv4183(self,parent):
        '''
        子网掩码 Input
        '''
        ipt = Entry(parent, )
        ipt.place(x=10, y=0, width=200, height=30)
        return ipt
    def __tk_label_frame_lxyv7ih4(self,parent):
        frame = LabelFrame(parent,text="备注",)
        frame.place(x=15, y=64, width=479, height=65)
        return frame
    def __tk_input_lxyv8q02(self,parent):
        '''
        备注 Input
        '''
        ipt = Entry(parent, )
        ipt.place(x=10, y=0, width=459, height=37)
        return ipt
    def __tk_button_lxyvak75(self,parent):
        btn = Button(parent, text="增加", takefocus=False,)
        btn.place(x=506, y=80, width=70, height=40)
        return btn
    def __tk_button_lxyvatz0(self,parent):
        btn = Button(parent, text="删除", takefocus=False,)
        btn.place(x=590, y=80, width=70, height=40)
        return btn
    def __tk_button_lxyvcfa0(self,parent):
        btn = Button(parent, text="DHCP", takefocus=False,)
        btn.place(x=672, y=80, width=70, height=40)
        return btn
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
    def __event_bind(self):
        self.tk_table_lxyugkyn.bind('<Double-Button-1>',self.ctl.IPListDClick)
        self.tk_table_lxyugkyn.bind('<<TreeviewSelect>>',self.ctl.on_tree_select)
        self.tk_list_box_lxyukxkh.bind('<<ListboxSelect>>',self.ctl.NetWorkCard)
        self.tk_list_box_lxyukxkh.bind('<Button-3>',self.ctl.NetListRClick)
        self.tk_button_lxyvcfa0.bind('<Button-1>',self.ctl.NetForDHCP)
        self.tk_button_lxyvak75.bind('<Button-1>',self.ctl.ADDNETINFO)
        self.tk_button_lxyvatz0.bind('<Button-1>',self.ctl.DELNETINFO)
        
    def __style_config(self):
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()