# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1071, 730)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.window_icon = QWidget(self.centralwidget)
        self.window_icon.setObjectName(u"window_icon")
        self.window_icon.setStyleSheet(u"QWidget {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #f2f2f2, stop:1 #d9d9d9);\n"
"    border: 2px solid #aaaaaa;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59e5e5, stop:1 #ffffff);\n"
"    border: 2px solid #888888;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #D9EFFF , stop:1 #b0b0b0);\n"
"    border: 2px solid #666666;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    background: #cccccc;\n"
"    height: 8px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 #ffffff, stop:1 #bbbbbb);\n"
"    border: 2px solid #888888;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin: -5px 0;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QDial {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y"
                        "2:1, stop:0 #f2f2f2, stop:1 #d9d9d9);\n"
"    border: 2px solid #aaaaaa;\n"
"    border-radius: 50px;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.window_icon)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.window_icon)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-color: #48cae4;\n"
"color: rgb(255, 255, 255);")
        self.label_6.setPixmap(QPixmap(u":/icon/icons/Settings-Sound--Streamline-Ultimate.png"))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.but_cam_1_icon = QPushButton(self.window_icon)
        self.but_cam_1_icon.setObjectName(u"but_cam_1_icon")
        icon = QIcon()
        icon.addFile(u":/icon/icons/Expand-Full--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_cam_1_icon.setIcon(icon)
        self.but_cam_1_icon.setCheckable(True)
        self.but_cam_1_icon.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.but_cam_1_icon)

        self.but_4_cam_icon = QPushButton(self.window_icon)
        self.but_4_cam_icon.setObjectName(u"but_4_cam_icon")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/Shrink-4--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_4_cam_icon.setIcon(icon1)
        self.but_4_cam_icon.setCheckable(True)
        self.but_4_cam_icon.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.but_4_cam_icon)

        self.but_NG_1_icon = QPushButton(self.window_icon)
        self.but_NG_1_icon.setObjectName(u"but_NG_1_icon")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/Paginate-Filter-1--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_NG_1_icon.setIcon(icon2)
        self.but_NG_1_icon.setCheckable(True)
        self.but_NG_1_icon.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.but_NG_1_icon)

        self.but_NG_4_icon = QPushButton(self.window_icon)
        self.but_NG_4_icon.setObjectName(u"but_NG_4_icon")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/Paginate-Filter-4--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_NG_4_icon.setIcon(icon3)
        self.but_NG_4_icon.setCheckable(True)
        self.but_NG_4_icon.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.but_NG_4_icon)

        self.but_output_icon = QPushButton(self.window_icon)
        self.but_output_icon.setObjectName(u"but_output_icon")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/Accounting-Calculator--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_output_icon.setIcon(icon4)
        self.but_output_icon.setCheckable(True)
        self.but_output_icon.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.but_output_icon)

        self.but_screenshot_icon = QPushButton(self.window_icon)
        self.but_screenshot_icon.setObjectName(u"but_screenshot_icon")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icons/Paginate-Filter-Camera--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_screenshot_icon.setIcon(icon5)
        self.but_screenshot_icon.setCheckable(True)
        self.but_screenshot_icon.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.but_screenshot_icon)

        self.but_information_icon = QPushButton(self.window_icon)
        self.but_information_icon.setObjectName(u"but_information_icon")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icons/Alert-Hexagon--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_information_icon.setIcon(icon6)
        self.but_information_icon.setCheckable(True)
        self.but_information_icon.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.but_information_icon)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 255, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.but_exit_icon = QPushButton(self.window_icon)
        self.but_exit_icon.setObjectName(u"but_exit_icon")
        icon7 = QIcon()
        icon7.addFile(u":/icon/icons/Logout-2--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_exit_icon.setIcon(icon7)
        self.but_exit_icon.setCheckable(True)
        self.but_exit_icon.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.but_exit_icon)


        self.gridLayout.addWidget(self.window_icon, 0, 0, 1, 1)

        self.window_expand = QWidget(self.centralwidget)
        self.window_expand.setObjectName(u"window_expand")
        self.window_expand.setStyleSheet(u"QWidget {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #f2f2f2, stop:1 #d9d9d9);\n"
"    border: 2px solid #aaaaaa;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59e5e5, stop:1 #ffffff);\n"
"    border: 2px solid #888888;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #D9EFFF , stop:1 #b0b0b0);\n"
"    border: 2px solid #666666;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    background: #cccccc;\n"
"    height: 8px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 #ffffff, stop:1 #bbbbbb);\n"
"    border: 2px solid #888888;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin: -5px 0;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QDial {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y"
                        "2:1, stop:0 #f2f2f2, stop:1 #d9d9d9);\n"
"    border: 2px solid #aaaaaa;\n"
"    border-radius: 50px;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.window_expand)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_18 = QPushButton(self.window_expand)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setEnabled(False)
        self.pushButton_18.setStyleSheet(u"background-color: #48cae4;\n"
"color: rgb(255, 255, 255);")
        icon8 = QIcon()
        icon8.addFile(u":/icon/icons/Settings-Toggle-Vertical--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_18.setIcon(icon8)

        self.verticalLayout_5.addWidget(self.pushButton_18)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.but_cam_1_expand = QPushButton(self.window_expand)
        self.but_cam_1_expand.setObjectName(u"but_cam_1_expand")
        self.but_cam_1_expand.setIcon(icon)
        self.but_cam_1_expand.setCheckable(True)
        self.but_cam_1_expand.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.but_cam_1_expand)

        self.but_4_cam_expand = QPushButton(self.window_expand)
        self.but_4_cam_expand.setObjectName(u"but_4_cam_expand")
        self.but_4_cam_expand.setIcon(icon1)
        self.but_4_cam_expand.setCheckable(True)
        self.but_4_cam_expand.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.but_4_cam_expand)

        self.but_NG_1_expand = QPushButton(self.window_expand)
        self.but_NG_1_expand.setObjectName(u"but_NG_1_expand")
        self.but_NG_1_expand.setIcon(icon2)
        self.but_NG_1_expand.setCheckable(True)
        self.but_NG_1_expand.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.but_NG_1_expand)

        self.but_NG_4_expand = QPushButton(self.window_expand)
        self.but_NG_4_expand.setObjectName(u"but_NG_4_expand")
        self.but_NG_4_expand.setIcon(icon3)
        self.but_NG_4_expand.setCheckable(True)
        self.but_NG_4_expand.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.but_NG_4_expand)

        self.but_output_expand = QPushButton(self.window_expand)
        self.but_output_expand.setObjectName(u"but_output_expand")
        self.but_output_expand.setIcon(icon4)
        self.but_output_expand.setCheckable(True)
        self.but_output_expand.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.but_output_expand)

        self.but_screenshot_expand = QPushButton(self.window_expand)
        self.but_screenshot_expand.setObjectName(u"but_screenshot_expand")
        self.but_screenshot_expand.setIcon(icon5)
        self.but_screenshot_expand.setCheckable(True)
        self.but_screenshot_expand.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.but_screenshot_expand)

        self.but_information_expand = QPushButton(self.window_expand)
        self.but_information_expand.setObjectName(u"but_information_expand")
        self.but_information_expand.setIcon(icon6)
        self.but_information_expand.setCheckable(True)
        self.but_information_expand.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.but_information_expand)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 253, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.but_exit_expand = QPushButton(self.window_expand)
        self.but_exit_expand.setObjectName(u"but_exit_expand")
        self.but_exit_expand.setIcon(icon7)

        self.verticalLayout_5.addWidget(self.but_exit_expand)


        self.gridLayout.addWidget(self.window_expand, 0, 1, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setStyleSheet(u"QWidget {\n"
"	background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #59e5e5;\n"
"	border-radius: 10px;\n"
"	border: 2px solid #0c0c0c;\n"
"}\n"
"\n"
"QPushButton:hover  {\n"
"	background-color:#DDDDDD ;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #4b4b4b;\n"
"	background-color: rgb(75, 75, 75);\n"
"    height: 8px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #E0E0E0, stop:1 #A0A0A0);\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #4A90E2;\n"
"    border: 2px solid black;\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    margin: -5px 0;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #a6c8ff;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #F5F5F5  ;\n"
"    border-radius: 2px;\n"
"	border: 1px solid #4b4b4b;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #5c5c5c;\n"
"    background: #2e2e2e;\n"
"    width: 25px;\n"
""
                        "    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #59e5e5; /* M\u00e0u c\u1ee7a thanh k\u00e9o */\n"
"    min-height: 50px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #0099cc; /* M\u00e0u khi hover v\u00e0o */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"    border: none;\n"
"}")
        self.window_1 = QWidget()
        self.window_1.setObjectName(u"window_1")
        self.gridLayout_10 = QGridLayout(self.window_1)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(-1, -1, 50, -1)
        self.but_tool_cam1 = QPushButton(self.window_1)
        self.but_tool_cam1.setObjectName(u"but_tool_cam1")
        self.but_tool_cam1.setMinimumSize(QSize(0, 30))
        icon9 = QIcon()
        icon9.addFile(u":/icon/icons/Navigation-Menu-1--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_tool_cam1.setIcon(icon9)
        self.but_tool_cam1.setCheckable(False)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.but_tool_cam1)

        self.label_8 = QLabel(self.window_1)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.label_8)


        self.gridLayout_10.addLayout(self.formLayout_3, 0, 0, 1, 1)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)

        self.label_ok_cam1 = QPushButton(self.window_1)
        self.label_ok_cam1.setObjectName(u"label_ok_cam1")
        self.label_ok_cam1.setEnabled(False)
        self.label_ok_cam1.setMinimumSize(QSize(0, 30))
        self.label_ok_cam1.setStyleSheet(u"background-color: #c6c6c6;")
        icon10 = QIcon()
        icon10.addFile(u":/icon/icons/Like-1--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.label_ok_cam1.setIcon(icon10)

        self.verticalLayout_6.addWidget(self.label_ok_cam1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)

        self.label_ng_cam1 = QPushButton(self.window_1)
        self.label_ng_cam1.setObjectName(u"label_ng_cam1")
        self.label_ng_cam1.setEnabled(False)
        self.label_ng_cam1.setMinimumSize(QSize(0, 30))
        self.label_ng_cam1.setStyleSheet(u"background-color: #c6c6c6;")
        icon11 = QIcon()
        icon11.addFile(u":/icon/icons/Thumb-Down-Dislike--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.label_ng_cam1.setIcon(icon11)

        self.verticalLayout_6.addWidget(self.label_ng_cam1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_7)


        self.formLayout_4.setLayout(0, QFormLayout.LabelRole, self.verticalLayout_6)

        self.widget = QWidget(self.window_1)
        self.widget.setObjectName(u"widget")
        self.gridLayout_7 = QGridLayout(self.widget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(9)
        self.gridLayout_7.setVerticalSpacing(0)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(False)
        self.groupBox.setFont(font1)
        self.groupBox.setStyleSheet(u"")
        self.groupBox.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.show_pic_cam_cam1 = QLabel(self.groupBox)
        self.show_pic_cam_cam1.setObjectName(u"show_pic_cam_cam1")
        self.show_pic_cam_cam1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")
        self.show_pic_cam_cam1.setScaledContents(True)

        self.gridLayout_3.addWidget(self.show_pic_cam_cam1, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setFont(font1)
        self.groupBox_2.setStyleSheet(u"")
        self.groupBox_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setCheckable(False)
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QStackedWidget(self.groupBox_2)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.real = QWidget()
        self.real.setObjectName(u"real")
        self.gridLayout_5 = QGridLayout(self.real)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.show_pic_real_cam1 = QLabel(self.real)
        self.show_pic_real_cam1.setObjectName(u"show_pic_real_cam1")
        self.show_pic_real_cam1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.gridLayout_5.addWidget(self.show_pic_real_cam1, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.real)
        self.thread = QWidget()
        self.thread.setObjectName(u"thread")
        self.gridLayout_6 = QGridLayout(self.thread)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.show_pic_thread_cam1 = QLabel(self.thread)
        self.show_pic_thread_cam1.setObjectName(u"show_pic_thread_cam1")
        self.show_pic_thread_cam1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")
        self.show_pic_thread_cam1.setScaledContents(True)

        self.gridLayout_6.addWidget(self.show_pic_thread_cam1, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.thread)
        self.vitual = QWidget()
        self.vitual.setObjectName(u"vitual")
        self.gridLayout_20 = QGridLayout(self.vitual)
        self.gridLayout_20.setSpacing(0)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.show_pic_virtual_cam1 = QLabel(self.vitual)
        self.show_pic_virtual_cam1.setObjectName(u"show_pic_virtual_cam1")
        self.show_pic_virtual_cam1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.gridLayout_20.addWidget(self.show_pic_virtual_cam1, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.vitual)

        self.gridLayout_4.addWidget(self.stackedWidget_2, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_2, 0, 1, 1, 1)


        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.widget)


        self.gridLayout_10.addLayout(self.formLayout_4, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.window_1)
        self.groupBox_3.setObjectName(u"groupBox_3")
        font2 = QFont()
        font2.setPointSize(8)
        self.groupBox_3.setFont(font2)
        self.gridLayout_8 = QGridLayout(self.groupBox_3)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(13, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.but_take_picture_cam1 = QPushButton(self.groupBox_3)
        self.but_take_picture_cam1.setObjectName(u"but_take_picture_cam1")
        self.but_take_picture_cam1.setMinimumSize(QSize(0, 50))
        icon12 = QIcon()
        icon12.addFile(u":/icon/icons/Cursor-Select-Frame--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_take_picture_cam1.setIcon(icon12)

        self.horizontalLayout_2.addWidget(self.but_take_picture_cam1)

        self.but_saving_cam1 = QPushButton(self.groupBox_3)
        self.but_saving_cam1.setObjectName(u"but_saving_cam1")
        self.but_saving_cam1.setMinimumSize(QSize(0, 50))
        icon13 = QIcon()
        icon13.addFile(u":/icon/icons/Time-Clock-File-Refresh--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_saving_cam1.setIcon(icon13)

        self.horizontalLayout_2.addWidget(self.but_saving_cam1)

        self.but_undo_cam1 = QPushButton(self.groupBox_3)
        self.but_undo_cam1.setObjectName(u"but_undo_cam1")
        self.but_undo_cam1.setMinimumSize(QSize(0, 50))
        icon14 = QIcon()
        icon14.addFile(u":/icon/icons/Navigation-Right--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_undo_cam1.setIcon(icon14)

        self.horizontalLayout_2.addWidget(self.but_undo_cam1)

        self.but_take_sample_cam1 = QPushButton(self.groupBox_3)
        self.but_take_sample_cam1.setObjectName(u"but_take_sample_cam1")
        self.but_take_sample_cam1.setMinimumSize(QSize(0, 50))
        icon15 = QIcon()
        icon15.addFile(u":/icon/icons/Append-Data-To-Spreadsheet--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_take_sample_cam1.setIcon(icon15)

        self.horizontalLayout_2.addWidget(self.but_take_sample_cam1)

        self.but_calib_cam1 = QPushButton(self.groupBox_3)
        self.but_calib_cam1.setObjectName(u"but_calib_cam1")
        self.but_calib_cam1.setMinimumSize(QSize(0, 50))
        icon16 = QIcon()
        icon16.addFile(u":/icon/icons/Cell-Select-1--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_calib_cam1.setIcon(icon16)

        self.horizontalLayout_2.addWidget(self.but_calib_cam1)

        self.but_result_cam1 = QPushButton(self.groupBox_3)
        self.but_result_cam1.setObjectName(u"but_result_cam1")
        self.but_result_cam1.setMinimumSize(QSize(0, 50))
        icon17 = QIcon()
        icon17.addFile(u":/icon/icons/Navigation-Arrows-Right-1--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_result_cam1.setIcon(icon17)

        self.horizontalLayout_2.addWidget(self.but_result_cam1)

        self.horizontalSpacer_5 = QSpacerItem(13, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.gridLayout_8.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_3, 2, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.window_1)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font2)
        self.gridLayout_12 = QGridLayout(self.groupBox_4)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.groupBox_4)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_9 = QGridLayout(self.widget_4)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, -1, -1, -1)
        self.show_h_high_cam1 = QLabel(self.widget_4)
        self.show_h_high_cam1.setObjectName(u"show_h_high_cam1")

        self.verticalLayout_7.addWidget(self.show_h_high_cam1)

        self.show_s_high_cam1 = QLabel(self.widget_4)
        self.show_s_high_cam1.setObjectName(u"show_s_high_cam1")

        self.verticalLayout_7.addWidget(self.show_s_high_cam1)

        self.show_v_high_cam1 = QLabel(self.widget_4)
        self.show_v_high_cam1.setObjectName(u"show_v_high_cam1")

        self.verticalLayout_7.addWidget(self.show_v_high_cam1)

        self.show_bright_cam1 = QLabel(self.widget_4)
        self.show_bright_cam1.setObjectName(u"show_bright_cam1")

        self.verticalLayout_7.addWidget(self.show_bright_cam1)

        self.show_ratio_cam1 = QLabel(self.widget_4)
        self.show_ratio_cam1.setObjectName(u"show_ratio_cam1")

        self.verticalLayout_7.addWidget(self.show_ratio_cam1)


        self.gridLayout_9.addLayout(self.verticalLayout_7, 0, 0, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, 10, -1)
        self.slider_h_high_cam1 = QSlider(self.widget_4)
        self.slider_h_high_cam1.setObjectName(u"slider_h_high_cam1")
        self.slider_h_high_cam1.setMaximum(179)
        self.slider_h_high_cam1.setPageStep(1)
        self.slider_h_high_cam1.setOrientation(Qt.Horizontal)

        self.verticalLayout_8.addWidget(self.slider_h_high_cam1)

        self.slider_s_high_cam1 = QSlider(self.widget_4)
        self.slider_s_high_cam1.setObjectName(u"slider_s_high_cam1")
        self.slider_s_high_cam1.setMaximum(255)
        self.slider_s_high_cam1.setPageStep(1)
        self.slider_s_high_cam1.setOrientation(Qt.Horizontal)

        self.verticalLayout_8.addWidget(self.slider_s_high_cam1)

        self.slider_v_high_cam1 = QSlider(self.widget_4)
        self.slider_v_high_cam1.setObjectName(u"slider_v_high_cam1")
        self.slider_v_high_cam1.setMaximum(255)
        self.slider_v_high_cam1.setPageStep(1)
        self.slider_v_high_cam1.setOrientation(Qt.Horizontal)

        self.verticalLayout_8.addWidget(self.slider_v_high_cam1)

        self.slider_bright_cam1 = QSlider(self.widget_4)
        self.slider_bright_cam1.setObjectName(u"slider_bright_cam1")
        self.slider_bright_cam1.setMinimum(-255)
        self.slider_bright_cam1.setMaximum(255)
        self.slider_bright_cam1.setOrientation(Qt.Horizontal)

        self.verticalLayout_8.addWidget(self.slider_bright_cam1)

        self.slider_ratio_cam1 = QSlider(self.widget_4)
        self.slider_ratio_cam1.setObjectName(u"slider_ratio_cam1")
        self.slider_ratio_cam1.setOrientation(Qt.Horizontal)

        self.verticalLayout_8.addWidget(self.slider_ratio_cam1)


        self.gridLayout_9.addLayout(self.verticalLayout_8, 0, 1, 1, 1)


        self.gridLayout_12.addWidget(self.widget_4, 0, 0, 1, 1)

        self.widget_5 = QWidget(self.groupBox_4)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_11 = QGridLayout(self.widget_5)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_9.setContentsMargins(10, -1, -1, -1)
        self.show_h_low_cam1 = QLabel(self.widget_5)
        self.show_h_low_cam1.setObjectName(u"show_h_low_cam1")

        self.verticalLayout_9.addWidget(self.show_h_low_cam1)

        self.show_s_low_cam1 = QLabel(self.widget_5)
        self.show_s_low_cam1.setObjectName(u"show_s_low_cam1")

        self.verticalLayout_9.addWidget(self.show_s_low_cam1)

        self.show_v_low_cam1 = QLabel(self.widget_5)
        self.show_v_low_cam1.setObjectName(u"show_v_low_cam1")

        self.verticalLayout_9.addWidget(self.show_v_low_cam1)

        self.show_r_circle_cam1 = QLabel(self.widget_5)
        self.show_r_circle_cam1.setObjectName(u"show_r_circle_cam1")

        self.verticalLayout_9.addWidget(self.show_r_circle_cam1)

        self.show_contrast_cam1 = QLabel(self.widget_5)
        self.show_contrast_cam1.setObjectName(u"show_contrast_cam1")

        self.verticalLayout_9.addWidget(self.show_contrast_cam1)

        self.show_value_now_cam1 = QLabel(self.widget_5)
        self.show_value_now_cam1.setObjectName(u"show_value_now_cam1")

        self.verticalLayout_9.addWidget(self.show_value_now_cam1)


        self.gridLayout_11.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, -1, 5, -1)
        self.slider_h_low_cam1 = QSlider(self.widget_5)
        self.slider_h_low_cam1.setObjectName(u"slider_h_low_cam1")
        self.slider_h_low_cam1.setMaximum(179)
        self.slider_h_low_cam1.setPageStep(1)
        self.slider_h_low_cam1.setOrientation(Qt.Horizontal)

        self.verticalLayout_10.addWidget(self.slider_h_low_cam1)

        self.slider_s_low_cam1 = QSlider(self.widget_5)
        self.slider_s_low_cam1.setObjectName(u"slider_s_low_cam1")
        self.slider_s_low_cam1.setMaximum(255)
        self.slider_s_low_cam1.setPageStep(1)
        self.slider_s_low_cam1.setOrientation(Qt.Horizontal)

        self.verticalLayout_10.addWidget(self.slider_s_low_cam1)

        self.slider_v_low_cam1 = QSlider(self.widget_5)
        self.slider_v_low_cam1.setObjectName(u"slider_v_low_cam1")
        self.slider_v_low_cam1.setMaximum(255)
        self.slider_v_low_cam1.setPageStep(1)
        self.slider_v_low_cam1.setOrientation(Qt.Horizontal)

        self.verticalLayout_10.addWidget(self.slider_v_low_cam1)

        self.slider_r_circle_cam1 = QSlider(self.widget_5)
        self.slider_r_circle_cam1.setObjectName(u"slider_r_circle_cam1")
        self.slider_r_circle_cam1.setMaximum(2000)
        self.slider_r_circle_cam1.setPageStep(1)
        self.slider_r_circle_cam1.setOrientation(Qt.Horizontal)

        self.verticalLayout_10.addWidget(self.slider_r_circle_cam1)

        self.show_value_contrast_cam1 = QLineEdit(self.widget_5)
        self.show_value_contrast_cam1.setObjectName(u"show_value_contrast_cam1")

        self.verticalLayout_10.addWidget(self.show_value_contrast_cam1)

        self.verticalSpacer_15 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_15)


        self.gridLayout_11.addLayout(self.verticalLayout_10, 0, 1, 1, 1)


        self.gridLayout_12.addWidget(self.widget_5, 0, 1, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_4, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.window_1)
        self.window_2 = QWidget()
        self.window_2.setObjectName(u"window_2")
        self.gridLayout_14 = QGridLayout(self.window_2)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setContentsMargins(-1, -1, 70, -1)
        self.but_tool_calib = QPushButton(self.window_2)
        self.but_tool_calib.setObjectName(u"but_tool_calib")
        self.but_tool_calib.setMinimumSize(QSize(0, 30))
        self.but_tool_calib.setIcon(icon9)
        self.but_tool_calib.setCheckable(False)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.but_tool_calib)

        self.label_9 = QLabel(self.window_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.label_9)


        self.gridLayout_14.addLayout(self.formLayout_5, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.window_2)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_13 = QGridLayout(self.widget_2)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.show_pic_calib_calib = QLabel(self.widget_2)
        self.show_pic_calib_calib.setObjectName(u"show_pic_calib_calib")
        sizePolicy.setHeightForWidth(self.show_pic_calib_calib.sizePolicy().hasHeightForWidth())
        self.show_pic_calib_calib.setSizePolicy(sizePolicy)
        self.show_pic_calib_calib.setMinimumSize(QSize(0, 0))
        self.show_pic_calib_calib.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")
        self.show_pic_calib_calib.setScaledContents(True)

        self.gridLayout_13.addWidget(self.show_pic_calib_calib, 1, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(200, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_6, 1, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_13.addItem(self.verticalSpacer_8, 0, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(200, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_8, 1, 2, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_13.addItem(self.verticalSpacer_9, 2, 1, 1, 1)


        self.gridLayout_14.addWidget(self.widget_2, 1, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.window_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setFont(font2)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_3.setSpacing(100)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.but_take_calib = QPushButton(self.groupBox_5)
        self.but_take_calib.setObjectName(u"but_take_calib")
        self.but_take_calib.setMinimumSize(QSize(0, 40))
        self.but_take_calib.setIcon(icon5)

        self.horizontalLayout_3.addWidget(self.but_take_calib)

        self.but_calib_calib = QPushButton(self.groupBox_5)
        self.but_calib_calib.setObjectName(u"but_calib_calib")
        self.but_calib_calib.setMinimumSize(QSize(0, 40))
        icon18 = QIcon()
        icon18.addFile(u":/icon/icons/Graph-Stats-Circle--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_calib_calib.setIcon(icon18)

        self.horizontalLayout_3.addWidget(self.but_calib_calib)

        self.but_clear_calib = QPushButton(self.groupBox_5)
        self.but_clear_calib.setObjectName(u"but_clear_calib")
        self.but_clear_calib.setMinimumSize(QSize(0, 40))
        icon19 = QIcon()
        icon19.addFile(u":/icon/icons/Bin-1--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_clear_calib.setIcon(icon19)

        self.horizontalLayout_3.addWidget(self.but_clear_calib)

        self.but_back_home_calib = QPushButton(self.groupBox_5)
        self.but_back_home_calib.setObjectName(u"but_back_home_calib")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.but_back_home_calib.sizePolicy().hasHeightForWidth())
        self.but_back_home_calib.setSizePolicy(sizePolicy2)
        self.but_back_home_calib.setMinimumSize(QSize(0, 40))
        icon20 = QIcon()
        icon20.addFile(u":/icon/icons/Move-Left--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_back_home_calib.setIcon(icon20)

        self.horizontalLayout_3.addWidget(self.but_back_home_calib)


        self.gridLayout_14.addWidget(self.groupBox_5, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.window_2)
        self.window_3 = QWidget()
        self.window_3.setObjectName(u"window_3")
        self.gridLayout_18 = QGridLayout(self.window_3)
        self.gridLayout_18.setSpacing(0)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(-1, 0, 0, 0)
        self.widget_3 = QWidget(self.window_3)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.gridLayout_17 = QGridLayout(self.widget_3)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_9, 0, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.widget_3)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setFont(font2)
        self.groupBox_6.setAlignment(Qt.AlignCenter)
        self.gridLayout_15 = QGridLayout(self.groupBox_6)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, -1, 0, 0)
        self.show_pic_real_sample = QLabel(self.groupBox_6)
        self.show_pic_real_sample.setObjectName(u"show_pic_real_sample")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.show_pic_real_sample.sizePolicy().hasHeightForWidth())
        self.show_pic_real_sample.setSizePolicy(sizePolicy3)
        self.show_pic_real_sample.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.gridLayout_15.addWidget(self.show_pic_real_sample, 0, 0, 1, 1)


        self.gridLayout_17.addWidget(self.groupBox_6, 0, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_10, 0, 2, 1, 1)

        self.groupBox_7 = QGroupBox(self.widget_3)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setFont(font2)
        self.groupBox_7.setAlignment(Qt.AlignCenter)
        self.gridLayout_16 = QGridLayout(self.groupBox_7)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, -1, 0, 0)
        self.show_pic_sample_sample = QLabel(self.groupBox_7)
        self.show_pic_sample_sample.setObjectName(u"show_pic_sample_sample")
        sizePolicy3.setHeightForWidth(self.show_pic_sample_sample.sizePolicy().hasHeightForWidth())
        self.show_pic_sample_sample.setSizePolicy(sizePolicy3)
        self.show_pic_sample_sample.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.gridLayout_16.addWidget(self.show_pic_sample_sample, 0, 0, 1, 1)


        self.gridLayout_17.addWidget(self.groupBox_7, 0, 3, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_11, 0, 4, 1, 1)


        self.gridLayout_18.addWidget(self.widget_3, 1, 0, 1, 1)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setHorizontalSpacing(0)
        self.formLayout_6.setVerticalSpacing(0)
        self.formLayout_6.setContentsMargins(-1, -1, 80, -1)
        self.but_tool_sample = QPushButton(self.window_3)
        self.but_tool_sample.setObjectName(u"but_tool_sample")
        self.but_tool_sample.setMinimumSize(QSize(0, 30))
        self.but_tool_sample.setIcon(icon9)
        self.but_tool_sample.setCheckable(False)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.but_tool_sample)

        self.label_10 = QLabel(self.window_3)
        self.label_10.setObjectName(u"label_10")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy4)
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.label_10)


        self.gridLayout_18.addLayout(self.formLayout_6, 0, 0, 1, 1)

        self.groupBox_8 = QGroupBox(self.window_3)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_4.setSpacing(100)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.but_take_sample = QPushButton(self.groupBox_8)
        self.but_take_sample.setObjectName(u"but_take_sample")
        self.but_take_sample.setMinimumSize(QSize(0, 40))
        self.but_take_sample.setIcon(icon5)

        self.horizontalLayout_4.addWidget(self.but_take_sample)

        self.but_sample_sample = QPushButton(self.groupBox_8)
        self.but_sample_sample.setObjectName(u"but_sample_sample")
        self.but_sample_sample.setMinimumSize(QSize(0, 40))
        icon21 = QIcon()
        icon21.addFile(u":/icon/icons/Check--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_sample_sample.setIcon(icon21)

        self.horizontalLayout_4.addWidget(self.but_sample_sample)

        self.but_clear_sample = QPushButton(self.groupBox_8)
        self.but_clear_sample.setObjectName(u"but_clear_sample")
        self.but_clear_sample.setMinimumSize(QSize(0, 40))
        self.but_clear_sample.setIcon(icon19)

        self.horizontalLayout_4.addWidget(self.but_clear_sample)

        self.but_back_home_sample = QPushButton(self.groupBox_8)
        self.but_back_home_sample.setObjectName(u"but_back_home_sample")
        self.but_back_home_sample.setMinimumSize(QSize(0, 40))
        self.but_back_home_sample.setIcon(icon20)

        self.horizontalLayout_4.addWidget(self.but_back_home_sample)


        self.gridLayout_18.addWidget(self.groupBox_8, 3, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.verticalSpacer_10, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.window_3)
        self.window_4 = QWidget()
        self.window_4.setObjectName(u"window_4")
        self.gridLayout_32 = QGridLayout(self.window_4)
        self.gridLayout_32.setSpacing(0)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setHorizontalSpacing(0)
        self.formLayout_7.setVerticalSpacing(0)
        self.formLayout_7.setContentsMargins(-1, -1, 80, -1)
        self.but_tool_4cam = QPushButton(self.window_4)
        self.but_tool_4cam.setObjectName(u"but_tool_4cam")
        self.but_tool_4cam.setMinimumSize(QSize(0, 30))
        self.but_tool_4cam.setIcon(icon9)
        self.but_tool_4cam.setCheckable(False)

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.but_tool_4cam)

        self.label_11 = QLabel(self.window_4)
        self.label_11.setObjectName(u"label_11")
        sizePolicy4.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy4)
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.label_11)


        self.gridLayout_32.addLayout(self.formLayout_7, 0, 0, 1, 1)

        self.widget_6 = QWidget(self.window_4)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_26 = QGridLayout(self.widget_6)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setHorizontalSpacing(5)
        self.gridLayout_26.setVerticalSpacing(0)
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.groupBox_11 = QGroupBox(self.widget_6)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setFont(font2)
        self.groupBox_11.setAlignment(Qt.AlignCenter)
        self.gridLayout_24 = QGridLayout(self.groupBox_11)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, -1, 0, 0)
        self.space_screen2_4cam = QStackedWidget(self.groupBox_11)
        self.space_screen2_4cam.setObjectName(u"space_screen2_4cam")
        self.space_real_2_4cam = QWidget()
        self.space_real_2_4cam.setObjectName(u"space_real_2_4cam")
        self.gridLayout_28 = QGridLayout(self.space_real_2_4cam)
        self.gridLayout_28.setSpacing(0)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.show_pic_real_2_4cam = QLabel(self.space_real_2_4cam)
        self.show_pic_real_2_4cam.setObjectName(u"show_pic_real_2_4cam")
        sizePolicy.setHeightForWidth(self.show_pic_real_2_4cam.sizePolicy().hasHeightForWidth())
        self.show_pic_real_2_4cam.setSizePolicy(sizePolicy)
        self.show_pic_real_2_4cam.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.gridLayout_28.addWidget(self.show_pic_real_2_4cam, 0, 0, 1, 1)

        self.space_screen2_4cam.addWidget(self.space_real_2_4cam)
        self.space_result_2_4cam = QWidget()
        self.space_result_2_4cam.setObjectName(u"space_result_2_4cam")
        self.gridLayout_35 = QGridLayout(self.space_result_2_4cam)
        self.gridLayout_35.setSpacing(0)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setContentsMargins(0, 0, 0, 0)
        self.show_pic_result_2_4cam = QLabel(self.space_result_2_4cam)
        self.show_pic_result_2_4cam.setObjectName(u"show_pic_result_2_4cam")
        sizePolicy.setHeightForWidth(self.show_pic_result_2_4cam.sizePolicy().hasHeightForWidth())
        self.show_pic_result_2_4cam.setSizePolicy(sizePolicy)
        self.show_pic_result_2_4cam.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.gridLayout_35.addWidget(self.show_pic_result_2_4cam, 0, 0, 1, 1)

        self.space_screen2_4cam.addWidget(self.space_result_2_4cam)

        self.gridLayout_24.addWidget(self.space_screen2_4cam, 0, 1, 1, 1)


        self.gridLayout_26.addWidget(self.groupBox_11, 2, 0, 1, 2)

        self.groupBox_10 = QGroupBox(self.widget_6)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setFont(font2)
        self.groupBox_10.setAlignment(Qt.AlignCenter)
        self.gridLayout_23 = QGridLayout(self.groupBox_10)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, -1, 0, 0)
        self.space_screen3_4cam = QStackedWidget(self.groupBox_10)
        self.space_screen3_4cam.setObjectName(u"space_screen3_4cam")
        self.space_real_3_4cam = QWidget()
        self.space_real_3_4cam.setObjectName(u"space_real_3_4cam")
        self.gridLayout_31 = QGridLayout(self.space_real_3_4cam)
        self.gridLayout_31.setSpacing(0)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.show_pic_real_3_4cam = QLabel(self.space_real_3_4cam)
        self.show_pic_real_3_4cam.setObjectName(u"show_pic_real_3_4cam")
        sizePolicy.setHeightForWidth(self.show_pic_real_3_4cam.sizePolicy().hasHeightForWidth())
        self.show_pic_real_3_4cam.setSizePolicy(sizePolicy)
        self.show_pic_real_3_4cam.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.gridLayout_31.addWidget(self.show_pic_real_3_4cam, 0, 0, 1, 1)

        self.space_screen3_4cam.addWidget(self.space_real_3_4cam)
        self.space_result_3_4cam = QWidget()
        self.space_result_3_4cam.setObjectName(u"space_result_3_4cam")
        self.gridLayout_34 = QGridLayout(self.space_result_3_4cam)
        self.gridLayout_34.setSpacing(0)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setContentsMargins(0, 0, 0, 0)
        self.show_pic_result_3_4cam = QLabel(self.space_result_3_4cam)
        self.show_pic_result_3_4cam.setObjectName(u"show_pic_result_3_4cam")
        sizePolicy.setHeightForWidth(self.show_pic_result_3_4cam.sizePolicy().hasHeightForWidth())
        self.show_pic_result_3_4cam.setSizePolicy(sizePolicy)
        self.show_pic_result_3_4cam.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.gridLayout_34.addWidget(self.show_pic_result_3_4cam, 0, 0, 1, 1)

        self.space_screen3_4cam.addWidget(self.space_result_3_4cam)

        self.gridLayout_23.addWidget(self.space_screen3_4cam, 0, 0, 1, 1)


        self.gridLayout_26.addWidget(self.groupBox_10, 0, 2, 1, 2)

        self.groupBox_12 = QGroupBox(self.widget_6)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setFont(font2)
        self.groupBox_12.setAlignment(Qt.AlignCenter)
        self.gridLayout_25 = QGridLayout(self.groupBox_12)
        self.gridLayout_25.setSpacing(0)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(0, -1, 0, 0)
        self.space_screen4_4cam = QStackedWidget(self.groupBox_12)
        self.space_screen4_4cam.setObjectName(u"space_screen4_4cam")
        self.space_real_4_4cam = QWidget()
        self.space_real_4_4cam.setObjectName(u"space_real_4_4cam")
        self.gridLayout_29 = QGridLayout(self.space_real_4_4cam)
        self.gridLayout_29.setSpacing(0)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.show_pic_real_4_4cam = QLabel(self.space_real_4_4cam)
        self.show_pic_real_4_4cam.setObjectName(u"show_pic_real_4_4cam")
        sizePolicy.setHeightForWidth(self.show_pic_real_4_4cam.sizePolicy().hasHeightForWidth())
        self.show_pic_real_4_4cam.setSizePolicy(sizePolicy)
        self.show_pic_real_4_4cam.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.gridLayout_29.addWidget(self.show_pic_real_4_4cam, 0, 0, 1, 1)

        self.space_screen4_4cam.addWidget(self.space_real_4_4cam)
        self.space_result_4_4cam = QWidget()
        self.space_result_4_4cam.setObjectName(u"space_result_4_4cam")
        self.gridLayout_36 = QGridLayout(self.space_result_4_4cam)
        self.gridLayout_36.setSpacing(0)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_36.setContentsMargins(0, 0, 0, 0)
        self.show_pic_result_4_4cam = QLabel(self.space_result_4_4cam)
        self.show_pic_result_4_4cam.setObjectName(u"show_pic_result_4_4cam")
        sizePolicy.setHeightForWidth(self.show_pic_result_4_4cam.sizePolicy().hasHeightForWidth())
        self.show_pic_result_4_4cam.setSizePolicy(sizePolicy)
        self.show_pic_result_4_4cam.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.gridLayout_36.addWidget(self.show_pic_result_4_4cam, 0, 0, 1, 1)

        self.space_screen4_4cam.addWidget(self.space_result_4_4cam)

        self.gridLayout_25.addWidget(self.space_screen4_4cam, 0, 0, 1, 1)


        self.gridLayout_26.addWidget(self.groupBox_12, 2, 3, 1, 1)

        self.groupBox_9 = QGroupBox(self.widget_6)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setFont(font2)
        self.groupBox_9.setAlignment(Qt.AlignCenter)
        self.gridLayout_19 = QGridLayout(self.groupBox_9)
        self.gridLayout_19.setSpacing(0)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, -1, 0, 0)
        self.space_screen1_4cam = QStackedWidget(self.groupBox_9)
        self.space_screen1_4cam.setObjectName(u"space_screen1_4cam")
        self.space_real_1_4cam = QWidget()
        self.space_real_1_4cam.setObjectName(u"space_real_1_4cam")
        self.gridLayout_30 = QGridLayout(self.space_real_1_4cam)
        self.gridLayout_30.setSpacing(0)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.show_pic_real_1_4cam = QLabel(self.space_real_1_4cam)
        self.show_pic_real_1_4cam.setObjectName(u"show_pic_real_1_4cam")
        sizePolicy.setHeightForWidth(self.show_pic_real_1_4cam.sizePolicy().hasHeightForWidth())
        self.show_pic_real_1_4cam.setSizePolicy(sizePolicy)
        self.show_pic_real_1_4cam.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.gridLayout_30.addWidget(self.show_pic_real_1_4cam, 0, 0, 1, 1)

        self.space_screen1_4cam.addWidget(self.space_real_1_4cam)
        self.space_result_1_4cam = QWidget()
        self.space_result_1_4cam.setObjectName(u"space_result_1_4cam")
        self.gridLayout_33 = QGridLayout(self.space_result_1_4cam)
        self.gridLayout_33.setSpacing(0)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setContentsMargins(0, 0, 0, 0)
        self.show_pic_result_1_4cam = QLabel(self.space_result_1_4cam)
        self.show_pic_result_1_4cam.setObjectName(u"show_pic_result_1_4cam")
        sizePolicy.setHeightForWidth(self.show_pic_result_1_4cam.sizePolicy().hasHeightForWidth())
        self.show_pic_result_1_4cam.setSizePolicy(sizePolicy)
        self.show_pic_result_1_4cam.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.gridLayout_33.addWidget(self.show_pic_result_1_4cam, 0, 0, 1, 1)

        self.space_screen1_4cam.addWidget(self.space_result_1_4cam)

        self.gridLayout_19.addWidget(self.space_screen1_4cam, 0, 1, 1, 1)


        self.gridLayout_26.addWidget(self.groupBox_9, 0, 0, 2, 1)


        self.gridLayout_32.addWidget(self.widget_6, 1, 0, 1, 1)

        self.groupBox_13 = QGroupBox(self.window_4)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setMinimumSize(QSize(0, 0))
        self.groupBox_13.setFont(font2)
        self.gridLayout_21 = QGridLayout(self.groupBox_13)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.formLayout_8.setHorizontalSpacing(0)
        self.formLayout_8.setVerticalSpacing(10)
        self.formLayout_8.setContentsMargins(10, 10, -1, -1)
        self.show_limit_ai_4cam = QLabel(self.groupBox_13)
        self.show_limit_ai_4cam.setObjectName(u"show_limit_ai_4cam")

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.show_limit_ai_4cam)

        self.slider_limit_ai_4cam = QSlider(self.groupBox_13)
        self.slider_limit_ai_4cam.setObjectName(u"slider_limit_ai_4cam")
        self.slider_limit_ai_4cam.setOrientation(Qt.Horizontal)

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.slider_limit_ai_4cam)

        self.show_limit_area_4cam = QLabel(self.groupBox_13)
        self.show_limit_area_4cam.setObjectName(u"show_limit_area_4cam")

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.show_limit_area_4cam)

        self.slider_limit_area_4cam = QSlider(self.groupBox_13)
        self.slider_limit_area_4cam.setObjectName(u"slider_limit_area_4cam")
        self.slider_limit_area_4cam.setOrientation(Qt.Horizontal)

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.slider_limit_area_4cam)


        self.gridLayout_21.addLayout(self.formLayout_8, 0, 0, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(50, 17, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_18, 0, 1, 1, 1)

        self.but_real_4cam_2 = QPushButton(self.groupBox_13)
        self.but_real_4cam_2.setObjectName(u"but_real_4cam_2")
        self.but_real_4cam_2.setMinimumSize(QSize(120, 50))
        self.but_real_4cam_2.setIcon(icon12)

        self.gridLayout_21.addWidget(self.but_real_4cam_2, 0, 2, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(50, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_14, 0, 3, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.but_real_4cam = QPushButton(self.groupBox_13)
        self.but_real_4cam.setObjectName(u"but_real_4cam")
        self.but_real_4cam.setMinimumSize(QSize(0, 30))
        icon22 = QIcon()
        icon22.addFile(u":/icon/icons/Picture-Landscape--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_real_4cam.setIcon(icon22)

        self.verticalLayout_11.addWidget(self.but_real_4cam)

        self.but_result_4cam = QPushButton(self.groupBox_13)
        self.but_result_4cam.setObjectName(u"but_result_4cam")
        self.but_result_4cam.setMinimumSize(QSize(0, 30))
        icon23 = QIcon()
        icon23.addFile(u":/icon/icons/Binocular--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_result_4cam.setIcon(icon23)

        self.verticalLayout_11.addWidget(self.but_result_4cam)


        self.gridLayout_21.addLayout(self.verticalLayout_11, 0, 4, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(50, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_15, 0, 5, 1, 1)


        self.gridLayout_32.addWidget(self.groupBox_13, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.window_4)
        self.window_5 = QWidget()
        self.window_5.setObjectName(u"window_5")
        self.gridLayout_42 = QGridLayout(self.window_5)
        self.gridLayout_42.setSpacing(0)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_42.setContentsMargins(0, 0, 0, 0)
        self.formLayout_9 = QFormLayout()
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.formLayout_9.setHorizontalSpacing(0)
        self.formLayout_9.setVerticalSpacing(0)
        self.formLayout_9.setContentsMargins(-1, -1, 80, -1)
        self.but_tool_ng1cam = QPushButton(self.window_5)
        self.but_tool_ng1cam.setObjectName(u"but_tool_ng1cam")
        self.but_tool_ng1cam.setMinimumSize(QSize(0, 30))
        self.but_tool_ng1cam.setIcon(icon9)
        self.but_tool_ng1cam.setCheckable(False)

        self.formLayout_9.setWidget(0, QFormLayout.LabelRole, self.but_tool_ng1cam)

        self.label_28 = QLabel(self.window_5)
        self.label_28.setObjectName(u"label_28")
        sizePolicy4.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy4)
        self.label_28.setFont(font)
        self.label_28.setAlignment(Qt.AlignCenter)

        self.formLayout_9.setWidget(0, QFormLayout.FieldRole, self.label_28)


        self.gridLayout_42.addLayout(self.formLayout_9, 0, 0, 1, 1)

        self.widget_7 = QWidget(self.window_5)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_41 = QGridLayout(self.widget_7)
        self.gridLayout_41.setSpacing(0)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setContentsMargins(0, 0, 0, 0)
        self.groupBox_14 = QGroupBox(self.widget_7)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setFont(font2)
        self.gridLayout_37 = QGridLayout(self.groupBox_14)
        self.gridLayout_37.setSpacing(0)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setContentsMargins(0, 0, 0, 0)
        self.list_ng1cam = QListWidget(self.groupBox_14)
        self.list_ng1cam.setObjectName(u"list_ng1cam")
        sizePolicy.setHeightForWidth(self.list_ng1cam.sizePolicy().hasHeightForWidth())
        self.list_ng1cam.setSizePolicy(sizePolicy)
        self.list_ng1cam.setStyleSheet(u"")

        self.gridLayout_37.addWidget(self.list_ng1cam, 0, 0, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(50)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, -1, 5, -1)
        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_11)

        self.but_up_ng1cam = QPushButton(self.groupBox_14)
        self.but_up_ng1cam.setObjectName(u"but_up_ng1cam")
        self.but_up_ng1cam.setMinimumSize(QSize(50, 60))
        icon24 = QIcon()
        icon24.addFile(u":/icon/icons/Navigation-Arrows-Up-1--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_up_ng1cam.setIcon(icon24)

        self.verticalLayout_12.addWidget(self.but_up_ng1cam)

        self.but_down_ng1cam = QPushButton(self.groupBox_14)
        self.but_down_ng1cam.setObjectName(u"but_down_ng1cam")
        self.but_down_ng1cam.setMinimumSize(QSize(50, 60))
        icon25 = QIcon()
        icon25.addFile(u":/icon/icons/Navigation-Arrows-Down-1--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_down_ng1cam.setIcon(icon25)

        self.verticalLayout_12.addWidget(self.but_down_ng1cam)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_12)


        self.gridLayout_37.addLayout(self.verticalLayout_12, 0, 1, 1, 1)


        self.gridLayout_41.addWidget(self.groupBox_14, 0, 0, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.groupBox_15 = QGroupBox(self.widget_7)
        self.groupBox_15.setObjectName(u"groupBox_15")
        sizePolicy.setHeightForWidth(self.groupBox_15.sizePolicy().hasHeightForWidth())
        self.groupBox_15.setSizePolicy(sizePolicy)
        self.groupBox_15.setFont(font2)
        self.gridLayout_38 = QGridLayout(self.groupBox_15)
        self.gridLayout_38.setSpacing(0)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setContentsMargins(0, -1, 0, 0)
        self.show_pic_real_ng1cam = QLabel(self.groupBox_15)
        self.show_pic_real_ng1cam.setObjectName(u"show_pic_real_ng1cam")
        self.show_pic_real_ng1cam.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.gridLayout_38.addWidget(self.show_pic_real_ng1cam, 0, 0, 1, 1)


        self.verticalLayout_13.addWidget(self.groupBox_15)

        self.groupBox_16 = QGroupBox(self.widget_7)
        self.groupBox_16.setObjectName(u"groupBox_16")
        sizePolicy.setHeightForWidth(self.groupBox_16.sizePolicy().hasHeightForWidth())
        self.groupBox_16.setSizePolicy(sizePolicy)
        self.groupBox_16.setFont(font2)
        self.gridLayout_40 = QGridLayout(self.groupBox_16)
        self.gridLayout_40.setSpacing(0)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setContentsMargins(0, -1, 0, 0)
        self.show_pic_result_ng1cam = QLabel(self.groupBox_16)
        self.show_pic_result_ng1cam.setObjectName(u"show_pic_result_ng1cam")
        self.show_pic_result_ng1cam.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.gridLayout_40.addWidget(self.show_pic_result_ng1cam, 0, 0, 1, 1)


        self.verticalLayout_13.addWidget(self.groupBox_16)


        self.gridLayout_41.addLayout(self.verticalLayout_13, 0, 1, 1, 1)


        self.gridLayout_42.addWidget(self.widget_7, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.window_5)
        self.window_6 = QWidget()
        self.window_6.setObjectName(u"window_6")
        self.gridLayout_48 = QGridLayout(self.window_6)
        self.gridLayout_48.setSpacing(0)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.gridLayout_48.setContentsMargins(0, 0, 0, 0)
        self.formLayout_10 = QFormLayout()
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.formLayout_10.setHorizontalSpacing(0)
        self.formLayout_10.setVerticalSpacing(0)
        self.formLayout_10.setContentsMargins(-1, -1, 80, -1)
        self.but_tool_ng4cam = QPushButton(self.window_6)
        self.but_tool_ng4cam.setObjectName(u"but_tool_ng4cam")
        self.but_tool_ng4cam.setMinimumSize(QSize(0, 30))
        self.but_tool_ng4cam.setIcon(icon9)
        self.but_tool_ng4cam.setCheckable(False)

        self.formLayout_10.setWidget(0, QFormLayout.LabelRole, self.but_tool_ng4cam)

        self.label_29 = QLabel(self.window_6)
        self.label_29.setObjectName(u"label_29")
        sizePolicy4.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy4)
        self.label_29.setFont(font)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.formLayout_10.setWidget(0, QFormLayout.FieldRole, self.label_29)


        self.gridLayout_48.addLayout(self.formLayout_10, 0, 0, 1, 2)

        self.groupBox_17 = QGroupBox(self.window_6)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setFont(font2)
        self.gridLayout_43 = QGridLayout(self.groupBox_17)
        self.gridLayout_43.setSpacing(0)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setContentsMargins(0, 0, 0, 0)
        self.list_ng4cam = QListWidget(self.groupBox_17)
        self.list_ng4cam.setObjectName(u"list_ng4cam")
        sizePolicy1.setHeightForWidth(self.list_ng4cam.sizePolicy().hasHeightForWidth())
        self.list_ng4cam.setSizePolicy(sizePolicy1)

        self.gridLayout_43.addWidget(self.list_ng4cam, 0, 0, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(50)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(5, -1, 5, -1)
        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_13)

        self.but_up_ng4cam = QPushButton(self.groupBox_17)
        self.but_up_ng4cam.setObjectName(u"but_up_ng4cam")
        self.but_up_ng4cam.setMinimumSize(QSize(50, 60))
        self.but_up_ng4cam.setIcon(icon24)

        self.verticalLayout_14.addWidget(self.but_up_ng4cam)

        self.but_down_ng4cam = QPushButton(self.groupBox_17)
        self.but_down_ng4cam.setObjectName(u"but_down_ng4cam")
        self.but_down_ng4cam.setMinimumSize(QSize(50, 60))
        self.but_down_ng4cam.setIcon(icon25)

        self.verticalLayout_14.addWidget(self.but_down_ng4cam)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_14)


        self.gridLayout_43.addLayout(self.verticalLayout_14, 0, 1, 1, 1)


        self.gridLayout_48.addWidget(self.groupBox_17, 1, 0, 1, 1)

        self.widget_8 = QWidget(self.window_6)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_47 = QGridLayout(self.widget_8)
        self.gridLayout_47.setSpacing(0)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.gridLayout_47.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        self.gridLayout_46 = QGridLayout(self.widget_9)
        self.gridLayout_46.setSpacing(10)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.gridLayout_46.setContentsMargins(0, -1, 0, 0)
        self.groupBox_18 = QGroupBox(self.widget_9)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setFont(font2)
        self.gridLayout_44 = QGridLayout(self.groupBox_18)
        self.gridLayout_44.setSpacing(0)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_44.setContentsMargins(0, -1, 0, 0)
        self.space_screen1_ng4cam = QStackedWidget(self.groupBox_18)
        self.space_screen1_ng4cam.setObjectName(u"space_screen1_ng4cam")
        self.space_real_1_ng4cam = QWidget()
        self.space_real_1_ng4cam.setObjectName(u"space_real_1_ng4cam")
        self.gridLayout_49 = QGridLayout(self.space_real_1_ng4cam)
        self.gridLayout_49.setSpacing(0)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.gridLayout_49.setContentsMargins(0, 0, 0, 0)
        self.show_pic_real_1_ng4cam = QLabel(self.space_real_1_ng4cam)
        self.show_pic_real_1_ng4cam.setObjectName(u"show_pic_real_1_ng4cam")
        self.show_pic_real_1_ng4cam.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.gridLayout_49.addWidget(self.show_pic_real_1_ng4cam, 0, 0, 1, 1)

        self.space_screen1_ng4cam.addWidget(self.space_real_1_ng4cam)
        self.space_result_1_ng4cam = QWidget()
        self.space_result_1_ng4cam.setObjectName(u"space_result_1_ng4cam")
        self.gridLayout_50 = QGridLayout(self.space_result_1_ng4cam)
        self.gridLayout_50.setSpacing(0)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.gridLayout_50.setContentsMargins(0, 0, 0, 0)
        self.show_pic_result_1_ng4cam = QLabel(self.space_result_1_ng4cam)
        self.show_pic_result_1_ng4cam.setObjectName(u"show_pic_result_1_ng4cam")
        self.show_pic_result_1_ng4cam.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.gridLayout_50.addWidget(self.show_pic_result_1_ng4cam, 0, 0, 1, 1)

        self.space_screen1_ng4cam.addWidget(self.space_result_1_ng4cam)

        self.gridLayout_44.addWidget(self.space_screen1_ng4cam, 0, 0, 1, 1)


        self.gridLayout_46.addWidget(self.groupBox_18, 0, 0, 1, 1)

        self.groupBox_19 = QGroupBox(self.widget_9)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.groupBox_19.setFont(font2)
        self.gridLayout_45 = QGridLayout(self.groupBox_19)
        self.gridLayout_45.setSpacing(0)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_45.setContentsMargins(0, -1, 0, 0)
        self.space_screen3_ng4cam = QStackedWidget(self.groupBox_19)
        self.space_screen3_ng4cam.setObjectName(u"space_screen3_ng4cam")
        self.space_real_3_ng4cam = QWidget()
        self.space_real_3_ng4cam.setObjectName(u"space_real_3_ng4cam")
        self.gridLayout_51 = QGridLayout(self.space_real_3_ng4cam)
        self.gridLayout_51.setSpacing(0)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.gridLayout_51.setContentsMargins(0, 0, 0, 0)
        self.show_pic_real_3_ng4cam = QLabel(self.space_real_3_ng4cam)
        self.show_pic_real_3_ng4cam.setObjectName(u"show_pic_real_3_ng4cam")
        self.show_pic_real_3_ng4cam.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.gridLayout_51.addWidget(self.show_pic_real_3_ng4cam, 0, 0, 1, 1)

        self.space_screen3_ng4cam.addWidget(self.space_real_3_ng4cam)
        self.space_result_3_ng4cam = QWidget()
        self.space_result_3_ng4cam.setObjectName(u"space_result_3_ng4cam")
        self.gridLayout_52 = QGridLayout(self.space_result_3_ng4cam)
        self.gridLayout_52.setSpacing(0)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.gridLayout_52.setContentsMargins(0, 0, 0, 0)
        self.show_pic_result_3_ng4cam = QLabel(self.space_result_3_ng4cam)
        self.show_pic_result_3_ng4cam.setObjectName(u"show_pic_result_3_ng4cam")
        self.show_pic_result_3_ng4cam.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.gridLayout_52.addWidget(self.show_pic_result_3_ng4cam, 0, 0, 1, 1)

        self.space_screen3_ng4cam.addWidget(self.space_result_3_ng4cam)

        self.gridLayout_45.addWidget(self.space_screen3_ng4cam, 0, 0, 1, 1)


        self.gridLayout_46.addWidget(self.groupBox_19, 0, 1, 1, 1)

        self.groupBox_39 = QGroupBox(self.widget_9)
        self.groupBox_39.setObjectName(u"groupBox_39")
        self.groupBox_39.setFont(font2)
        self.gridLayout_93 = QGridLayout(self.groupBox_39)
        self.gridLayout_93.setSpacing(0)
        self.gridLayout_93.setObjectName(u"gridLayout_93")
        self.gridLayout_93.setContentsMargins(0, -1, 0, 0)
        self.space_screen2_ng4cam = QStackedWidget(self.groupBox_39)
        self.space_screen2_ng4cam.setObjectName(u"space_screen2_ng4cam")
        self.space_real_2_ng4cam = QWidget()
        self.space_real_2_ng4cam.setObjectName(u"space_real_2_ng4cam")
        self.gridLayout_94 = QGridLayout(self.space_real_2_ng4cam)
        self.gridLayout_94.setSpacing(0)
        self.gridLayout_94.setObjectName(u"gridLayout_94")
        self.gridLayout_94.setContentsMargins(0, 0, 0, 0)
        self.show_pic_real_2_ng4cam = QLabel(self.space_real_2_ng4cam)
        self.show_pic_real_2_ng4cam.setObjectName(u"show_pic_real_2_ng4cam")
        self.show_pic_real_2_ng4cam.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.gridLayout_94.addWidget(self.show_pic_real_2_ng4cam, 0, 0, 1, 1)

        self.space_screen2_ng4cam.addWidget(self.space_real_2_ng4cam)
        self.space_result_2_ng4cam = QWidget()
        self.space_result_2_ng4cam.setObjectName(u"space_result_2_ng4cam")
        self.gridLayout_95 = QGridLayout(self.space_result_2_ng4cam)
        self.gridLayout_95.setSpacing(0)
        self.gridLayout_95.setObjectName(u"gridLayout_95")
        self.gridLayout_95.setContentsMargins(0, 0, 0, 0)
        self.show_pic_result_2_ng4cam = QLabel(self.space_result_2_ng4cam)
        self.show_pic_result_2_ng4cam.setObjectName(u"show_pic_result_2_ng4cam")
        self.show_pic_result_2_ng4cam.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.gridLayout_95.addWidget(self.show_pic_result_2_ng4cam, 0, 0, 1, 1)

        self.space_screen2_ng4cam.addWidget(self.space_result_2_ng4cam)

        self.gridLayout_93.addWidget(self.space_screen2_ng4cam, 0, 0, 1, 1)


        self.gridLayout_46.addWidget(self.groupBox_39, 1, 0, 1, 1)

        self.groupBox_40 = QGroupBox(self.widget_9)
        self.groupBox_40.setObjectName(u"groupBox_40")
        self.groupBox_40.setFont(font2)
        self.gridLayout_96 = QGridLayout(self.groupBox_40)
        self.gridLayout_96.setSpacing(0)
        self.gridLayout_96.setObjectName(u"gridLayout_96")
        self.gridLayout_96.setContentsMargins(0, -1, 0, 0)
        self.space_screen4_ng4cam = QStackedWidget(self.groupBox_40)
        self.space_screen4_ng4cam.setObjectName(u"space_screen4_ng4cam")
        self.space_real_4_ng4cam = QWidget()
        self.space_real_4_ng4cam.setObjectName(u"space_real_4_ng4cam")
        self.gridLayout_97 = QGridLayout(self.space_real_4_ng4cam)
        self.gridLayout_97.setSpacing(0)
        self.gridLayout_97.setObjectName(u"gridLayout_97")
        self.gridLayout_97.setContentsMargins(0, 0, 0, 0)
        self.show_pic_real_4_ng4cam = QLabel(self.space_real_4_ng4cam)
        self.show_pic_real_4_ng4cam.setObjectName(u"show_pic_real_4_ng4cam")
        self.show_pic_real_4_ng4cam.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.gridLayout_97.addWidget(self.show_pic_real_4_ng4cam, 0, 0, 1, 1)

        self.space_screen4_ng4cam.addWidget(self.space_real_4_ng4cam)
        self.space_result_4_ng4cam = QWidget()
        self.space_result_4_ng4cam.setObjectName(u"space_result_4_ng4cam")
        self.gridLayout_98 = QGridLayout(self.space_result_4_ng4cam)
        self.gridLayout_98.setSpacing(0)
        self.gridLayout_98.setObjectName(u"gridLayout_98")
        self.gridLayout_98.setContentsMargins(0, 0, 0, 0)
        self.show_pic_result_4_ng4cam = QLabel(self.space_result_4_ng4cam)
        self.show_pic_result_4_ng4cam.setObjectName(u"show_pic_result_4_ng4cam")
        self.show_pic_result_4_ng4cam.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;")

        self.gridLayout_98.addWidget(self.show_pic_result_4_ng4cam, 0, 0, 1, 1)

        self.space_screen4_ng4cam.addWidget(self.space_result_4_ng4cam)

        self.gridLayout_96.addWidget(self.space_screen4_ng4cam, 0, 0, 1, 1)


        self.gridLayout_46.addWidget(self.groupBox_40, 1, 1, 1, 1)


        self.gridLayout_47.addWidget(self.widget_9, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_12)

        self.but_left_ng4cam = QPushButton(self.widget_8)
        self.but_left_ng4cam.setObjectName(u"but_left_ng4cam")
        self.but_left_ng4cam.setMinimumSize(QSize(60, 50))
        icon26 = QIcon()
        icon26.addFile(u":/icon/icons/Navigation-Arrows-Left-1--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.but_left_ng4cam.setIcon(icon26)

        self.horizontalLayout_5.addWidget(self.but_left_ng4cam)

        self.but_right_ng4cam = QPushButton(self.widget_8)
        self.but_right_ng4cam.setObjectName(u"but_right_ng4cam")
        self.but_right_ng4cam.setMinimumSize(QSize(60, 50))
        self.but_right_ng4cam.setIcon(icon17)

        self.horizontalLayout_5.addWidget(self.but_right_ng4cam)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_13)


        self.gridLayout_47.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)


        self.gridLayout_48.addWidget(self.widget_8, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.window_6)
        self.window_7 = QWidget()
        self.window_7.setObjectName(u"window_7")
        self.gridLayout_57 = QGridLayout(self.window_7)
        self.gridLayout_57.setSpacing(0)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.gridLayout_57.setContentsMargins(0, 0, 0, 0)
        self.formLayout_11 = QFormLayout()
        self.formLayout_11.setObjectName(u"formLayout_11")
        self.formLayout_11.setHorizontalSpacing(0)
        self.formLayout_11.setVerticalSpacing(0)
        self.formLayout_11.setContentsMargins(-1, -1, 80, -1)
        self.but_tool_output = QPushButton(self.window_7)
        self.but_tool_output.setObjectName(u"but_tool_output")
        self.but_tool_output.setMinimumSize(QSize(0, 30))
        self.but_tool_output.setIcon(icon9)
        self.but_tool_output.setCheckable(False)

        self.formLayout_11.setWidget(0, QFormLayout.LabelRole, self.but_tool_output)

        self.label_38 = QLabel(self.window_7)
        self.label_38.setObjectName(u"label_38")
        sizePolicy4.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy4)
        self.label_38.setFont(font)
        self.label_38.setAlignment(Qt.AlignCenter)

        self.formLayout_11.setWidget(0, QFormLayout.FieldRole, self.label_38)


        self.gridLayout_57.addLayout(self.formLayout_11, 0, 0, 1, 1)

        self.widget_10 = QWidget(self.window_7)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy5)
        self.widget_10.setMinimumSize(QSize(0, 100))
        self.gridLayout_55 = QGridLayout(self.widget_10)
        self.gridLayout_55.setSpacing(0)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.gridLayout_55.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.show_date_from_output = QLabel(self.widget_10)
        self.show_date_from_output.setObjectName(u"show_date_from_output")
        font3 = QFont()
        font3.setPointSize(10)
        self.show_date_from_output.setFont(font3)

        self.verticalLayout_15.addWidget(self.show_date_from_output)

        self.show_to_date_output = QLabel(self.widget_10)
        self.show_to_date_output.setObjectName(u"show_to_date_output")
        self.show_to_date_output.setFont(font3)

        self.verticalLayout_15.addWidget(self.show_to_date_output)


        self.gridLayout_55.addLayout(self.verticalLayout_15, 0, 0, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.gridLayout_53 = QGridLayout()
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.label_36 = QLabel(self.widget_10)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(0, 50))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(False)
        self.label_36.setFont(font4)

        self.gridLayout_53.addWidget(self.label_36, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.widget_10)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 50))
        self.lineEdit.setFont(font3)
        self.lineEdit.setReadOnly(False)

        self.gridLayout_53.addWidget(self.lineEdit, 0, 1, 1, 1)


        self.verticalLayout_16.addLayout(self.gridLayout_53)

        self.show_value_now_output = QLabel(self.widget_10)
        self.show_value_now_output.setObjectName(u"show_value_now_output")
        self.show_value_now_output.setMinimumSize(QSize(0, 50))
        self.show_value_now_output.setFont(font3)

        self.verticalLayout_16.addWidget(self.show_value_now_output)

        self.gridLayout_54 = QGridLayout()
        self.gridLayout_54.setSpacing(50)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.gridLayout_54.setContentsMargins(100, -1, 20, -1)
        self.but_again_output = QPushButton(self.widget_10)
        self.but_again_output.setObjectName(u"but_again_output")
        self.but_again_output.setMinimumSize(QSize(0, 50))
        self.but_again_output.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_54.addWidget(self.but_again_output, 0, 0, 1, 1)

        self.but_save_output = QPushButton(self.widget_10)
        self.but_save_output.setObjectName(u"but_save_output")
        self.but_save_output.setMinimumSize(QSize(0, 50))
        self.but_save_output.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_54.addWidget(self.but_save_output, 0, 1, 1, 1)


        self.verticalLayout_16.addLayout(self.gridLayout_54)


        self.gridLayout_55.addLayout(self.verticalLayout_16, 0, 1, 1, 1)


        self.gridLayout_57.addWidget(self.widget_10, 1, 0, 1, 1)

        self.groupBox_20 = QGroupBox(self.window_7)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.groupBox_20.setFont(font4)
        self.groupBox_20.setAlignment(Qt.AlignCenter)
        self.gridLayout_56 = QGridLayout(self.groupBox_20)
        self.gridLayout_56.setSpacing(0)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.gridLayout_56.setContentsMargins(0, 10, 0, 0)
        self.horizontalSpacer_17 = QSpacerItem(143, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_56.addItem(self.horizontalSpacer_17, 0, 2, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(144, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_56.addItem(self.horizontalSpacer_16, 0, 0, 1, 1)

        self.data_output = QTableWidget(self.groupBox_20)
        self.data_output.setObjectName(u"data_output")
        self.data_output.setMinimumSize(QSize(600, 0))

        self.gridLayout_56.addWidget(self.data_output, 0, 1, 1, 1)


        self.gridLayout_57.addWidget(self.groupBox_20, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.window_7)
        self.window_8 = QWidget()
        self.window_8.setObjectName(u"window_8")
        self.gridLayout_58 = QGridLayout(self.window_8)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.textEdit = QTextEdit(self.window_8)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(False)

        self.gridLayout_58.addWidget(self.textEdit, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.window_8)

        self.gridLayout.addWidget(self.stackedWidget, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.window_header = QWidget(self.centralwidget)
        self.window_header.setObjectName(u"window_header")
        sizePolicy4.setHeightForWidth(self.window_header.sizePolicy().hasHeightForWidth())
        self.window_header.setSizePolicy(sizePolicy4)
        self.horizontalLayout = QHBoxLayout(self.window_header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.label_2 = QLabel(self.window_header)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/icon/icons/Time-Monthly-1--Streamline-Ultimate.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.time_and_day = QDateTimeEdit(self.window_header)
        self.time_and_day.setObjectName(u"time_and_day")
        self.time_and_day.setEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.time_and_day)


        self.horizontalLayout.addLayout(self.formLayout)

        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.window_header)
        self.label.setObjectName(u"label")
        font5 = QFont()
        font5.setPointSize(16)
        font5.setBold(True)
        self.label.setFont(font5)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(6)
        self.formLayout_2.setVerticalSpacing(0)
        self.label_3 = QLabel(self.window_header)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/icon/icons/Pie-Line-Graph-Desktop--Streamline-Ultimate.png"))

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.show_disk_header = QLabel(self.window_header)
        self.show_disk_header.setObjectName(u"show_disk_header")

        self.verticalLayout.addWidget(self.show_disk_header)

        self.show_ram_header = QLabel(self.window_header)
        self.show_ram_header.setObjectName(u"show_ram_header")

        self.verticalLayout.addWidget(self.show_ram_header)


        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.verticalLayout)


        self.horizontalLayout.addLayout(self.formLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.gridLayout_2.addWidget(self.window_header, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.but_cam_1_icon.toggled.connect(self.but_cam_1_expand.setChecked)
        self.but_cam_1_expand.toggled.connect(self.but_cam_1_icon.setChecked)
        self.but_4_cam_icon.toggled.connect(self.but_4_cam_expand.setChecked)
        self.but_4_cam_expand.toggled.connect(self.but_4_cam_icon.setChecked)
        self.but_NG_1_icon.toggled.connect(self.but_NG_1_expand.setChecked)
        self.but_NG_1_expand.toggled.connect(self.but_NG_1_icon.setChecked)
        self.but_NG_4_icon.toggled.connect(self.but_NG_4_expand.setChecked)
        self.but_NG_4_expand.toggled.connect(self.but_NG_4_icon.setChecked)
        self.but_output_icon.toggled.connect(self.but_output_expand.setChecked)
        self.but_output_expand.toggled.connect(self.but_output_icon.setChecked)
        self.but_screenshot_icon.toggled.connect(self.but_screenshot_expand.setChecked)
        self.but_screenshot_expand.toggled.connect(self.but_screenshot_icon.setChecked)
        self.but_information_icon.toggled.connect(self.but_information_expand.setChecked)
        self.but_information_expand.toggled.connect(self.but_information_icon.setChecked)

        self.stackedWidget.setCurrentIndex(3)
        self.stackedWidget_2.setCurrentIndex(0)
        self.space_screen2_4cam.setCurrentIndex(1)
        self.space_screen4_4cam.setCurrentIndex(1)
        self.space_screen1_4cam.setCurrentIndex(1)
        self.space_screen1_ng4cam.setCurrentIndex(1)
        self.space_screen3_ng4cam.setCurrentIndex(1)
        self.space_screen2_ng4cam.setCurrentIndex(1)
        self.space_screen4_ng4cam.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_6.setText("")
        self.but_cam_1_icon.setText("")
        self.but_4_cam_icon.setText("")
        self.but_NG_1_icon.setText("")
        self.but_NG_4_icon.setText("")
        self.but_output_icon.setText("")
        self.but_screenshot_icon.setText("")
        self.but_information_icon.setText("")
        self.but_exit_icon.setText("")
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"M\u1edf r\u1ed9ng", None))
        self.but_cam_1_expand.setText(QCoreApplication.translate("MainWindow", u"Cam 1", None))
        self.but_4_cam_expand.setText(QCoreApplication.translate("MainWindow", u"4 Cam", None))
        self.but_NG_1_expand.setText(QCoreApplication.translate("MainWindow", u"NG 1", None))
        self.but_NG_4_expand.setText(QCoreApplication.translate("MainWindow", u"NG 4", None))
        self.but_output_expand.setText(QCoreApplication.translate("MainWindow", u"S\u1ea3n l\u01b0\u1ee3ng", None))
        self.but_screenshot_expand.setText(QCoreApplication.translate("MainWindow", u"Screenshot", None))
        self.but_information_expand.setText(QCoreApplication.translate("MainWindow", u"Th\u00f4ng tin", None))
        self.but_exit_expand.setText(QCoreApplication.translate("MainWindow", u"Tho\u00e1t ", None))
        self.but_tool_cam1.setText(QCoreApplication.translate("MainWindow", u"Thanh c\u00f4ng c\u1ee5", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Cam 1", None))
        self.label_ok_cam1.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_ng_cam1.setText(QCoreApplication.translate("MainWindow", u"NG", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Th\u1ef1c t\u1ebf", None))
        self.show_pic_cam_cam1.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"K\u1ebft qu\u1ea3 tr\u1ea3 v\u1ec1", None))
        self.show_pic_real_cam1.setText("")
        self.show_pic_thread_cam1.setText("")
        self.show_pic_virtual_cam1.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"N\u00fat nh\u1ea5n", None))
        self.but_take_picture_cam1.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ee5p", None))
        self.but_saving_cam1.setText(QCoreApplication.translate("MainWindow", u"L\u01b0u gi\u00e1 tr\u1ecb", None))
        self.but_undo_cam1.setText(QCoreApplication.translate("MainWindow", u"Quay l\u1ea1i", None))
        self.but_take_sample_cam1.setText(QCoreApplication.translate("MainWindow", u"L\u1ea5y m\u1eabu", None))
        self.but_calib_cam1.setText(QCoreApplication.translate("MainWindow", u"Calib", None))
        self.but_result_cam1.setText(QCoreApplication.translate("MainWindow", u"K\u1ebft qu\u1ea3", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"B\u1ea3ng \u0111i\u1ec1u khi\u1ec3n", None))
        self.show_h_high_cam1.setText(QCoreApplication.translate("MainWindow", u"H cao", None))
        self.show_s_high_cam1.setText(QCoreApplication.translate("MainWindow", u"S cao", None))
        self.show_v_high_cam1.setText(QCoreApplication.translate("MainWindow", u"V cao", None))
        self.show_bright_cam1.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ed9 s\u00e1ng", None))
        self.show_ratio_cam1.setText(QCoreApplication.translate("MainWindow", u"Ph\u1ea7n tr\u0103m ng\u01b0\u1ee1ng:            ", None))
        self.show_h_low_cam1.setText(QCoreApplication.translate("MainWindow", u"H th\u1ea5p", None))
        self.show_s_low_cam1.setText(QCoreApplication.translate("MainWindow", u"S th\u1ea5p", None))
        self.show_v_low_cam1.setText(QCoreApplication.translate("MainWindow", u"V th\u1ea5p", None))
        self.show_r_circle_cam1.setText(QCoreApplication.translate("MainWindow", u"R tr\u00f2n t\u00e2m", None))
        self.show_contrast_cam1.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ed9 th\u01b0\u01a1ng ph\u1ea3n:             ", None))
        self.show_value_now_cam1.setText(QCoreApplication.translate("MainWindow", u"Gi\u00e1 tr\u1ecb hi\u1ec7n t\u1ea1i", None))
        self.show_value_contrast_cam1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0111\u1ed9 t\u01b0\u01a1ng ph\u1ea3n 0.0-3.0", None))
        self.but_tool_calib.setText(QCoreApplication.translate("MainWindow", u"Thanh c\u00f4ng c\u1ee5", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"M\u00e0n h\u00ecnh Calib", None))
        self.show_pic_calib_calib.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"N\u00fat nh\u1ea5n", None))
        self.but_take_calib.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ee5p \u1ea3nh", None))
        self.but_calib_calib.setText(QCoreApplication.translate("MainWindow", u"Calib", None))
        self.but_clear_calib.setText(QCoreApplication.translate("MainWindow", u"Clear ", None))
        self.but_back_home_calib.setText(QCoreApplication.translate("MainWindow", u"V\u1ec1 m\u00e0n h\u00ecnh ch\u00ednh", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u1ea2nh th\u1ef1c t\u1ebf ", None))
        self.show_pic_real_sample.setText("")
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u1ea2nh m\u1eabu", None))
        self.show_pic_sample_sample.setText("")
        self.but_tool_sample.setText(QCoreApplication.translate("MainWindow", u"Thanh c\u00f4ng c\u1ee5", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"M\u00e0n h\u00ecnh l\u1ea5y m\u1eabu", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"N\u00fat nh\u1ea5n", None))
        self.but_take_sample.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ee5p \u1ea3nh ", None))
        self.but_sample_sample.setText(QCoreApplication.translate("MainWindow", u"L\u1ea5y m\u1eabu", None))
        self.but_clear_sample.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a m\u1eabu", None))
        self.but_back_home_sample.setText(QCoreApplication.translate("MainWindow", u"V\u1ec1 m\u00e0n h\u00ecnh ch\u00ednh", None))
        self.but_tool_4cam.setText(QCoreApplication.translate("MainWindow", u"Thanh c\u00f4ng c\u1ee5", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"4 Cam", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"M\u00e0n h\u00ecnh  2", None))
        self.show_pic_real_2_4cam.setText("")
        self.show_pic_result_2_4cam.setText("")
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"M\u00e0n h\u00ecnh  3", None))
        self.show_pic_real_3_4cam.setText("")
        self.show_pic_result_3_4cam.setText("")
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"M\u00e0n h\u00ecnh  4", None))
        self.show_pic_real_4_4cam.setText("")
        self.show_pic_result_4_4cam.setText("")
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"M\u00e0n h\u00ecnh  1", None))
        self.show_pic_real_1_4cam.setText("")
        self.show_pic_result_1_4cam.setText("")
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"B\u1ea3ng \u0111i\u1ec1u khi\u1ec3n", None))
        self.show_limit_ai_4cam.setText(QCoreApplication.translate("MainWindow", u"Ng\u01b0\u1ee1ng AI:               ", None))
        self.show_limit_area_4cam.setText(QCoreApplication.translate("MainWindow", u"Ng\u01b0\u1ee1ng ph\u00e2n \u0111\u1ecbnh:                ", None))
        self.but_real_4cam_2.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ee5p \u1ea3nh", None))
        self.but_real_4cam.setText(QCoreApplication.translate("MainWindow", u"H\u00ecnh \u1ea3nh th\u1ef1c t\u1ebf", None))
        self.but_result_4cam.setText(QCoreApplication.translate("MainWindow", u"K\u1ebft qu\u1ea3 ", None))
        self.but_tool_ng1cam.setText(QCoreApplication.translate("MainWindow", u"Thanh c\u00f4ng c\u1ee5", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"NG 1 Cam", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Danh s\u00e1ch NG", None))
        self.but_up_ng1cam.setText("")
        self.but_down_ng1cam.setText("")
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"H\u00ecnh \u1ea3nh th\u1ef1c t\u1ebf ", None))
        self.show_pic_real_ng1cam.setText("")
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"K\u1ebft qu\u1ea3 ", None))
        self.show_pic_result_ng1cam.setText("")
        self.but_tool_ng4cam.setText(QCoreApplication.translate("MainWindow", u"Thanh c\u00f4ng c\u1ee5", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"NG 4 Cam", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"Danh s\u00e1ch NG", None))
        self.but_up_ng4cam.setText("")
        self.but_down_ng4cam.setText("")
        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", u"M\u00e0n h\u00ecnh 1", None))
        self.show_pic_real_1_ng4cam.setText("")
        self.show_pic_result_1_ng4cam.setText("")
        self.groupBox_19.setTitle(QCoreApplication.translate("MainWindow", u"M\u00e0n h\u00ecnh 3", None))
        self.show_pic_real_3_ng4cam.setText("")
        self.show_pic_result_3_ng4cam.setText("")
        self.groupBox_39.setTitle(QCoreApplication.translate("MainWindow", u"M\u00e0n h\u00ecnh 2", None))
        self.show_pic_real_2_ng4cam.setText("")
        self.show_pic_result_2_ng4cam.setText("")
        self.groupBox_40.setTitle(QCoreApplication.translate("MainWindow", u"M\u00e0n h\u00ecnh 4", None))
        self.show_pic_real_4_ng4cam.setText("")
        self.show_pic_result_4_ng4cam.setText("")
        self.but_left_ng4cam.setText("")
        self.but_right_ng4cam.setText("")
        self.but_tool_output.setText(QCoreApplication.translate("MainWindow", u"Thanh c\u00f4ng c\u1ee5", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"S\u1ea3n l\u01b0\u1ee3ng ", None))
        self.show_date_from_output.setText(QCoreApplication.translate("MainWindow", u"T\u1eeb ng\u00e0y :                                       ", None))
        self.show_to_date_output.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ebfn ng\u00e0y:                                       ", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp gi\u00e1 tr\u1ecb 1 set:  ", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"nh\u1eadp gi\u00e1 tr\u1ecb v\u00e0o......", None))
        self.show_value_now_output.setText(QCoreApplication.translate("MainWindow", u"Gi\u00e1 tr\u1ecb hi\u1ec7n t\u1ea1i:", None))
        self.but_again_output.setText(QCoreApplication.translate("MainWindow", u"B\u1eaft \u0111\u1ea7u l\u1ea1i ", None))
        self.but_save_output.setText(QCoreApplication.translate("MainWindow", u"L\u01b0u gi\u00e1 tr\u1ecb ", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("MainWindow", u"B\u1ea3ng theo d\u00f5i s\u1ea3n l\u01b0\u1ee3ng ", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ff0000;\">Th\u00f4ng tin phi\u00ean b\u1ea3n</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ff0000;\">Version: 1.0<br />Ng\u00e0y t\u1ea1o: 3/2025</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ff0000;\">\u0110\u01a1n v\u1ecb ph\u00e1t"
                        " h\u00e0nh: Pronics Precision <br />Ng\u01b0\u1eddi ph\u00e1t tri\u1ec3n: Ho\u00e0ng Vi\u1ec7t H\u01b0ng - (+84) 83 4729 608</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ff0000;\">Email: viethung18102000@gmail.com</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ff0000;\"><br /></p></body></html>", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"PRONICS PRECISION AUTOMATION", None))
        self.label_3.setText("")
        self.show_disk_header.setText(QCoreApplication.translate("MainWindow", u"Disk", None))
        self.show_ram_header.setText(QCoreApplication.translate("MainWindow", u"Ram:                ", None))
    # retranslateUi

