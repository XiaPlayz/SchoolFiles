import tkinter as tk

def convert_length(*args):
    try:
        input_value = float(input_var.get())
        selection = choice_var.get()

        if selection == '1':
            inch_to_cm = 2.54
            conversion = input_value * inch_to_cm
        elif selection == '2':
            cm_to_inch = 0.3937
            conversion = input_value * cm_to_inch
        else:
            result_text.config(state=tk.NORMAL)
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, 'Invalid Selection. Please choose 1 or 2.')
            result_text.config(state=tk.DISABLED)
            return

        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"{input_value} {'inches' if selection == '1' else 'centimeters'} is equal to {conversion:.2f} {'centimeters' if selection == '1' else 'inches'}")
        result_text.config(state=tk.DISABLED)
    except ValueError:
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, 'Invalid input. Please enter a valid number.')
        result_text.config(state=tk.DISABLED)

def on_choice_change(*args):
    convert_length()

app = tk.Tk()
app.title("Length Converter")
app.resizable(False, False)

choice_var = tk.StringVar()
choice_var.set('1')
choice_var.trace("w", on_choice_change)

img = tk.PhotoImage(file='C:/Users/benji/Desktop/My Fucking Files/Python Shits/ruler.png')
app.iconphoto(False, img)

choice_label = tk.Label(app, text="Select your choice:")
choice_label.pack()

inch_radio = tk.Radiobutton(app, text="Inches to Centimeters", variable=choice_var, value='1')
inch_radio.pack()
cm_radio = tk.Radiobutton(app, text="Centimeters to Inches", variable=choice_var, value='2')
cm_radio.pack()

input_label = tk.Label(app, text="Enter value and choose the conversion type:")
input_label.pack()

input_var = tk.StringVar()
input_var.trace("w", on_choice_change)

input_entry = tk.Entry(app, textvariable=input_var)
input_entry.pack()

result_label = tk.Label(app, text="Result")
result_label.pack()
result_text = tk.Text(app, height=2, width=40, state=tk.DISABLED)
result_text.pack()

app.mainloop()