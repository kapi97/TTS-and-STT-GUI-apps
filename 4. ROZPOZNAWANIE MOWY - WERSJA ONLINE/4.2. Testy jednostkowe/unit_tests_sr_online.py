import sys
from sr_online import Program
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
program = Program()

class TestMain:

    def test_01_textbox(self):
        program.textBox.setText("Test numer jeden")
        assert program.textBox.toPlainText() == "Test numer jeden"

    def test_02_open(self):
        program.open_text()
        assert program.textBox.toPlainText() == "Test numer dwa"

    def test_03_save(self):
        program.textBox.setText("Test numer trzy") 
        program.save_text()
        assert program.textBox.toPlainText() == "Test numer trzy"