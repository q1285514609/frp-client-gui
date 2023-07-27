import re
import subprocess
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from typing import Dict
import os
import random
import string
from configparser import ConfigParser

from aliyunsdkcore.client import AcsClient


class WinGUI(Tk):
    widget_dic: Dict[str, Widget] = {}

    def __init__(self):
        super().__init__()
        self.__win()

        self.widget_dic["tk_label_frame_lkhx43s2"] = self.__tk_label_frame_lkhx43s2(self)
        self.widget_dic["tk_table_tab_list"] = self.__tk_table_tab_list(self)
        self.widget_dic["tk_tabs_lki5rwm9"] = self.__tk_tabs_lki5rwm9(self)
        self.widget_dic["tk_label_lki5t18g"] = self.__tk_label_lki5t18g(self.widget_dic["tk_tabs_lki5rwm9_0"])
        self.widget_dic["tk_label_input_server_port"] = self.__tk_label_input_server_port(
            self.widget_dic["tk_tabs_lki5rwm9_0"])
        self.widget_dic["tk_label_input_server_token"] = self.__tk_label_input_server_token(
            self.widget_dic["tk_tabs_lki5rwm9_0"])
        self.widget_dic["tk_input_input_server_id"] = self.__tk_input_input_server_id(
            self.widget_dic["tk_tabs_lki5rwm9_0"])
        self.widget_dic["tk_input_input_server_port"] = self.__tk_input_input_server_port(
            self.widget_dic["tk_tabs_lki5rwm9_0"])
        self.widget_dic["tk_input_input_server_token"] = self.__tk_input_input_server_token(
            self.widget_dic["tk_tabs_lki5rwm9_0"])
        self.widget_dic["tk_button_but_server_save"] = self.__tk_button_but_server_save(
            self.widget_dic["tk_tabs_lki5rwm9_0"])
        self.widget_dic["tk_label_lki73b45"] = self.__tk_label_lki73b45(self.widget_dic["tk_tabs_lki5rwm9_1"])
        self.widget_dic["tk_input_input_client_port"] = self.__tk_input_input_client_port(
            self.widget_dic["tk_tabs_lki5rwm9_1"])
        self.widget_dic["tk_button_but_portRandom"] = self.__tk_button_but_portRandom(
            self.widget_dic["tk_tabs_lki5rwm9_1"])
        self.widget_dic["tk_label_lki73ps6"] = self.__tk_label_lki73ps6(self.widget_dic["tk_tabs_lki5rwm9_1"])
        self.widget_dic["tk_input_input_client_name"] = self.__tk_input_input_client_name(
            self.widget_dic["tk_tabs_lki5rwm9_1"])
        self.widget_dic["tk_button_but_domainRandom"] = self.__tk_button_but_domainRandom(
            self.widget_dic["tk_tabs_lki5rwm9_1"])
        self.widget_dic["tk_button_but_start"] = self.__tk_button_but_start(self.widget_dic["tk_tabs_lki5rwm9_1"])
        self.widget_dic["tk_button_but_client_add"] = self.__tk_button_but_client_add(
            self.widget_dic["tk_tabs_lki5rwm9_1"])

        self.widget_dic["tk_input_intput_client_before"] = self.__tk_input_intput_client_before(
            self.widget_dic["tk_tabs_lki5rwm9_1"])
        self.widget_dic["tk_input_intput_client_after"] = self.__tk_input_intput_client_after(
            self.widget_dic["tk_tabs_lki5rwm9_1"])

        self.widget_dic["tk_label_lkkiirgw"] = self.__tk_label_lkkiirgw(self.widget_dic["tk_tabs_lki5rwm9_2"])
        self.widget_dic["tk_input_AccessKeyID"] = self.__tk_input_AccessKeyID(self.widget_dic["tk_tabs_lki5rwm9_2"])
        self.widget_dic["tk_label_lkkiix86"] = self.__tk_label_lkkiix86(self.widget_dic["tk_tabs_lki5rwm9_2"])
        self.widget_dic["tk_input_AccessKeySecret"] = self.__tk_input_AccessKeySecret(
        self.widget_dic["tk_tabs_lki5rwm9_2"])
        self.widget_dic["tk_button_ali_save"] = self.__tk_button_ali_save(self.widget_dic["tk_tabs_lki5rwm9_2"])
    def __win(self):
        self.title("frp客户端配置GUI")
        # 设置窗口大小、居中
        width = 308
        height = 370
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)
        # 自动隐藏滚动条

    def scrollbar_autohide(self, bar, widget):
        self.__scrollbar_hide(bar, widget)
        widget.bind("<Enter>", lambda e: self.__scrollbar_show(bar, widget))
        bar.bind("<Enter>", lambda e: self.__scrollbar_show(bar, widget))
        widget.bind("<Leave>", lambda e: self.__scrollbar_hide(bar, widget))
        bar.bind("<Leave>", lambda e: self.__scrollbar_hide(bar, widget))

    def __scrollbar_show(self, bar, widget):
        bar.lift(widget)

    def __scrollbar_hide(self, bar, widget):
        bar.lower(widget)

    def vbar(self, ele, x, y, w, h, parent):
        sw = 15  # Scrollbar 宽度
        x = x + w - sw
        vbar = Scrollbar(parent)
        ele.configure(yscrollcommand=vbar.set)
        vbar.config(command=ele.yview)
        vbar.place(x=x, y=y, width=sw, height=h)
        self.scrollbar_autohide(vbar, ele)

    def __tk_label_frame_lkhx43s2(self, parent):
        frame = LabelFrame(parent, text="已有记录", )
        frame.place(x=9, y=170, width=285, height=191)
        return frame

    def __tk_table_tab_list(self, parent):
        # 表头字段 表头宽度
        columns = {"端口": 55, "域名": 200}
        tk_table = Treeview(parent, show="headings", columns=list(columns), )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸

        tk_table.place(x=17, y=190, width=273, height=166)
        self.vbar(tk_table, 17, 190, 273, 166, parent)
        return tk_table

    def __tk_tabs_lki5rwm9(self, parent):
        frame = Notebook(parent)
        self.widget_dic["tk_tabs_lki5rwm9_0"] = self.__tk_frame_lki5rwm9_0(frame)
        frame.add(self.widget_dic["tk_tabs_lki5rwm9_0"], text="服务端")
        self.widget_dic["tk_tabs_lki5rwm9_1"] = self.__tk_frame_lki5rwm9_1(frame)
        frame.add(self.widget_dic["tk_tabs_lki5rwm9_1"], text="客户端")
        frame.select(self.widget_dic["tk_tabs_lki5rwm9_1"])
        self.widget_dic["tk_tabs_lki5rwm9_2"] = self.__tk_frame_lki5rwm9_2(frame)
        frame.add(self.widget_dic["tk_tabs_lki5rwm9_2"], text="阿里云")
        frame.place(x=10, y=10, width=287, height=155)
        return frame

    def __tk_frame_lki5rwm9_0(self, parent):
        frame = Frame(parent)
        frame.place(x=10, y=10, width=287, height=155)
        return frame

    def __tk_frame_lki5rwm9_1(self, parent):
        frame = Frame(parent)
        frame.place(x=10, y=10, width=287, height=155)
        return frame

    def __tk_frame_lki5rwm9_2(self, parent):
        frame = Frame(parent)
        frame.place(x=10, y=10, width=287, height=155)
        return frame
    def __tk_label_lki5t18g(self, parent):
        label = Label(parent, text="ip:", anchor="center", )
        label.place(x=50, y=10, width=24, height=30)
        return label

    def __tk_label_input_server_port(self, parent):
        label = Label(parent, text="端口:", anchor="center", )
        label.place(x=38, y=50, width=34, height=30)
        return label

    def __tk_label_input_server_token(self, parent):
        label = Label(parent, text="token:", anchor="center", )
        label.place(x=30, y=90, width=40, height=30)
        return label

    def __tk_input_input_server_id(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=70, y=10, width=150, height=30)
        return ipt

    def __tk_input_input_server_port(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=70, y=50, width=150, height=30)
        return ipt

    def __tk_input_input_server_token(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=70, y=90, width=150, height=30)
        return ipt

    def __tk_button_but_server_save(self, parent):
        btn = Button(parent, text="保存", takefocus=False, )
        btn.place(x=230, y=29, width=50, height=77)
        return btn

    def __tk_label_lki73b45(self, parent):
        label = Label(parent, text="端口号:", anchor="center", )
        label.place(x=12, y=10, width=43, height=30)
        return label

    def __tk_input_input_client_port(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=70, y=10, width=150, height=30)
        return ipt

    def __tk_button_but_portRandom(self, parent):
        btn = Button(parent, text="随机", takefocus=False, )
        btn.place(x=230, y=10, width=50, height=30)
        return btn

    def __tk_label_lki73ps6(self, parent):
        label = Label(parent, text="域名:", anchor="center", )
        label.place(x=12, y=52, width=32, height=30)
        return label


    def __tk_input_input_client_name(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=70, y=50, width=70, height=30)
        return ipt

    def __tk_button_but_domainRandom(self, parent):
        btn = Button(parent, text="随机", takefocus=False, )
        btn.place(x=230, y=52, width=50, height=30)
        return btn

    def __tk_button_but_start(self, parent):
        btn = Button(parent, text="启动程序", takefocus=False, )
        btn.place(x=180, y=90, width=73, height=29)
        return btn

    def __tk_button_but_client_add(self, parent):
        btn = Button(parent, text="添加配置", takefocus=False, )
        btn.place(x=30, y=93, width=81, height=29)
        return btn

    def __tk_input_intput_client_before(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=40, y=50, width=31, height=30)
        return ipt

    def __tk_input_intput_client_after(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=140, y=50, width=92, height=30)
        return ipt

    def __tk_label_lkkiirgw(self, parent):
        label = Label(parent, text="AccessKeyID:", anchor="center", )
        label.place(x=10, y=10, width=79, height=30)
        return label

    def __tk_input_AccessKeyID(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=90, y=10, width=190, height=30)
        return ipt

    def __tk_label_lkkiix86(self, parent):
        label = Label(parent, text="AccessKeySecret:", anchor="center", )
        label.place(x=10, y=50, width=105, height=30)
        return label

    def __tk_input_AccessKeySecret(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=116, y=50, width=165, height=30)
        return ipt
    def __tk_button_ali_save(self, parent):
        btn = Button(parent, text="保存配置", takefocus=False, )
        btn.place(x=80, y=92, width=105, height=30)
        return btn
