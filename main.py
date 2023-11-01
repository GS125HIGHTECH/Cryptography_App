from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QApplication
import base64


class Ui_MainWindow(object):
    def __init__(self):
        self.textEdit_3 = None
        self.scrollAreaWidgetContents_3 = None
        self.encryption_type = None
        self.actionRedo = None
        self.actionUndo = None
        self.actionNew = None
        self.actionExit = None
        self.actionSave = None
        self.encode_decode = None
        self.statusbar = None
        self.menuExit = None
        self.menuFile = None
        self.textEdit_2 = None
        self.scrollAreaWidgetContents_2 = None
        self.scrollArea_2 = None
        self.scrollArea_3 = None
        self.textEdit = None
        self.scrollAreaWidgetContents = None
        self.scrollArea = None
        self.label_2 = None
        self.label_3 = None
        self.pushButton_3 = None
        self.pushButton_2 = None
        self.pushButton = None
        self.radioButton_3 = None
        self.radioButton_2 = None
        self.radioButton = None
        self.label = None
        self.centralwidget = None
        self.menubar = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Cryptography App")
        MainWindow.setFixedSize(820, 660)
        MainWindow.setMaximumSize(820, 660)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("encryption.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 45, 400, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(20, 100, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 150, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 200, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_3.setCheckable(True)
        self.radioButton_3.setChecked(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("QPushButton { color: green; }")
        self.pushButton.setGeometry(QtCore.QRect(640, 285, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.confirm)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 563, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton2")
        self.pushButton_2.clicked.connect(self.copy_text)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(670, 66, 120, 30))
        self.pushButton_3.setStyleSheet("QPushButton { color: red; }")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton3")
        self.pushButton_3.clicked.connect(self.erase_text)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 315, 400, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 10, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(189, 99, 600, 180))
        self.scrollArea.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 598, 178))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 600, 180))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setStyleSheet("background-color: white; color: black;")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(28, 360, 760, 200))
        self.scrollArea_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 758, 198))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 0, 760, 200))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_2.setFont(font)
        self.textEdit_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textEdit_2.setUndoRedoEnabled(False)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textEdit_2.setObjectName("textEdit_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.scrollArea_3 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_3.setGeometry(QtCore.QRect(388, 5, 400, 50))
        self.scrollArea_3.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 398, 48))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.textEdit_3 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_3.setGeometry(QtCore.QRect(0, 0, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_3.setFont(font)
        self.textEdit_3.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_3.setStyleSheet("background-color: white; color: black;")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.encode_decode = QtWidgets.QComboBox(self.centralwidget)
        self.encode_decode.setGeometry(QtCore.QRect(15, 20, 140, 30))
        self.encode_decode.setStyleSheet("QComboBox { font-family: Arial; font-size: 12pt; font-weight: bold; }")
        self.encode_decode.setObjectName("encode_decode")
        self.encode_decode.addItem("Encode")
        self.encode_decode.addItem("Decode")
        self.encode_decode.setCurrentIndex(0)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(self.save_file)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(self.exit_app)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionNew.triggered.connect(self.reset_fields)
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionUndo.triggered.connect(self.textEdit.undo)
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionRedo.triggered.connect(self.textEdit.redo)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuExit.addAction(self.actionUndo)
        self.menuExit.addAction(self.actionRedo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())

        self.encryption_type = "Vigenere"
        self.radioButton.toggled.connect(self.set_encryption_type)
        self.radioButton_2.toggled.connect(self.set_encryption_type)
        self.radioButton_3.toggled.connect(self.set_encryption_type)

        self.translateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def set_encryption_type(self):
        self.textEdit_2.clear()
        self.textEdit_3.clear()
        if self.radioButton.isChecked():
            self.label_3.show()
            self.scrollArea_3.show()
            self.encryption_type = "Vigenere"
        elif self.radioButton_2.isChecked():
            self.label_3.hide()
            self.scrollArea_3.hide()
            self.encryption_type = "ROT13"
        elif self.radioButton_3.isChecked():
            self.label_3.hide()
            self.scrollArea_3.hide()
            self.encryption_type = "Base64"

    def translateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cryptography App"))
        self.label.setText(_translate("MainWindow", "Please enter your input here:"))
        self.radioButton.setText(_translate("MainWindow", "Vigenere Cypher"))
        self.radioButton_2.setText(_translate("MainWindow", "ROT13"))
        self.radioButton_3.setText(_translate("MainWindow", "Base64"))
        self.pushButton.setText(_translate("MainWindow", "Confirm"))
        self.pushButton_2.setText(_translate("MainWindow", "Copy"))
        self.pushButton_3.setText(_translate("MainWindow", "Erase"))
        self.label_2.setText(_translate("MainWindow", "Result:"))
        self.label_3.setText(_translate("MainWindow", "Key:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuExit.setTitle(_translate("MainWindow", "Edit"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save a file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit app"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Shift+X"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create a new file"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setStatusTip(_translate("MainWindow", "Undo an action"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setStatusTip(_translate("MainWindow", "Redo an action"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z"))

    def save_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(None, "Zapisz plik", "",
                                                   "Pliki tekstowe (*.txt);;Wszystkie pliki (*)", options=options)

        if file_name:
            with open(file_name, "w") as file:
                input_text = self.textEdit.toPlainText()
                result_text = self.textEdit_2.toPlainText()

                if self.radioButton.isChecked():
                    key = self.textEdit_3.toPlainText()
                    file.write("User Input:\n" + input_text + "\n\nKey:\n" + key + "\n\nResult:\n" + result_text)
                else:
                    file.write("User Input:\n" + input_text + "\n\nResult:\n" + result_text)

    @staticmethod
    def exit_app():
        reply = QMessageBox.question(None, 'Confirm Exit', 'Are you sure you want to exit the application?', QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)

        if reply == QMessageBox.Yes:
            sys.exit(0)

    def reset_fields(self):
        reply = QMessageBox.question(None, 'Confirm New', 'Are you sure you want to start a new file? Any unsaved changes will be lost.', QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)

        if reply == QMessageBox.Yes:
            self.textEdit.clear()
            self.textEdit_2.clear()

    def erase_text(self):
        self.textEdit.clear()
        self.textEdit_3.clear()

    def copy_text(self):
        result_text = self.textEdit_2.toPlainText()
        clipboard = QApplication.clipboard()
        clipboard.setText(result_text)

    @staticmethod
    def encode_rot13(text):
        encoded_text = ""
        for char in text:
            if char.isalpha():
                if char.isupper():
                    encoded_char = chr(((ord(char) - ord('A') + 13) % 26) + ord('A'))
                else:
                    encoded_char = chr(((ord(char) - ord('a') + 13) % 26) + ord('a'))
                encoded_text += encoded_char
            else:
                encoded_text += char
        return encoded_text

    def decode_rot13(self, text):
        return self.encode_rot13(text)

    @staticmethod
    def vigenere_encode(text, key):
        encrypted_text = ""
        key_length = len(key)

        for i in range(len(text)):
            char = text[i]
            key_char = key[i % key_length]
            shift = ord(key_char.lower()) - ord('a')

            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            elif char.isupper():
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:
                encrypted_char = char

            encrypted_text += encrypted_char

        return encrypted_text

    @staticmethod
    def vigenere_decode(text, key):
        decrypted_text = ""
        key_length = len(key)

        for i in range(len(text)):
            char = text[i]
            key_char = key[i % key_length]
            shift = ord(key_char.lower()) - ord('a')

            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
            elif char.isupper():
                decrypted_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
            else:
                decrypted_char = char

            decrypted_text += decrypted_char

        return decrypted_text

    def confirm(self):
        input_text = self.textEdit.toPlainText()
        operation = self.encode_decode.currentText()
        key = self.textEdit_3.toPlainText()

        if operation == "Encode":
            if self.radioButton.isChecked():
                if len(key) < 2:
                    QMessageBox.warning(None, "Warning", "Key must have a length of at least 2 characters.")
                    return

                if not key.isalnum():
                    QMessageBox.warning(None, "Warning", "Key must contain only alphanumeric characters.")
                    return

                encoded_text = self.vigenere_encode(input_text, key)
                self.textEdit_2.setPlainText(encoded_text)

                pass
            elif self.radioButton_2.isChecked():
                encoded_text = self.encode_rot13(input_text)
                self.textEdit_2.setPlainText(encoded_text)
                pass
            elif self.radioButton_3.isChecked():
                try:
                    encoded_text = base64.b64encode(input_text.encode()).decode()
                    self.textEdit_2.setPlainText(encoded_text)
                except Exception as e:
                    self.textEdit_2.setPlainText("Error decoding Base64: " + str(e))
        else:  # "Decode"
            if self.radioButton.isChecked():
                if len(key) < 2:
                    QMessageBox.warning(None, "Warning", "Key must have a length of at least 2 characters.")
                    return

                if not key.isalnum():
                    QMessageBox.warning(None, "Warning", "Key must contain only alphanumeric characters.")
                    return
                decoded_text = self.vigenere_decode(input_text, key)
                self.textEdit_2.setPlainText(decoded_text)

                pass
            elif self.radioButton_2.isChecked():
                decoded_text = self.decode_rot13(input_text)
                self.textEdit_2.setPlainText(decoded_text)
                pass
            elif self.radioButton_3.isChecked():
                try:
                    decoded_text = base64.b64decode(input_text).decode()
                    self.textEdit_2.setPlainText(decoded_text)
                except Exception as e:
                    self.textEdit_2.setPlainText("Error decoding Base64: " + str(e))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
