import sys
import random
from PyQt5.QtWidgets import *
from gtts import gTTS
from gtts import lang
from pydub import AudioSegment
from pydub.playback import play
from tempfile import TemporaryFile

langs_keys = list(lang.tts_langs().keys())
langs_values = list(lang.tts_langs().values())


class Program(QWidget):

    def __init__(self):
        super().__init__()

        self.textBox = QTextEdit(self)

        self.readButton = QPushButton("Read text")
        self.openButton = QPushButton("Open text file")
        self.saveButton = QPushButton("Save to sound file")

        self.progressBar = QProgressBar(self)
        self.progressBar.setMaximum(100)

        self.normalVoice = QRadioButton("Normal")
        self.slowVoice = QRadioButton("Slow")
        self.normalVoice.setChecked(True)

        self.voiceComboKeys = QComboBox()
        self.voiceComboKeys.addItems(langs_keys)
        self.voiceComboKeys.setCurrentIndex(langs_keys.index("pl"))

        self.voiceComboValues = QComboBox()
        self.voiceComboValues.addItems(langs_values)
        self.voiceComboValues.setCurrentIndex(langs_values.index("Polish"))

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        h1_layout = QHBoxLayout()
        h2_layout = QHBoxLayout()

        h1_layout.addWidget(self.normalVoice)
        h1_layout.addWidget(self.slowVoice)
        h1_layout.addWidget(self.voiceComboValues)
        layout.addLayout(h1_layout)

        layout.addWidget(self.textBox)

        h2_layout.addWidget(self.readButton)
        h2_layout.addWidget(self.openButton)
        h2_layout.addWidget(self.saveButton)
        layout.addLayout(h2_layout)

        self.readButton.clicked.connect(self.read_text)
        self.openButton.clicked.connect(self.open_text)
        self.saveButton.clicked.connect(self.save_to_sound)

        layout.addWidget(self.progressBar)

        self.setLayout(layout)
        self.setWindowTitle("Text To Speech - online")
        self.resize(300, 350)
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

    def select_rate(self):
        if self.normalVoice.isChecked():
            self.rate = False
        if self.slowVoice.isChecked():
            self.rate = True

    def select_combo(self):
        self.select_rate()
        index = self.voiceComboValues.currentIndex()
        print(self.voiceComboValues.itemText(index))

        readText = self.textBox.toPlainText()

        if readText != '':
            self.tts = gTTS(text=readText, lang=self.voiceComboKeys.itemText(index), slow=self.rate)
        else:
            self.tts = None

    def operation(self):
        self.select_combo()

        r = random.randint(1, 1000000)
        audioFile = "audio-" + str(r) + ".mp3"

        try:
            self.tts.save(audioFile)
            sound = AudioSegment.from_file(audioFile)
            sound.export(audioFile, format="wav")
        except:
            return False

    def read_text(self):
        try:
            if self.textBox.toPlainText() != '':
                self.select_combo()
                mp3_fp = TemporaryFile()
                self.tts.write_to_fp(mp3_fp)
                mp3_fp.seek(0)

                song = AudioSegment.from_file(mp3_fp, format="mp3")
                play(song)
            else:
                pass
        except:
            return False

    def showDialog(self):
        messageBox = QMessageBox()
        messageBox.setIcon(QMessageBox.Information)
        messageBox.setText("Completed")
        messageBox.setWindowTitle("Message")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

    def save_to_sound(self):
        if self.textBox.toPlainText() != '':
            self.operation()

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