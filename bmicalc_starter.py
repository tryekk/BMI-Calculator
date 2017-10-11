from Tkinter import *


class MyApp(object):
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("BMI Calculator")
        self.root.geometry('420x470+300+200')
        self.label = Label(self.root, text="Calculate your BMI",
                           font=('Helvetica', 20, 'bold'))
        self.label.pack(padx=20, pady=10)

        self.labeltext = StringVar()
        self.labeltext.set("--")
        Label(self.root, textvariable=self.labeltext, font=('Helvetica', 15, 'bold')).pack()

        self.targettext2 = StringVar()
        self.targettext2.set("")
        Label(self.root, textvariable=self.targettext2, font=('Helvetica', 13, 'bold')).pack()

        self.targettext = StringVar()
        self.targettext.set("Please fill in all the fields")
        Label(self.root, textvariable=self.targettext, font=('Helvetica', 13, 'bold')).pack()

        self.targettime = StringVar()
        self.targettime.set("")
        Label(self.root, textvariable=self.targettime, font=('Helvetica', 13, 'bold')).pack()

        self.filler = StringVar()
        self.filler.set("")
        Label(self.root, textvariable=self.filler).pack()

        self.labeltext0 = StringVar()
        self.labeltext0.set("Use imperial (Y/N)")
        Label(self.root, textvariable=self.labeltext0).pack()
        self.entrytext0 = StringVar()
        Entry(self.root, textvariable=self.entrytext0).pack()
        self.entrytext0.trace('w', self.entry_changed)
        self.entrytext0.trace('w', self.target_data)

        self.labeltext1 = StringVar()
        self.labeltext1.set("Enter Height")
        Label(self.root, textvariable=self.labeltext1).pack()
        self.entrytext1 = StringVar()
        Entry(self.root, textvariable=self.entrytext1).pack()
        self.entrytext1.trace('w', self.entry_changed)
        self.entrytext1.trace('w', self.target_data)

        self.labeltext2 = StringVar()
        self.labeltext2.set("Enter Weight")
        Label(self.root, textvariable=self.labeltext2).pack()
        self.entrytext2 = StringVar()
        Entry(self.root, textvariable=self.entrytext2).pack()
        self.entrytext2.trace('w', self.entry_changed)
        self.entrytext2.trace('w', self.target_data)

        self.labeltext3 = StringVar()
        self.labeltext3.set("Target BMI*")
        Label(self.root, textvariable=self.labeltext3).pack()
        self.entrytext3 = StringVar()
        Entry(self.root, textvariable=self.entrytext3).pack()
        self.entrytext3.trace('w', self.target_data)

        self.timetext = StringVar()
        self.timetext.set("How long to reach goal (Weeks)*")
        Label(self.root, textvariable=self.timetext).pack()
        self.entrytime = StringVar()
        Entry(self.root, textvariable=self.entrytime).pack()
        self.entrytime.trace('w', self.target_data)

        self.filler = StringVar()
        self.filler.set("")
        Label(self.root, textvariable=self.filler).pack()

        self.option = StringVar()
        self.option.set("* Optional")
        Label(self.root, textvariable=self.option, font=('Helvetica', 12, 'bold')).pack()

        self.root.mainloop()

    def entry_changed(self, a, b, c):
        try:
            imperial = str(self.entrytext0.get())
            height = float(self.entrytext1.get())
            mass = float(self.entrytext2.get())
        except ValueError:
            self.labeltext.set("--")
            return
        height = float(height)
        mass = float(mass)

        self.c_i = (mass / (height ** 2)) * 703
        self.c_m = ((mass / height) / height) * 10000
        self.c_i = float(self.c_i)
        self.c_m = float(self.c_m)

        if imperial == "y":
            self.labeltext.set('BMI: %.2f' % self.c_i)
        else:
            self.labeltext.set('BMI: %.2f' % self.c_m)

    def target_data(self, a, b, c):
        try:
            imperial = str(self.entrytext0.get())
            height = float(self.entrytext1.get())
            mass = float(self.entrytext2.get())
            target_bmi = float(self.entrytext3.get())
            target_time = float(self.entrytime.get())
        except ValueError:
            self.targettime.set('')
            self.targettext.set('')
            self.targettext2.set('')
            return

        self.c_i = (mass / (height ** 2)) * 703
        self.c_m = ((mass / height) / height) * 10000
        self.c_i = float(self.c_i)
        self.c_m = float(self.c_m)

        target_i = (target_bmi * (height ** 2)) / 703
        lose_target_i = mass - target_i
        gain_target_i = target_i - mass
        target_m = ((target_bmi * height) * height) / 10000
        lose_target_m = mass - target_m
        gain_target_m = target_m - mass

        lose_time_i = (lose_target_i / target_time)
        gain_time_i = (gain_target_i / target_time)
        lose_time_m = (lose_target_m / target_time)
        gain_time_m = (gain_target_m / target_time)

        if imperial == "y":
            if self.c_i > target_bmi:
                self.targettext.set('You are {:.2f} pounds off your goal'.format(lose_target_i))
                self.targettext2.set('Your target weight is {:.2f} pounds'.format(target_i))
                self.targettime.set('You need to lose {:.2f} pounds / week'.format(lose_time_i))
            else:
                self.targettext.set('You are {:.2f} pounds off your goal'.format(gain_target_i))
                self.targettext2.set('Your target weight is {:.2f} pounds'.format(target_i))
                self.targettime.set('You need to gain {:.2f} pounds / week'.format(gain_time_i))
        else:
            if self.c_m > target_bmi:
                self.targettext.set('You are {:.2f} kilos off your goal'.format(lose_target_m))
                self.targettext2.set('Your target weight is {:.2f} kilos'.format(target_m))
                self.targettime.set('You need to lose {:.2f} kilos / week'.format(lose_time_m))
            else:
                self.targettext.set('You are {:.2f} kilos off your goal'.format(gain_target_m))
                self.targettext2.set('Your target weight is {:.2f} kilos'.format(target_m))
                self.targettime.set('You need to gain {:.2f} kilos / week'.format(gain_time_m))

MyApp()
