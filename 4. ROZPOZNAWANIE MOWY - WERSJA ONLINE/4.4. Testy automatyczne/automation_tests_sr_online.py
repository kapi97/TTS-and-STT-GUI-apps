from sr_online import Program
from sr_online import langs_gtts_values
from PyQt5.QtCore import Qt
from PyQt5 import QtTest
import pyautogui
  
def test_01_openPlayAndConvert(qtbot):
    program = Program()
    
    QtTest.QTest.qWait(500)
    pyautogui.moveTo(800, 300, 1)
    QtTest.QTest.qWait(500)    
    pyautogui.click(800, 300)
    pyautogui.hotkey('enter')
    
    qtbot.mouseClick(program.openSoundButton, Qt.LeftButton)    
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.playButton, Qt.LeftButton)
    QtTest.QTest.qWait(3000)
    qtbot.mouseClick(program.saveSoundButton, Qt.LeftButton)
    assert program.textBox.toPlainText() == "test numer 1"

def test_02_recordPlayAndConvert(qtbot):
    program = Program()   
    qtbot.mouseClick(program.recordButton, Qt.LeftButton)
    QtTest.QTest.qWait(500)    
    qtbot.mouseClick(program.playButton, Qt.LeftButton)
    QtTest.QTest.qWait(3000)
    qtbot.mouseClick(program.saveSoundButton, Qt.LeftButton)
    assert program.textBox.toPlainText() == "test numer 2"
    
def test_03_changeLanguage_openPlayAndConvert(qtbot):
    program = Program()
    qtbot.mouseClick(program.voiceComboValues, Qt.LeftButton)
    program.voiceComboValues.setCurrentIndex(langs_gtts_values.index("English"))
    
    QtTest.QTest.qWait(500)
    pyautogui.moveTo(800, 340, 1)
    QtTest.QTest.qWait(500)    
    pyautogui.click(800, 340)
    pyautogui.hotkey('enter')
    
    qtbot.mouseClick(program.openSoundButton, Qt.LeftButton)    
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.playButton, Qt.LeftButton)
    QtTest.QTest.qWait(3000)
    qtbot.mouseClick(program.saveSoundButton, Qt.LeftButton)
    assert program.textBox.toPlainText() == "Test numer jeden"

def test_04_changeLanguage_recordPlayAndConvert(qtbot):
    program = Program()
    QtTest.QTest.qWait(500)
    qtbot.mouseClick(program.voiceComboValues, Qt.LeftButton)
    program.voiceComboValues.setCurrentIndex(langs_gtts_values.index("English"))
    
    qtbot.mouseClick(program.recordButton, Qt.LeftButton)
    QtTest.QTest.qWait(500)    
    qtbot.mouseClick(program.playButton, Qt.LeftButton)
    QtTest.QTest.qWait(3000)
    qtbot.mouseClick(program.saveSoundButton, Qt.LeftButton)
    assert program.textBox.toPlainText() == "Test numer dwa"