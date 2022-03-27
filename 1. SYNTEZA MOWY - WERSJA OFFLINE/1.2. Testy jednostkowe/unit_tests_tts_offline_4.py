import sys
from tts_offline import Program
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
program = Program()

class TestMain:
    
    def test_01_selectVoice(self):
        program.voice2.click()
        assert program.voice2.isChecked() == False
        assert program.voice2.text() == "Voice 1"
        
    def test_02_selectRate(self):
        program.rateSpinbox.setValue(30)
        assert program.rateSpinbox.value() == 90
        
    def test_03_selectVolume(self):
        program.volumeSlider.setValue(80)
        assert program.volumeSlider.value() == 90