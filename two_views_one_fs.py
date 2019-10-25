import sys
from PySide2.QtWidgets import QApplication, QSplitter, QFileSystemModel, QTreeView, QListView
from PySide2.QtCore import QDir

if __name__ == '__main__':
    app = QApplication(sys.argv)
    splitter = QSplitter()
    model = QFileSystemModel()
    model.setRootPath("/")
    tree = QTreeView(splitter)
    tree.setModel(model)
    tree.setRootIndex(model.index("/"))
    list = QListView(splitter)
    list.setModel(model)
    list.setRootIndex(model.index("/"))
    splitter.setWindowTitle("A model with two views or two views with one model")
    splitter.show()
    app.exec_()



