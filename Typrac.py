from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QTextEdit, QPushButton
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        self.text_1 = "type this particular text to practice your keyboarding skills <br>this is the continuation of the text you are typing nice job "
        self.index = 0
        
        super().__init__()
        self.setWindowTitle("Typrac by Russel")
        self.setFixedSize(666, 483)
       
        # Vertical box layouts
        vertical_box_layout_1 = QVBoxLayout()
        
        # Labels
        self.label_1 = QLabel(self.text_1)
        self.label_1.setStyleSheet("font-size: 25px;")
        self.label_1.setTextFormat(Qt.RichText) # Setting the text format to rich text is necessary to properly interpret and display HTML tags like <br> for line breaks, <span> for styling, and other HTML formatting tags.
        
        # Buttons
        self.button_1 = QPushButton("Reset", clicked = lambda: self.reset_text())
        self.button_1.setFocusPolicy(Qt.NoFocus)
        
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
                self.backspace()
                
        event.accept()        
                
    def update_text(self):
        # Highlighting the typed part in blue and the rest in black
        self.typed = f"<span style = 'color: blue;'>{self.text_1[:self.index]}</span>"
        self.remaining = f"<span style='color: black;'>{self.text_1[self.index:]}</span>"
        self.label_1.setText(self.typed + self.remaining)

        # If the whole text is typed, show a message
        if self.index == len(self.text_1):
            self.label_1.setText("Great job!")
    
    # This method is for backspacing
    def backspace(self):
        self.typed = f"<span style = 'color: blue;'>{self.text_1[:self.index]}</span>"
        self.remaining = f"<span style='color: black;'>{self.text_1[self.index:]}</span>"
        self.label_1.setText(self.typed + self.remaining)
        
    def reset_text(self):
        self.index = 0
        self.label_1.setText(self.text_1)
            
app = QApplication([])
window = Window()
print(len(window.text_1))
app.exec_()