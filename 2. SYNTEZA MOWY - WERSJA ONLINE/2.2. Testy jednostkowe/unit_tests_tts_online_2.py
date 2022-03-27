import sys
from tts_online import Program
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
program = Program()

class TestMain:

    def test_01_textbox(self):
        program.textBox.setText("Test nr 1")
        assert program.textBox.toPlainText() == "Test numer jeden"

    def test_02_open(self):
        program.open_text()
        assert program.textBox.toPlainText() == "Test numer dwa"

    def test_03_read(self):
        program.textBox.setText("Test nr 3") 
        program.read_text()
        assert program.textBox.toPlainText() == "Test numer trzy"

    def test_04_save(self):
        program.textBox.setText("Test nr 4") 
        program.save_to_sound()
        assert program.textBox.toPlainText() == "Test numer cztery"