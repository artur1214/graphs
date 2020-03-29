from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import sys
import random
import logic


class MainWindow(QtWidgets.QWidget):
    graph_res = []
    graph_res1 = []
    res_graph = None
    def __init__(self):
        self.cur_value = 0
        super().__init__()
        loadUi('graph.ui', self)
        self.ok_btn.clicked.connect(self.ok_pressed)
        self.spin.valueChanged.connect(self.change_graph_size)
        self.random_btn.clicked.connect(self.__random_fill)

    def __random_fill(self):
        m = random.random()
        t = False
        for i in range(self.cur_value):
            for j in range(self.cur_value):
                if random.random() > m:
                    t = True
                else:
                    t = False
                self.graph.cellWidget(i, j).setChecked(t)

    def change_graph_size(self):
        n = self.cur_value - int(self.spin.value())
        self.cur_value = int(self.spin.value())
        self.graph.setColumnCount(self.cur_value)
        self.graph.setRowCount(self.cur_value)
        if n < 0:
            for i in range(self.cur_value):
                for j in range(n + self.cur_value, self.cur_value):
                    self.graph.setCellWidget(i, self.cur_value - 1, QtWidgets.QCheckBox())
                    if i == self.cur_value - 1:
                        for m in range(self.cur_value - 1):
                            self.graph.setCellWidget(i, m, QtWidgets.QCheckBox())

    def ok_pressed(self):
        self.graph_res = []
        self.graph_res1 = []
        for i in range(self.cur_value):
            self.graph_res1.append([])
            for j in range(self.cur_value):
                if self.graph.cellWidget(i, j).isChecked():
                    self.graph_res.append((i + 1, j + 1))
                    self.graph_res1[i].append(j)
        self.res_graph = logic.Graph(self.graph_res1)
        #self.res_graph.analize()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    try:
        window = MainWindow()
        window.show()
    except Exception as e:
        print(e)
    sys.exit(app.exec_())
