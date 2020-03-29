from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import sys
import random
import logic
from algoritms import min_path


class MainWindow(QtWidgets.QWidget):
    graph_res = []
    graph_res1 = []
    res_graph = None

    def __init__(self):
        self.cur_value = 0
        super().__init__()
        loadUi('graphview.ui', self)
        self.ok_btn.clicked.connect(self.ok_pressed1)
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
                if t:
                    self.graph.cellWidget(i, j).setValue(random.randint(1, 100))
                else:
                    self.graph.cellWidget(i, j).setValue(0)

    def change_graph_size(self):
        n = self.cur_value - int(self.spin.value())
        self.cur_value = int(self.spin.value())
        self.graph.setColumnCount(self.cur_value)
        self.graph.setRowCount(self.cur_value)
        if n < 0:
            for i in range(self.cur_value):
                for j in range(n + self.cur_value, self.cur_value):
                    # self.graph.setCellWidget(i, self.cur_value - 1, QtWidgets.QCheckBox())
                    self.graph.setCellWidget(i, self.cur_value-1, QtWidgets.QSpinBox())
                    self.graph.cellWidget(i, self.cur_value-1).setRange(0, 100)
                    if i == self.cur_value - 1:
                        for m in range(self.cur_value - 1):
                            self.graph.setCellWidget(i, m, QtWidgets.QSpinBox())
                            self.graph.cellWidget(i, m).setRange(0, 100)

    def ok_pressed(self):
        self.graph_res = []
        self.graph_res1 = []
        for i in range(self.cur_value):
            self.graph_res1.append([])
            for j in range(self.cur_value):
                if self.graph.cellWidget(i, j).value():
                    self.graph_res.append((i + 1, j + 1))
                    self.graph_res1[i].append(j)
        self.res_graph = logic.Graph(self.graph_res1)

    def ok_pressed1(self):
        self.graph_res1 = dict()
        for i in range(self.cur_value):
            self.graph_res1[i] = dict()
            for j in range(self.cur_value):
                if self.graph.cellWidget(i, j).value():
                    self.graph_res1[i][j] = self.graph.cellWidget(i, j).value()
        self.res_graph = logic.Graph(self.graph_res1)
        self.res_graph.analize()
        self.label.setText(str(self.res_graph.analize_res))

if __name__ == '__main__':
    try:
        app = QtWidgets.QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)

