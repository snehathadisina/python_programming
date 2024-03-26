import tkinter as tk
A=tk.Tk()
A.title("BMI Calculator")
def calculate_bmi():
    age=int(age_entry.get())
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    height_in_meters=height/100
    bmi = weight / (height_in_meters ** 2)
    result_label.config(text=f"Your BMI is: {bmi:.2f}")


    if bmi<16:
        ch=tk.Label(A,text="you are severely underweight")
        ch.pack()
    elif bmi>=16 and bmi<18.5:
        ch=tk.Label(A,text="you are underweight")
        ch.pack()
    elif bmi>=18.5 and bmi<=24:
        ch=tk.Label(A,text="you are healthy")
        ch.pack()
    elif bmi>=25 and bmi<30:
        ch=tk.Label(A,text="you are overweight")
        ch.pack()
    else:
        ch=tk.Label(A,text="you are obese range")
        ch.pack()

#A = tk.Tk()
#A.title("BMI Calculator")

frame = tk.Frame(A)
frame.pack(padx=10, pady=10)

age_label = tk.Label(frame, text="Enter your age (2-100):")
age_label.grid(row=0, column=0, padx=4, pady=4)

age_entry = tk.Entry(frame)
age_entry.grid(row=0, column=1, padx=4, pady=4)


weight_label = tk.Label(frame, text="Enter your weight (kg):")
weight_label.grid(row=1, column=0, padx=4, pady=4)

weight_entry = tk.Entry(frame)
weight_entry.grid(row=1, column=1, padx=4, pady=4)

height_label = tk.Label(frame, text="Enter your height(centimeters):")
height_label.grid(row=2, column=0, padx=4, pady=4)

height_entry = tk.Entry(frame)
height_entry.grid(row=2, column=1, padx=4, pady=4)

calculate_button = tk.Button(frame, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=3, columnspan=3, padx=4, pady=4)

result_label = tk.Label(frame, text="")
result_label.grid(row=4, columnspan=3, padx=4, pady=4)

A.mainloop()
