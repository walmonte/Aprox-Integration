# The gui is based in a tkinter tutorial found at: https://www.geeksforgeeks.org/python-tkinter-entry-widget/
import tkinter as tk
from tkinter import messagebox
from math import pow, cos, pi
from aproximation_rules import mid_rule, trap_rule, simpsons_rule

my_func = ''
interval = [] # x values between which we want to calculate the area (usually refered as 'a' and 'b')
n = 0 #  number of rectangles/partitions

def f_of_x(x_values):
    # TODO: take a function from the user
    result = []
    for i in range(0, len(x_values)):
        x = x_values[i]
        result.append( pow(1+(cos(x)), 1/3) )
    
    return result

# GUI------------------------------------------------------------------
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
   
    try:
        my_func = func_entry.get()
        print('func ok') 

        for word in (interval_entry.get()).split(','):
            if word.isdigit():
                interval.append(int(word))
        print('inetrval ok') 
        n = n_entry.get()
        n = int(n)

        if len(interval) != 2:
            prompt_error()
    except:
        prompt_error()
    
    m = round(mid_rule(n, interval, f_of_x), 6)
    t = round(trap_rule(n, interval, f_of_x), 6)
    s = round(simpsons_rule(n, interval, f_of_x), 6)
    m_label2.configure(text=m)
    t_label2.configure(text=t)
    s_label2.configure(text=s)
    clear_entries()
    print('OK')

window=tk.Tk() 
window.title("Aproximate Integral Calculator")
window.geometry("500x300") # sets the window's size 
calc_frame = tk.Frame(window)
calc_frame.pack(side='bottom')
instruct_frame = tk.Frame(window)
instruct_frame.pack(side='top',expand=True)

# declaring string variable to store the inputs
func_var=tk.StringVar() 
interval_var=tk.StringVar()
n_var=tk.StringVar() 
   
# label for the function
func_label = tk.Label(calc_frame, text = 'Function f(x)', 
                      font=('calibre', 
                            10)) 
   
# input for the function
func_entry = tk.Entry(calc_frame, 
                      textvariable = func_var,
                      font=('calibre',10,'normal')) 
   
# creating a label for the interval 
interval_label = tk.Label(calc_frame, 
                       text = 'Interval [a,b]', 
                       font = ('calibre',10)) 
   
# creating a entry for the interval 
interval_entry=tk.Entry(calc_frame, 
                     textvariable = interval_var, 
                     text='[a,b] simply enter a,b',
                     font = ('calibre',10)) 
   
# creating a label for n (# of rectangles/partitions) 
n_label = tk.Label(calc_frame, 
                       text = 'No. of partitions', 
                       font = ('calibre',10)) 
   
# creating a entry for n 
n_entry=tk.Entry(calc_frame, 
                     textvariable = n_var, 
                     font = ('calibre',10,'normal')) 

# creating the Result label(s)

# Defining labels for the result ---> m = midpoint; t = trap; s= simpson's
m_label1 = tk.Label(calc_frame, text="Midpoint Rule =",font=('calibre',10))
t_label1 = tk.Label(calc_frame, text="Trapezoidal Rule =",font=('calibre',10))
s_label1 = tk.Label(calc_frame, text="Simpson's Rule =",font=('calibre',10))
m_label2 = tk.Label(calc_frame,font = ('calibre',10,'bold'))
t_label2 = tk.Label(calc_frame,font = ('calibre',10,'bold'))
s_label2 =  tk.Label(calc_frame,font = ('calibre',10,'bold'))

# Button that will call the compute function  
sub_btn=tk.Button(calc_frame,text = 'Compute', 
                  command = compute) 

instruct_msg = ("Hello, this is a calculator built to compute aproximate integration."+
                "\nSimply enter the function to be integrated as well as the interval"+
                "\nto be analized and the number of partitions. Please use note that"+
                "\nthe '^' operand does not work, use pow(base, exp) instead. Also"+
                "\nnote that the square root of x can be written as pow(x,1/2).")

# Label with extra notes on how to use the program
instructions_label = tk.Label(instruct_frame, text=instruct_msg,font=('calibre',10))
   
# placing the label and entry in position using grid method 
func_label.grid(sticky='W',row=0,column=0,pady=3, padx=2) 
func_entry.grid(row=0,column=1,pady=3, padx=2) 
interval_label.grid(sticky='W',row=1,column=0,pady=3, padx=2) 
interval_entry.grid(row=1,column=1,pady=3, padx=2)
interval_entry.insert(0, 'Simply enter a,b')
interval_entry.bind("<FocusIn>", handle_focus_in)
interval_entry.bind("<Return>", handle_enter)
n_label.grid(sticky='W',row=2,column=0,pady=3, padx=2)
n_entry.grid(row=2,column=1,pady=3, padx=2) 
sub_btn.grid(row=3,column=1,pady=3, padx=2)
#result_label1.grid(row=4,column=0)
m_label1.grid(row=4,column=0,sticky='W',pady=3, padx=2)
t_label1.grid(row=5,column=0,sticky='W',pady=3, padx=2)
s_label1.grid(row=6,column=0,sticky='W',pady=3, padx=2)
m_label2.grid(row=4,column=1,sticky='W',pady=3, padx=2)
t_label2.grid(row=5,column=1,sticky='W',pady=3, padx=2)
s_label2.grid(row=6,column=1,sticky='W',pady=3, padx=2)

#calc_frame.grid()
#frame.grid()
instructions_label.grid(row=0,column=0, sticky='W', pady=5)


# infinite loop for the window to display 
calc_frame.mainloop() 