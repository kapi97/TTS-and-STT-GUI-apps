import sys
from tts_offline import Program
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

    def test_03_read(self):
        program.textBox.setText("Test numer trzy") 
        program.read_text()
        assert program.textBox.toPlainText() == "Test numer trzy"

    def test_04_save(self):
        program.textBox.setText("Test numer cztery") 
        program.save_to_sound()
        assert program.textBox.toPlainText() == "Test numer cztery"