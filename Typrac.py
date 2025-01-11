from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QTextEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor

class Window(QWidget):
    def __init__(self):
        self.text_1 = "type this particular text to practice your <br>keyboarding skills this is the <br>continuation of the text you are typing <br>nice job "
        self.index = 0
        self.letters_and_numbers = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        
        super().__init__()
        self.setWindowTitle("Typrac by Russel")
        self.setFixedSize(666, 483)
        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color: black;")
        
        # Vertical box layouts
        vertical_box_layout_1 = QVBoxLayout()
        
        # Labels
        self.label_1 = QLabel(self.text_1)
        self.label_1.setAlignment(Qt.AlignCenter)
        self.label_1.setStyleSheet("color: white; font-weight: bold;")
        font_settings_for_label_1 = QFont("Courier", 20)
        self.label_1.setFont(font_settings_for_label_1)
        
        # Buttons
        self.button_1 = QPushButton("Reset", clicked = lambda: self.reset_text())
        self.button_1.setFocusPolicy(Qt.NoFocus)
        self.button_1.setStyleSheet("background-color: Reset; height: 30px; color: white; font-weight: bold; font-family: Courier; font-size: 20px")

        
        # Setting layouts
        self.setLayout(vertical_box_layout_1)
        vertical_box_layout_1.addWidget(self.label_1)
        vertical_box_layout_1.addWidget(self.button_1)
        
        # Displaying the window
        self.show()
            
    def keyPressEvent(self, event):
        print(self.index)
        if self.index < len(self.text_1):
            if event.text() == self.text_1[self.index]:
                self.index += 1
                try:
                    if self.text_1[self.index] == "<":
                        self.index += 4
                except IndexError:
                    pass
                self.update_text()
                
            elif event.key() == 16777219 and self.index > 0:
                self.index -= 1
                if self.text_1[self.index] == ">":
                    self.index -= 4
                self.update_text()
            
            #elif event.text != self.text_1[self.index] and event.text() in self.letters_and_numbers:
                #self.index += 1
                #self.wrong_text()
                
                
        event.accept()   
    
        # self.past = f"<span style = 'color: green;'>{self.text_1[:self.index - 1]}</span>"
    # def wrong_text(self):
        # self.letter_before_index = f"<span style = 'color: red;'>{self.text_1[self.index - 1]}</span>"
        # self.remains = f"<span style = 'color: white;'>{self.text_1[self.index + 1:]}</span>"  if self.index < len(self.text_1) else ""
        #self.current = f"<u>{self.text_1[self.index]}</u>" if self.index < len(self.text_1) else ""
        #self.label_1.setText(self.past + self.letter_before_index + self.current + self.remains)
        #self.past = self.past + self.letter_before_index
        
    def update_text(self):
        self.typed = f"<span style = 'color: green;'>{self.text_1[:self.index]}</span>"
        self.remaining = f"<span style='color: white;'>{self.text_1[self.index + 1:]}</span>" if self.index < len(self.text_1) else ""
        self.current = f"<u>{self.text_1[self.index]}</u>" if self.index < len(self.text_1) else ""
        self.label_1.setText(self.typed + self.current + self.remaining)

        # If the whole text is typed, show a message
        if self.index == len(self.text_1):
            self.label_1.setText("Great job!")
    
    # This method fires when you enter the reset button
    def reset_text(self):
        self.index = 0
        self.label_1.setText(self.text_1)
            
app = QApplication([])
window = Window()
print(window.label_1.text())
app.exec_()
