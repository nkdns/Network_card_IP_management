from ui import Win as MainWin
from sqlite import ql as sql3
import tkinter as tk
from tkinter import messagebox
import subprocess,psutil,socket
class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: MainWin
    sq3:sql3
    def __init__(self,sq3):
        self.treechoose_id:str = ''
        self.treechoose_ip:str = ''
        self.treechoose_netmask:str = ''
        self.Interface_Name:str = ''
        self.sq3 = sq3

    def init(self, ui):
        self.ui = ui
        self.getinfo()
        self.getnetlist()
        self.ui.tk_button_lxyvatz0.configure(state="disabled")

    def IPListDClick(self,evt):
        try:
            # 使用 wmic 命令设置 IP 地址
            subprocess.run(['netsh', 'interface', 'ip', 'set', 'address', 'name=' + self.Interface_Name,
                            'static', self.treechoose_ip, self.treechoose_netmask], check=True)
            print(f'成功将网卡 {self.Interface_Name} 的 IP 地址设置为 {self.treechoose_ip}')
            query = "UPDATE config SET LastInterface = ? WHERE id = 1"
            self.sq3.I_U_D(query,(self.Interface_Name,))
            messagebox.showinfo("配置成功", f"已设置网卡{self.Interface_Name}IPv4为{self.treechoose_ip}")
        except subprocess.CalledProcessError as e:
            print(f'设置网卡 IP 地址失败: {e}')
            messagebox.showerror("错误", f"设置网卡{self.Interface_Name}IP失败")

    def NetListRClick(self,evt):
        print("<Button-3>事件未处理:",evt)

    def on_tree_select(self,evt):
        item = self.ui.tk_table_lxyugkyn.selection()[0]
        itemvalues = self.ui.tk_table_lxyugkyn.item(item,"values")
        self.ui.tk_button_lxyvatz0.configure(state="normal")
        self.treechoose_id = itemvalues[0]
        self.treechoose_ip = itemvalues[1]
        self.treechoose_netmask = itemvalues[2]
        self.ui.tk_input_lxyv1hm1.delete(0, tk.END)
        self.ui.tk_input_lxyv1hm1.insert(0, self.treechoose_ip)
        self.ui.tk_input_lxyv4183.delete(0, tk.END)
        self.ui.tk_input_lxyv4183.insert(0, self.treechoose_netmask)
        self.ui.tk_input_lxyv8q02.delete(0, tk.END)
        self.ui.tk_input_lxyv8q02.insert(0, itemvalues[3])

    def NetForDHCP(self,evt):
        try:
            # 将网卡 IP 地址设置为自动获取(DHCP)
            subprocess.run(['netsh', 'interface', 'ip', 'set', 'address', 'name=' + self.Interface_Name, 'dhcp'], check=True)
            print(f'成功将网卡 {self.Interface_Name} 的 IP 地址设置为自动获取(DHCP)')
            query = "UPDATE config SET LastInterface = ? WHERE id = 1"
            self.sq3.I_U_D(query,(self.Interface_Name,))
            messagebox.showinfo("配置成功", f"已设置网卡{self.Interface_Name}IPv4为DHCP获取模式")
        except subprocess.CalledProcessError as e:
            print(f'设置网卡 IP 地址失败: {e}')
            messagebox.showerror("错误", f"设置网卡{self.Interface_Name}为DHCP模式失败")

    def NetWorkCard(self,evt=None):
        index = self.ui.tk_list_box_lxyukxkh.curselection()[0]
        itemvalues = self.ui.tk_list_box_lxyukxkh.get(index)
        self.Interface_Name = itemvalues
        self.ui.tk_label_lxyv2g52.config(text=self.Interface_Name)
        for nic, addrs in psutil.net_if_addrs().items():
            if nic == itemvalues:
                for addr in addrs:
                    if addr.family == socket.AF_INET:
                        self.ui.tk_input_lxyv1hm1.delete(0, tk.END)
                        self.ui.tk_input_lxyv1hm1.insert(0, addr.address)
                        self.ui.tk_input_lxyv4183.delete(0, tk.END)
                        self.ui.tk_input_lxyv4183.insert(0, addr.netmask)
                        self.ui.tk_input_lxyv8q02.delete(0, tk.END)
                        query = 'SELECT * FROM IPinfo WHERE IP = ? AND NetMask = ?'
                        res=self.sq3.select(query,(addr.address,addr.netmask))
                        if res:
                            self.ui.tk_input_lxyv8q02.insert(0, res[0][3])
                        self.ui.title(f'网络切换器-当前网卡[{itemvalues}]-ip[{addr.address}]-子网[{addr.netmask}]')

    def ADDNETINFO(self,evt):
        ip = self.ui.tk_input_lxyv1hm1.get()
        netmaske = self.ui.tk_input_lxyv4183.get()
        remarks = self.ui.tk_input_lxyv8q02.get()
        query = 'SELECT * FROM IPinfo WHERE IP = ? AND NetMask = ?'
        res=self.sq3.select(query,(ip,netmaske))
        if len(res)==0:
            query = 'INSERT INTO IPinfo (IP, NetMask, Remarks) VALUES (?, ?, ?)'
            self.sq3.I_U_D(query,(ip,netmaske,remarks))
            self.getinfo()
        else:
            messagebox.showerror("错误", "不可重复添加")

    def DELNETINFO(self,evt):
        chooseres= messagebox.askyesno(
            title='确认删除？',
            message=f'是否删除ID为:{self.treechoose_id},的IP:{self.treechoose_ip}'
        )
        if chooseres:
            query = 'DELETE FROM IPinfo WHERE id = ?'
            self.sq3.I_U_D(query,(self.treechoose_id,))
            self.ui.tk_button_lxyvatz0.configure(state="disabled")
            self.getinfo()
    
    def getinfo(self) -> None:
        for item in self.ui.tk_table_lxyugkyn.get_children():
            self.ui.tk_table_lxyugkyn.delete(item)
        query = 'SELECT * FROM IPinfo'
        res=self.sq3.select(query)
        if res:
            for item in res:
                self.ui.tk_table_lxyugkyn.insert('', 'end', values=item)
        self.ui.tk_input_lxyv1hm1.delete(0, tk.END)
        self.ui.tk_input_lxyv4183.delete(0, tk.END)
        self.ui.tk_input_lxyv8q02.delete(0, tk.END)
        self.treechoose_id:str = ''
        self.treechoose_ip:str = ''
        self.treechoose_netmask:str = ''

    def getnetlist(self):
        query = 'SELECT * FROM config WHERE id = 1'
        res=self.sq3.select(query)
        network_interfaces = psutil.net_if_addrs()
        for interface_name, interface_data in network_interfaces.items():
            self.ui.tk_list_box_lxyukxkh.insert('end',interface_name)
        if res[0][1]:
            all_items = self.ui.tk_list_box_lxyukxkh.get(0, tk.END)
            for i, item in enumerate(all_items):
                if item == res[0][1]:
                    self.ui.tk_list_box_lxyukxkh.selection_set(i)
                    self.ui.tk_list_box_lxyukxkh.see(i)
                    self.NetWorkCard()
                    break
