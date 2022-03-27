import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyttsx3
engine = pyttsx3.init()


class Program(QWidget):

    def __init__(self):
        super().__init__()

        self.textBox = QTextEdit(self)

        self.readButton = QPushButton("Read text")
        self.openButton = QPushButton("Open text file")
        self.saveButton = QPushButton("Save to sound file")

        self.progressBar = QProgressBar(self)
        self.progressBar.setMaximum(100)

        self.voice1 = QRadioButton("Voice 1")
        self.voice2 = QRadioButton("Voice 2")
        self.voice1.setChecked(True)

        self.rateLabel = QLabel("Rate:")
        self.rateLabel.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        self.rateSpinbox = QSpinBox(self)
        self.rateSpinbox.setRange(80, 250)
        currentRateValue = 120
        self.rateSpinbox.setValue(currentRateValue)
        self.rateSpinbox.setSingleStep(10)

        self.volumeLabel = QLabel("Volume:")
        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.setRange(0, 100)
        self.volumeSlider.setValue(100)
        self.volumeSlider.setTickPosition(QSlider.TicksBelow)
        self.volumeSlider.setTickInterval(10)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        h1_layout = QHBoxLayout()
        h2_layout = QHBoxLayout()

        h1_layout.addWidget(self.voice1)
        h1_layout.addWidget(self.voice2)
        h1_layout.addWidget(self.rateLabel)
        h1_layout.addWidget(self.rateSpinbox)
        layout.addLayout(h1_layout)

        layout.addWidget(self.volumeLabel)
        layout.addWidget(self.volumeSlider)

        layout.addWidget(self.textBox)

        h2_layout.addWidget(self.readButton)
        h2_layout.addWidget(self.openButton)
        h2_layout.addWidget(self.saveButton)
        layout.addLayout(h2_layout)

        layout.addWidget(self.progressBar)

        self.readButton.clicked.connect(self.read_text)
        self.openButton.clicked.connect(self.open_text)
        self.saveButton.clicked.connect(self.save_to_sound)

        self.setLayout(layout)
        self.setWindowTitle("Text To Speech - offline")
        self.resize(300, 400)
        self.center()
        self.show()

    def center(self):
        centerWindow = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        centerWindow.moveCenter(centerPoint)
        self.move(centerWindow.topLeft())

    def open_text(self):
        filename = QFileDialog.getOpenFileName(self, "Open File", "", "Text File (*.txt)")
        if filename != ('', ''):
            try:
                f = open(filename[0], 'r', encoding='UTF-8')
            except:
                f = open(filename[0], 'r')
            fileText = f.read()
            self.textBox.setText(fileText)
            f.close()

    def change_volume(self):
        volume = float(self.volumeSlider.value()) / 100
        engine.setProperty('volume', volume)

    def select_rate(self):
        rate = self.rateSpinbox.value()
        engine.setProperty('rate', rate)

    def select_voice(self):
        voice = engine.getProperty('voices')

        if self.voice1.isChecked():
            engine.setProperty('voice', voice[0].id)
            print("Voice:")
            print("ID: %s" % voice[0].id)
            print("Name: %s" % voice[0].name)

        if self.voice2.isChecked():
            engine.setProperty('voice', voice[1].id)
            print("Voice:")
            print("ID: %s" % voice[1].id)
            print("Name: %s" % voice[1].name)

    def operations(self):
        self.change_volume()
        self.select_rate()
        self.select_voice()

    def read_text(self):
        if self.textBox.toPlainText() != '':
            self.operations()

            readText = self.textBox.toPlainText()
            engine.say(readText)
            engine.runAndWait()
        else:
            pass

    def showDialog(self):
        messageBox = QMessageBox()
        messageBox.setIcon(QMessageBox.Information)
        messageBox.setText("Completed")
        messageBox.setWindowTitle("Message")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

    def save_to_sound(self):
        if self.textBox.toPlainText() != '':
            self.operations()

            readText = self.textBox.toPlainText()
            r = random.randint(1, 1000000)
            audioFile = "opf-" + str(r) + ".mp3"

            engine.save_to_file(readText, audioFile)
            engine.runAndWait()

            completed = 0
            while completed < 100:
                completed += 0.0001
                self.progressBar.setValue(completed)

            self.showDialog()
        else:
            pass


def main():
    app = QApplication(sys.argv)
    program = Program()
    program.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()