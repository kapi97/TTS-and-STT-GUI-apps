import sys
import time
from sr_offline import Program
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
program = Program()

class TestMain:

    def test_01_openPlayAndConvert(self):
        program.open_sound_file()
        program.play_sound()
        time.sleep(3)
        program.operation()
        assert program.textBox.toPlainText() == "I speak English"
        
    def test_02_recordPlayAndConvert(self):
        program.record_sound()
        program.play_sound()
        time.sleep(3)
        program.operation()
        assert program.textBox.toPlainText() == "I speak English"