import Pyro4
import tkinter as Tk
from tkinter import ttk
#import matplotlim_venn

calc = Pyro4.Proxy("PYRONAME:juanfe.com")


class Calculator:
    ''' main class that constructs the calc and preforms the calculations '''

    def __init__(self, master):
        # Variables globales necesarias a lo largo de un solo cálculo.
        self.top_string = ''  # cadena para la etiqueta en la parte superior de la calculadora
        self.number1 = 0  # almacenamiento del primer número seleccionado
        self.number2 = 0  # almacenamiento del segundo número seleccionado
        self.add = False  # + boolean
        self.subtract = False  # - boolean
        self.multiply = False  # x boolean
        self.divide = False  # / boolean
        self.conjuntos = False

        # Diseño de etiqueta superior
        self.label = Tk.Label(master, text='0', bg='black', fg='white', height=2, width=4)
        self.label.grid(row=0, column=0, columnspan=4, sticky=Tk.N + Tk.E + Tk.S + Tk.W)
        self.label.config(font='Verdana 16 bold')

        # Button Layout
        Tk.Button(master, text='1', height=2, width=6, command=lambda: self.number_pressed(1)).grid(row=1, column=0)
        Tk.Button(master, text='2', height=2, width=6, command=lambda: self.number_pressed(2)).grid(row=1, column=1)
        Tk.Button(master, text='3', height=2, width=6, command=lambda: self.number_pressed(3)).grid(row=1, column=2)
        Tk.Button(master, text='4', height=2, width=6, command=lambda: self.number_pressed(4)).grid(row=2, column=0)
        Tk.Button(master, text='5', height=2, width=6, command=lambda: self.number_pressed(5)).grid(row=2, column=1)
        Tk.Button(master, text='6', height=2, width=6, command=lambda: self.number_pressed(6)).grid(row=2, column=2)
        Tk.Button(master, text='7', height=2, width=6, command=lambda: self.number_pressed(7)).grid(row=3, column=0)
        Tk.Button(master, text='8', height=2, width=6, command=lambda: self.number_pressed(8)).grid(row=3, column=1)
        Tk.Button(master, text='9', height=2, width=6, command=lambda: self.number_pressed(9)).grid(row=3, column=2)
        Tk.Button(master, text='0', command=lambda: self.number_pressed(0)).grid(row=4, columnspan=2,
                                                                                 sticky=Tk.N + Tk.E + Tk.S + Tk.W)
        Tk.Button(master, text='+', height=2, width=6, command=lambda: self.sign_pressed("+")).grid(row=1, column=3)
        Tk.Button(master, text='-', height=2, width=6, command=lambda: self.sign_pressed("-")).grid(row=2, column=3)
        Tk.Button(master, text='x', height=2, width=6, command=lambda: self.sign_pressed("*")).grid(row=3, column=3)
        Tk.Button(master, text='/', height=2, width=6, command=lambda: self.sign_pressed("/")).grid(row=4, column=3)
        Tk.Button(master, text='C', height=2, width=6, command=self.clear_all).grid(row=4, column=2)
        Tk.Button(master, text='=', height=2, command=self.equals).grid(row=5, columnspan=4,
                                                                        sticky=Tk.N + Tk.E + Tk.S + Tk.W)
        Tk.Button(master, text='CONJUNTOS', height=2, command=self.Conjuntos).grid(row=6, columnspan=4,
                                                                                sticky=Tk.N + Tk.E + Tk.S + Tk.W)

    def number_pressed(self, button_number):
        ''' Esta función se activa cuando se pulsan los botones 0 - 9'''
        if self.number1 is 0 and not any([self.add, self.subtract, self.multiply, self.divide]):
            self.number1 = button_number
            self.top_string = str(button_number)
            self.label.config(text=str(button_number))

        elif self.number1 is not 0 and not any([self.add, self.subtract, self.multiply, self.divide]):
            self.top_string += str(button_number)
            self.number1 = int(self.top_string)
            self.label.config(text=self.top_string)

        elif self.number2 is 0:
            self.number2 = button_number
            self.top_string = str(button_number)
            self.label.config(text=str(button_number))

        elif self.number1 is not 0:
            self.top_string += str(button_number)
            self.number2 = int(self.top_string)
            self.label.config(text=self.top_string)

    def sign_pressed(self, sign):
        ''' Esta función se activa cuando se presiona +, -, * o /. Las primeras comprobaciones num1 y num2 ya están almacenadas.
        Si es así, realiza un num1 igual al total, luego muestra num1, luego restablece el signo al último en que se presionó.
        Lo que permite multiplicar los cálculos antes de presionar el botón = '''
        if self.number2 is not 0 and self.number1 is not 0:
            self.number1 = self.equals()
            self.label.config(text=str(self.number1))
            self.top_string = ''
        if sign is "+":
            self.add = True
            self.subtract = False  # - boolean
            self.multiply = False  # x boolean
            self.divide = False
        if sign is "-":
            self.add = False
            self.subtract = True  # - boolean
            self.multiply = False  # x boolean
            self.divide = False
        if sign is "*":
            self.add = False
            self.subtract = False  # - boolean
            self.multiply = True  # x boolean
            self.divide = False
        if sign is "/":
            self.add = False
            self.subtract = False  # - boolean
            self.multiply = False  # x boolean
            self.divide = True
        else:
            if sign is "+":
                self.add = True
            if sign is "-":
                self.subtract = True
            if sign is "*":
                self.multiply = True
            if sign is "/":
                self.divide = True

    def equals(self):
        ''' El cálculo de los disparos borra todos los vars '''
        total = 0
        if self.add is True:
            total = calc.somar(self.number1, self.number2)
            self.number2 = 0  # Se restablece para el siguiente cálculo si no se pulsa "Borrar".

        elif self.subtract is True:
            total = calc.subtrair(self.number1, self.number2)
            self.number2 = 0

        elif self.multiply is True:
            total = calc.multiplicar(self.number1, self.number2)
            self.number2 = 0

        elif self.divide is True:
            total = calc.dividir(self.number1, self.number2)
            total = int(total) if total.is_integer() else total
            self.number2 = 0

        self.top_string = ''
        self.add = False
        self.subtract = False
        self.multiply = False
        self.divide = False
        self.label.config(text=str(total))
        return total

    def clear_all(self):
        '''Borra todos los vars'''
        self.top_string = ''  # primera cadena que aparece después de seleccionar el signo (9 +)
        self.number1 = 0  # storage of first number selected
        self.number2 = 0  # storage of second number selected
        self.add = False  # + boolean
        self.subtract = False  # - boolean
        self.multiply = False  # x boolean
        self.divide = False  # / boolean
        self.label.config(text='0')  # top label
    def Conjuntos(self):
        self.Conjuntos = True

        #self.conjA = ttk.Entry(self.num_conjA)

        from matplotlib import pyplot as plt
        from matplotlib_venn import venn2
        venn2((1, 1, 1))
        plt.show()



if __name__ == '__main__':
    ROOT = Tk.Tk()
    ROOT.wm_title('Calculator')
    ROOT.resizable(width=False, height=False)
    Calculator(ROOT)
    ROOT.mainloop()