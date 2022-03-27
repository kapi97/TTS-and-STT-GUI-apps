import sys
from tts_offline import Program
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
program = Program()

class TestMain:

    def test_01_changeVoice(self):
        program.textBox.setText("I speak English")
        program.voice2.click()
        program.read_text()
        assert program.textBox.toPlainText() == "I speak English"
        assert program.voice2.isChecked() == True
        assert program.voice2.text() == "Voice 2"
        
        program.textBox.setText("Mówię po polsku")
        program.voice1.click()
        program.read_text()
        assert program.textBox.toPlainText() == "Mówię po polsku"
        assert program.voice1.isChecked() == True
        assert program.voice1.text() == "Voice 1"

    def test_02_changeRate(self):
        program.textBox.setText("Mówię wolno")
        program.rateSpinbox.setValue(80)
        program.read_text()
        assert program.textBox.toPlainText() == "Mówię wolno"
        assert program.rateSpinbox.value() == 80

        program.textBox.setText("Mówię szybko")
        program.rateSpinbox.setValue(200)
        program.read_text()
        assert program.textBox.toPlainText() == "Mówię szybko"
        assert program.rateSpinbox.value() == 200

    def test_03_changeVolume(self):
        program.textBox.setText("Mówię głośno")
        program.volumeSlider.setValue(80)
        program.read_text()
        assert program.textBox.toPlainText() == "Mówię głośno"
        assert program.volumeSlider.value() == 80

        program.textBox.setText("Mówię cicho")
        program.volumeSlider.setValue(20)
        program.read_text()
        assert program.textBox.toPlainText() == "Mówię cicho"
        assert program.volumeSlider.value() == 20