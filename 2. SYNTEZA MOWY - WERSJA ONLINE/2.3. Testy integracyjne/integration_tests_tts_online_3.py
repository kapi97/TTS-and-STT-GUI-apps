import sys
from tts_online import Program
from tts_online import langs_values
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
program = Program()

class TestMain:

    def test_01_saySlowAndNormal(self):
        program.textBox.setText("Mówię wolno")
        program.slowVoice.click()
        program.read_text()
        assert program.textBox.toPlainText() == "Mówię wolno"
        assert program.slowVoice.isChecked() == True
        assert program.slowVoice.text() == "Slow"
        
        program.textBox.setText("Mówię normalnie")
        program.normalVoice.click()
        program.read_text()
        assert program.textBox.toPlainText() == "Mówię normalnie"
        assert program.normalVoice.isChecked() == True
        assert program.normalVoice.text() == "Normal"
        
    def test_02_sayInDifferentLanguages(self):
        program.textBox.setText("I speak English")
        program.voiceComboValues.setCurrentIndex(langs_values.index("English"))
        program.read_text()
        assert program.textBox.toPlainText() == "I speak English"
        assert program.voiceComboValues.currentText() == "English"
        
        program.textBox.setText("Mówię po polsku")
        program.voiceComboValues.setCurrentIndex(langs_values.index("Polish"))
        program.read_text()
        assert program.textBox.toPlainText() == "Mówię po polsku"
        assert program.voiceComboValues.currentText() == "Polish"
        
    def test_03_changeRateAndLanguage(self):
        program.textBox.setText("I speak English")
        program.slowVoice.click()
        program.voiceComboValues.setCurrentIndex(langs_values.index("English"))
        program.read_text()
        assert program.textBox.toPlainText() == "I speak English"
        assert program.voiceComboValues.currentText() == "English"
        assert program.slowVoice.isChecked() == True
        assert program.slowVoice.text() == "Slow"