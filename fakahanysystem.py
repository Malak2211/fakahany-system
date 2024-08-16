#Welcome to the fakahany system🍎
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(722, 580)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 130, 721, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.fruit = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.fruit.setContentsMargins(0, 0, 0, 0)
        self.fruit.setSpacing(0)
        self.fruit.setObjectName("fruit")
        self.apple = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.apple.setObjectName("apple")
        self.fruit.addWidget(self.apple)
        self.banana = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.banana.setObjectName("banana")
        self.fruit.addWidget(self.banana)
        self.guava = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.guava.setObjectName("guava")
        self.fruit.addWidget(self.guava)
        self.passion = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.passion.setObjectName("passion")
        self.fruit.addWidget(self.passion)
        self.watermelon = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.watermelon.setObjectName("watermelon")
        self.fruit.addWidget(self.watermelon)
        self.mango3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.mango3.setObjectName("mango3")
        self.fruit.addWidget(self.mango3)
        self.pomegrate = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pomegrate.setObjectName("pomegrate")
        self.fruit.addWidget(self.pomegrate)
        self.grape = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.grape.setObjectName("grape")
        self.fruit.addWidget(self.grape)
        self.apricot = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.apricot.setObjectName("apricot")
        self.fruit.addWidget(self.apricot)
        self.esm_el_ma7el = QtWidgets.QLabel(self.centralwidget)
        self.esm_el_ma7el.setGeometry(QtCore.QRect(220, 20, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.esm_el_ma7el.setFont(font)
        self.esm_el_ma7el.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.esm_el_ma7el.setObjectName("esm_el_ma7el")
        self.total = QtWidgets.QLabel(self.centralwidget)
        self.total.setGeometry(QtCore.QRect(20, 310, 291, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.total.setFont(font)
        self.total.setObjectName("total")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 320, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 180, 721, 21))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.price = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.price.setContentsMargins(0, 0, 0, 0)
        self.price.setSpacing(0)
        self.price.setObjectName("price")
        self.applepr = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.applepr.setObjectName("applepr")
        self.price.addWidget(self.applepr)
        self.bananapr = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.bananapr.setObjectName("bananapr")
        self.price.addWidget(self.bananapr)
        self.guavapr = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.guavapr.setObjectName("guavapr")
        self.price.addWidget(self.guavapr)
        self.passionpr = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.passionpr.setObjectName("passionpr")
        self.price.addWidget(self.passionpr)
        self.watermelonpr = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.watermelonpr.setObjectName("watermelonpr")
        self.price.addWidget(self.watermelonpr)
        self.mango3pr = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.mango3pr.setObjectName("mango3pr")
        self.price.addWidget(self.mango3pr)
        self.pomegratepr = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.pomegratepr.setObjectName("pomegratepr")
        self.price.addWidget(self.pomegratepr)
        self.grapepr = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.grapepr.setObjectName("grapepr")
        self.price.addWidget(self.grapepr)
        self.apricotpr = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.apricotpr.setObjectName("apricotpr")
        self.price.addWidget(self.apricotpr)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 722, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.apple.setText(_translate("MainWindow", "Apples"))
        self.banana.setText(_translate("MainWindow", "Bananas"))
        self.guava.setText(_translate("MainWindow", "Guavas"))
        self.passion.setText(_translate("MainWindow", "Passionfruit"))
        self.watermelon.setText(_translate("MainWindow", "Watermelon"))
        self.mango3.setText(_translate("MainWindow", "Mangoes (عويس)"))
        self.pomegrate.setText(_translate("MainWindow", "Pomegrate"))
        self.grape.setText(_translate("MainWindow", "Mangoes(سكري)"))
        self.apricot.setText(_translate("MainWindow", "Apricots"))
        self.esm_el_ma7el.setText(_translate("MainWindow", "Fakahany System🍎"))
        self.total.setText(_translate("MainWindow", "Total cost: 0.00 EGP"))
        self.pushButton.setText(_translate("MainWindow", "CHECKOUT"))
        self.applepr.setText(_translate("MainWindow", "            0"))
        self.bananapr.setText(_translate("MainWindow", "            0"))
        self.guavapr.setText(_translate("MainWindow", "            0"))
        self.passionpr.setText(_translate("MainWindow", "            0"))
        self.watermelonpr.setText(_translate("MainWindow", "           0"))
        self.mango3pr.setText(_translate("MainWindow", "            0"))
        self.pomegratepr.setText(_translate("MainWindow", "            0"))
        self.grapepr.setText(_translate("MainWindow", "            0"))
        self.apricotpr.setText(_translate("MainWindow", "            0"))

from PyQt5 import QtWidgets, QtCore
class Supermarket_App(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.fruits={
            "Apples": 0,
            "Bananas": 0,
            "Guavas": 0,
            "Passionfruit": 0,
            "Watermelon": 0,
            "Mangoes (عويس)": 0,
            "Pomegrate": 0,
            "Grapes": 0,
            "Apricots": 0
    }
        self.price={
            "Apples": 2.4,
            "Bananas": 6.0,
            "Guavas": 4.5,
            "Passionfruit": 7.0,
            "Watermelon": 100.2,
            "Mangoes (عويس)": 5.0,
            "Pomegrate": 20.8,
            "Grapes": 7.0,
            "Apricots": 3.0
        }
        self.ui.apple.clicked.connect(self.update_apple_count)
        self.ui.banana.clicked.connect(self.update_banana_count)
        self.ui.guava.clicked.connect(self.update_guava_count)
        self.ui.passion.clicked.connect(self.update_passion_count)
        self.ui.watermelon.clicked.connect(self.update_watermelon_count)
        self.ui.mango3.clicked.connect(self.update_mango3_count)
        self.ui.pomegrate.clicked.connect(self.update_pomegrate_count)
        self.ui.grape.clicked.connect(self.update_grape_count)
        self.ui.apricot.clicked.connect(self.update_apricot_count)
        self.ui.pushButton.clicked.connect(self.checkout)
        self.update_price()

    def fruit_count(self, fruit_name):
           
                self.fruits[fruit_name] += 1
                self.update_price()
               
                 
                 

    def update_price(self):
            self.ui.applepr.setText(f"            {self.fruits['Apples']}")
            self.ui.bananapr.setText(f"           {self.fruits['Bananas']}")
            self.ui.guavapr.setText(f"            {self.fruits['Guavas']}")
            self.ui.passionpr.setText(f"            {self.fruits['Passionfruit']}")
            self.ui.watermelonpr.setText(f"            {self.fruits['Watermelon']}")
            self.ui.mango3pr.setText(f"            {self.fruits['Mangoes (عويس)']}")
            self.ui.pomegratepr.setText(f"            {self.fruits['Pomegrate']}")
            self.ui.grapepr.setText(f"            {self.fruits['Grapes']} ")
            self.ui.apricotpr.setText(f"            {self.fruits['Apricots']}")
            total_cost = 0
            for fruit_name, count in self.fruits.items():
                total_cost += count * self.price[fruit_name]
            self.ui.total.setText(f"Total cost: {total_cost:.2f} EGP")
      
    def update_apple_count(self):
        self.fruit_count("Apples")

    def update_banana_count(self):
        self.fruit_count("Bananas")

    def update_guava_count(self):
        self.fruit_count("Guavas")

    def update_passion_count(self):
        self.fruit_count("Passionfruit")

    def update_watermelon_count(self):
        self.fruit_count("Watermelon")

    def update_mango3_count(self):
        self.fruit_count("Mangoes (عويس)")

    def update_pomegrate_count(self):
        self.fruit_count("Pomegrate")

    def update_grape_count(self):
        self.fruit_count("Grapes")

    def update_apricot_count(self):
        self.fruit_count("Apricots")
    
   
        
    def checkout(self,fruit_name):
            for fruit_name in self.fruits:
                   self.fruits[fruit_name] = 0
                   self.update_price()

          
       
   


app = QtWidgets.QApplication([])
window = Supermarket_App()
window.show()
app.exec_()