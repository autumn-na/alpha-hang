import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QLineEdit)

name = ''

class Alpha(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl_name = QLabel('이름:',self)
        self.add_but = QPushButton('시작', self)

        self.add_but.clicked.connect(self.Start)

        self.nameEdit = QLineEdit()

        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(self.lbl_name)
        hbox_1.addWidget(self.nameEdit)

        hbox_2 = QHBoxLayout()
        hbox_2.addStretch(1)
        hbox_2.addWidget(self.add_but)


        vbox = QVBoxLayout()
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)


        self.setLayout(vbox)


        self.setGeometry(150, 150, 300, 150)
        self.setWindowTitle('AlPha Hang!')
        self.show()

    def Start(self):
        global name
        if self.nameEdit.text():
            name = self.nameEdit.text()
            sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Alpha()
    sys.exit(app.exec_())

