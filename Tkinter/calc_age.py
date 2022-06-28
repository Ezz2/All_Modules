# By Ezz

from tkinter import *
from tkinter import messagebox

# Create App Wondow
age_app = Tk()

# Change App Title
age_app.title("Calculate Age")

# Set Dimenstions
age_app.geometry("400x200")

# Age Label
the_text = Label(age_app, text="Write Your Age", height=2, font=("Arial", 20))
the_text.pack() # Place The Text Into The Main Window

# Age Variable
age = StringVar()

# Set Defaul Value For Age
age.set("00")

# Create The Input For Age
age_input = Entry(age_app, width=2, font=("Arial", 30), textvariable=age)
age_input.pack()

def calc():

   # Get Age In Years
   the_age_value = age.get()

   # Get times Units

   months = int(the_age_value) * 12
   weeks = months * 4
   days = int(the_age_value) * 365

   line_one = f"Your Age In Months Is: {months}"
   line_two = f"Your Age In Weeks Is: {weeks}"
   line_three = f"Your Age In Day Is: {days}"

   print(line_one)
   print(line_two)
   print(line_three)

   open('D:\ezz.programing\python\All_Modules\Tkinter\Tkinter.txt', 'a').write('Age: ' + the_age_value+'\n')
   open('D:\ezz.programing\python\All_Modules\Tkinter\Tkinter.txt', 'a').write('Months: ' + line_one+'\n')
   open('D:\ezz.programing\python\All_Modules\Tkinter\Tkinter.txt', 'a').write('Weeks: ' + line_two+'\n')
   open('D:\ezz.programing\python\All_Modules\Tkinter\Tkinter.txt', 'a').write('Days: ' + line_three+'\n')


   all_line = [line_one, line_two, line_three]

   messagebox.showinfo("Your Age In All Time Units", "\n".join(all_line))

# Create the Calculate Buttom
btn = Button(age_app, text="Calculate Age", width=20, height=2, bg="#e91e63", fg="White", borderwidth=0, command=calc)
btn.pack()

# Run App Infinity
age_app.mainloop()
