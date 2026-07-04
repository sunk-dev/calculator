class Control:
    def __init__(self,view):
        self.view=view
        self.connetSignals()
    def connetSignals(self):
        self.view.btn1.clicked.connect(self.view.activateMessage)
        self.view.btn2.clicked.connect(self.view.clearMessage)
        