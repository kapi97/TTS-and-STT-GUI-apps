import sys
from tts_online import Program
from tts_online import langs_values
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
program = Program()

class TestMain:

    def test_01_saySlow(self):
        program.textBox.setText("Mówię wolno")
        program.slowVoice.click()
        program.read_text()
        assert program.textBox.toPlainText() == "Mówię wolno"
        assert program.slowVoice.isChecked() == False
        assert program.slowVoice.text() == "Slow"
    
    def test_02_sayNormal(self):    
        program.textBox.setText("Mówię normalnie")
        program.normalVoice.click()
        program.read_text()
        assert program.textBox.toPlainText() == "Mówię normalnie"
        assert program.normalVoice.isChecked() == True
        assert program.normalVoice.text() == "Slow"
        
    def test_03_sayInDifferentLanguages(self):
        program.textBox.setText("I speak English")
        program.voiceComboValues.setCurrentIndex(langs_values.index("English"))
        program.read_text()
        assert program.textBox.toPlainText() == "I speak English"
        assert program.voiceComboValues.currentText() == "Polish"