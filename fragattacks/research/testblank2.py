import sys
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os
import time
import psutil
timetotal = QTime(0, 0, 0)
timecmd = QTime(0, 0, 0)
complete = 0
totalprocess=0
group=""
finaloutput=""
passed=0
failed=0
unknown=0
network=""
networkname=""
networkpassword=""
check1=0
check2=0
consolelogfile=""
resultfile=""
resultlist=[]
k=0

class Worker(QObject):
	finished = pyqtSignal()
	progress = pyqtSignal(int)
	processno = pyqtSignal(int)
	process = pyqtSignal(str)
	output = pyqtSignal(str)
	expectedtime = pyqtSignal(str)

	def run(self):
		"""Long-running task."""
		i=0
		processno=0
		global network
		if(group=="Group-1"):
			process="./fragattack.py "+network+" ping"
			processno=processno+1
			self.expectedtime.emit("00:00:10")
			self.processno.emit(processno)
			stream1 = os.popen(process)
			output1 = stream1.read()
			i=i+1
			self.progress.emit(i)
			self.output.emit(output1)
			self.process.emit(process)

			process="./fragattack.py "+network+" ping I,E,E"
			processno=processno+1
			self.expectedtime.emit("00:00:09")
			self.processno.emit(processno)
			stream1 = os.popen(process)
			output1 = stream1.read()
			i=i+1
			self.progress.emit(i)
			self.output.emit(output1)
			self.process.emit(process)

			process="./fragattack.py "+network+" ping I,E,E --delay 5"
			processno=processno+1
			self.expectedtime.emit("00:00:07")
			self.processno.emit(processno)
			stream1 = os.popen(process)
			output1 = stream1.read()
			i=i+1
			self.progress.emit(i)
			self.output.emit(output1)
			self.process.emit(process)
   
			process="./fragattack.py "+network+" ping-frag-sep"
			processno=processno+1
			self.expectedtime.emit("00:00:13")
			self.processno.emit(processno)
			stream1 = os.popen(process)
			output1 = stream1.read()
			i=i+1
			self.progress.emit(i)
			self.output.emit(output1)
			self.process.emit(process)
   
			process="./fragattack.py "+network+" ping-frag-sep --pn-per-qos"
			processno=processno+1
			self.expectedtime.emit("00:00:14")
			self.processno.emit(processno)
			stream1 = os.popen(process)
			output1 = stream1.read()
			i=i+1
			self.progress.emit(i)
			self.output.emit(output1)
			self.process.emit(process)
   
			process="./fragattack.py "+network+" ping I,E --amsdu"
			processno=processno+1
			self.expectedtime.emit("00:00:14")
			self.processno.emit(processno)
			stream1 = os.popen(process)
			output1 = stream1.read()
			i=i+1
			self.progress.emit(i)
			self.output.emit(output1)
			self.process.emit(process)
   
			process="./fragattack.py "+network+" ping I,P,P"
			processno=processno+1
			self.expectedtime.emit("00:00:07")
			self.processno.emit(processno)
			stream1 = os.popen(process)
			output1 = stream1.read()
			i=i+1
			self.progress.emit(i)
			self.output.emit(output1)
			self.process.emit(process)
   
			process="./fragattack.py "+network+" ping I,P"
			processno=processno+1
			self.expectedtime.emit("00:00:08")
			self.processno.emit(processno)
			stream1 = os.popen(process)
			output1 = stream1.read()
			i=i+1
			self.progress.emit(i)
			self.output.emit(output1)
			self.process.emit(process)
   
			process="./fragattack.py "+network+" ping I,E,P"
			processno=processno+1
			self.expectedtime.emit("00:00:09")
			self.processno.emit(processno)
			stream1 = os.popen(process)
			output1 = stream1.read()
			i=i+1
			self.progress.emit(i)
			self.output.emit(output1)
			self.process.emit(process)
   
   
			process="./fragattack.py "+network+" ping I,P,E"
			processno=processno+1
			self.expectedtime.emit("00:00:07")
			self.processno.emit(processno)
			stream1 = os.popen(process)
			output1 = stream1.read()
			i=i+1
			self.progress.emit(i)
			self.output.emit(output1)
			self.process.emit(process)

		if(group=="Group-2"):
			process="ping www.google.com"
			processno=processno+1
			self.expectedtime.emit("00:00:03")
			self.processno.emit(processno)
			stream1 = os.popen(process)
			output1 = stream1.read()
			i=i+1
			self.progress.emit(i)
			self.output.emit(output1)
			self.process.emit(process)

			process="ping ab"
			processno=processno+1
			self.expectedtime.emit("00:00:03")
			self.processno.emit(processno)
			stream1 = os.popen(process)
			output1 = stream1.read()
			i=i+1
			self.progress.emit(i)
			self.output.emit(output1)
			self.process.emit(process)

		self.finished.emit()


