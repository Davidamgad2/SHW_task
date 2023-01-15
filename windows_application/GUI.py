from PyQt5 import QtCore, QtGui, QtWidgets, uic
import requests
import json

url = 'http://localhost:8000/quote/random'

class Ui_Quote(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_Quote,self).__init__()
        uic.loadUi("windows_application/Design.ui", self)

        self.author_label=self.findChild(QtWidgets.QLabel,"Author")
        self.quote_label=self.findChild(QtWidgets.QLabel,"QuoteData")
        self.get_quote=self.findChild(QtWidgets.QPushButton,"pushButton")
        self.get_quote.clicked.connect(self._get_quote)

    
    def _get_quote(self):
        """Handling the request to get quote and parse the data into it"""
        try:
            headers = {'Authorization': 'bearer SHEBAK@2022'}
            _quote_data=requests.get(url,headers=headers)
            json_data=_quote_data.json()
            self.quote_label.setText(json_data['quote'])
            self.quote_label.adjustSize()
            self.quote_label.setWordWrap(True)

            self.author_label.setText(json_data['author'])
        except:
            pass

if __name__ == "__main__":
    import sys
    import os
    app = QtWidgets.QApplication(sys.argv)
    Queue_system = Ui_Quote()
    Queue_system.show()

    sys.exit(app.exec_())


