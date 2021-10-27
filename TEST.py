import PyQt5.QtWidgets as qtw
from PyQt5 import QtCore

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simple Calculator')
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()
        self.temp_nums = []
        self.fin_nums = []
        self.show()

    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        #Buttons
        self.result_field_1 = qtw.QLineEdit()
        self.result_field_1.setAlignment(QtCore.Qt.AlignRight)
        self.result_field_1.setStyleSheet("color: black;")
        self.result_field_2 = qtw.QLineEdit()
        self.result_field_2.setAlignment(QtCore.Qt.AlignRight)
        self.result_field_2.setStyleSheet("color: black;")
        btn_9 = qtw.QPushButton('9', clicked = lambda:self.num_press('9'))
        btn_8 = qtw.QPushButton('8', clicked = lambda:self.num_press('8'))
        btn_7 = qtw.QPushButton('7', clicked = lambda:self.num_press('7'))
        btn_6 = qtw.QPushButton('6', clicked = lambda:self.num_press('6'))
        btn_5 = qtw.QPushButton('5', clicked = lambda:self.num_press('5'))
        btn_4 = qtw.QPushButton('4', clicked = lambda:self.num_press('4'))
        btn_3 = qtw.QPushButton('3', clicked = lambda:self.num_press('3'))
        btn_2 = qtw.QPushButton('2', clicked = lambda:self.num_press('2'))
        btn_1 = qtw.QPushButton('1', clicked = lambda:self.num_press('1'))
        btn_0 = qtw.QPushButton('0', clicked = lambda:self.num_press('0'))
        btn_plus = qtw.QPushButton('+', clicked = lambda:self.func_press('+'))
        btn_mins = qtw.QPushButton('-', clicked = lambda:self.func_press('-'))
        btn_mult = qtw.QPushButton('*', clicked = lambda:self.func_press('*'))
        btn_divd = qtw.QPushButton('/', clicked = lambda:self.func_press('/'))
        btn_result = qtw.QPushButton('=', clicked = self.func_result)
        btn_clearall = qtw.QPushButton('C', clicked = self.clear_calc)
        btn_clear = qtw.QPushButton('CE', clicked = self.clear_result)
        btn_float = qtw.QPushButton('.', clicked = lambda:self.num_press('.'))
        btn_9.setStyleSheet("background-color: yellow;")
        btn_8.setStyleSheet("background-color: yellow;")
        btn_7.setStyleSheet("background-color: yellow;")
        btn_6.setStyleSheet("background-color: yellow;")
        btn_5.setStyleSheet("background-color: yellow;")
        btn_4.setStyleSheet("background-color: yellow;")
        btn_3.setStyleSheet("background-color: yellow;")
        btn_2.setStyleSheet("background-color: yellow;")
        btn_1.setStyleSheet("background-color: yellow;")
        btn_0.setStyleSheet("background-color: yellow;")
        btn_result.setStyleSheet("background-color: red;")
        btn_float.setStyleSheet("background-color: green;")
        btn_clear.setStyleSheet("background-color: orange;")
        btn_clearall.setStyleSheet("background-color: blue;")
        btn_plus.setStyleSheet("background-color: #ffb2d4;")
        btn_mins.setStyleSheet("background-color: #ffb2d4;")
        btn_mult.setStyleSheet("background-color: #ffb2d4;")
        btn_divd.setStyleSheet("background-color: #ffb2d4;")

        #Adding buttons to layout
        container.layout().addWidget(self.result_field_2,0,0,1,4)
        container.layout().addWidget(self.result_field_1,1,0,1,4)
        container.layout().addWidget(btn_7,2,0,1,1)
        container.layout().addWidget(btn_8,2,1,1,1)
        container.layout().addWidget(btn_9,2,2,1,1)
        container.layout().addWidget(btn_divd,2,3,1,1)
        container.layout().addWidget(btn_4,3,0,1,1)
        container.layout().addWidget(btn_5,3,1,1,1)
        container.layout().addWidget(btn_6,3,2,1,1)
        container.layout().addWidget(btn_mult,3,3,1,1)
        container.layout().addWidget(btn_1,4,0,1,1)
        container.layout().addWidget(btn_2,4,1,1,1)
        container.layout().addWidget(btn_3,4,2,1,1)
        container.layout().addWidget(btn_mins,4,3,1,1)
        container.layout().addWidget(btn_result,5,0,1,1)
        container.layout().addWidget(btn_0,5,1,1,1)
        container.layout().addWidget(btn_float,5,2,1,1)
        container.layout().addWidget(btn_plus,5,3,1,1)
        container.layout().addWidget(btn_clear,6,0,1,2)
        container.layout().addWidget(btn_clearall,6,2,1,2)
        self.layout().addWidget(container)

    def num_press(self, key_number):
        self.temp_nums.append(key_number)
        temp_string = ''.join(self.temp_nums)
        self.result_field_1.setText(temp_string)

    def func_press(self, operator):
        temp_string = ''.join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.fin_nums.append(operator)
        self.result_field_2.setText(''.join(self.fin_nums))
        self.temp_nums = []
        self.result_field_1.clear()

    def func_result(self):
        fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums)
        self.result_field_2.setText(fin_string)
        result_string = eval(fin_string)
        self.result_field_1.setText(str(result_string))

    def clear_calc(self):
        self.result_field_1.clear()
        self.result_field_2.clear()
        self.temp_nums = []
        self.fin_nums = []

    def clear_result(self):
        self.result_field_2.setText(''.join(self.fin_nums))
        self.result_field_1.clear()
        self.temp_nums = []

app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec_()