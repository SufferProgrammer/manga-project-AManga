#!/usr/bin/python3.5
from Handler import Handler
from PyQt4 import QtGui
from PyQt4 import QtCore
from UI import main_ui
import sys
import os

class Main(QtGui.QMainWindow, main_ui.Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.screenControl()
        self.webView.load(QtCore.QUrl('http://pii-chan.tk'))
        self.webView.hasFocus()
        
    def screenControl(self):
        mainWindowsPos = self.frameGeometry()
        centerGetDisplayScreen = QtGui.QDesktopWidget().availableGeometry().center()
        mainWindowsPos.moveCenter(centerGetDisplayScreen)
        self.move(mainWindowsPos.topLeft())
                    
        
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    
    splash_img = QtGui.QPixmap('UI/image/icon/splash.png')
    makeSplash = QtGui.QSplashScreen(splash_img, QtCore.Qt.WindowStaysOnTopHint)
    prog = QtGui.QProgressBar(makeSplash)
    prog.move(175, 270)
    makeSplash.setMask(splash_img.mask())
    makeSplash.show()
    prog.setTextVisible(True)
    for count in range(0, 101):
        prog.setValue(count)
        if prog.text() == '99%':
            app.processEvents()
            connection = Handler.Request()
            reqCodeConnection = connection.getResponseStatus()
            if reqCodeConnection == 200:
                form = Main()
                makeSplash.finish(form)
                form.show()
                
            else:
                prog.setFormat('Error...')
                errorNotif = QtGui.QMessageBox()
                askRetryConnection = errorNotif.question(makeSplash, 'Error connection', 'Connection to server error, want to reconnect ?', QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
                if askRetryConnection == QtGui.QMessageBox.Yes:
                    QtCore.QProcess.startDetached(__file__, 'AManga.py')
                    sys.exit(0)
                else:
                    sys.exit(0)

    sys.exit(app.exec_())

