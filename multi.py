from tkinter import Label, Button, Entry, OptionMenu, IntVar, StringVar, Frame, Toplevel
from tkinter.constants import BOTH
import menu

alphabet = 'abcdefghijklmnopqrstuvwxyz'


class Multi:
    def back_to_menu(self):
        self.gui_multi_output.destroy()
        menu.gui_menu.deiconify()

    def compute_product(self):
        pass

    def output_matrix(self):
        # create window
        self.gui_multi_input.destroy()
        self.gui_multi_output = Toplevel()
        self.gui_multi_output.title("Inverse")
        self.gui_multi_output.resizable(False, False)

        self.frame_multi_output = Frame(self.gui_multi_output, highlightbackground='black', highlightthickness=1)
        self.frame_multi_output.pack(fill=BOTH, expand=True, padx=5, pady=5)

        self.gui_multi_output.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_multi_output.mainloop()

    def input_matrix(self):
        self.gui_multi_menu.destroy()
        self.gui_multi_input = Toplevel()
        self.gui_multi_input.title("Inverse")
        self.gui_multi_input.resizable(False, False)

        self.frame_multi_input = Frame(self.gui_multi_input, highlightbackground='black', highlightthickness=1)
        self.frame_multi_input.pack(fill=BOTH, expand=True, padx=5, pady=5)
        # window_dimensions = str(self.m_length.get()**3+90) + "x" + str(self.m_height.get())
        # print(window_dimensions)
        # window.geometry(window_dimensions)
        # self.gui_inverse_input.resizable(False, False)

        Label(self.frame_multi_input, text="Enter matrix A:", font=('arial', 10, 'bold')).grid(row=1, column=1)

        # to create matrix of entry cells we need to create a 2d list of entries
        # thank god to stackoverflow peeps for that

        # empty arrays for Entry and StringVars
        text_var = []
        entries = []

        self.rows_a, self.cols_a = (self.ma_rows.get(), self.ma_cols.get())
        for i in range(self.rows_a):
            # append an empty list to arrays to append to later
            text_var.append([])
            entries.append([])
            for j in range(self.cols_a):
                # for column indications
                if i == 1:
                    Label(self.frame_multi_input, text=alphabet[j]).grid(row=1, column=j + 2)

                # append StringVar
                text_var[i].append(StringVar())

                # append the entry into the list
                entries[i].append(Entry(self.frame_multi_input, textvariable=text_var[i][j], width=3))

                # display entry
                entries[i][j].grid(row=i + 2, column=j + 2)

                # for row indications
                Label(self.frame_multi_input, text=i + 1).grid(row=i + 2, column=1, sticky='e')

        Label(self.frame_multi_input, text="Enter matrix B:", font=('arial', 10, 'bold')).grid(row=self.rows_a * 2,
                                                                                               column=1)

        # to create matrix of entry cells we need to create a 2d list of entries

        # empty arrays for Entry and StringVars
        text_var_b = []
        entries_b = []

        self.rows_b, self.cols_b = (self.ma_cols.get(), self.mb_cols.get())
        for i in range(self.rows_b):
            print(i)
            # append an empty list to arrays to append to later
            text_var_b.append([])
            entries_b.append([])
            for j in range(self.cols_b):
                # for column indications
                if i == 1:
                    Label(self.frame_multi_input, text=alphabet[j]).grid(row=self.rows_a * 2, column=j + 2)

                # append StringVar
                text_var_b[i].append(StringVar())

                # append the entry into the list
                entries_b[i].append(Entry(self.frame_multi_input, textvariable=text_var_b[i][j], width=3))

                # display entry
                entries_b[i][j].grid(row=i + self.rows_a + 5, column=j + 2)

                # for row indications
                Label(self.frame_multi_input, text=i + 1).grid(row=i + self.rows_a + 5, column=1, sticky='e')

        # callback function to get StringVars/convert them to strings
        # and store in matrix[]

        # def get_mat():
        #     self.matrix = []
        #     for i2 in range(self.rows_a):
        #         self.matrix.append([])
        #         for j2 in range(self.cols_a):
        #             self.matrix[i2].append(text_var[i2][j2].get())
        #     print(self.matrix)

        Button(self.frame_multi_input, text="Enter", width=8).grid(row=self.cols_a + self.cols_b + 10,
                                                                   column=1)

        self.gui_multi_input.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_multi_input.mainloop()

    def __init__(self):
        self.matrix = None
        self.gui_multi_input = None
        self.frame_multi_input = None
        self.rows_a, self.cols_a = None, None
        self.rows_b, self.cols_b = None, None
        self.gui_multi_output = None
        self.frame_multi_output = None

        menu.gui_menu.withdraw()
        self.gui_multi_menu = Toplevel()
        self.gui_multi_menu.title("Multiply")
        self.gui_multi_menu.resizable(False, False)

        self.frame_multi_menu = Frame(self.gui_multi_menu, highlightbackground='black', highlightthickness=1)
        self.frame_multi_menu.pack(fill=BOTH, expand=True, padx=5, pady=5)

        # inputs
        # Label(self.frame_multi_menu, text='NOTE: Matrix A height and Matrix B length').grid(row=1, column=1, columnspan=6)
        # Label(self.frame_multi_menu, text='...are to be equal for multiplication').grid(row=2, column=1, columnspan=6)
        # A matrix
        Label(self.frame_multi_menu, text='Matrix A dimensions:', font=('arial', 10, 'bold')).grid(row=3, column=1,
                                                                                                   columnspan=1)
        Label(self.frame_multi_menu, text='Matrix B dimensions:', font=('arial', 10, 'bold')).grid(row=4, column=1,
                                                                                                   columnspan=1)

        self.ma_rows = IntVar()
        self.ma_rows.set(2)
        OptionMenu(self.frame_multi_menu, self.ma_rows, *range(2, 5)).grid(row=3, column=2)

        Label(self.frame_multi_menu, text='x').grid(row=3, column=3)

        self.ma_cols = IntVar()
        self.ma_cols.set(2)
        OptionMenu(self.frame_multi_menu, self.ma_cols, *range(2, 5)).grid(row=3, column=4)

        # B matrix
        self.mb_rows = IntVar()
        # self.mb_rows.set(self.ma_cols.get())
        Label(self.frame_multi_menu, text="[n]", font=('arial', 10, 'bold'), padx=5, pady=5).grid(row=4, column=2)
        # OptionMenu(self.frame_multi_menu, self.mb_rows, *range(2, 16)).grid(row=2, column=2)

        Label(self.frame_multi_menu, text='x').grid(row=4, column=3)

        self.mb_cols = IntVar()
        self.mb_cols.set(2)
        OptionMenu(self.frame_multi_menu, self.mb_cols, *range(2, 5)).grid(row=4, column=4)

        Button(self.frame_multi_menu, text='Enter', padx=16, pady=5, command=self.input_matrix).grid(row=5, column=4)

        self.gui_multi_menu.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_multi_menu.mainloop()