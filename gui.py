from tkinter import Tk, Frame, StringVar, Label, Entry, Button, Checkbutton, IntVar, W, NSEW, EW

class GUI(Tk):
    
    def __init__(self, root, *args, **kwargs):
        super(GUI, self).__init__(*args, **kwargs)
        self.__root = root
        self.__var_et_folder1_name = StringVar()
        self.__var_et_folder2_name = StringVar()
        self.columnconfigure(0, weight=1)
        self.title("Compare Files")
        self.resizable(True, False)
        self.geometry("500x160")
        self.__var_ck_delete_duplicates = IntVar()
        self.__var_ck_delete_duplicates.set(1)
        frame = Frame(self)
        frame.grid(column=0, row=0, sticky=NSEW, padx=(10, 10), pady=(10, 10))
        frame.columnconfigure(0, weight=1)
        lb_folder1_name = Label(frame, text="Folder Origin")
        lb_folder1_name.grid(column=0, row=0, sticky=W)
        et_folder1_name = Entry(frame, textvariable=self.__var_et_folder1_name)
        et_folder1_name.grid(column=0, row=2, sticky=EW) 
        lb_folder2_name = Label(frame, text="Folder Target")
        lb_folder2_name.grid(column=0, row=3, sticky=W) 
        et_folder2_name = Entry(frame, textvariable=self.__var_et_folder2_name)
        et_folder2_name.grid(column=0, row=4, sticky=EW)
        ck_delete_duplicates = Checkbutton(frame, text="Delete File If Duplicated", variable=self.__var_ck_delete_duplicates) 
        ck_delete_duplicates.grid(column=0, row=5, sticky=W)
        bt_search = Button(frame, text="Search")
        bt_search.bind("<Button-1>", self.bt_search_click)
        bt_search.grid(column=0, row=6, sticky=W, padx=4, pady=(5, 0))    
    
    def bt_search_click(self, event):
        self.__root.find(self.__var_et_folder1_name.get(), self.__var_et_folder2_name.get())
#GUI()