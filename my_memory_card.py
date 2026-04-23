from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QVBoxLayout, QGroupBox, QHBoxLayout, QRadioButton, QButtonGroup)
from random import randint, shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

current_question = -1

question_list = []
question_list.append(Question(
    'Сколько волос на голове?', '10000', '1', '2', '3'
))
question_list.append(Question(
    'Кто основал Петербург?', 'Петр', 'Антон', 'Володя', 'Андрей'
))
question_list.append(Question(
    'Го в доту?', 'ДА!!!', 'Нет', 'Возможно', 'Позже'
))
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(500, 500)

question = QLabel("Вопрос")
button = QPushButton('Ответить')
button.resize(500,500)

RadioGroupBox = QGroupBox("Варианты ответов")

rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

AnsGroupBox = QGroupBox('Результат')
result_label = QLabel('Правильно/Неправильно')
correct_label =QLabel('Правильный вариант')
layout_ans = QVBoxLayout()
layout_ans.addWidget(result_label, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_ans.addWidget(correct_label, alignment=Qt.AlignCenter)
AnsGroupBox.setLayout(layout_ans)

RadioGroupBox.setLayout(layout_ans1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(question, alignment=Qt.AlignCenter)

layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addWidget(button)

layout_main = QVBoxLayout()
layout_main.addLayout(layout_line1, stretch=2)
layout_main.addStretch(3)
layout_main.addLayout(layout_line2, stretch=8)
layout_main.addStretch(3)
layout_main.addLayout(layout_line3, stretch=2)
#layout_main.addStretch(6)
#layout_main.setSpacing(5)

main_win.setLayout(layout_main)

def show_resual():
    AnsGroupBox.show()
    RadioGroupBox.hide()
    button.setText('Следующий вопрос')

def show_qestion():    
    AnsGroupBox.hide()
    RadioGroupBox.show()
    button.setText('Ответить')
    RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # вернули ограничения, теперь только одна радиокнопка может быть выбрана



answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)

    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    correct_label.setText(q.right_answer)
    show_qestion()



def check_answer():
    if answers[0].isChecked():
        result_label.setText('Правильно!')
        show_resual()
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():   
            result_label.setText('Неправильно!')     
            show_resual()

def next_questoion():
    global current_question
    current_question += 1
    if current_question >= len(question_list):
        current_question = 0
    ask(question_list[current_question])

def click_button():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_questoion()


next_questoion()
button.clicked.connect(click_button)

#запуск приложения
main_win.show()
app.exec_()
