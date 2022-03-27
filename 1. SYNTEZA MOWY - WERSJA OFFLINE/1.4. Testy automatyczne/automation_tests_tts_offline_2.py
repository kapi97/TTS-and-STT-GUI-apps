from tts_offline import Program
from PyQt5.QtCore import Qt
from PyQt5 import QtTest

def test_01_changeVoice(qtbot):
    program = Program()
    qtbot.keyClicks(program.textBox, "I speak English")
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.voice2, Qt.LeftButton)
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.readButton, Qt.LeftButton)
    assert program.textBox.toPlainText() == "I speak English"
    assert program.voice2.isChecked() == True
    assert program.voice2.text() == "Voice 2"
    
    program.textBox.clear()
    qtbot.keyClicks(program.textBox, "Przemawiam po polsku")
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.voice1, Qt.LeftButton)
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.readButton, Qt.LeftButton)
    assert program.textBox.toPlainText() == "Przemawiam po polsku"
    assert program.voice1.isChecked() == True
    assert program.voice1.text() == "Voice 1"

def test_02_changeRate(qtbot):
    program = Program()
    qtbot.keyClicks(program.textBox, "Przemawiam wolno")
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.rateSpinbox, Qt.LeftButton)
    program.rateSpinbox.setValue(80)
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.readButton, Qt.LeftButton)
    assert program.textBox.toPlainText() == "Przemawiam wolno"
    assert program.rateSpinbox.value() == 80

    program.textBox.clear()
    qtbot.keyClicks(program.textBox, "Przemawiam szybko")
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.rateSpinbox, Qt.LeftButton)
    program.rateSpinbox.setValue(200)
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.readButton, Qt.LeftButton)
    assert program.textBox.toPlainText() == "Przemawiam szybko"
    assert program.rateSpinbox.value() == 200

def test_03_changeVolume(qtbot):
    program = Program()
    qtbot.keyClicks(program.textBox, "Przemawiam glosno")
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.volumeSlider, Qt.LeftButton)
    program.volumeSlider.setValue(80)
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.readButton, Qt.LeftButton)
    assert program.textBox.toPlainText() == "Przemawiam glosno"
    assert program.volumeSlider.value() == 80

    program.textBox.clear()
    qtbot.keyClicks(program.textBox, "Przemawiam cicho")
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.volumeSlider, Qt.LeftButton)
    program.volumeSlider.setValue(20)
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.readButton, Qt.LeftButton)
    assert program.textBox.toPlainText() == "Przemawiam cicho"
    assert program.volumeSlider.value() == 20