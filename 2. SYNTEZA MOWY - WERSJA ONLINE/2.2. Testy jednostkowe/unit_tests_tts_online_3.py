import sys
from tts_online import Program
from tts_online import langs_values
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
program = Program()

class TestMain:

    def test_01_selectRate(self):
        program.slowVoice.click()
        assert program.slowVoice.isChecked() == True
        assert program.slowVoice.text() == "Slow"
        
    def test_02_selectIndex(self):
        program.voiceComboValues.setCurrentIndex(langs_values.index("English"))
        assert program.voiceComboValues.currentText() == "English"