# –*–coding:utf-8 –*–
# time:2021-01-19 15:23
# 关于tkinter
# 窗口
'''
基于tkinter 模块开发
'''
import tkinter as tk
import tkinter.messagebox
import pickle
from PIL import Image,ImageTk



# 创建一个窗口
window = tk.Tk()
# 给窗口取一个名字。
window.title('欢迎加入学习系统')
# 获取屏幕宽度和高度
scn_w, scn_h = window.maxsize()
# 计算中心坐标
cen_x = (scn_w - 300) / 2
cen_y = (scn_h - 300) / 2
# 设置窗口初始大小和位置
size_xy = '%dx%d+%d+%d' % (600, 600, cen_x, cen_y)

window.geometry(size_xy)  # 设置窗口坐标
window.wm_attributes('-topmost', 1)  # 窗口置顶


# 画布放置图片
canvas = tk.Canvas(window, height=600, width=500)
im = Image.open( "images/1.png" )
imagefile = ImageTk.PhotoImage(im)
image = canvas.create_image(0, 0, anchor='nw', image=imagefile)
canvas.pack(side='top')
# 标签 用户名密码
tk.Label(window, text='用户名:').place(x=140, y=150)
tk.Label(window, text='密码:').place(x=140, y=190)
# 用户名输入框
var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=210, y=150)
# 密码输入框
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=210, y=190)



def usr_log_in():
    '''
    usr_log_in  登录函数
    '''
    # 输入框获取用户名密码
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    '''
        if len( var_usr_name.get() ) or len(var_usr_pwd.get()) != 6:
        tk.messagebox.showerror(message = '用户名或密码长度不足6位数！')
        # bt_login.config(state="disabled")
    else:
        
        bt_login.config(state='active')
    '''
    
    # 从本地字典获取用户信息，如果没有则新建本地数据库
    try:
        with open('usr_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usr_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)
    # 判断用户名和密码是否匹配
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='欢迎您:' + usr_name,
                                   message='欢迎您:'+usr_name)
            show_info()
        else:
            tk.messagebox.showerror(message='用户名或密码错误！')
    # 用户名密码不能为空
    elif usr_name == '' or usr_name == ' ' or usr_pwd == '' or usr_pwd == ' ':
        tk.messagebox.showerror(message='用户名或密码为空！')
    # 不在数据库中弹出是否注册的框
    else:
        is_signup = tk.messagebox.showinfo(title = '提示', message = '账号或密码错误，请重新检查.')

        if is_signup:
            pass
            # usr_sign_up()


# 登陆成功展示函数
def show_info():
    '''
       show_info 新建登陆成功界面
    '''
    window.withdraw()
    window_info_up = tk.Toplevel(window)
    size_xy = '%dx%d+%d+%d' % (500, 658, cen_x, cen_y)
    window_info_up.geometry(size_xy)  # 设置窗口坐标
    window_info_up.wm_attributes('-topmost', 1)  # 窗口置顶
    window_info_up.title('欢迎')
    # 画布放置图片
    canvas = tk.Canvas(window_info_up, height=987, width=658)
    im = Image.open( "images/1.png" )
    imagefile = ImageTk.PhotoImage(im)
    # imagefile=tk.PhotoImage(file='71.gif')
    image1 = canvas.create_image(0, 0, anchor='nw', image=imagefile)
    canvas.pack(side='top')
    tk.Label(window_info_up, text='欢 迎 您 , {}'.format(var_usr_name.get())).place(x=180, y=60)
    tk.Label(window_info_up, text='无论你可以飞多远，永远不要忘记你来自哪里.').place(x=125, y=100)
    # tk.Label(window_info_up, text='无论你可以飞多远，永远不要忘记你来自哪里.').place(x=25, y=140)

    def usr_sign_quit() :
        global window # global全局变量
        window.destroy()
        
    bt_logquit = tk.Button(window_info_up, text='退出', command=usr_sign_quit)
    bt_logquit.place(x=430, y=10)

    def callback():
        window.destroy()
    window_info_up.protocol("WM_DELETE_WINDOW", callback)
    window_info_up.mainloop()

# 注册函数
def usr_sign_up():
    '''
    usr_sign_up 注册函数
    '''
    # 确认注册时的相应函数
    def signtowcg():
        # 获取输入框内的内容
        nn = new_name.get()
        np = new_pwd.get()
        npf = new_pwd_confirm.get()

        # 本地加载已有用户信息,如果没有则已有用户信息为空
        try:
            with open('usr_info.pickle', 'rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
        except FileNotFoundError:
            exist_usr_info = {}

            # 检查用户名存在、密码为空、密码前后不一致
        if nn in exist_usr_info:
            tk.messagebox.showerror('提示:', '用户名已存在！')
        elif np == '' or nn == ' ':
            tk.messagebox.showerror('提示:', '用户名或密码为空！')
        elif np != npf:
            tk.messagebox.showerror('提示:', '密码不一致！')
        # 注册信息没有问题则将用户名密码写入数据库
        else:
            exist_usr_info[nn] = np
            with open('usr_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('欢迎', '登录成功!')
            # 注册成功关闭注册框
            window_sign_up.destroy()
    # 新建注册界面
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry(size_xy)  # 设置窗口坐标
    window_sign_up.wm_attributes('-topmost', 1)  # 窗口置顶
    window_sign_up.title('注册')
    # 画布放置图片
    canvas = tk.Canvas(window_sign_up, height=987, width=658)
    im = Image.open( "images/1.png" )
    imagefile = ImageTk.PhotoImage(im)
    # imagefile=tk.PhotoImage(file='71.gif')
    image1 = canvas.create_image(0, 0, anchor='nw', image=imagefile)
    canvas.pack(side='top')
    # 用户名变量及标签、输入框
    new_name = tk.StringVar()
    tk.Label(window_sign_up, text='用户名：').place(x=100, y=100)
    tk.Entry(window_sign_up, textvariable=new_name).place(x=240, y=100)
    # 密码变量及标签、输入框
    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='密码：').place(x=100, y=140)
    tk.Entry(window_sign_up, textvariable=new_pwd, show='111111').place(x=240, y=140)
    # 重复密码变量及标签、输入框
    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='重复密码：').place(x=100, y=180)
    tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*').place(x=240, y=180)
    # 确认注册按钮及位置
    bt_confirm_sign_up = tk.Button(window_sign_up, text='确认注册',
                                   command=signtowcg)
    bt_confirm_sign_up.place(x=240, y=220)
    def Return(Event=None) :
        '''
        返回登录页面
        '''
        window_sign_up.destroy()
        usr_log_in()
    # 返回按钮
    bt_return = tk.Button(window_sign_up, text='返回', command=Return)
    bt_return.place(x=340, y=220)
    window_sign_up.mainloop()

# 关闭的函数
def close_sign_quit():
    '''
    关闭函数
    '''
    window.destroy()

    
def Refresh():
    
    window.update()

# 登录 注册按钮
bt_login = tk.Button(window, text='登录', command=usr_log_in)
bt_login.place(x=140, y=230)
bt_logup = tk.Button(window, text='注册', command=usr_sign_up)
bt_logup.place(x=210, y=230)
bt_logquit = tk.Button(window, text='退出', command=close_sign_quit)
bt_logquit.place(x=280, y=230)
bt_Refresh = tk.Button(window, text='刷新', command=Refresh)
bt_Refresh.place(x=480, y=20)
# 主循环
window.mainloop()