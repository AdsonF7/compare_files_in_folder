from tkinter import Tk, StringVar, Label, Entry, Button

class GUI(Tk):
    
    def __init__(self, root, *args, **kwargs):
        super(GUI, self).__init__(*args, **kwargs)
        self.__root = root
        self.var_folder_name = StringVar()
        lb_folder_name = Label(self, text="Folder")
        lb_folder_name.grid(column=0, row=0) 
        et_folder_name = Entry(self, textvariable=self.var_folder_name)
        et_folder_name.grid(column=0, row=1) 
        bt_search = Button(self, text="Search")
        bt_search.bind("<Button-1>", self.bt_search_click)
        bt_search.grid(column=0, row=2)    
    
    def bt_search_click(self, event):
        print("OK")
GUI()