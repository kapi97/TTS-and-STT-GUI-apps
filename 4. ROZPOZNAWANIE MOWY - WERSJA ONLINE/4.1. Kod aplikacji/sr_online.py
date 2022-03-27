import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import winsound
import speech_recognition as sr

from os import path
import os
import random

from gtts import lang
langs_gtts_values = list(lang.tts_langs().values())
langs_gtts_keys = list(lang.tts_langs().keys())

from pydub import AudioSegment
from pydub.playback import play


class Program(QWidget):

    def __init__(self):
        super().__init__()

        self.labelFileName = QLabel(self)
        self.labelFileName.setText("File Name:")
        self.labelFileName.setStyleSheet("background-color:#ffffff; border: 1px solid gray")

        self.recordButton = QPushButton("Record your voice")
        self.playButton = QPushButton("Play")
        self.stopButton = QPushButton("Stop")

        self.openSoundButton = QPushButton("Open sound file")
        self.saveSoundButton = QPushButton("Convert and save to text file")

        self.orLabel = QLabel("or")
        self.orLabel.setAlignment(Qt.AlignCenter)
        self.langLabel = QLabel("Select language: ")

        self.textBox = QTextEdit(self)
        self.infoLabel = QLabel("Optionally:")
        self.openTextButton = QPushButton("Open generated text file")
        self.saveTextButton = QPushButton("Save revised text file")
        self.progressBar = QProgressBar(self)
        self.progressBar.setMaximum(100)

        self.voiceComboValues = QComboBox()
        self.voiceComboValues.addItems(langs_gtts_values)
        self.voiceComboValues.setCurrentIndex(langs_gtts_values.index("Polish"))

        self.voiceComboKeys = QComboBox()
        self.voiceComboKeys.addItems(langs_gtts_keys)
        self.voiceComboKeys.setCurrentIndex(langs_gtts_keys.index("pl"))

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        h1_layout = QHBoxLayout()
        h2_layout = QHBoxLayout()
        h3_layout = QHBoxLayout()
        h4_layout = QHBoxLayout()

        h1_layout.addWidget(self.openSoundButton)
        h1_layout.addWidget(self.orLabel)
        h1_layout.addWidget(self.recordButton)
        layout.addLayout(h1_layout)

        h2_layout.addWidget(self.langLabel)
        h2_layout.addWidget(self.voiceComboValues)
        layout.addLayout(h2_layout)

        layout.addWidget(self.labelFileName)

        h3_layout.addWidget(self.playButton)
        h3_layout.addWidget(self.stopButton)
        layout.addLayout(h3_layout)

        layout.addWidget(self.saveSoundButton)

        self.openSoundButton.clicked.connect(self.open_sound_file)
        self.saveSoundButton.clicked.connect(self.operation)

        self.recordButton.clicked.connect(self.record_sound)
        self.playButton.clicked.connect(self.play_sound)
        self.stopButton.clicked.connect(self.stop_sound)

        layout.addWidget(self.progressBar)

        layout.addWidget(self.textBox)

        layout.addWidget(self.infoLabel)

        h4_layout.addWidget(self.openTextButton)
        h4_layout.addWidget(self.saveTextButton)
        layout.addLayout(h4_layout)

        self.openTextButton.clicked.connect(self.open_text)
        self.saveTextButton.clicked.connect(self.save_text)

        self.setLayout(layout)
        self.setWindowTitle("Speech Recognition - online")
        self.resize(325, 500)
        self.center()
        self.show()

    def center(self):
        centerWindow = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        centerWindow.moveCenter(centerPoint)
        self.move(centerWindow.topLeft())

    def open_sound_file(self):
        filename = QFileDialog.getOpenFileName(self, "Open Sound", "", "Sound Files (*.mp3 *.ogg *.wav *.m4a)")
        if filename != ('', ''):

            try:
                self.audioClip = filename[0]
                self.labelFileName.setText(self.audioClip)

            finally:
                AudioSegment.from_file(self.audioClip).export(self.audioClip, format="wav")

            self.outputFile = os.path.splitext(self.audioClip)[0]

    def record_sound(self):
        try:
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                audio = recognizer.listen(source)
                
            try:
                r = random.randint(1, 1000000)
                self.audioClip = "speech" + str(r) + ".wav"
                with open("speech" + str(r) + ".wav", "wb") as f:
                    f.write(audio.get_wav_data())

                    self.labelFileName.setText(self.audioClip)

                    self.outputFile = os.path.splitext(self.audioClip)[0]
                    
            except sr.UnknownValueError:
                print("Google could not understand audio")
            except sr.RequestError as e:
                print("Google error; {0}".format(e))
                
        except:
            pass

    def play_sound(self):
        try:
            winsound.PlaySound(self.audioClip, winsound.SND_ASYNC)
        except:
            return False

    def stop_sound(self):
        winsound.PlaySound(None, winsound.SND_PURGE)

    def saveToFile(self, transcriptOperation):
        try:
            sys.stdout = open(self.outputFile + ".txt", "w", encoding='utf-8')
        except:
            sys.stdout = open(self.outputFile + ".txt", "w")

        print("Converted Audio Is : \n" + transcriptOperation)

        completed = 0
        while completed < 100:
            completed += 0.0001
            self.progressBar.setValue(completed)

        self.textBox.setText(transcriptOperation)
        sys.stdout.close()

    def showDialog(self):
        messageBox = QMessageBox()
        messageBox.setIcon(QMessageBox.Information)
        messageBox.setText("Completed")
        messageBox.setWindowTitle("Message")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

    def operation(self):
        try:
            audio_file = path.join(path.dirname(path.realpath(__file__)), self.audioClip)
        except:
            return False

        recognizer = sr.Recognizer()
        af = sr.AudioFile(audio_file)
        with af as source:
            audio = recognizer.record(source)

        try:
            index = self.voiceComboValues.currentIndex()
            transcript = recognizer.recognize_google(audio, language=self.voiceComboKeys.itemText(index))
            self.saveToFile(transcript)
            self.showDialog()

        except sr.UnknownValueError:
            try:
                print("Google could not understand audio")
            except:
                pass
        except sr.RequestError as e:
            print("Google error; {0}".format(e))

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

    def save_text(self):
        filename = QFileDialog.getSaveFileName(self, "Save File", "", "Text File (*.txt)")
        if filename != ('', ''):
            try:
                f = open(filename[0], 'w', encoding='UTF-8')
            except:
                f = open(filename[0], 'w')
            revisedText = self.textBox.toPlainText()
            f.write(revisedText)
            f.close()


def main():
    app = QApplication(sys.argv)
    program = Program()
    program.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()