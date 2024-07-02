from ui import Win as MainWin
from control import Controller as MainUIController
from sqlite import ql as ql3Controller
import ctypes,sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ == "__main__":
    if is_admin() and True:
        app = MainWin(MainUIController(ql3Controller()))
        app.mainloop()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)