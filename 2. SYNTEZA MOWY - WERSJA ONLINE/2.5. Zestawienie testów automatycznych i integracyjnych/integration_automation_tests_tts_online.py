import sys
import time
from tts_online import Program
from tts_online import langs_values
from PyQt5.QtWidgets import QApplication

from PyQt5.QtCore import Qt
from PyQt5 import QtTest

app = QApplication(sys.argv)
program = Program()

def test_changeRateAndLanguage(qtbot):
    program = Program()
    qtbot.keyClicks(program.textBox, "I speak English")
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.slowVoice, Qt.LeftButton)
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.voiceComboValues, Qt.LeftButton)
    program.voiceComboValues.setCurrentIndex(langs_values.index("English"))
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.readButton, Qt.LeftButton)
    assert program.textBox.toPlainText() == "I speak English"
    assert program.voiceComboValues.currentText() == "English"
    assert program.slowVoice.isChecked() == True
    assert program.slowVoice.text() == "Slow"

class TestMain:

    def test_changeRateAndLanguage(self):
        program.textBox.setText("I speak English")
        time.sleep(0.5)
        program.slowVoice.click()
        time.sleep(0.5)
        program.voiceComboValues.setCurrentIndex(langs_values.index("English"))
        time.sleep(0.5)
        program.read_text()
        assert program.textBox.toPlainText() == "I speak English"
        assert program.voiceComboValues.currentText() == "English"
        assert program.slowVoice.isChecked() == True
        assert program.slowVoice.text() == "Slow"
