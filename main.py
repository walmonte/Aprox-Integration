# The gui is based in a tkinter tutorial found at: https://www.geeksforgeeks.org/python-tkinter-entry-widget/
# Developed by: Willian Almonte

import tkinter as tk
from tkinter import messagebox
import aproximation_rules

def handle_focus_in(_):
    interval_entry.delete(0, tk.END)
    interval_entry.config(fg='black')

def handle_focus_out(_):
    interval_entry.delete(0, tk.END)
    interval_entry.config(fg='grey')
    interval_entry.insert(0, "Simply enter a,b")

def handle_enter(txt):
    print(interval_entry.get())
    handle_focus_out('')

def clear_entries():
    
    func_var.set("") 
    interval_var.set("")
    n_var.set("") 

    interval_entry.delete(0, 'end')
    interval_entry.insert(0, 'Simply enter a,b')

def prompt_error():
    tk.messagebox.showerror(title='Input error', message='Invalid input. Please try again')
    clear_entries()

def compute(): 

    func_str = ''
    interval = [] # x values between which we want to calculate the area (usually refered as 'a' and 'b')
    n = 0 #  number of rectangles/partitions
   
    try:
        func_str = func_entry.get()
        error_catcher = [ eval(func_str) for x in range(1)]
        print('Function read OK') 

        for word in (interval_entry.get()).split(','):
            if word.isdigit():
                interval.append(int(word))
        print('Interval read OK') 
        n = n_entry.get()
        n = int(n)

        if len(interval) != 2:
            prompt_error()
    except:
        prompt_error()

    m, t, s = aproximation_rules.compute(n, interval, func_str)

    m_label2.configure(text=m)
    t_label2.configure(text=t)
    s_label2.configure(text=s)
    clear_entries()
    print('compute() OK')

# ------------------------------------
# Set up a new window with two frames
window=tk.Tk() 
window.title("Aproximate Integral Calculator")
window.geometry("600x210") # sets the window's size 

# Instructions frame
instruct_frame = tk.Frame(window)
instruct_frame.pack(side='left', fill='both', expand=1)

# Calculator frame
calc_frame = tk.Frame(window)
calc_frame.pack(side='right',fill="both", expand=1)

# Declare string variable to store the user inputs
func_var=tk.StringVar() 
interval_var=tk.StringVar()
n_var=tk.StringVar() 

# -----------------------------------------
# Define all objects in the window

# Instructions Label, contains notes on how to use the program
instruct_msg = ("Hello, this is a calculator built to compute aproximate integration. \n\nSimply enter the function to be integrated, the interval to be analized, and the number of partitions. Please pay close attention to parenthesis and the Python version of math expressions such as: \n\n2^4 --> pow(2,4) \nsqrt(x) --> pow(x,1/2) \n2x --> 2*x")
instructions_label = tk.Label(instruct_frame, text=instruct_msg, font=('calibre',10), wraplength=250, justify='left')

# Input labels and antries

# labels
func_label = tk.Label(calc_frame, text = 'Function f(x)', font=('calibre',10))
interval_label = tk.Label(calc_frame, text = 'Interval [a,b]', font = ('calibre',10))
n_label = tk.Label(calc_frame, text = 'No. of partitions', font = ('calibre',10)) 

# entries
func_entry = tk.Entry(calc_frame, textvariable = func_var, font=('calibre',10,'normal'))
interval_entry=tk.Entry(calc_frame, textvariable = interval_var, text='[a,b] simply enter a,b', font = ('calibre',10))
n_entry=tk.Entry(calc_frame, textvariable = n_var, font = ('calibre',10,'normal')) 

# creating the Result label(s)

# Defining labels for the result ---> m = midpoint; t = trap; s= simpson's
m_label1 = tk.Label(calc_frame, text="Midpoint Rule =",font=('calibre',10))
t_label1 = tk.Label(calc_frame, text="Trapezoidal Rule =",font=('calibre',10))
s_label1 = tk.Label(calc_frame, text="Simpson's Rule =",font=('calibre',10))
m_label2 = tk.Label(calc_frame,font = ('calibre',10,'bold'))
t_label2 = tk.Label(calc_frame,font = ('calibre',10,'bold'))
s_label2 =  tk.Label(calc_frame,font = ('calibre',10,'bold'))

# Button; calls the compute function  
sub_btn = tk.Button(calc_frame,text = 'Compute', command = compute) 

#-------------------------------------------------------------
# Place the labels, entries, and buttons in position with grid()
 
# Instructions section
instructions_label.grid(row=0,column=0, sticky='W', pady=3, padx=15)

# Inputs Section
func_label.grid(sticky='W',row=0,column=0,pady=3, padx=2) 
func_entry.grid(row=0,column=1,pady=3, padx=2) 
interval_label.grid(sticky='W',row=1,column=0,pady=3, padx=2) 
interval_entry.grid(row=1,column=1,pady=3, padx=2)
interval_entry.insert(0, 'Simply enter a,b')
interval_entry.bind("<FocusIn>", handle_focus_in)
interval_entry.bind("<Return>", handle_enter)
n_label.grid(sticky='W',row=2,column=0,pady=3, padx=2)
n_entry.grid(row=2,column=1,pady=3, padx=2) 

# Results section
m_label1.grid(row=4,column=0,sticky='W',pady=3, padx=2)
t_label1.grid(row=5,column=0,sticky='W',pady=3, padx=2)
s_label1.grid(row=6,column=0,sticky='W',pady=3, padx=2)
m_label2.grid(row=4,column=1,sticky='W',pady=3, padx=2)
t_label2.grid(row=5,column=1,sticky='W',pady=3, padx=2)
s_label2.grid(row=6,column=1,sticky='W',pady=3, padx=2)

# 'Compute' button
sub_btn.grid(row=3,column=1,pady=3, padx=2)

if __name__ == "__main__":
    # infinite loop for the window to display 
    window.mainloop()
