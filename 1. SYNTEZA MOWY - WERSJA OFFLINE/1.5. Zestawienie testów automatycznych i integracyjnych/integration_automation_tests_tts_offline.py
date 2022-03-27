import sys
import time
from tts_offline import Program
from PyQt5.QtWidgets import QApplication

from PyQt5.QtCore import Qt
from PyQt5 import QtTest

app = QApplication(sys.argv)

def test_changeVoiceRateAndVolume(qtbot):
    program = Program()
    qtbot.keyClicks(program.textBox, "I speak English")
    QtTest.QTest.qWait(500)

    qtbot.mouseClick(program.voice2, Qt.LeftButton)
    QtTest.QTest.qWait(500)

    qtbot.mouseClick(program.rateSpinbox, Qt.LeftButton)
    program.rateSpinbox.setValue(200)
    QtTest.QTest.qWait(500)

    qtbot.mouseClick(program.volumeSlider, Qt.LeftButton)
    program.volumeSlider.setValue(80)
    QtTest.QTest.qWait(500)

    qtbot.mouseClick(program.readButton, Qt.LeftButton)

    assert program.textBox.toPlainText() == "I speak English" 
    assert program.voice2.isChecked() == True
    assert program.voice2.text() == "Voice 2"
    assert program.rateSpinbox.value() == 200
    assert program.volumeSlider.value() == 80

class TestMain:

    def test_changeVoiceRateAndVolume(self):
        program = Program()
        program.textBox.setText("I speak English")
        time.sleep(0.5)
        program.voice2.click()
        time.sleep(0.5)
        program.rateSpinbox.setValue(200)
        time.sleep(0.5)
        program.volumeSlider.setValue(80)
        time.sleep(0.5)
        program.read_text()

        assert program.textBox.toPlainText() == "I speak English"
        assert program.voice2.isChecked() == True
        assert program.voice2.text() == "Voice 2"
        assert program.rateSpinbox.value() == 200
        assert program.volumeSlider.value() == 80