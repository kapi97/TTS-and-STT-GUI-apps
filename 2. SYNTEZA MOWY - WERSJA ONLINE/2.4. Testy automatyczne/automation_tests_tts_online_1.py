from tts_online import Program
from PyQt5.QtCore import Qt
from PyQt5 import QtTest
import pyautogui
  
def test_01_writeReadAndSave(qtbot):
    program = Program()
    QtTest.QTest.qWait(500)
    qtbot.keyClicks(program.textBox, "Test numer jeden")
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.readButton, Qt.LeftButton)
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.saveButton, Qt.LeftButton)
    assert program.textBox.toPlainText() == "Test numer jeden"

def test_02_openReadAndSave(qtbot):
    program = Program()
    
    QtTest.QTest.qWait(500)
    pyautogui.moveTo(800, 340, 1)
    QtTest.QTest.qWait(500)    
    pyautogui.click(800, 340)
    pyautogui.hotkey('enter')
    
    qtbot.mouseClick(program.openButton, Qt.LeftButton)
    QtTest.QTest.qWait(500)    
    qtbot.mouseClick(program.readButton, Qt.LeftButton)
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.saveButton, Qt.LeftButton)
    assert program.textBox.toPlainText() == "Test numer dwa"