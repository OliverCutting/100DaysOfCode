from tkinter import *

app = Tk()

app.title("Mile to Km Converter")
app.minsize(width=300, height=200)
app.config(padx=20, pady=20)

title = Label(text="Converter", font=("Arial", 24)).grid(column=1, row=0)

def callback(sv):
  miles_to_km()

def miles_to_km():
  conversion = float(miles_input.get()) * 1.689
  km_result_label.config(text=f"{conversion}")

sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
miles_input = Entry(textvariable=sv)
miles_label = Label(text="Miles", font=("Arial", 18)).grid(column=2, row=1)
miles_input.grid(column=1, row=1)
miles_input.insert(END, "1")

is_equal_label = Label(text="is equal to").grid(column=0, row=2)
km_result_label = Label(text="1.689")
km_result_label.grid(column=1, row=2)
km_label = Label(text="Km").grid(column=2, row=2)

app.mainloop()