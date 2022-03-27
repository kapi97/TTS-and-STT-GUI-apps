from tts_online import Program
from tts_online import langs_values
from PyQt5.QtCore import Qt
from PyQt5 import QtTest

def test_01_saySlowAndNormal(qtbot):
    program = Program()
    qtbot.keyClicks(program.textBox, "Przemawiam wolno")
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.slowVoice, Qt.LeftButton)
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.readButton, Qt.LeftButton)
    assert program.textBox.toPlainText() == "Przemawiam wolno"
    assert program.slowVoice.isChecked() == True
    assert program.slowVoice.text() == "Slow"
    
    program.textBox.clear()
    qtbot.keyClicks(program.textBox, "Przemawiam normalnie")
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.normalVoice, Qt.LeftButton)
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.readButton, Qt.LeftButton)
    assert program.textBox.toPlainText() == "Przemawiam normalnie"
    assert program.normalVoice.isChecked() == True
    assert program.normalVoice.text() == "Normal"

def test_02_sayInDifferentLanguages(qtbot):
    program = Program()
    qtbot.keyClicks(program.textBox, "I speak English")
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.voiceComboValues, Qt.LeftButton)
    program.voiceComboValues.setCurrentIndex(langs_values.index("English"))
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.readButton, Qt.LeftButton)
    assert program.textBox.toPlainText() == "I speak English"
    assert program.voiceComboValues.currentText() == "English"

    program.textBox.clear()
    qtbot.keyClicks(program.textBox, 'Przemawiam po polsku')
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.voiceComboValues, Qt.LeftButton)
    program.voiceComboValues.setCurrentIndex(langs_values.index("Polish"))
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.readButton, Qt.LeftButton)
    assert program.textBox.toPlainText() == "Przemawiam po polsku"
    assert program.voiceComboValues.currentText() == "Polish"

def test_03_changeRateAndLanguage(qtbot):
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