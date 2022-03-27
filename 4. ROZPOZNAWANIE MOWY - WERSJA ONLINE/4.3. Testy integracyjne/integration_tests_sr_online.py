import sys
import time
from sr_online import Program
from sr_online import langs_gtts_values
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
program = Program()

class TestMain:

    def test_01_openPlayAndConvert(self):
        program.open_sound_file()
        program.play_sound()
        time.sleep(3)
        program.operation()
        assert program.textBox.toPlainText() == "mówię po polsku"
        
    def test_02_recordPlayAndConvert(self):
        program.record_sound()
        program.play_sound()
        time.sleep(3)
        program.operation()
        assert program.textBox.toPlainText() == "mówię po polsku"
        
    def test_03_changeLanguage_openPlayAndConvert(self):
        program.voiceComboValues.setCurrentIndex(langs_gtts_values.index("English"))
        program.open_sound_file()
        program.play_sound()
        time.sleep(3)
        program.operation()
        assert program.textBox.toPlainText() == "I speak English"
        assert program.voiceComboValues.currentText() == "English"

    def test_04_changeLanguage_recordPlayAndConvert(self):
        program.voiceComboValues.setCurrentIndex(langs_gtts_values.index("English"))
        program.record_sound()
        program.play_sound()
        program.operation()
        assert program.textBox.toPlainText() == "I speak English"
        assert program.voiceComboValues.currentText() == "English"