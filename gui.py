import tkinter as tk
import json
from translate_sprider import sprider


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # 从JSON文件中加载语言字典
        with open("languages.json", "r", encoding="utf8") as f:
            self.languages_dict = json.load(f)

    def main_Page(self):
        """
               设置主页面的基本属性，包括标题、图标、大小和背景色
        """
        self.master.title("XiaoxingTransaction")
        self.master.iconbitmap("FxemojiStar.ico")
        self.master.minsize(480, 220)
        self.master.geometry("480x220-100+100")
        self.master.config(background="white")

    def component_Settings(self):
        """
               设置页面的组件，包括框架、按钮和文本框
        """

        # 创建左右框架和顶部框架
        self.frame_left = tk.Frame(self.master, bg="white", width=240, height=190)
        self.frame_right = tk.Frame(self.master, bg="gray", width=240, height=190)
        self.frame_top = tk.Frame(self.master, bg="white", height=30)

        # 创建源语言选择按钮并绑定事件
        self.language_button_left = tk.Button(self.frame_top, text="自动检测", font=("Consolas", 10), bd=2, bg="white",
                                              overrelief="sunken", cursor="hand2")
        self.language_button_left.bind("<Button-1>", self.select_language)
        self.language_button_left.pack(side="left")
        self.language_button_right = tk.Button(self.frame_top, text="英语", font=("Consolas", 10), bd=2, bg="white",
                                               overrelief="sunken", cursor="hand2")
        self.language_button_right.bind("<Button-1>", self.select_language)
        self.language_button_right.pack(side="right")

        # 创建文本输入框和翻译按钮
        self.text_input = tk.Text(self.frame_left, bg="white", font=("Consolas", 12), width=24, height=10)
        self.text_input.bind("<BackSpace>", self.delete_output)
        self.translate_button = tk.Button(self.frame_left, text="翻译", font=("Consolas", 10), bd=2, bg="white",
                                          overrelief="sunken", cursor="hand2", command=self.translate)
        self.translate_button.pack(side="bottom", anchor="w")

        # 创建翻译输出框
        self.translate_output = tk.Text(self.frame_right, bg="white", font=("Consolas", 12), width=24, height=10)

        # 将组件添加到主窗口
        self.frame_top.pack(fill="x")
        self.text_input.pack(fill="both", expand=True)
        self.frame_left.pack(side="left", fill="both", expand=True)
        self.translate_output.pack(fill="both", expand=True)
        self.frame_right.pack(side="right", fill="both", expand=True)

    def translate(self):
        """
                翻译功能，获取输入文本并调用翻译接口
        """
        text = self.text_input.get(1.0, tk.END)
        self.fromLang = self.languages_dict[self.language_button_left["text"]]  # 翻译源语言
        self.to = self.languages_dict[self.language_button_right["text"]]  # 翻译目标语言
        if text.strip() != "":
            translated_text = sprider.get_Translate(text=text, to=self.to, fromLang=self.fromLang)
            self.translate_output.delete(1.0, tk.END)
            self.translate_output.insert(1.0, translated_text)

    def delete_output(self, event):
        """
        删除翻译输出框的内容
        """
        self.translate_output.delete(1.0, tk.END)

    def select_language(self, event):
        """
                显示语言选择列表框
        """

        # 获取触发事件的按钮位置
        x = event.widget.winfo_x()
        y = event.widget.winfo_y()

        # 创建语言选择列表框框架和滚动条
        self.language_selection_frame = tk.Frame(self.master, bg="white", width=100, height=6)
        scrollbar = tk.Scrollbar(self.language_selection_frame,takefocus=True,activerelief="solid")
        scrollbar.pack(side="right", fill="y")
        # 创建语言列表框并填充数据
        self.language_listbox = tk.Listbox(self.language_selection_frame, bg="white", font=("Consolas", 12), width=15,
                                           height=7, yscrollcommand=scrollbar.set, relief="ridge")
        for index, key in enumerate(self.languages_dict):
            self.language_listbox.insert(index, key)
        self.language_listbox.pack(side="left", fill="both")
        scrollbar.config(command=self.language_listbox.yview)

        # 根据触发事件的按钮位置放置列表框框架
        if x > 200:
            self.flag = "right"
            self.language_selection_frame.place(x=x + event.widget.winfo_width(), y=y + event.widget.winfo_height(), anchor="ne")
            self.language_button_right.unbind("<Button-1>")
            self.language_button_right.bind("<Button-1>", self.hide_listbox)
            self.language_button_left.config(state=tk.DISABLED)
            self.language_button_left.unbind("<Button-1>")
        else:
            self.flag = "left"
            self.language_selection_frame.place(x=x, y=y + event.widget.winfo_height(), anchor="nw")
            self.language_button_left.unbind("<Button-1>")
            self.language_button_left.bind("<Button-1>", self.hide_listbox)
            self.language_button_right.config(state=tk.DISABLED)
            self.language_button_right.unbind("<Button-1>")

        # 绑定隐藏语言选择列表框事件
        self.frame_top.bind("<Button-1>", self.hide_listbox)
        self.frame_left.bind("<Button-1>", self.hide_listbox)
        self.text_input.bind("<Button-1>", self.hide_listbox)
        self.translate_output.bind("<Button-1>", self.hide_listbox)
        self.language_listbox.bind("<Button-1>", self.change_language)

    def change_language(self, event):
        """
                选择语言并更新按钮文本
        """
        index = self.language_listbox.nearest(event.y)
        selected_text = self.language_listbox.get(index)
        if self.flag == "left":
            self.language_button_left["text"] = selected_text
        else:
            self.language_button_right["text"] = selected_text
        self.delete_output(event)
        self.hide_listbox(event)

    def hide_listbox(self, event):
        """
                隐藏语言选择列表框并恢复按钮状态
        """
        self.language_selection_frame.place_forget()
        self.frame_top.unbind("<Button-1>")
        self.text_input.unbind("<Button-1>")
        self.translate_output.unbind("<Button-1>")
        self.language_button_left.unbind("<Button-1>")
        self.language_button_left.bind("<Button-1>", self.select_language)
        self.language_button_right.unbind("<Button-1>")
        self.language_button_right.bind("<Button-1>", self.select_language)
        self.language_button_left.config(state=tk.NORMAL)
        self.language_button_right.config(state=tk.NORMAL)

    def main(self):
        """
            主函数，初始化翻译接口并启动主循环
        """
        sprider.get_TokenKey()
        self.main_Page()
        self.component_Settings()
        self.master.mainloop()



