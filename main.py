from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess

compiler = Tk()
compiler.title("New IDE for programmer.")
file_path = ''

def setPath(path):
    global file_path 
    file_path = path

def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    codeOutput.insert('1.0', output)
    codeOutput.insert('1.0',  error) 
    # code = editor.get('1.0',END)
    # exec(code)

def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files','*.py')])
    else:
        path = file_path
    with open(path,'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        setPath(path)

def openFile():
    path = askopenfilename(filetypes=[('Python Files','*.py')])
    with open(path,'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        setPath(path)

menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open',command=openFile)
file_menu.add_command(label='Save',command=save_as)
file_menu.add_command(label='Save As',command=save_as)
file_menu.add_command(label='Exit',command=exit)

menu_bar.add_cascade(label='File', menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run',command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)

compiler.config(menu=menu_bar)

editor = Text()
editor.pack()

codeOutput = Text(height=10)
codeOutput.pack()

compiler.mainloop()