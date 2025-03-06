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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateTimeEdit, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 560)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout_10 = QGridLayout(self.centralwidget)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.space_header = QWidget(self.centralwidget)
        self.space_header.setObjectName(u"space_header")
        sizePolicy.setHeightForWidth(self.space_header.sizePolicy().hasHeightForWidth())
        self.space_header.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.space_header)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.space_header)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        self.label_4.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_2.setContentsMargins(-1, -1, 10, -1)
        self.label_5 = QLabel(self.space_header)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/icon/icons/Time-Monthly-1--Streamline-Ultimate.png"))
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.dateTimeEdit = QDateTimeEdit(self.space_header)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dateTimeEdit.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit.setSizePolicy(sizePolicy1)
        self.dateTimeEdit.setMinimumSize(QSize(0, 0))
        self.dateTimeEdit.setReadOnly(True)
        self.dateTimeEdit.setFixedWidth(120)

        self.horizontalLayout_2.addWidget(self.dateTimeEdit)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.label_6 = QLabel(self.space_header)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setTextFormat(Qt.MarkdownText)
        self.label_6.setPixmap(QPixmap(u":/icon/icons/Pie-Line-Graph-Desktop--Streamline-Ultimate.png"))
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_8 = QLabel(self.space_header)
        self.label_8.setObjectName(u"label_8")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_8.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_8)

        self.label_7 = QLabel(self.space_header)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 0))
        self.label_7.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_7)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.gridLayout_10.addWidget(self.space_header, 0, 0, 1, 1)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.space_full_icon = QWidget(self.centralwidget)
        self.space_full_icon.setObjectName(u"space_full_icon")
        sizePolicy.setHeightForWidth(self.space_full_icon.sizePolicy().hasHeightForWidth())
        self.space_full_icon.setSizePolicy(sizePolicy)
        self.space_full_icon.setStyleSheet(u"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(255, 85, 0);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.space_full_icon)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.space_full_icon)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setPixmap(QPixmap(u":/icon/icons/Settings-Sound--Streamline-Ultimate.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(20, 15, 20, 15)
        self.pushButton_3 = QPushButton(self.space_full_icon)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)
        icon = QIcon()
        icon.addFile(u":/icon/icons/Expand-Full--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.space_full_icon)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy2.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy2)
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/Shrink-4--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.space_full_icon)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy2.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy2)
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/Paginate-Filter-1--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.space_full_icon)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy2.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy2)
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/Paginate-Filter-4--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon3)
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.space_full_icon)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy2.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy2)
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/Accounting-Calculator--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_7.setIcon(icon4)
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_7)

        self.pushButton = QPushButton(self.space_full_icon)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        icon5 = QIcon()
        icon5.addFile(u":/icon/icons/Paginate-Filter-Camera--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_8 = QPushButton(self.space_full_icon)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy2.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy2)
        icon6 = QIcon()
        icon6.addFile(u":/icon/icons/Alert-Hexagon--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_8.setIcon(icon6)
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_8)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 403, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton_9 = QPushButton(self.space_full_icon)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy2.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy2)
        icon7 = QIcon()
        icon7.addFile(u":/icon/icons/Logout-2--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_9.setIcon(icon7)

        self.verticalLayout_3.addWidget(self.pushButton_9)


        self.horizontalLayout_40.addWidget(self.space_full_icon)

        self.space_expand = QWidget(self.centralwidget)
        self.space_expand.setObjectName(u"space_expand")
        sizePolicy.setHeightForWidth(self.space_expand.sizePolicy().hasHeightForWidth())
        self.space_expand.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.space_expand)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_2 = QLabel(self.space_expand)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 35))
        self.label_2.setPixmap(QPixmap(u":/icon/icons/Settings-Toggle-Vertical--Streamline-Ultimate.png"))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.space_expand)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 35))
        self.label_3.setFont(font1)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_2.setContentsMargins(20, 15, 20, 15)
        self.pushButton_18 = QPushButton(self.space_expand)
        self.pushButton_18.setObjectName(u"pushButton_18")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setPointSize(10)
        self.pushButton_18.setFont(font2)
        self.pushButton_18.setIcon(icon)
        self.pushButton_18.setCheckable(True)
        self.pushButton_18.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_18)

        self.pushButton_17 = QPushButton(self.space_expand)
        self.pushButton_17.setObjectName(u"pushButton_17")
        sizePolicy3.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy3)
        self.pushButton_17.setFont(font2)
        self.pushButton_17.setIcon(icon1)
        self.pushButton_17.setCheckable(True)
        self.pushButton_17.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_17)

        self.pushButton_16 = QPushButton(self.space_expand)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy3.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy3)
        self.pushButton_16.setIcon(icon2)
        self.pushButton_16.setCheckable(True)
        self.pushButton_16.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_16)

        self.pushButton_15 = QPushButton(self.space_expand)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy3.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy3)
        self.pushButton_15.setFont(font2)
        self.pushButton_15.setIcon(icon3)
        self.pushButton_15.setCheckable(True)
        self.pushButton_15.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_15)

        self.pushButton_14 = QPushButton(self.space_expand)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy3.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy3)
        self.pushButton_14.setFont(font2)
        icon8 = QIcon()
        icon8.addFile(u"icons/Accounting-Calculator--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_14.setIcon(icon8)
        self.pushButton_14.setCheckable(True)
        self.pushButton_14.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_14)

        self.pushButton_13 = QPushButton(self.space_expand)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy3.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy3)
        self.pushButton_13.setFont(font2)
        self.pushButton_13.setIcon(icon5)
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_13)

        self.pushButton_12 = QPushButton(self.space_expand)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy3.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy3)
        self.pushButton_12.setMinimumSize(QSize(0, 0))
        self.pushButton_12.setFont(font2)
        self.pushButton_12.setIcon(icon6)
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_12)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 403, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.pushButton_10 = QPushButton(self.space_expand)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy2.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy2)
        self.pushButton_10.setIcon(icon7)

        self.verticalLayout_4.addWidget(self.pushButton_10)


        self.horizontalLayout_40.addWidget(self.space_expand)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_6 = QHBoxLayout(self.widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.space_main_1 = QWidget()
        self.space_main_1.setObjectName(u"space_main_1")
        sizePolicy.setHeightForWidth(self.space_main_1.sizePolicy().hasHeightForWidth())
        self.space_main_1.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.space_main_1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget_11 = QWidget(self.space_main_1)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy)
        self.widget_11.setMinimumSize(QSize(0, 0))
        self.gridLayout_7 = QGridLayout(self.widget_11)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_30 = QLabel(self.widget_11)
        self.label_30.setObjectName(u"label_30")
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.label_30.setFont(font3)
        self.label_30.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_30, 0, 1, 1, 1)

        self.pushButton_11 = QPushButton(self.widget_11)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy2.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy2)
        self.pushButton_11.setMinimumSize(QSize(0, 0))
        self.pushButton_11.setMaximumSize(QSize(120, 16777215))
        self.pushButton_11.setFont(font2)
        icon9 = QIcon()
        icon9.addFile(u":/icon/icons/Navigation-Menu-1--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_11.setIcon(icon9)
        self.pushButton_11.setIconSize(QSize(24, 24))
        self.pushButton_11.setCheckable(True)

        self.gridLayout_7.addWidget(self.pushButton_11, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget_11, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetMinimumSize)
        self.widget_2 = QWidget(self.space_main_1)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.widget_2.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.widget_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_3 = QSpacerItem(20, 300, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetMinimumSize)
        self.pushButton_19 = QPushButton(self.widget_2)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_19.sizePolicy().hasHeightForWidth())
        self.pushButton_19.setSizePolicy(sizePolicy4)
        self.pushButton_19.setMinimumSize(QSize(0, 0))
        self.pushButton_19.setFont(font2)
        self.pushButton_19.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u":/icon/icons/Like-1--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_19.setIcon(icon10)

        self.verticalLayout_6.addWidget(self.pushButton_19)

        self.pushButton_20 = QPushButton(self.widget_2)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy4)
        self.pushButton_20.setFont(font2)
        icon11 = QIcon()
        icon11.addFile(u":/icon/icons/Thumb-Down-Dislike--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_20.setIcon(icon11)

        self.verticalLayout_6.addWidget(self.pushButton_20)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.verticalSpacer_4 = QSpacerItem(20, 300, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)


        self.horizontalLayout_5.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.space_main_1)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(100)
        sizePolicy5.setVerticalStretch(100)
        sizePolicy5.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy5)
        self.verticalLayout_8 = QVBoxLayout(self.widget_3)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_3)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setMaximumSize(QSize(16777215, 16777215))
        self.label_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_9)

        self.label_11 = QLabel(self.widget_3)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setMinimumSize(QSize(0, 0))
        self.label_11.setMaximumSize(QSize(16777215, 30))
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_11)


        self.horizontalLayout_5.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.space_main_1)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(100)
        sizePolicy6.setVerticalStretch(100)
        sizePolicy6.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy6)
        self.verticalLayout_9 = QVBoxLayout(self.widget_4)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_4)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)
        self.label_10.setMaximumSize(QSize(16777215, 16777215))
        self.label_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.label_10)

        self.label_12 = QLabel(self.widget_4)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setMaximumSize(QSize(16777215, 30))
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_12)


        self.horizontalLayout_5.addWidget(self.widget_4)


        self.gridLayout_4.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.pushButton_21 = QPushButton(self.space_main_1)
        self.pushButton_21.setObjectName(u"pushButton_21")
        sizePolicy3.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy3)
        self.pushButton_21.setFont(font2)
        icon12 = QIcon()
        icon12.addFile(u":/icon/icons/Cursor-Select-Frame--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_21.setIcon(icon12)

        self.horizontalLayout_7.addWidget(self.pushButton_21)

        self.pushButton_28 = QPushButton(self.space_main_1)
        self.pushButton_28.setObjectName(u"pushButton_28")
        sizePolicy3.setHeightForWidth(self.pushButton_28.sizePolicy().hasHeightForWidth())
        self.pushButton_28.setSizePolicy(sizePolicy3)
        self.pushButton_28.setFont(font2)
        icon13 = QIcon()
        icon13.addFile(u":/icon/icons/Time-Clock-File-Refresh--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_28.setIcon(icon13)

        self.horizontalLayout_7.addWidget(self.pushButton_28)

        self.pushButton_22 = QPushButton(self.space_main_1)
        self.pushButton_22.setObjectName(u"pushButton_22")
        sizePolicy3.setHeightForWidth(self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy3)
        self.pushButton_22.setFont(font2)
        icon14 = QIcon()
        icon14.addFile(u":/icon/icons/Append-Data-To-Spreadsheet--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_22.setIcon(icon14)

        self.horizontalLayout_7.addWidget(self.pushButton_22)

        self.pushButton_29 = QPushButton(self.space_main_1)
        self.pushButton_29.setObjectName(u"pushButton_29")
        sizePolicy3.setHeightForWidth(self.pushButton_29.sizePolicy().hasHeightForWidth())
        self.pushButton_29.setSizePolicy(sizePolicy3)
        self.pushButton_29.setFont(font2)
        icon15 = QIcon()
        icon15.addFile(u":/icon/icons/Cell-Select-1--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_29.setIcon(icon15)

        self.horizontalLayout_7.addWidget(self.pushButton_29)

        self.pushButton_30 = QPushButton(self.space_main_1)
        self.pushButton_30.setObjectName(u"pushButton_30")
        sizePolicy3.setHeightForWidth(self.pushButton_30.sizePolicy().hasHeightForWidth())
        self.pushButton_30.setSizePolicy(sizePolicy3)
        self.pushButton_30.setFont(font2)
        icon16 = QIcon()
        icon16.addFile(u":/icon/icons/Move-Right--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_30.setIcon(icon16)

        self.horizontalLayout_7.addWidget(self.pushButton_30)


        self.gridLayout_4.addLayout(self.horizontalLayout_7, 2, 0, 1, 1)

        self.groupBox = QGroupBox(self.space_main_1)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"        border: 2px solid #630094;\n"
"        border-radius: 5px;\n"
"        background-color: lightgray;\n"
"    }")
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_7 = QWidget(self.groupBox)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy3.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy3)
        self.gridLayout = QGridLayout(self.widget_7)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_17 = QLabel(self.widget_7)
        self.label_17.setObjectName(u"label_17")
        sizePolicy3.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy3)
        self.label_17.setMinimumSize(QSize(0, 0))
        self.label_17.setMaximumSize(QSize(16777212, 16777215))

        self.horizontalLayout_8.addWidget(self.label_17)

        self.horizontalSlider = QSlider(self.widget_7)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy7)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_8.addWidget(self.horizontalSlider)


        self.gridLayout.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_18 = QLabel(self.widget_7)
        self.label_18.setObjectName(u"label_18")
        sizePolicy3.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy3)
        self.label_18.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_9.addWidget(self.label_18)

        self.horizontalSlider_2 = QSlider(self.widget_7)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        sizePolicy7.setHeightForWidth(self.horizontalSlider_2.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_2.setSizePolicy(sizePolicy7)
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.horizontalLayout_9.addWidget(self.horizontalSlider_2)


        self.gridLayout.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_19 = QLabel(self.widget_7)
        self.label_19.setObjectName(u"label_19")
        sizePolicy3.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy3)
        self.label_19.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_10.addWidget(self.label_19)

        self.horizontalSlider_3 = QSlider(self.widget_7)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        sizePolicy7.setHeightForWidth(self.horizontalSlider_3.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_3.setSizePolicy(sizePolicy7)
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)

        self.horizontalLayout_10.addWidget(self.horizontalSlider_3)


        self.gridLayout.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_20 = QLabel(self.widget_7)
        self.label_20.setObjectName(u"label_20")
        sizePolicy3.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy3)
        self.label_20.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_11.addWidget(self.label_20)

        self.horizontalSlider_4 = QSlider(self.widget_7)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        sizePolicy7.setHeightForWidth(self.horizontalSlider_4.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_4.setSizePolicy(sizePolicy7)
        self.horizontalSlider_4.setOrientation(Qt.Horizontal)

        self.horizontalLayout_11.addWidget(self.horizontalSlider_4)


        self.gridLayout.addLayout(self.horizontalLayout_11, 3, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_25 = QLabel(self.widget_7)
        self.label_25.setObjectName(u"label_25")
        sizePolicy3.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy3)
        self.label_25.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_12.addWidget(self.label_25)

        self.horizontalSlider_9 = QSlider(self.widget_7)
        self.horizontalSlider_9.setObjectName(u"horizontalSlider_9")
        sizePolicy7.setHeightForWidth(self.horizontalSlider_9.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_9.setSizePolicy(sizePolicy7)
        self.horizontalSlider_9.setOrientation(Qt.Horizontal)

        self.horizontalLayout_12.addWidget(self.horizontalSlider_9)


        self.gridLayout.addLayout(self.horizontalLayout_12, 4, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_7, 0, 0, 1, 1)

        self.widget_8 = QWidget(self.groupBox)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.widget_8)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_21 = QLabel(self.widget_8)
        self.label_21.setObjectName(u"label_21")
        sizePolicy3.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy3)
        self.label_21.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_13.addWidget(self.label_21)

        self.horizontalSlider_5 = QSlider(self.widget_8)
        self.horizontalSlider_5.setObjectName(u"horizontalSlider_5")
        sizePolicy7.setHeightForWidth(self.horizontalSlider_5.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_5.setSizePolicy(sizePolicy7)
        self.horizontalSlider_5.setOrientation(Qt.Horizontal)

        self.horizontalLayout_13.addWidget(self.horizontalSlider_5)


        self.gridLayout_2.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_22 = QLabel(self.widget_8)
        self.label_22.setObjectName(u"label_22")
        sizePolicy3.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy3)
        self.label_22.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_14.addWidget(self.label_22)

        self.horizontalSlider_6 = QSlider(self.widget_8)
        self.horizontalSlider_6.setObjectName(u"horizontalSlider_6")
        sizePolicy7.setHeightForWidth(self.horizontalSlider_6.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_6.setSizePolicy(sizePolicy7)
        self.horizontalSlider_6.setOrientation(Qt.Horizontal)

        self.horizontalLayout_14.addWidget(self.horizontalSlider_6)


        self.gridLayout_2.addLayout(self.horizontalLayout_14, 1, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_23 = QLabel(self.widget_8)
        self.label_23.setObjectName(u"label_23")
        sizePolicy3.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy3)
        self.label_23.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_15.addWidget(self.label_23)

        self.horizontalSlider_7 = QSlider(self.widget_8)
        self.horizontalSlider_7.setObjectName(u"horizontalSlider_7")
        sizePolicy7.setHeightForWidth(self.horizontalSlider_7.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_7.setSizePolicy(sizePolicy7)
        self.horizontalSlider_7.setOrientation(Qt.Horizontal)

        self.horizontalLayout_15.addWidget(self.horizontalSlider_7)


        self.gridLayout_2.addLayout(self.horizontalLayout_15, 2, 0, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_24 = QLabel(self.widget_8)
        self.label_24.setObjectName(u"label_24")
        sizePolicy3.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy3)
        self.label_24.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_16.addWidget(self.label_24)

        self.horizontalSlider_8 = QSlider(self.widget_8)
        self.horizontalSlider_8.setObjectName(u"horizontalSlider_8")
        sizePolicy7.setHeightForWidth(self.horizontalSlider_8.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_8.setSizePolicy(sizePolicy7)
        self.horizontalSlider_8.setOrientation(Qt.Horizontal)

        self.horizontalLayout_16.addWidget(self.horizontalSlider_8)


        self.gridLayout_2.addLayout(self.horizontalLayout_16, 3, 0, 1, 1)

        self.label_26 = QLabel(self.widget_8)
        self.label_26.setObjectName(u"label_26")
        sizePolicy3.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.label_26, 4, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_8, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.space_main_1)
        self.space_main_2 = QWidget()
        self.space_main_2.setObjectName(u"space_main_2")
        self.gridLayout_5 = QGridLayout(self.space_main_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SetMaximumSize)
        self.widget_12 = QWidget(self.space_main_2)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy)
        self.widget_12.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_34 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.pushButton_49 = QPushButton(self.widget_12)
        self.pushButton_49.setObjectName(u"pushButton_49")
        self.pushButton_49.setMinimumSize(QSize(0, 15))
        self.pushButton_49.setMaximumSize(QSize(120, 16777215))
        self.pushButton_49.setFont(font2)
        self.pushButton_49.setIcon(icon9)
        self.pushButton_49.setIconSize(QSize(24, 24))
        self.pushButton_49.setCheckable(True)

        self.horizontalLayout_34.addWidget(self.pushButton_49)

        self.label_31 = QLabel(self.widget_12)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font3)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.label_31)


        self.gridLayout_5.addWidget(self.widget_12, 0, 0, 1, 1)

        self.widget_9 = QWidget(self.space_main_2)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
        self.horizontalLayout_17 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_5)

        self.label_27 = QLabel(self.widget_9)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(600, 600))
        self.label_27.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_17.addWidget(self.label_27)

        self.horizontalSpacer_6 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_6)


        self.gridLayout_5.addWidget(self.widget_9, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.space_main_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 100))
        self.groupBox_2.setFont(font2)
        self.horizontalLayout_18 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_18.setSpacing(100)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(50, 10, 50, 10)
        self.pushButton_31 = QPushButton(self.groupBox_2)
        self.pushButton_31.setObjectName(u"pushButton_31")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.pushButton_31.sizePolicy().hasHeightForWidth())
        self.pushButton_31.setSizePolicy(sizePolicy8)
        self.pushButton_31.setIcon(icon5)

        self.horizontalLayout_18.addWidget(self.pushButton_31)

        self.pushButton_32 = QPushButton(self.groupBox_2)
        self.pushButton_32.setObjectName(u"pushButton_32")
        icon17 = QIcon()
        icon17.addFile(u":/icon/icons/Graph-Stats-Circle--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_32.setIcon(icon17)

        self.horizontalLayout_18.addWidget(self.pushButton_32)

        self.pushButton_33 = QPushButton(self.groupBox_2)
        self.pushButton_33.setObjectName(u"pushButton_33")
        icon18 = QIcon()
        icon18.addFile(u":/icon/icons/Bin-1--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_33.setIcon(icon18)

        self.horizontalLayout_18.addWidget(self.pushButton_33)

        self.pushButton_34 = QPushButton(self.groupBox_2)
        self.pushButton_34.setObjectName(u"pushButton_34")
        icon19 = QIcon()
        icon19.addFile(u":/icon/icons/Move-Left--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_34.setIcon(icon19)

        self.horizontalLayout_18.addWidget(self.pushButton_34)


        self.gridLayout_5.addWidget(self.groupBox_2, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.space_main_2)
        self.space_main_3 = QWidget()
        self.space_main_3.setObjectName(u"space_main_3")
        self.gridLayout_6 = QGridLayout(self.space_main_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.widget_13 = QWidget(self.space_main_3)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy)
        self.widget_13.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_35 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.pushButton_50 = QPushButton(self.widget_13)
        self.pushButton_50.setObjectName(u"pushButton_50")
        self.pushButton_50.setMinimumSize(QSize(0, 15))
        self.pushButton_50.setMaximumSize(QSize(120, 16777215))
        self.pushButton_50.setFont(font2)
        self.pushButton_50.setIcon(icon9)
        self.pushButton_50.setIconSize(QSize(24, 24))

        self.horizontalLayout_35.addWidget(self.pushButton_50)

        self.label_32 = QLabel(self.widget_13)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font3)
        self.label_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_32)


        self.gridLayout_6.addWidget(self.widget_13, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.space_main_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(16777215, 100))
        self.groupBox_3.setFont(font2)
        self.horizontalLayout_20 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.pushButton_35 = QPushButton(self.groupBox_3)
        self.pushButton_35.setObjectName(u"pushButton_35")

        self.horizontalLayout_20.addWidget(self.pushButton_35)

        self.pushButton_36 = QPushButton(self.groupBox_3)
        self.pushButton_36.setObjectName(u"pushButton_36")

        self.horizontalLayout_20.addWidget(self.pushButton_36)

        self.pushButton_37 = QPushButton(self.groupBox_3)
        self.pushButton_37.setObjectName(u"pushButton_37")

        self.horizontalLayout_20.addWidget(self.pushButton_37)

        self.pushButton_38 = QPushButton(self.groupBox_3)
        self.pushButton_38.setObjectName(u"pushButton_38")

        self.horizontalLayout_20.addWidget(self.pushButton_38)


        self.gridLayout_6.addWidget(self.groupBox_3, 3, 0, 1, 1)

        self.widget_10 = QWidget(self.space_main_3)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy)
        self.horizontalLayout_19 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_7)

        self.groupBox_12 = QGroupBox(self.widget_10)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.gridLayout_8 = QGridLayout(self.groupBox_12)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.groupBox_12)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(460, 460))
        self.label_28.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_8.addWidget(self.label_28, 0, 0, 1, 1)


        self.horizontalLayout_19.addWidget(self.groupBox_12)

        self.horizontalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_8)

        self.groupBox_13 = QGroupBox(self.widget_10)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.gridLayout_9 = QGridLayout(self.groupBox_13)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.groupBox_13)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(460, 460))
        self.label_29.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.label_29, 0, 0, 1, 1)


        self.horizontalLayout_19.addWidget(self.groupBox_13)

        self.horizontalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_9)


        self.gridLayout_6.addWidget(self.widget_10, 1, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_11, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.space_main_3)
        self.space_main_4 = QWidget()
        self.space_main_4.setObjectName(u"space_main_4")
        sizePolicy.setHeightForWidth(self.space_main_4.sizePolicy().hasHeightForWidth())
        self.space_main_4.setSizePolicy(sizePolicy)
        self.gridLayout_13 = QGridLayout(self.space_main_4)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.groupBox_4 = QGroupBox(self.space_main_4)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 100))
        self.groupBox_4.setMaximumSize(QSize(16777215, 130))
        self.groupBox_4.setFont(font2)
        self.gridLayout_12 = QGridLayout(self.groupBox_4)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_42 = QLabel(self.groupBox_4)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_21.addWidget(self.label_42)

        self.horizontalSlider_10 = QSlider(self.groupBox_4)
        self.horizontalSlider_10.setObjectName(u"horizontalSlider_10")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.horizontalSlider_10.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_10.setSizePolicy(sizePolicy9)
        self.horizontalSlider_10.setOrientation(Qt.Horizontal)

        self.horizontalLayout_21.addWidget(self.horizontalSlider_10)


        self.verticalLayout_19.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_43 = QLabel(self.groupBox_4)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_22.addWidget(self.label_43)

        self.horizontalSlider_11 = QSlider(self.groupBox_4)
        self.horizontalSlider_11.setObjectName(u"horizontalSlider_11")
        sizePolicy9.setHeightForWidth(self.horizontalSlider_11.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_11.setSizePolicy(sizePolicy9)
        self.horizontalSlider_11.setOrientation(Qt.Horizontal)

        self.horizontalLayout_22.addWidget(self.horizontalSlider_11)


        self.verticalLayout_19.addLayout(self.horizontalLayout_22)


        self.gridLayout_12.addLayout(self.verticalLayout_19, 0, 0, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.pushButton_39 = QPushButton(self.groupBox_4)
        self.pushButton_39.setObjectName(u"pushButton_39")
        icon20 = QIcon()
        icon20.addFile(u":/icon/icons/Picture-Landscape--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_39.setIcon(icon20)

        self.verticalLayout_18.addWidget(self.pushButton_39)

        self.pushButton_40 = QPushButton(self.groupBox_4)
        self.pushButton_40.setObjectName(u"pushButton_40")
        icon21 = QIcon()
        icon21.addFile(u":/icon/icons/Binocular--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_40.setIcon(icon21)

        self.verticalLayout_18.addWidget(self.pushButton_40)


        self.gridLayout_12.addLayout(self.verticalLayout_18, 0, 2, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_10, 0, 3, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_11, 0, 1, 1, 1)


        self.gridLayout_13.addWidget(self.groupBox_4, 4, 0, 1, 1)

        self.widget_14 = QWidget(self.space_main_4)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy)
        self.widget_14.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_36 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.pushButton_51 = QPushButton(self.widget_14)
        self.pushButton_51.setObjectName(u"pushButton_51")
        self.pushButton_51.setMinimumSize(QSize(0, 15))
        self.pushButton_51.setMaximumSize(QSize(120, 16777215))
        self.pushButton_51.setFont(font2)
        self.pushButton_51.setIcon(icon9)
        self.pushButton_51.setIconSize(QSize(24, 24))

        self.horizontalLayout_36.addWidget(self.pushButton_51)

        self.label_33 = QLabel(self.widget_14)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font3)
        self.label_33.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_33)


        self.gridLayout_13.addWidget(self.widget_14, 0, 0, 1, 1)

        self.widget_15 = QWidget(self.space_main_4)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(0, 0))
        self.widget_15.setMaximumSize(QSize(16777215, 1200))
        self.gridLayout_17 = QGridLayout(self.widget_15)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_34 = QLabel(self.widget_15)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(16777215, 20))
        self.label_34.setFont(font2)
        self.label_34.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_34)

        self.widget_16 = QWidget(self.widget_15)
        self.widget_16.setObjectName(u"widget_16")
        sizePolicy.setHeightForWidth(self.widget_16.sizePolicy().hasHeightForWidth())
        self.widget_16.setSizePolicy(sizePolicy)
        self.gridLayout_11 = QGridLayout(self.widget_16)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_12, 0, 0, 1, 1)

        self.label_35 = QLabel(self.widget_16)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_11.addWidget(self.label_35, 0, 1, 2, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_13, 1, 2, 1, 1)


        self.verticalLayout_14.addWidget(self.widget_16)


        self.gridLayout_17.addLayout(self.verticalLayout_14, 0, 0, 1, 1)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_36 = QLabel(self.widget_15)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(16777215, 20))
        self.label_36.setFont(font2)
        self.label_36.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_36)

        self.widget_17 = QWidget(self.widget_15)
        self.widget_17.setObjectName(u"widget_17")
        sizePolicy.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy)
        self.gridLayout_14 = QGridLayout(self.widget_17)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_14, 0, 0, 1, 1)

        self.label_37 = QLabel(self.widget_17)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_14.addWidget(self.label_37, 0, 1, 2, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_15, 1, 2, 1, 1)


        self.verticalLayout_15.addWidget(self.widget_17)


        self.gridLayout_17.addLayout(self.verticalLayout_15, 0, 1, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_38 = QLabel(self.widget_15)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(16777215, 20))
        self.label_38.setFont(font2)
        self.label_38.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_38)

        self.widget_18 = QWidget(self.widget_15)
        self.widget_18.setObjectName(u"widget_18")
        sizePolicy.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy)
        self.gridLayout_15 = QGridLayout(self.widget_18)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_16, 0, 0, 1, 1)

        self.label_39 = QLabel(self.widget_18)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_15.addWidget(self.label_39, 0, 1, 2, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_17, 1, 2, 1, 1)


        self.verticalLayout_16.addWidget(self.widget_18)


        self.gridLayout_17.addLayout(self.verticalLayout_16, 1, 0, 1, 1)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_40 = QLabel(self.widget_15)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(16777215, 20))
        self.label_40.setFont(font2)
        self.label_40.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_40)

        self.widget_19 = QWidget(self.widget_15)
        self.widget_19.setObjectName(u"widget_19")
        sizePolicy.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy)
        self.gridLayout_16 = QGridLayout(self.widget_19)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_18, 0, 0, 1, 1)

        self.label_41 = QLabel(self.widget_19)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_16.addWidget(self.label_41, 0, 1, 2, 1)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_19, 1, 2, 1, 1)


        self.verticalLayout_17.addWidget(self.widget_19)


        self.gridLayout_17.addLayout(self.verticalLayout_17, 1, 1, 1, 1)


        self.gridLayout_13.addWidget(self.widget_15, 2, 0, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_12, 3, 0, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_18, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.space_main_4)
        self.space_main_5 = QWidget()
        self.space_main_5.setObjectName(u"space_main_5")
        sizePolicy.setHeightForWidth(self.space_main_5.sizePolicy().hasHeightForWidth())
        self.space_main_5.setSizePolicy(sizePolicy)
        self.gridLayout_21 = QGridLayout(self.space_main_5)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.widget_20 = QWidget(self.space_main_5)
        self.widget_20.setObjectName(u"widget_20")
        sizePolicy4.setHeightForWidth(self.widget_20.sizePolicy().hasHeightForWidth())
        self.widget_20.setSizePolicy(sizePolicy4)
        self.horizontalLayout_37 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.pushButton_52 = QPushButton(self.widget_20)
        self.pushButton_52.setObjectName(u"pushButton_52")
        sizePolicy4.setHeightForWidth(self.pushButton_52.sizePolicy().hasHeightForWidth())
        self.pushButton_52.setSizePolicy(sizePolicy4)
        self.pushButton_52.setMinimumSize(QSize(0, 15))
        self.pushButton_52.setMaximumSize(QSize(120, 16777215))
        self.pushButton_52.setFont(font2)
        self.pushButton_52.setIcon(icon9)
        self.pushButton_52.setIconSize(QSize(24, 24))

        self.horizontalLayout_37.addWidget(self.pushButton_52)

        self.label_48 = QLabel(self.widget_20)
        self.label_48.setObjectName(u"label_48")
        sizePolicy9.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy9)
        self.label_48.setFont(font3)
        self.label_48.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_48)


        self.gridLayout_21.addWidget(self.widget_20, 0, 0, 1, 1)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_23.setContentsMargins(-1, -1, 25, -1)
        self.groupBox_5 = QGroupBox(self.space_main_5)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setFont(font2)
        self.gridLayout_18 = QGridLayout(self.groupBox_5)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.horizontalSpacer_20 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_20, 0, 2, 1, 1)

        self.listWidget = QListWidget(self.groupBox_5)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QSize(350, 0))

        self.gridLayout_18.addWidget(self.listWidget, 0, 0, 1, 1)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalSpacer_13 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_13)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(20)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setSizeConstraint(QLayout.SetMinimumSize)
        self.pushButton_41 = QPushButton(self.groupBox_5)
        self.pushButton_41.setObjectName(u"pushButton_41")
        sizePolicy2.setHeightForWidth(self.pushButton_41.sizePolicy().hasHeightForWidth())
        self.pushButton_41.setSizePolicy(sizePolicy2)
        icon22 = QIcon()
        icon22.addFile(u":/icon/icons/Navigation-Arrows-Up-1--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_41.setIcon(icon22)

        self.verticalLayout_20.addWidget(self.pushButton_41)

        self.pushButton_42 = QPushButton(self.groupBox_5)
        self.pushButton_42.setObjectName(u"pushButton_42")
        sizePolicy2.setHeightForWidth(self.pushButton_42.sizePolicy().hasHeightForWidth())
        self.pushButton_42.setSizePolicy(sizePolicy2)
        icon23 = QIcon()
        icon23.addFile(u":/icon/icons/Navigation-Arrows-Down-1--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_42.setIcon(icon23)

        self.verticalLayout_20.addWidget(self.pushButton_42)


        self.verticalLayout_21.addLayout(self.verticalLayout_20)

        self.verticalSpacer_14 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_14)


        self.gridLayout_18.addLayout(self.verticalLayout_21, 0, 1, 1, 1)


        self.horizontalLayout_23.addWidget(self.groupBox_5)

        self.widget_22 = QWidget(self.space_main_5)
        self.widget_22.setObjectName(u"widget_22")
        sizePolicy.setHeightForWidth(self.widget_22.sizePolicy().hasHeightForWidth())
        self.widget_22.setSizePolicy(sizePolicy)
        self.widget_22.setMinimumSize(QSize(500, 0))
        self.gridLayout_19 = QGridLayout(self.widget_22)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_46 = QLabel(self.widget_22)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(16777215, 30))
        self.label_46.setFont(font2)

        self.verticalLayout_22.addWidget(self.label_46)

        self.label_44 = QLabel(self.widget_22)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_22.addWidget(self.label_44)


        self.gridLayout_19.addLayout(self.verticalLayout_22, 0, 0, 1, 1)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_47 = QLabel(self.widget_22)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMaximumSize(QSize(16777215, 30))
        self.label_47.setFont(font2)

        self.verticalLayout_23.addWidget(self.label_47)

        self.label_45 = QLabel(self.widget_22)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_23.addWidget(self.label_45)


        self.gridLayout_19.addLayout(self.verticalLayout_23, 1, 0, 1, 1)


        self.horizontalLayout_23.addWidget(self.widget_22)


        self.gridLayout_21.addLayout(self.horizontalLayout_23, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.space_main_5)
        self.space_main_6 = QWidget()
        self.space_main_6.setObjectName(u"space_main_6")
        self.gridLayout_30 = QGridLayout(self.space_main_6)
        self.gridLayout_30.setSpacing(0)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.widget_21 = QWidget(self.space_main_6)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_38 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.pushButton_53 = QPushButton(self.widget_21)
        self.pushButton_53.setObjectName(u"pushButton_53")
        self.pushButton_53.setMinimumSize(QSize(0, 15))
        self.pushButton_53.setMaximumSize(QSize(120, 16777215))
        self.pushButton_53.setFont(font2)
        self.pushButton_53.setIcon(icon9)
        self.pushButton_53.setIconSize(QSize(24, 24))

        self.horizontalLayout_38.addWidget(self.pushButton_53)

        self.label_49 = QLabel(self.widget_21)
        self.label_49.setObjectName(u"label_49")
        sizePolicy9.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy9)
        self.label_49.setFont(font3)
        self.label_49.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.label_49)


        self.gridLayout_30.addWidget(self.widget_21, 0, 0, 1, 1)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.widget_23 = QWidget(self.space_main_6)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setMaximumSize(QSize(400, 16777215))
        self.horizontalLayout_24 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.groupBox_6 = QGroupBox(self.widget_23)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setFont(font2)
        self.gridLayout_29 = QGridLayout(self.groupBox_6)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.listWidget_2 = QListWidget(self.groupBox_6)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setMinimumSize(QSize(300, 0))

        self.gridLayout_29.addWidget(self.listWidget_2, 0, 0, 1, 1)


        self.horizontalLayout_24.addWidget(self.groupBox_6)

        self.horizontalSpacer_22 = QSpacerItem(21, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_22)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_15)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setSpacing(20)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.pushButton_43 = QPushButton(self.widget_23)
        self.pushButton_43.setObjectName(u"pushButton_43")
        sizePolicy2.setHeightForWidth(self.pushButton_43.sizePolicy().hasHeightForWidth())
        self.pushButton_43.setSizePolicy(sizePolicy2)
        self.pushButton_43.setIcon(icon22)

        self.verticalLayout_24.addWidget(self.pushButton_43)

        self.pushButton_44 = QPushButton(self.widget_23)
        self.pushButton_44.setObjectName(u"pushButton_44")
        sizePolicy2.setHeightForWidth(self.pushButton_44.sizePolicy().hasHeightForWidth())
        self.pushButton_44.setSizePolicy(sizePolicy2)
        self.pushButton_44.setIcon(icon23)

        self.verticalLayout_24.addWidget(self.pushButton_44)


        self.verticalLayout_25.addLayout(self.verticalLayout_24)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_16)


        self.horizontalLayout_24.addLayout(self.verticalLayout_25)

        self.horizontalSpacer_23 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_23)


        self.horizontalLayout_29.addWidget(self.widget_23)

        self.widget_24 = QWidget(self.space_main_6)
        self.widget_24.setObjectName(u"widget_24")
        self.gridLayout_28 = QGridLayout(self.widget_24)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.groupBox_7 = QGroupBox(self.widget_24)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setFont(font2)
        self.gridLayout_23 = QGridLayout(self.groupBox_7)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_50 = QLabel(self.groupBox_7)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_23.addWidget(self.label_50, 0, 0, 1, 1)


        self.horizontalLayout_28.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.widget_24)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setFont(font2)
        self.gridLayout_24 = QGridLayout(self.groupBox_8)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_51 = QLabel(self.groupBox_8)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_24.addWidget(self.label_51, 0, 0, 1, 1)


        self.horizontalLayout_28.addWidget(self.groupBox_8)


        self.gridLayout_28.addLayout(self.horizontalLayout_28, 0, 0, 1, 1)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.groupBox_9 = QGroupBox(self.widget_24)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setFont(font2)
        self.gridLayout_25 = QGridLayout(self.groupBox_9)
        self.gridLayout_25.setSpacing(0)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_52 = QLabel(self.groupBox_9)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_25.addWidget(self.label_52, 0, 0, 1, 1)


        self.horizontalLayout_27.addWidget(self.groupBox_9)

        self.groupBox_10 = QGroupBox(self.widget_24)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setFont(font2)
        self.gridLayout_26 = QGridLayout(self.groupBox_10)
        self.gridLayout_26.setSpacing(0)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_53 = QLabel(self.groupBox_10)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_26.addWidget(self.label_53, 0, 0, 1, 1)


        self.horizontalLayout_27.addWidget(self.groupBox_10)


        self.gridLayout_28.addLayout(self.horizontalLayout_27, 1, 0, 1, 1)

        self.verticalSpacer_17 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_28.addItem(self.verticalSpacer_17, 2, 0, 1, 1)

        self.widget_25 = QWidget(self.widget_24)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setMaximumSize(QSize(16777215, 50))
        self.gridLayout_27 = QGridLayout(self.widget_25)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalSpacer_24 = QSpacerItem(40, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.pushButton_45 = QPushButton(self.widget_25)
        self.pushButton_45.setObjectName(u"pushButton_45")
        sizePolicy2.setHeightForWidth(self.pushButton_45.sizePolicy().hasHeightForWidth())
        self.pushButton_45.setSizePolicy(sizePolicy2)
        icon24 = QIcon()
        icon24.addFile(u":/icon/icons/Navigation-Arrows-Left-1--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_45.setIcon(icon24)

        self.horizontalLayout_25.addWidget(self.pushButton_45)

        self.pushButton_46 = QPushButton(self.widget_25)
        self.pushButton_46.setObjectName(u"pushButton_46")
        sizePolicy2.setHeightForWidth(self.pushButton_46.sizePolicy().hasHeightForWidth())
        self.pushButton_46.setSizePolicy(sizePolicy2)
        icon25 = QIcon()
        icon25.addFile(u":/icon/icons/Navigation-Arrows-Right-1--Streamline-Ultimate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_46.setIcon(icon25)

        self.horizontalLayout_25.addWidget(self.pushButton_46)


        self.horizontalLayout_26.addLayout(self.horizontalLayout_25)

        self.horizontalSpacer_25 = QSpacerItem(40, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_25)


        self.gridLayout_27.addLayout(self.horizontalLayout_26, 0, 0, 1, 1)


        self.gridLayout_28.addWidget(self.widget_25, 3, 0, 1, 1)


        self.horizontalLayout_29.addWidget(self.widget_24)


        self.gridLayout_30.addLayout(self.horizontalLayout_29, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.space_main_6)
        self.space_main_7 = QWidget()
        self.space_main_7.setObjectName(u"space_main_7")
        self.gridLayout_32 = QGridLayout(self.space_main_7)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.widget_26 = QWidget(self.space_main_7)
        self.widget_26.setObjectName(u"widget_26")
        sizePolicy.setHeightForWidth(self.widget_26.sizePolicy().hasHeightForWidth())
        self.widget_26.setSizePolicy(sizePolicy)
        self.widget_26.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_39 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.pushButton_54 = QPushButton(self.widget_26)
        self.pushButton_54.setObjectName(u"pushButton_54")
        sizePolicy.setHeightForWidth(self.pushButton_54.sizePolicy().hasHeightForWidth())
        self.pushButton_54.setSizePolicy(sizePolicy)
        self.pushButton_54.setMinimumSize(QSize(0, 15))
        self.pushButton_54.setMaximumSize(QSize(120, 16777215))
        self.pushButton_54.setFont(font2)
        self.pushButton_54.setIcon(icon9)
        self.pushButton_54.setIconSize(QSize(24, 24))

        self.horizontalLayout_39.addWidget(self.pushButton_54)

        self.label_54 = QLabel(self.widget_26)
        self.label_54.setObjectName(u"label_54")
        sizePolicy9.setHeightForWidth(self.label_54.sizePolicy().hasHeightForWidth())
        self.label_54.setSizePolicy(sizePolicy9)
        self.label_54.setMinimumSize(QSize(0, 50))
        self.label_54.setFont(font3)
        self.label_54.setFrameShadow(QFrame.Plain)
        self.label_54.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.label_54)


        self.gridLayout_32.addWidget(self.widget_26, 0, 0, 1, 1)

        self.widget_27 = QWidget(self.space_main_7)
        self.widget_27.setObjectName(u"widget_27")
        self.horizontalLayout_32 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalSpacer_28 = QSpacerItem(311, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_28)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_55 = QLabel(self.widget_27)
        self.label_55.setObjectName(u"label_55")
        sizePolicy.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy)
        self.label_55.setFont(font2)

        self.verticalLayout_26.addWidget(self.label_55)

        self.label_56 = QLabel(self.widget_27)
        self.label_56.setObjectName(u"label_56")
        sizePolicy.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy)
        self.label_56.setFont(font2)

        self.verticalLayout_26.addWidget(self.label_56)


        self.horizontalLayout_32.addLayout(self.verticalLayout_26)

        self.horizontalSpacer_29 = QSpacerItem(311, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_29)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setSpacing(6)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_57 = QLabel(self.widget_27)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font2)

        self.horizontalLayout_30.addWidget(self.label_57)

        self.lineEdit = QLineEdit(self.widget_27)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy9.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy9)

        self.horizontalLayout_30.addWidget(self.lineEdit)


        self.verticalLayout_27.addLayout(self.horizontalLayout_30)

        self.label_58 = QLabel(self.widget_27)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font2)

        self.verticalLayout_27.addWidget(self.label_58)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setSizeConstraint(QLayout.SetMinimumSize)
        self.pushButton_47 = QPushButton(self.widget_27)
        self.pushButton_47.setObjectName(u"pushButton_47")
        sizePolicy9.setHeightForWidth(self.pushButton_47.sizePolicy().hasHeightForWidth())
        self.pushButton_47.setSizePolicy(sizePolicy9)
        self.pushButton_47.setFont(font2)

        self.horizontalLayout_31.addWidget(self.pushButton_47)

        self.pushButton_48 = QPushButton(self.widget_27)
        self.pushButton_48.setObjectName(u"pushButton_48")
        sizePolicy9.setHeightForWidth(self.pushButton_48.sizePolicy().hasHeightForWidth())
        self.pushButton_48.setSizePolicy(sizePolicy9)
        self.pushButton_48.setFont(font2)

        self.horizontalLayout_31.addWidget(self.pushButton_48)


        self.verticalLayout_27.addLayout(self.horizontalLayout_31)

        self.checkBox = QCheckBox(self.widget_27)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy2.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy2)
        self.checkBox.setFont(font2)

        self.verticalLayout_27.addWidget(self.checkBox)


        self.horizontalLayout_32.addLayout(self.verticalLayout_27)

        self.horizontalSpacer_30 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_30)


        self.gridLayout_32.addWidget(self.widget_27, 1, 0, 1, 1)

        self.groupBox_11 = QGroupBox(self.space_main_7)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.groupBox_11.setFont(font4)
        self.groupBox_11.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_33 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_26 = QSpacerItem(278, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_26)

        self.tableWidget = QTableWidget(self.groupBox_11)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(600, 0))

        self.horizontalLayout_33.addWidget(self.tableWidget)

        self.horizontalSpacer_27 = QSpacerItem(279, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_27)


        self.gridLayout_32.addWidget(self.groupBox_11, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.space_main_7)
        self.space_main_8 = QWidget()
        self.space_main_8.setObjectName(u"space_main_8")
        sizePolicy.setHeightForWidth(self.space_main_8.sizePolicy().hasHeightForWidth())
        self.space_main_8.setSizePolicy(sizePolicy)
        self.gridLayout_33 = QGridLayout(self.space_main_8)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.textEdit = QTextEdit(self.space_main_8)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(False)

        self.gridLayout_33.addWidget(self.textEdit, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.space_main_8)

        self.horizontalLayout_6.addWidget(self.stackedWidget)


        self.horizontalLayout_40.addWidget(self.widget)


        self.gridLayout_10.addLayout(self.horizontalLayout_40, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_3.toggled.connect(self.pushButton_18.setChecked)
        self.pushButton_18.toggled.connect(self.pushButton_3.setChecked)
        self.pushButton_4.toggled.connect(self.pushButton_17.setChecked)
        self.pushButton_17.toggled.connect(self.pushButton_4.setChecked)
        self.pushButton_5.toggled.connect(self.pushButton_16.setChecked)
        self.pushButton_16.toggled.connect(self.pushButton_5.setChecked)
        self.pushButton_6.toggled.connect(self.pushButton_15.setChecked)
        self.pushButton_15.toggled.connect(self.pushButton_6.setChecked)
        self.pushButton_7.toggled.connect(self.pushButton_14.setChecked)
        self.pushButton_14.toggled.connect(self.pushButton_7.setChecked)
        self.pushButton.toggled.connect(self.pushButton_13.setChecked)
        self.pushButton_13.toggled.connect(self.pushButton.setChecked)
        self.pushButton_8.toggled.connect(self.pushButton_12.setChecked)
        self.pushButton_12.toggled.connect(self.pushButton_8.setChecked)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"PRONICS PRECISION AUTOMATION", None))
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Disk:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"RAM:", None))
        self.label.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.pushButton.setText("")
        self.pushButton_8.setText("")
        self.pushButton_9.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"M\u1edf r\u1ed9ng", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Cam 1", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"4 Cam", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"NG 1 cam", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"NG 4 cam", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"S\u1ea3n l\u01b0\u1ee3ng", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Screenshot", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Th\u00f4ng tin", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Tho\u00e1t", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Cam 1", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"T\u00f9y ch\u1ec9nh", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"NG", None))
        self.label_9.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"H\u00ecnh \u1ea3nh Cam", None))
        self.label_10.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"K\u1ebft qu\u1ea3 tr\u1ea3 v\u1ec1", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ee5p", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"L\u01b0u gi\u00e1 tr\u1ecb", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"L\u1ea5y m\u1eabu", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"Calib", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn k\u1ebft qu\u1ea3 tr\u1ea3 v\u1ec1", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"B\u1ea3ng \u0111i\u1ec1u khi\u1ec3n", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"H cao", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"S cao", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"V cao", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ed9 s\u00e1ng", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Ph\u1ea7n tr\u0103m ng\u01b0\u1ee1ng ", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"H th\u1ea5p", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"S th\u1ea5p", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"V  th\u1ea5p", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ed9 t\u01b0\u01a1ng ph\u1ea3n", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Gi\u00e1 tr\u1ecb hi\u1ec7n t\u1ea1i", None))
        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"T\u00f9y ch\u1ec9nh", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"M\u00e0n h\u00ecnh Calib", None))
        self.label_27.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"B\u1ea3ng \u0111i\u1ec1u khi\u1ec3n", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ee5p \u1ea3nh ", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"Calib camera", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"Clear m\u1eabu", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"V\u1ec1 m\u00e0n h\u00ecnh ch\u00ednh", None))
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"T\u00f9y ch\u1ec9nh", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"M\u00e0n h\u00ecnh l\u1ea5y m\u1eabu", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"B\u1ea3ng \u0111i\u1ec1u khi\u1ec3n", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ee5p \u1ea3nh ", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"L\u1ea5y m\u1eabu", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a m\u1eabu", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"V\u1ec1 m\u00e0n h\u00ecnh ch\u00ednh", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"\u1ea2nh ch\u1ee5p", None))
        self.label_28.setText("")
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"\u1ea2nh m\u1eabu", None))
        self.label_29.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"B\u1ea3ng \u0111i\u1ec1u khi\u1ec3n", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Ng\u01b0\u1ee1ng AI:", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Gi\u1edbi h\u1ea1n v\u00f9ng NG:", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"H\u00ecnh \u1ea3nh th\u1ef1c t\u1ebf", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"K\u1ebft qu\u1ea3", None))
        self.pushButton_51.setText(QCoreApplication.translate("MainWindow", u"T\u00f9y ch\u1ec9nh", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"4 Cam", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"M\u00e0n h\u00ecnh 1 ", None))
        self.label_35.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"M\u00e0n h\u00ecnh 3", None))
        self.label_37.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"M\u00e0n h\u00ecnh 2", None))
        self.label_39.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"M\u00e0n h\u00ecnh 4", None))
        self.label_41.setText("")
        self.pushButton_52.setText(QCoreApplication.translate("MainWindow", u"T\u00f9y ch\u1ec9nh", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"NG 1 Cam", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Danh s\u00e1ch h\u00e0ng NG", None))
        self.pushButton_41.setText("")
        self.pushButton_42.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"H\u00ecnh \u1ea3nh th\u1ef1c t\u1ebf ", None))
        self.label_44.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"K\u1ebft qu\u1ea3", None))
        self.label_45.setText("")
        self.pushButton_53.setText(QCoreApplication.translate("MainWindow", u"T\u00f9y ch\u1ec9nh", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"NG 4 Cam", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Danh s\u00e1ch h\u00e0ng NG", None))
        self.pushButton_43.setText("")
        self.pushButton_44.setText("")
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"M\u00e0n h\u00ecnh 1", None))
        self.label_50.setText("")
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"M\u00e0n h\u00ecnh 3", None))
        self.label_51.setText("")
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"M\u00e0n h\u00ecnh 2", None))
        self.label_52.setText("")
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"M\u00e0n h\u00ecnh 4", None))
        self.label_53.setText("")
        self.pushButton_45.setText("")
        self.pushButton_46.setText("")
        self.pushButton_54.setText(QCoreApplication.translate("MainWindow", u"T\u00f9y ch\u1ec9nh", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"S\u1ea3n l\u01b0\u1ee3ng", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"T\u1eeb ng\u00e0y:", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ebfn ng\u00e0y:", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp gi\u00e1 tr\u1ecb 1 set:", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Gi\u00e1 tr\u1ecb hi\u1ec7n t\u1ea1i:", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"B\u1eaft \u0111\u1ea7u ", None))
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"L\u01b0u gi\u00e1 tr\u1ecb", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"T\u1ef1 \u0111\u1ed9ng l\u01b0u s\u1ea3n l\u01b0\u1ee3ng ng\u00e0y", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"B\u1ea3ng theo d\u00f5i s\u1ea3n l\u01b0\u1ee3ng", None))
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
    # retranslateUi