class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

        self.config = ConfigParser()
        self.config_file = "frpc.ini"
        self.client_config_file = "clientConfigGUI.ini"

        # 创建右键菜单
        self.create_popup_menu()

        # 读取配置文件
        self.config.read(self.config_file)
        self.client_config = ConfigParser()
        self.client_config.read(self.client_config_file)

        if 'common' in self.config.sections():
            server_id = self.config.get('common', 'server_addr', fallback='')
            server_port = self.config.get('common', 'server_port', fallback='')
            server_token = self.config.get('common', 'token', fallback='')
            # 将数据设置到输入框中
            self.widget_dic["tk_input_input_server_id"].insert(0, server_id)
            self.widget_dic["tk_input_input_server_port"].insert(0, server_port)
            self.widget_dic["tk_input_input_server_token"].insert(0, server_token)
        self.update_table()

        if 'client' in self.client_config.sections():
            before = self.client_config.get('client', 'before', fallback='')
            after = self.client_config.get('client', 'after', fallback='')
            # 将数据设置到输入框中
            self.widget_dic["tk_input_intput_client_before"].insert(0, before)
            self.widget_dic["tk_input_intput_client_after"].insert(0, after)

        if 'aliyun' in self.client_config.sections():
            access_key_id = self.client_config.get('aliyun', 'AccessKeyID', fallback='')
            access_key_secret = self.client_config.get('aliyun', 'AccessKeySecret', fallback='')
            # 将数据设置到输入框中
            self.widget_dic["tk_input_AccessKeyID"].insert(0, access_key_id)
            self.widget_dic["tk_input_AccessKeySecret"].insert(0, access_key_secret)
            # 使用从配置文件中读取的 access_key_id 和 access_key_secret 创建 AcsClient
            self.client = AcsClient(access_key_id, access_key_secret, "")
    # 添加新的域名解析记录
    def add_domain_parse(self, after, domain, Type, value):
        if not is_valid_domain(after):
            messagebox.showinfo("提示", "请输入正确的域名")

        from aliyunsdkalidns.request.v20150109.AddDomainRecordRequest import AddDomainRecordRequest

        request = AddDomainRecordRequest()
        request.set_accept_format('json')
        request.set_DomainName(after)
        request.set_RR(domain)
        request.set_Type(Type)
        request.set_Value(value)
        response = self.client.do_action_with_exception(request)

    def delete_domain_parse(self, after, domain):
        if not is_valid_domain(after):
            messagebox.showinfo("提示", "请输入正确的域名")

        from aliyunsdkalidns.request.v20150109.DeleteSubDomainRecordsRequest import DeleteSubDomainRecordsRequest

        request = DeleteSubDomainRecordsRequest()
        request.set_accept_format('json')
        request.set_DomainName(after)
        request.set_RR(domain)
        response = self.client.do_action_with_exception(request)

    def start_frpc(self):
        # 运行命令，并捕获命令的输出
        cmd = ["frpc.exe", "-c", "frpc.ini"]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                   creationflags=subprocess.CREATE_NO_WINDOW)
        rc = process.poll()

    def create_popup_menu(self):
        # 创建右键菜单
        self.popup_menu = Menu(self, tearoff=0)
        # 创建右键菜单
        self.popup_menu.add_command(label="复制域名", command=self.copy_domain)
        self.popup_menu.add_command(label="删除", command=self.delete_selected_row)

    def show_popup_menu(self, event):
        # 显示右键菜单
        self.popup_menu.post(event.x_root, event.y_root)

    def copy_domain(self):
        # 复制选中行的域名列的内容
        selected_items = self.widget_dic["tk_table_tab_list"].selection()
        if not selected_items:
            messagebox.showinfo("提示", "请选择需要复制的域名")
            return
        selected_item = selected_items[0]
        domain = self.widget_dic["tk_table_tab_list"].item(selected_item, "values")[1]
        self.clipboard_clear()
        self.clipboard_append(domain)

    def delete_selected_row(self):
        # 删除选中的行
        selected_items = self.widget_dic["tk_table_tab_list"].selection()
        if not selected_items:
            messagebox.showinfo("提示", "请选择需要删除的选项")
            return
        selected_item = selected_items[0]
        # 获取端口和域名
        local_port, custom_domains = self.widget_dic["tk_table_tab_list"].item(selected_item, "values")
        # 删除表格中的行
        self.widget_dic["tk_table_tab_list"].delete(selected_item)

        # 删除frpc.ini配置文件中的配置
        self.config.read(self.config_file)
        for section in self.config.sections():
            if (self.config.has_option(section, 'local_port') and self.config.get(section,
                                                                                  'local_port') == local_port and
                    self.config.has_option(section, 'custom_domains') and self.config.get(section,
                                                                                          'custom_domains') == custom_domains):
                self.config.remove_section(section)
                with open(self.config_file, 'w') as configfile:
                    self.config.write(configfile)
                break

        # 删除域名解析
        self.delete_domain_parse(".".join(custom_domains.split(".")[-2:]),  ".".join(custom_domains.split(".")[0:2]))

    def generate_random_port(self):
        # 生成1024到65535之间的随机端口
        return str(random.randint(1024, 65535))

    def generate_random_domain(self):
        # 生成随机的10位全英文字母的字符串
        return ''.join(random.choices(string.ascii_lowercase, k=10))

    def add_server_config(self, evt):
        # 添加服务器配置
        server_id = self.widget_dic["tk_input_input_server_id"].get()
        server_port = self.widget_dic["tk_input_input_server_port"].get()
        server_token = self.widget_dic["tk_input_input_server_token"].get()
        # 读取配置文件
        self.config.read(self.config_file)
        # 判断common是否存在，不存在则创建
        if 'common' not in self.config.sections():
            self.config.add_section('common')
        self.config.set('common', 'server_addr', server_id)
        self.config.set('common', 'server_port', server_port)
        self.config.set('common', 'token', server_token)
        # 写入配置文件
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)

    def update_table(self):
        # 先清空表格
        for i in self.widget_dic["tk_table_tab_list"].get_children():
            self.widget_dic["tk_table_tab_list"].delete(i)
        # 重新加载数据
        self.config.read(self.config_file)
        sections = [i for i in self.config.sections() if i.startswith('web')]
        for section in sections:
            local_port = self.config.get(section, 'local_port')
            custom_domains = self.config.get(section, 'custom_domains')
            self.widget_dic["tk_table_tab_list"].insert('', 'end', values=(local_port, custom_domains))

    def start_app(self, evt):
        # 启动frpc
        os.system("start frpc.exe -c frpc.ini")

    def port_random(self, evt):
        # 随机生成端口号并显示
        self.widget_dic["tk_input_input_client_port"].delete(0, 'end')
        self.widget_dic["tk_input_input_client_port"].insert(0, self.generate_random_port())

    def domain_random(self, evt):
        # 随机生成域名并显示
        self.widget_dic["tk_input_input_client_name"].delete(0, 'end')
        self.widget_dic["tk_input_input_client_name"].insert(0, self.generate_random_domain())

    def add_client_config(self, evt):
        # 添加或修改客户端配置
        domain = self.widget_dic["tk_input_input_client_name"].get()
        port = self.widget_dic["tk_input_input_client_port"].get()
        before = self.widget_dic["tk_input_intput_client_before"].get()
        after = self.widget_dic["tk_input_intput_client_after"].get()

        # 将 before 和 after 保存到配置文件中
        if 'client' not in self.client_config.sections():
            self.client_config.add_section('client')
        self.client_config.set('client', 'before', before)
        self.client_config.set('client', 'after', after)
        with open(self.client_config_file, 'w') as configfile:
            self.client_config.write(configfile)

        # 读取配置文件
        self.config.read(self.config_file)
        # 检查是否存在相同的端口或域名
        for section in self.config.sections():
            if (self.config.has_option(section, 'local_port') and self.config.get(section, 'local_port') == port) or \
                    (self.config.has_option(section, 'custom_domains') and self.config.get(section,
                                                                                           'custom_domains') == f"{self.client_config.get('client', 'before', fallback='')}{domain}{self.client_config.get('client', 'after', fallback='')}"):
                self.config.set(section, 'type', 'http')
                self.config.set(section, 'local_port', port)
                self.config.set(section, 'custom_domains', f"{self.client_config.get('client', 'before', fallback='')}{domain}{self.client_config.get('client', 'after', fallback='')}")
                break
        else:
            # 如果没有找到相同的端口或域名，则添加新的配置
            web_number = len([i for i in self.config.sections() if i.startswith('web_client')]) + 1
            section = f"web_client{web_number}"
            self.config.add_section(section)
            self.config.set(section, 'type', 'http')
            self.config.set(section, 'local_port', port)
            self.config.set(section, 'custom_domains', f"{self.client_config.get('client', 'before', fallback='')}{domain}{self.client_config.get('client', 'after', fallback='')}")
        # 写入配置文件
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)
        # 更新表格
        self.update_table()

        # 新增域名解析
        self.add_domain_parse(".".join(self.client_config.get('client', 'after', fallback='').split('.')[1:]), self.client_config.get('client', 'before', fallback='') + domain, 'A', self.config.get('common', 'server_addr', fallback=''))

    def but_ali_save(self, evt):
        # 保存 AccessKeyID 和 AccessKeySecret 到配置文件中
        access_key_id = self.widget_dic["tk_input_AccessKeyID"].get()
        access_key_secret = self.widget_dic["tk_input_AccessKeySecret"].get()
        if 'aliyun' not in self.client_config.sections():
            self.client_config.add_section('aliyun')
        self.client_config.set('aliyun', 'AccessKeyID', access_key_id)
        self.client_config.set('aliyun', 'AccessKeySecret', access_key_secret)
        with open(self.client_config_file, 'w') as configfile:
            self.client_config.write(configfile)
    def __event_bind(self):
        self.widget_dic["tk_button_but_server_save"].bind('<Button-1>', self.add_server_config)
        self.widget_dic["tk_button_but_portRandom"].bind('<Button-1>', self.port_random)
        self.widget_dic["tk_button_but_domainRandom"].bind('<Button-1>', self.domain_random)
        self.widget_dic["tk_button_but_start"].bind('<Button-1>', self.start_app)
        self.widget_dic["tk_button_but_client_add"].bind('<Button-1>', self.add_client_config)
        self.widget_dic["tk_table_tab_list"].bind("<Button-3>", self.show_popup_menu)
        self.widget_dic["tk_button_ali_save"].bind('<Button-1>', self.but_ali_save)
        pass

# 判断是否为域名
def is_valid_domain(domain):
    pattern = re.compile(
        r'^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+(?:[a-z]{2,6})$'
    )
    return bool(pattern.match(domain))

if __name__ == "__main__":
    win = Win()
    win.mainloop()
