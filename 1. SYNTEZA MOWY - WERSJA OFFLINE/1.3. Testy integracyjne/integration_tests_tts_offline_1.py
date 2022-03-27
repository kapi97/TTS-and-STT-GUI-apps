import sys
from tts_offline import Program
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
program = Program()

class TestMain:

    def test_01_openAndRead(self):
        program.open_text()
        program.read_text()
        assert program.textBox.toPlainText() == "Test numer jeden"

    def test_03_readAndSave(self):
        program.textBox.setText("Test numer dwa")
        program.read_text()
        program.save_to_sound()
        assert program.textBox.toPlainText() == "Test numer dwa"
               
    def test_03_openReadAndSave(self):
        program.open_text()
        program.read_text()
        program.save_to_sound()
        assert program.textBox.toPlainText() == "Test numer trzy"