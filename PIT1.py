import tkinter as ayawkol

def convert_length():
    try:
        input_value = float(input_entry.get())
        selection = choice_var.get()

        if selection == '1':
            inch_to_cm = 2.54
            conversion = input_value * inch_to_cm
        elif selection == '2':
            cm_to_inch = 0.3937
            conversion = input_value * cm_to_inch
        else:
            result_label.config(text='Invalid Selection. Please choose 1 or 2.')
            return

        result_label.config(text=f"Result: {input_value} {'inches' if selection == '1' else 'centimeters'} is equal to {conversion:.2f} {'centimeters' if selection == '1' else 'inches'}")
    except ValueError:
        result_label.config(text='Invalid input. Please enter a valid number.')

app = ayawkol.Tk()
app.title("Length Converter")

choice_var = ayawkol.StringVar()
choice_var.set('1')

choice_label = ayawkol.Label(app, text="Select your choice:")
choice_label.pack()

inch_radio = ayawkol.Radiobutton(app, text="Inches to Centimeters", variable=choice_var, value='1')
inch_radio.pack()
cm_radio = ayawkol.Radiobutton(app, text="Centimeters to Inches", variable=choice_var, value='2')
cm_radio.pack()

input_label = ayawkol.Label(app, text="Enter value and choose the conversion type:")
input_label.pack()

input_entry = ayawkol.Entry(app)
input_entry.pack()

convert_button = ayawkol.Button(app, text="Convert", command=convert_length)
convert_button.pack()

result_label = ayawkol.Label(app, text="")
result_label.pack()

app.mainloop()
