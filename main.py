import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget
from random import randint
from UI import Ui_Form


class GoodMood(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.draw)

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        r = randint(0, min(self.window().width(), self.window().height())) // 2
        qp.drawEllipse(randint(0, self.window().width() - 2 * r),
                       randint(0, self.window().height() - 2 * r), r, r)

    def draw(self):
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GoodMood()
    ex.show()
    sys.exit(app.exec())
