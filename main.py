from tkinter import *
from .algorithm import ANOVA 
import tkinter.messagebox as msgbox 
class Window:
    def __init__(self, master):
        self.master = master
        self.anova = ANOVA()
        self.main_master = Frame(self.master)
        self.canvas = Canvas(self.master,width=650,height = 900)
        self.Main = Frame(self.canvas,width=400,height=400)
        # TOP SECTION
        self.top = Frame(self.Main)
        self.title = Label(self.top, text = "ANOVA sheet")
        self.title.pack(padx = 5, pady = 5)
        self.top.pack(padx = 5, pady = 5)
        # TOP SECTION 
        # MIDDLE SECTION
        self.middle = Frame(self.Main)
        self.row = 11
        self.column = 12
        self.cells = [[None for i in range(self.column)] for j in
        range(self.row)]
        self.heading = [Label(self.middle, text = f"Group {x + 1}") for x in
        range(self.column)]
        self.cells[0] = self.heading
        for idx,x in enumerate(self.heading):
            x.grid(row = 0, column = idx)
        for i in range(1,self.row):
            for j in range(self.column):
                self.cells[i][j] = Entry(self.middle, width = 5) 
                self.cells[i][j].grid(row = i, column = j)
        self.middle.pack(padx = 5, pady = 5) 
# MIDDLE SECTION
        # BOTTOM SECTION
        self.bottom = Frame(self.Main)
        self.help_button = Button(self.bottom,text="Help", command =
        self.help)
        self.help_button.pack(padx = 5, pady = 5, side = RIGHT)
        self.clearButton = Button(self.bottom, text = "Clear", command =
        self.clear)
        self.clearButton.pack(padx = 5, pady = 5, side = LEFT)
        self.calButton = Button(self.bottom, text = "Calculate", command =
        self.calculate)
        self.calButton.pack(padx = 5, pady = 5, side = LEFT)
        self.bottom.pack(padx = 5, pady = 2, expand = True, fill = BOTH) 
        # BOTTOM SECTION
        self.Main.pack(padx = 5, pady = 2, expand = True, fill = X) 
        self.master.bind("<Configure>",lambda e:
        self.canvas.configure(scrollregion = self.canvas.bbox("all")))
        self.canvas.pack()
        self.canvas.create_window((0,0),window=self.main_master,anchor="nw") 
        # self.main_master.pack()
    def help(self):
        msgbox.showinfo("Anova Calculator Help",
        """The One-way ANOVA test is used to compare three or more treatment
        means using a single factor.STEPS IN USING THE CALCULATOR:
1. Enter the data or observations according to the treatments (groups) in a 
column-wise form.
2. Click on the "calculate" button to analyse the data and show result.
NOTE:
a. In this calculator, the observations are assumed to be normally 
distributed satisfying the normality assumptions.
b. The "clear" button is used to delete all observations in the filled cells.
"""
)
    def transfer_data(self):
        for i in range(self.column):
            c = []
        for j in range(1,self.row):
            block = self.cells[j][i].get() 
            if block and block.isnumeric():
                c.append(int(block))
        if c:
            self.anova.treatment.append(c)
        self.anova.num_treatment = len(self.anova.treatment) 
    def clear(self):
        for i in range(1,self.row):
            for j in range(self.column):
                self.cells[i][j].delete(0, 'end')
        for x in self.value_list:
            x.config(text="")
        self.anova.num_treatment = 0 
        self.anova.treatment = []
    def calculate(self): 
        self.open_result() 
        self.transfer_data()
        if len(self.anova.treatment) > 0:
            data, self.conclusion = self.anova.run() 
            self.display_anova(data)
        if self.conclusion:
            self.conclusion_label.config(text = "CONCLUSION: We reject H0 (accept H1) and conclude that the treatment means are not equal", fg = "red")
        else:
            self.conclusion_label.config(text = "CONCLUSION: We do notreject H0 (accept H0) and conclude that the treatment means are equal", 
            fg="green")
    def open_result(self):
        self.result_window = Toplevel(self.master,width=650,height=650) 
        self.result_window.title("Result Window")
        # Table Label
        self.table_row = 4
        self.table_column = 5
        self.table = Frame(self.result_window)
        #Packing the Anova calculation table 
        self.anova_table()
        self.table.pack(padx=5,pady=2,fill = X) 
        # writeup section
        self.writeup = self.anova_writeup()
        self.writeup_label = Label(self.result_window, text = 
        "\n".join(self.writeup),anchor="w",justify='left')

root = Tk()
window = Window(root)
root.mainloop()