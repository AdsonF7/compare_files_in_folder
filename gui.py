from tkinter import Tk, Frame, StringVar, Label, Entry, Button, Checkbutton, IntVar, W, NSEW, EW
from tkinter.filedialog import askdirectory
class GUI(Tk):
    
    def __init__(self, app, *args, **kwargs):
        super(GUI, self).__init__(*args, **kwargs)
        self._app = app
        self._var_et_folder1_path = StringVar()
        self._var_et_folder2_path = StringVar()
        self.columnconfigure(0, weight=1)
        self.title("Compare Files")
        self.resizable(True, False)
        self.geometry("500x160")
        self._var_ck_delete_duplicates = IntVar()
        self._var_ck_delete_duplicates.set(1)
        frame = Frame(self)
        frame.grid(column=0, row=0, sticky=NSEW, padx=(10, 10), pady=(10, 10))
        frame.columnconfigure(0, weight=1)
        lb_folder1_path = Label(frame, text="Folder Origin")
        lb_folder1_path.grid(column=0, row=0, sticky=W)
        bt_folder1_path = Button(frame, textvariable=self._var_et_folder1_path)
        bt_folder1_path.grid(column=0, row=2, sticky=EW)
        bt_folder1_path.bind("<Button-1>", lambda event, var=self._var_et_folder1_path: self.open_directory(var))
        lb_folder2_path = Label(frame, text="Folder Target")
        lb_folder2_path.grid(column=0, row=3, sticky=W) 
        bt_folder2_path = Button(frame, textvariable=self._var_et_folder2_path)
        bt_folder2_path.grid(column=0, row=4, sticky=EW)
        bt_folder2_path.bind("<Button-1>", lambda event, var=self._var_et_folder2_path: self.open_directory(var))
        ck_delete_duplicates = Checkbutton(frame, text="Delete File If Duplicated", variable=self._var_ck_delete_duplicates) 
        ck_delete_duplicates.grid(column=0, row=5, sticky=W)
        bt_search = Button(frame, text="Search")
        bt_search.bind("<Button-1>", self.bt_search_click)
        bt_search.grid(column=0, row=6, sticky=W, padx=4, pady=(5, 0))    
    
    def open_directory(self, var):
        result = askdirectory()
        if result: var.set(result)
        
    def bt_search_click(self, event):
        self._app.find(self._var_et_folder1_path.get(), self._var_et_folder2_path.get(), self._var_ck_delete_duplicates.get())