class FirstPage(QMainWindow):
	def __init__(self):
		super(FirstPage,self).__init__()
		self.splash = QSplashScreen(QPixmap('Splash2.png'))
		self.splash.show()
		time.sleep(2)
		self.secondPage()

		# label.mousePressEvent = self.secondPage
	   

	# def secondPage(self, event):                       
	#     self.secondWindow = SecondPage()
	#     self.secondWindow.show()
	#     self.close()

	def secondPage(self):                       
		self.secondPage = SecondPage()
		self.secondPage.show()
		self.splash.hide()
		self.close()

class SecondPage(QMainWindow):     
	def closeEvent(self, event):
         cmd="airmon-ng stop "+network+" &&  sudo systemctl restart NetworkManager.service"
       	 stream1 = os.popen(cmd)
       	 output1 = stream1.read()
         event.accept()	
        
	def __init__(self):
		super(SecondPage,self).__init__()
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()

		self.setGeometry(0, 0, 755, 551)
		self.setFixedSize(755, 551)
		qr.moveCenter(cp)
		self.move(qr.topLeft())
		self.setWindowTitle("FRAG Test Tool")
		# self.Background = QLabel(self)
		# self.Background.setGeometry(QRect(-10, -10, 821, 591))
		# self.Background.setText("")
		# self.Background.setPixmap(QPixmap("background.jpg"))
		# self.Background.setObjectName("Background")

		#logo frame
		self.LogoFrame = QFrame(self)
		self.LogoFrame.setGeometry(QRect(20, 20, 351, 421))
		#self.LogoFrame.setStyleSheet("border-style: none;")
		#self.LogoFrame.setFrameShape(QFrame.StyledPanel)
		#self.LogoFrame.setFrameShadow(QFrame.Raised)
		self.LogoFrame.setObjectName("LogoFrame")
		self.LogoMedium = QLabel(self.LogoFrame)
		self.LogoMedium.setGeometry(QRect(10, 50, 321, 341))
		self.LogoMedium.setText("")
		self.LogoMedium.setPixmap(QPixmap("logo.png"))
		self.LogoMedium.setObjectName("LogoMedium")


		#first frame
		self.IntroFrame = QFrame(self)
		self.IntroFrame.setGeometry(QRect(450, 20, 311, 421))
		#self.IntroFrame.setFrameShape(QFrame.StyledPanel)
		#self.IntroFrame.setFrameShadow(QFrame.Raised)
		self.IntroFrame.setObjectName("IntroFrame")
		self.IntroFrameBottom = QFrame(self)
		self.IntroFrameBottom.setGeometry(QRect(20, 460, 741, 81))
		#self.IntroFrameBottom.setFrameShape(QFrame.StyledPanel)
		#self.IntroFrameBottom.setFrameShadow(QFrame.Raised)
		self.IntroFrameBottom.setObjectName("IntroFrameBottom")
		self.Info = QTextEdit(self.IntroFrame)
		self.Info.setGeometry(QRect(0, 120, 240, 291))
		self.Info.setObjectName("Info")
		self.Info.setText("FragAttacks (fragmentation and aggregation attacks) which is a collection of new security vulnerabilities that affect Wi-Fi devices. An adversary that is within range of a victim's Wi-Fi network can abuse these vulnerabilities to steal user information or attack devices.\n\nOur tool helps people to find out whether these vulnerabilities are present in their network or not without much of a hassle.")
		self.Info.setEnabled(False)
		self.Info.setStyleSheet(
		"QTextEdit::disabled"
		"{"
		"background-color:transparent;"
		"color:black;"
		"border:none"
		"}")
		self.IntroNextButton = QPushButton(self.IntroFrameBottom)
		self.IntroNextButton.setGeometry(QRect(620, 20, 93, 28))
		self.IntroNextButton.setObjectName("IntroNextButton")
		self.IntroNextButton.setText("Next")
		self.IntroNextButton.clicked.connect(lambda: self.IntroNextPage())
		self.IntroNextButton.setCursor(QCursor(Qt.PointingHandCursor))
		

		
		# self.IntroFrame.show()
		# self.IntroFrameBottom.show()
		# self.IntroNextButton.show()

		#second frame
		self.NetworkFrame = QFrame(self)
		self.NetworkFrame.setGeometry(QRect(420, 20, 351, 421))
		#self.NetworkFrame.setFrameShape(QFrame.StyledPanel)
		#self.NetworkFrame.setFrameShadow(QFrame.Raised)
		self.NetworkFrame.setObjectName("NetworkFrame")
		self.NetworkFrameBottom = QFrame(self)
		self.NetworkFrameBottom.setGeometry(QRect(20,460,741,81))
		#self.NetworkFrameBottom.setFrameShape(QFrame.StyledPanel)
		#self.NetworkFrameBottom.setFrameShadow(QFrame.Raised)
		self.NetworkFrameBottom.setObjectName("NetworkFrameBottom")
		self.NetworksDrop = QComboBox(self.NetworkFrame)
		self.NetworksDrop.setGeometry(QRect(80, 50, 73, 22))
		self.NetworksDrop.setObjectName("NetworksDrop")
		self.MonitorButton = QPushButton(self.NetworkFrame)
		self.MonitorButton.setGeometry(QRect(200, 50, 93, 28))
		self.MonitorButton.setObjectName("MonitorButton")
		self.MonitorButton.setCursor(QCursor(Qt.PointingHandCursor))
		self.NameInput = QLineEdit(self.NetworkFrame)
		self.NameInput.setGeometry(QRect(130, 120, 113, 22))
		self.NameInput.setObjectName("NameInput")
		self.PasswordInput = QLineEdit(self.NetworkFrame)
		self.PasswordInput.setGeometry(QRect(130, 170, 113, 22))
		self.PasswordInput.setObjectName("PasswordInput")
		self.PasswordInput.setEchoMode(QLineEdit.Password)
		self.namelabel = QLabel(self.NetworkFrame)
		self.namelabel.setGeometry(QRect(70, 120, 55, 16))
		self.namelabel.setObjectName("namelabel")
		self.passwordlabel = QLabel(self.NetworkFrame)
		self.passwordlabel.setGeometry(QRect(60, 170, 55, 16))
		self.passwordlabel.setObjectName("passwordlabel")
		self.NetworkNextButton = QPushButton(self.NetworkFrameBottom)
		self.NetworkNextButton.setGeometry(QRect(620, 20, 93, 28))
		self.NetworkNextButton.setObjectName("NetworkNextButton")
		self.NetworkNextButton.setCursor(QCursor(Qt.PointingHandCursor))
		self.NetworkBackButton = QPushButton(self.NetworkFrameBottom)
		self.NetworkBackButton.setGeometry(QRect(40, 20, 93, 28))
		self.NetworkBackButton.setObjectName("NetworkBackButton")
		self.NetworkBackButton.setCursor(QCursor(Qt.PointingHandCursor))
		self.ViewPassword = QCheckBox(self.NetworkFrame)
		self.ViewPassword.setGeometry(QRect(270, 170, 81, 20))
		self.ViewPassword.setObjectName("ViewPassword")
		self.InputDetailsButton = QPushButton(self.NetworkFrame)
		self.InputDetailsButton.setGeometry(QRect(140, 250, 93, 28))
		self.InputDetailsButton.setObjectName("InputDetailsButton")
		self.InputDetailsButton.setCursor(QCursor(Qt.PointingHandCursor))
		self.NetworkBackButton.setText("Back")
		self.NetworkNextButton.setText("Next")
		self.namelabel.setText("Name")
		self.passwordlabel.setText("Password")
		self.MonitorButton.setText("Monitor Mode")
		self.ViewPassword.setText("View")
		self.InputDetailsButton.setText("Input Details")
		self.NetworkFrame.hide()
		self.NetworkFrameBottom.hide()
		i=0
		
		addresses = psutil.net_if_addrs()
		stats = psutil.net_if_stats()
		for intface, addr_list in addresses.items():
		    if(intface[0].lower()=="w"):   
		        self.NetworksDrop.addItem("")
		        self.NetworksDrop.setItemText(i,(intface))
		        i=i+1
		
		# num=["wlan1","wlan2","wlan0","lan"]
		# for n in num:
		# 	if(n[0].lower()=="w"):
		# 		self.NetworksDrop.addItem("")
		# 		self.NetworksDrop.setItemText(i,(n))
		# 		i=i+1

		self.MonitorButton.clicked.connect(lambda: self.getnetwork(self.NetworksDrop.currentText()))
		self.ViewPassword.clicked.connect(lambda: self.passwordview())
		self.InputDetailsButton.clicked.connect(lambda: self.inputdetails())
		self.NetworkBackButton.clicked.connect(lambda: self.NetworkBackPage())
		self.NetworkNextButton.clicked.connect(lambda: self.NetworkNextPage())


		#third frame
		self.LogoSmallFrame = QFrame(self)
		self.LogoSmallFrame.setGeometry(QRect(20, 10, 121, 111))
		#self.LogoSmallFrame.setFrameShape(QFrame.StyledPanel)
		#self.LogoSmallFrame.setFrameShadow(QFrame.Raised)
		self.LogoSmallFrame.setObjectName("LogoSmallFrame")
		self.LogoSmall = QLabel(self.LogoSmallFrame)
		self.LogoSmall.setGeometry(QRect(10, 10, 101, 91))
		self.LogoSmall.setText("")
		self.LogoSmall.setPixmap(QPixmap("logo-small.png"))
		self.LogoSmall.setObjectName("LogoSmall")
		self.GrouptestFrame = QFrame(self)
		self.GrouptestFrame.setGeometry(QRect(50, 10, 600, 451))
		#self.GrouptestFrame.setFrameShape(QFrame.StyledPanel)
		#self.GrouptestFrame.setFrameShadow(QFrame.Raised)
		self.GrouptestFrame.setObjectName("GrouptestFrame")
		self.GrouptestFrameBottom = QFrame(self)
		self.GrouptestFrameBottom.setGeometry(QRect(20,460,741,81))
		#self.GrouptestFrameBottom.setFrameShape(QFrame.StyledPanel)
		#self.GrouptestFrameBottom.setFrameShadow(QFrame.Raised)
		self.GrouptestFrameBottom.setObjectName("GrouptestFrameBottom")
		self.label = QLabel(self.GrouptestFrame)
		self.label.setGeometry(QRect(150, 150, 55, 16))
		self.label.setText("0")
		self.label.setObjectName("label")
		self.progressBar = QProgressBar(self.GrouptestFrame)
		self.progressBar.setGeometry(QRect(230, 150, 250, 23))
		self.progressBar.setProperty("value", 0)
		self.progressBar.setTextVisible(True)
		self.progressBar.setOrientation(Qt.Horizontal)
		self.progressBar.setObjectName("progressBar")
		self.GroupsDrop = QComboBox(self.GrouptestFrame)
		self.GroupsDrop.setGeometry(QRect(230, 50, 73, 28))
		self.GroupsDrop.setObjectName("GroupsDrop")
		self.GroupsDrop.addItem("Group-1")
		self.GroupsDrop.addItem("Group-2")
		self.GroupsDrop.addItem("Group-3")
		self.GroupsDrop.addItem("Group-4")
		self.GroupsDrop.addItem("Group-5")
		self.runbutton = QPushButton(self.GrouptestFrame)
		self.runbutton.setGeometry(QRect(350, 50, 93, 28))
		self.runbutton.setObjectName("runbutton")
		self.runbutton.clicked.connect(lambda: self.runclicked())
		self.runbutton.setText("Run")
		self.runbutton.setCursor(QCursor(Qt.PointingHandCursor))
		self.viewmore = QPushButton(self.GrouptestFrame)
		self.viewmore.setGeometry(QRect(500, 150, 93, 28))
		self.viewmore.setObjectName("viewmore")
		self.viewmore.setText("View Details")
		self.viewmore.clicked.connect(lambda: self.details())
		self.viewmore.setCursor(QCursor(Qt.PointingHandCursor))
		self.textEdit = QTextEdit(self.GrouptestFrame)
		self.textEdit.setReadOnly(True)
		self.textEdit.setGeometry(QRect(100, 200, 491, 171))
		self.textEdit.setAutoFillBackground(False)
		self.textEdit.setObjectName("textEdit")
		self.totaltime = QLabel(self.GrouptestFrame)
		self.totaltime.setGeometry(QRect(270, 390, 55, 16))
		self.totaltime.setText("0")
		self.totaltime.setObjectName("totaltime")
		self.totalelapsed = QLabel(self.GrouptestFrame)
		self.totalelapsed.setGeometry(QRect(150, 390, 115, 16))
		self.totalelapsed.setText("Total Time Elapsed:")
		self.totalelapsed.setObjectName("totalelapsed")
		self.totalexpected1 = QLabel(self.GrouptestFrame)
		self.totalexpected1.setGeometry(QRect(370, 390, 125, 16))
		self.totalexpected1.setText("Total Time Expected:")
		self.totalexpected1.setObjectName("totalexpected1")
		self.totalexpected2 = QLabel(self.GrouptestFrame)
		self.totalexpected2.setGeometry(QRect(500, 390, 55, 16))
		self.totalexpected2.setText("")
		self.cmdtime = QLabel(self.GrouptestFrame)
		self.cmdtime.setGeometry(QRect(270, 430, 55, 16))
		self.cmdtime.setText("0")
		self.cmdtime.setObjectName("cmdtime")
		self.cmdelapsed = QLabel(self.GrouptestFrame)
		self.cmdelapsed.setGeometry(QRect(150, 430, 115, 16))
		self.cmdelapsed.setText("Cmd Time Elapsed:")
		self.cmdelapsed.setObjectName("cmdelapsed")
		self.cmdexpected1 = QLabel(self.GrouptestFrame)
		self.cmdexpected1.setGeometry(QRect(370, 430, 125, 16))
		self.cmdexpected1.setText("Cmd Time Expected:")
		self.cmdexpected1.setObjectName("cmdexpected1")
		self.cmdexpected2 = QLabel(self.GrouptestFrame)
		self.cmdexpected2.setGeometry(QRect(500, 430, 55, 16))
		self.cmdexpected2.setText("")
		self.GrouptestNextButton = QPushButton(self.GrouptestFrameBottom)
		self.GrouptestNextButton.setGeometry(QRect(620, 20, 93, 28))
		self.GrouptestNextButton.setObjectName("GrouptestNextButton")
		self.GrouptestNextButton.setText("Next")
		self.GrouptestNextButton.setCursor(QCursor(Qt.PointingHandCursor))
		self.GrouptestBackButton = QPushButton(self.GrouptestFrameBottom)
		self.GrouptestBackButton.setGeometry(QRect(40, 20, 93, 28))
		self.GrouptestBackButton.setObjectName("GrouptestBackButton")
		self.GrouptestBackButton.setText("Back")
		self.GrouptestBackButton.setCursor(QCursor(Qt.PointingHandCursor))
		self.GrouptestFrame.hide()
		self.GrouptestFrameBottom.hide()
		self.LogoSmallFrame.hide()
		self.GrouptestBackButton.clicked.connect(lambda: self.GrouptestBackPage())
		self.GrouptestNextButton.clicked.connect(lambda: self.GrouptestNextPage())

		#final frame
		self.finalresult = QTextEdit(self)
		self.finalresult.setGeometry(QRect(430, 140, 300, 250))
		self.finalresult.setObjectName("finalresult")
		self.finalresult.hide()
		self.finalresult.setEnabled(False)
		self.finalBackButton = QPushButton(self)
		self.finalBackButton.setGeometry(QRect(60, 480, 93, 28))
		self.finalBackButton.setObjectName("finalBackButton")
		self.finalBackButton.setText("Back")
		self.finalBackButton.setCursor(QCursor(Qt.PointingHandCursor))
		self.finalBackButton.hide()
		self.finalBackButton.clicked.connect(lambda: self.finalBackPage())
		self.finalresult.setStyleSheet(
		"QTextEdit::disabled"
		"{"
		"background-color:transparent;"
		"color:black;"
		"border:none"
		"}")
		self.finishButton = QPushButton(self)
		self.finishButton.setGeometry(QRect(640, 480, 93, 28))
		self.finishButton.setObjectName("finishButton")
		self.finishButton.setText("Finish")
		self.finishButton.setCursor(QCursor(Qt.PointingHandCursor))
		self.finishButton.clicked.connect(lambda: self.fin())
		self.finishButton.hide()
	#first frame functions

	def IntroNextPage(self):
		global check1
		if(check1==0):
			self.IntroFrame.hide()
			self.IntroFrameBottom.hide()
			self.NetworkFrame.show()
			self.NetworkFrameBottom.show()
			self.namelabel.hide()
			self.NameInput.hide()
			self.passwordlabel.hide()
			self.PasswordInput.hide()
			self.ViewPassword.hide()
			self.InputDetailsButton.hide()
			self.NetworkNextButton.setEnabled(False)
			self.ViewPassword.setChecked(False)
			check1=1
		else:
			self.IntroFrame.hide()
			self.IntroFrameBottom.hide()
			self.NetworkFrame.show()
			self.NetworkFrameBottom.show()

	#second frame functions

	def getnetwork(self, net):
		global network
		network=net
		self.m1 = QMessageBox()
		self.m1.setIcon(QMessageBox.Warning)
		self.m1.setText(network+" is the network you have selected")
		self.Okbutton = self.m1.addButton('OK', QMessageBox.YesRole)
		self.Okbutton.move(20,0)
		self.Cancelbutton = self.m1.addButton('Cancel', QMessageBox.NoRole)
		self.m1.setInformativeText("To go into monitor mode your internet connection will get cut off. This is standard procedure, no need to panic.")
		self.m1.buttonClicked.connect(self.monitorconfirm)
		self.m1.exec()

	def monitorconfirm(self, option):
		global network
		if(option.text()=="OK"):
			cmd="airmon-ng check kill && airmon-ng start "+network
			print(network)
			stream1 = os.popen(cmd)
			output1 = stream1.read()
			# self.m2 = QMessageBox()
			# self.m2.setText(output1)
			# self.m2.exec()
			network=network+"mon"
			self.namelabel.show()
			self.NameInput.show()
			self.passwordlabel.show()
			self.PasswordInput.show()
			self.ViewPassword.show()
			self.InputDetailsButton.show()
			self.ViewPassword.setChecked(False)

		else:
			self.namelabel.hide()
			self.NameInput.hide()
			self.passwordlabel.hide()
			self.PasswordInput.hide()
			self.ViewPassword.hide()
			self.InputDetailsButton.hide()
			self.NetworkNextButton.setEnabled(False)
			self.ViewPassword.setChecked(False)

	def passwordview(self):
		if(self.ViewPassword.checkState()==2):
			self.PasswordInput.setEchoMode(QLineEdit.Normal)
		else:
			self.PasswordInput.setEchoMode(QLineEdit.Password)

	def inputdetails(self):
		networkname=self.NameInput.text()
		networkpassword=self.PasswordInput.text()
		if(networkname=="" or networkpassword==""):
			self.m2 = QMessageBox()
			self.m2.setIcon(QMessageBox.Critical)
			self.m2.setText("Please fill in all the details first.")
			self.m2.exec()
			self.NetworkNextButton.setEnabled(False)
		else:
			with open('client.conf', "w") as myfile:
				myfile.write('''ctrl_interface=wpaspy_ctrl
				# WPA3/SAE: support both hunting-and-pecking loop and hash-to-element
				sae_pwe=2

				# WPA2 home network
				network={
					ssid="'''+str(networkname)+'''"
					psk="'''+str(networkpassword)+'''"

					pairwise=CCMP
					#group=CCMP

					# Some network cards don't properly support injection on non-20MHz
					# channels. In that case uncomment this line to disable 40 MHz.
					#disable_ht40=1

					# Might be useful in very noisy environments to disable high bitrates.
					#disable_ht=1
				}

				# WPA3 home network
				network={
					ssid="'''+str(networkname)+'''"
					psk="'''+str(networkpassword)+'''"

					ieee80211w=1
					key_mgmt=SAE
				}

				# Enterprise network
				network={
					ssid="'''+str(networkname)+'''"
					key_mgmt=WPA-EAP
					eap=PEAP
					anonymous_identity="not anonymous"
					identity="user"
					phase2="auth=MSCHAPV2"
					password="'''+str(networkpassword)+'''"

					pairwise=CCMP
					#group=CCMP
				}

				# EAP-PWD with dynamic WEP keys (for research purposes)
				network={
					ssid="'''+str(networkname)+'''"
					key_mgmt=IEEE8021X
					eap=PWD
					identity="user"
					password="'''+str(networkpassword)+'''"

					pairwise=CCMP
					#group=CCMP
				}

				''')
			self.NetworkNextButton.setEnabled(True)
			
	def NetworkBackPage(self):
		self.NetworkFrame.hide()
		self.NetworkFrameBottom.hide()
		self.IntroFrame.show()
		self.IntroFrameBottom.show()

	def NetworkNextPage(self):
		self.NetworkFrame.hide()
		self.NetworkFrameBottom.hide()
		self.LogoFrame.hide()
		global check2
		if(check2==0):
			self.GrouptestFrame.show()
			self.GrouptestFrameBottom.show()
			self.totalelapsed.hide()
			self.totaltime.hide()
			self.totalexpected1.hide()
			self.totalexpected2.hide()
			self.cmdelapsed.hide()
			self.cmdtime.hide()
			self.cmdexpected1.hide()
			self.cmdexpected2.hide()
			self.textEdit.hide()
			self.label.hide()
			self.progressBar.hide()
			self.viewmore.hide()
			self.GrouptestNextButton.setEnabled(False)
			self.LogoSmallFrame.show()
			check2=1
		else:
			self.GrouptestFrame.show()
			self.GrouptestFrameBottom.show()
			self.LogoSmallFrame.show()


	#third frame functions
	def details(self):
		if(self.textEdit.isHidden()):
			self.totalelapsed.show()
			self.totaltime.show()
			self.totalexpected1.show()
			self.totalexpected2.show()
			self.cmdelapsed.show()
			self.cmdtime.show()
			self.cmdexpected1.show()
			self.cmdexpected2.show()
			self.textEdit.show()
		else:
			self.totalelapsed.hide()
			self.totaltime.hide()
			self.totalexpected1.hide()
			self.totalexpected2.hide()
			self.cmdelapsed.hide()
			self.cmdtime.hide()
			self.cmdexpected1.hide()
			self.cmdexpected2.hide()
			self.textEdit.hide()

	def reportprogress(self, n):
		self.progressBar.setProperty("value",n)
		global timecmd
		timecmd = QTime(0,0,0)
		self.cmdtime.setText(timecmd.toString("hh:mm:ss"))

	def reportoutput(self, output):
		global passed, failed, unknown, resultlist, consolelogfile
		self.textEdit.append(output)
		consolelogfile=consolelogfile+output+"\n"
		result="TEST COMPLETED SUCCESSFULLY"
		if result in output:
			passed=passed+1
			resultlist.append("Passed")
		else:
			failed=failed+1
			resultlist.append("Failed")

	def reportprocess(self, process):
		global totalprocess
		self.label.setText(str(process)+"/"+str(totalprocess))

	def timestart(self):
		global timetotal, timecmd, complete
		if(complete==0):
			timetotal = timetotal.addSecs(1)
			self.totaltime.setText(timetotal.toString("hh:mm:ss"))
			timecmd = timecmd.addSecs(1)
			self.cmdtime.setText(timecmd.toString("hh:mm:ss"))
			
	def finishcheck(self):
		global complete,finaloutput,consolelogfile, resultfile, group
		complete = 1
		self.runbutton.setEnabled(True)
		self.GroupsDrop.setEnabled(True)
		self.label.setText("Complete")
		self.cmdexpected2.setText("00:00:00")
		finaloutput = self.textEdit.toPlainText()
		self.GrouptestNextButton.setEnabled(True)
		self.GrouptestBackButton.setEnabled(True)
		print("passed "+str(passed))
		print("failed "+str(failed))

		with open("Consolelogs/"+group+"-console.txt", "w") as myfile:
			myfile.write(consolelogfile)
		with open("Reports/"+group+"-report.txt", "w") as myfile:
			myfile.write(resultfile)

	def commandtime(self, t):
		self.cmdexpected2.setText(t)

	def generateresult(self, p):
		global resultlist,k, resultfile
		resultfile = resultfile + p + "  " + str(resultlist[k]) +"\n"
		k=k+1

	def runclicked(self):
		self.GrouptestNextButton.setEnabled(False)
		self.GrouptestBackButton.setEnabled(False)
		global timetotal, timecmd, complete, totalprocess, group, passed, failed, unknown, k, resultfile, consolelogfile, resultlist
		k=0
		passed=0
		failed=0
		unknown=0
		resultfile=group+"\n"
		consolelogfile=group+"\n"
		resultlist=[]
		group = self.GroupsDrop.currentText()
		resultfile=group+"\n"
		consolelogfile=group+"\n"
		if(group=="Group-1"):
			totalprocess=10
			self.totalexpected2.setText("00:01:09")
		if(group=="Group-2"):
			totalprocess=2
			self.totalexpected2.setText("00:00:09")
		if(group=="Group-3"):
			totalprocess=3
			self.totalexpected2.setText("00:00:09")
		if(group=="Group-4"):
			totalprocess=3
			self.totalexpected2.setText("00:00:09")
		if(group=="Group-5"):
			totalprocess=3
			self.totalexpected2.setText("00:00:09")
		self.progressBar.setMaximum(totalprocess)
		self.label.show()
		self.progressBar.show()
		self.viewmore.show()
		self.textEdit.setText("")
		self.progressBar.setProperty("value",0)
		complete=0
		timetotal = QTime(0, 0, 0)
		timecmd = QTime(0, 0, 0)
		self.timer = QTimer()
		self.timer.timeout.connect(self.timestart)
		self.timer.start(1000)
		self.thread = QThread()
		self.worker = Worker()
		self.worker.moveToThread(self.thread)
		self.thread.started.connect(self.worker.run)
		self.worker.finished.connect(self.thread.quit)
		self.worker.finished.connect(self.worker.deleteLater)
		self.thread.finished.connect(self.thread.deleteLater)
		self.worker.progress.connect(self.reportprogress)
		self.worker.output.connect(self.reportoutput)
		self.worker.processno.connect(self.reportprocess)
		self.worker.expectedtime.connect(self.commandtime)
		self.worker.process.connect(self.generateresult)
		self.thread.start()

		self.runbutton.setEnabled(False)
		self.GroupsDrop.setEnabled(False)
		self.thread.finished.connect(self.finishcheck)
		
	def GrouptestBackPage(self):
		self.GrouptestFrame.hide()
		self.GrouptestFrameBottom.hide()
		self.LogoSmallFrame.hide()
		self.NetworkFrame.show()
		self.NetworkFrameBottom.show()
		self.LogoFrame.show()

	def GrouptestNextPage(self):
		global passed,failed
		self.GrouptestFrame.hide()
		self.GrouptestFrameBottom.hide()
		self.LogoSmallFrame.hide()
		self.finalresult.setText("In this Group "+str((passed/(failed+passed)*100))+"% attacks were found to be successful.\n\nA report and console log has been generated in the report folder and consolelog folder respectively.")
		self.finalresult.show()
		self.LogoFrame.show()
		self.finalBackButton.show()
		self.finishButton.show()

	def finalBackPage(self):
		self.finalresult.hide()
		self.LogoFrame.hide()
		self.finalBackButton.hide()
		self.finishButton.hide()
		self.GrouptestFrame.show()
		self.GrouptestFrameBottom.show()
		self.LogoSmallFrame.show()

	def fin(self):
		self.close()
		
def run():
	app = QApplication(sys.argv)
	GUI = FirstPage()
	sys.exit(app.exec_())

run()