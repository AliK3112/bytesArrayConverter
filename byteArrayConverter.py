import struct
from tkinter import *


def attachZeros(str, n):
    while len(str) < n:
        str.append('00')
    return str


def stripArray(str, n):
    while len(str) > n:
        str.pop()
    return str


def toUInt(str, n):
    str = attachZeros(str, n)
    str = stripArray(str, n)
    temp = ""
    for i in range(0, n):
        temp += str[n-1-i]
    return int(temp, 16)


def toInt(str, n):
    str = attachZeros(str, n)
    str = stripArray(str, n)
    temp = ""
    for i in range(0, n):
        temp += str[n-1-i]
    temp = int(temp, 16)
    max = 2**(8 * n)
    return (temp - max) if temp > max//2 else temp


def toFloat(str, n):
    str = attachZeros(str, n)
    str = stripArray(str, n)
    temp = ""
    for i in range(0, n):
        temp += str[n-1-i]
    temp = bytes.fromhex(temp)
    result = struct.unpack('f', temp)
    return result[0]


root = Tk()
root.title("Array Bytes Converter")
root.minsize(400, 300)
root.maxsize(534, 400)
root.geometry('400x300')
root.iconbitmap('./myicon.ico')
header = Label(root, text="Array Bytes converter")
header.pack(side='top', fill='x')
inputBox = Entry(root)
inputBox.pack(side='top', fill='x', padx=10)
answerLabel = Label(root, text="Conversion")
answerLabel.pack(fill='x', pady=10)
outputBox = Text(root, height=1, state='disabled')
outputBox.pack(side='top', fill='x', padx=10)
conversionType = ['float', 'int32']
# Status widget
status_widget = Label(root, text='')


def Convert(type):
    value = inputBox.get()
    if value == "":
        return
    for c in value:
        if not (c.isalnum() or c == " "):
            status_widget.config(text="Invalid input")
            return
    status_widget.config(text="")
    value = value.strip()
    value = value.split(' ')

    # Checking which type of conversion to perform and performing that
    if type == 0:
        result = toFloat(value, 4)
    elif type == 1:
        result = toUInt(value, 4)
    elif type == 2:
        result = toUInt(value, 2)
    elif type == 3:
        result = toUInt(value, 1)
    elif type == 4:
        result = toInt(value, 4)
    elif type == 5:
        result = toInt(value, 2)
    elif type == 6:
        result = toInt(value, 1)
    else:
        return

    outputBox.config(state='normal')
    outputBox.delete('1.0', 'end')
    outputBox.insert('end', str(result))
    outputBox.config(state='disabled')
    # outputBox.config(result)
    return


# convertButtonFloat = Button(root, text="Float", padx=10,
#                             pady=5, fg="white", bg="#263D42", command=lambda e=0: Convert(e))
# convertButtonFloat.pack(pady=5)

buttons = []
labels = ['Float', 'UInt32', 'UInt16', 'UInt8', 'Int32', 'Int16', 'Int8']
n_buttons = len(labels)
btn_frame = Frame(root)
for i in range(0, n_buttons):
    obj = Button(btn_frame, text=labels[i], width=5, height=2, padx=10,
                 pady=5, fg="white", bg="#263D42", command=lambda e=i: Convert(e))
    # obj.pack(side='left', padx=10)
    buttons.append(obj)

# buttons[0].pack(side='left', padx=5, fill='x')
# buttons[1].pack(side='left', padx=5, fill='x')
# buttons[2].pack(side='left', padx=5, fill='x')
# buttons[3].pack(side='left', padx=5, fill='x')
# buttons[4].pack(side='left', padx=5, fill='x')
# buttons[5].pack(side='left', padx=5, fill='x')
# buttons[6].pack(side='left', padx=5, fill='x')
buttons[0].grid(row=0, column=0, padx=5, pady=5)
buttons[1].grid(row=1, column=0, padx=5, pady=5)
buttons[2].grid(row=1, column=1, padx=5, pady=5)
buttons[3].grid(row=1, column=2, padx=5, pady=5)
buttons[4].grid(row=2, column=0, padx=5, pady=5)
buttons[5].grid(row=2, column=1, padx=5, pady=5)
buttons[6].grid(row=2, column=2, padx=5, pady=5)
btn_frame.pack(side='left')

status_widget.pack(side='bottom', fill='x', anchor='sw')


def main():
    root.mainloop()
    return


if __name__ == "__main__":
    main()
