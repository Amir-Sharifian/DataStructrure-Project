'''
GUI part of Data structures project
Affogato team
January 2021
University of Isfahan
'''

from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
from data import read_inputs
from data_process import run


class Gui:
    data = {}

    def phases_window(self):
        self.win.destroy()
        self.win11 = Tk()
        self.win11.title('phases')
        self.win11.geometry('600x200')
        self.win11.resizable(False, False)

        self.btn_phase1 = Button(self.win11, text='phase1 ', state='active',
                                 command=lambda: self.p1_window())  # self.output_window -> self.p1_window()

        self.btn_phase2 = Button(self.win11, text='phase2 ', state='active',
                                 command=lambda: self.output_window('phase2', self.p2))

        self.btn_phase3 = Button(self.win11, text='phase3 ', state='active',
                                 command=lambda: self.output_window('phase3', self.p3))

        self.btn_phase4 = Button(self.win11, text='phase4 ', state='active',
                                 command=lambda: self.output_window('phase4', self.p4))

        self.btn_phase1.place(x=70, y=60)
        self.btn_phase2.place(x=180, y=60)
        self.btn_phase3.place(x=290, y=60)
        self.btn_phase4.place(x=400, y=60)

    # ======= V (new method)
    def p1_window(self):
        self.win8 = Tk()
        self.ph1_ch = (
            'people', 'bank_accounts', 'houses', 'cars', 'phone_numbers',
            'calls', 'ownerships', 'relationships', 'transactions')
        self.win8.title('phase 1')
        self.win8.geometry("400x180")
        self.win8.resizable(False, False)

        def btn82_listener():
            self.output_window('smugglers', self.p1[0])

        def btn83_listener():
            self.output_window('Suspects', self.p1[1])

        def btn81_listener():
            self.output_window(self.cb8.get(), self.p1[2][self.cb8.get()])

        self.cb8 = Combobox(self.win8, values=self.ph1_ch, state='readonly')
        self.btn81 = Button(self.win8, text='show', command=lambda: btn81_listener())
        self.btn82 = Button(self.win8, text='smugglers', command=lambda: btn83_listener())
        self.btn83 = Button(self.win8, text='Suspects', command=lambda: btn82_listener())

        self.cb8.place(x=69, y=52)
        self.btn81.place(x=270, y=52)
        self.btn82.place(y=120, x=98)
        self.btn83.place(y=120, x=250)

    # =======^

    def btn0_listener(self):
        self.win0.destroy()
        self.general_window()

    def general_window(self):
        # main window:
        self.win = Tk()
        self.win.title('DS Project')
        self.win.geometry("700x200")
        self.win.resizable(False, False)

        input_tupel = (
            'people', 'bank_accounts', 'houses', 'cars', 'phone_numbers', 'calls',
            'ownerships', 'relationships', 'transactions')
        self.path_dict = {}
        for i in input_tupel:
            self.path_dict[i] = ''

        # functions:

        def return_data(key, address):
            self.data[key] = address

        def btn_path_listener(d: dict):
            x = askopenfilename()
            d[self.cb.get()] = x
            return_data(self.cb.get(), x)

        def btn_submit_listener():
            read_inputs(self.data)
            x = run()
            self.p1 = x[0]
            self.p2 = x[1]
            self.p3 = x[2]
            self.p4 = x[3]
            self.phases_window()

        # wigets:
        self.lb1 = Label(self.win, text='\n you must enter files path \n', font=18)
        self.cb = Combobox(self.win, values=input_tupel, state='readonly')
        self.btn_path = Button(self.win, text='select file', command=lambda: btn_path_listener(self.path_dict))

        self.btn_submit = Button(self.win, text='submit ', command=lambda: btn_submit_listener())

        # combiner:
        self.btn_submit.place(x=530, y=100)
        self.lb1.place(x=250, y=10)
        self.cb.place(x=170, y=100)
        self.btn_path.place(x=390, y=100)
        mainloop()

    def get_path_dict(self):
        return self.path_dict

    def get_address(self, x):
        return self.path_dict[x]

    def output_window(self, ttl: str, output_list: list):
        total_rows = len(output_list)
        total_columns = len(output_list[0])
        if total_rows < 30:
            root = Tk()
            root.title(ttl)
            for i in range(total_rows):
                for j in range(total_columns):
                    e = Entry(root)
                    e.grid(row=i, column=j)
                    e.insert(END, output_list[i][j])
        else:
            root = Tk()
            scrollbar = Scrollbar(root, orient="vertical")
            lb = Listbox(root, width=50, height=20, yscrollcommand=scrollbar.set)
            scrollbar.config(command=lb.yview)

            scrollbar.pack(side="right", fill="y")
            lb.pack(side="left", fill="both", expand=True)
            for i in output_list:
                s = ""
                for j in i:
                    s += str(j) + "  |   "
                lb.insert("end", s)

            mainloop()

    def get_data(self, p1: tuple, p2: list, p3: list, p4: list):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def __init__(self):
        self.win0 = Tk()
        self.win0.resizable(False, False)
        self.win0.title("Hello")
        self.win0.geometry("200x250")
        s = '''\n\n\n
         Data structures Project
            Affogato team
            Arshia Hemmat
           Amir Sharifian
          Alireza Tabatabaei
         University of Isfahan
            January 2021\n\n'''

        lb0 = Label(self.win0, text=s).pack()
        btn0 = Button(self.win0, text='let\'s go', command=self.btn0_listener).pack(side='bottom')
        mainloop()
