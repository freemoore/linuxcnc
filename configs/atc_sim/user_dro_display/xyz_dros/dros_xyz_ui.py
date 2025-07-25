# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/buildbot/buildbot/worker/probe_basic-dev/sources/debian/python3-probe-basic/usr/share/configs/atc_sim/user_dro_display/xyz_dros/dros_xyz.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dros_xyz(object):
    def setupUi(self, dros_xyz):
        dros_xyz.setObjectName("dros_xyz")
        dros_xyz.resize(469, 286)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dros_xyz.sizePolicy().hasHeightForWidth())
        dros_xyz.setSizePolicy(sizePolicy)
        dros_xyz.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalLayout = QtWidgets.QVBoxLayout(dros_xyz)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_xyz = QtWidgets.QWidget(dros_xyz)
        self.widget_xyz.setObjectName("widget_xyz")
        self.verticalLayout_55 = QtWidgets.QVBoxLayout(self.widget_xyz)
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_55.setSpacing(19)
        self.verticalLayout_55.setObjectName("verticalLayout_55")
        self.horizontalLayout_81 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_81.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_81.setSpacing(8)
        self.horizontalLayout_81.setObjectName("horizontalLayout_81")
        self.frame = QtWidgets.QFrame(self.widget_xyz)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 40))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame.setStyleSheet(".QFrame{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179,172);\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    background-color: rgb(90, 90, 90);\n"
"    padding: -5px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_136 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_136.setContentsMargins(15, -1, 20, -1)
        self.horizontalLayout_136.setSpacing(8)
        self.horizontalLayout_136.setObjectName("horizontalLayout_136")
        self.axis_column_header = StatusLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axis_column_header.sizePolicy().hasHeightForWidth())
        self.axis_column_header.setSizePolicy(sizePolicy)
        self.axis_column_header.setMinimumSize(QtCore.QSize(60, 17))
        self.axis_column_header.setMaximumSize(QtCore.QSize(60, 17))
        self.axis_column_header.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 16pt \"Bebas Kai\";\n"
"    padding-left: 1px;\n"
"    padding-right: 20px;\n"
"}")
        self.axis_column_header.setAlignment(QtCore.Qt.AlignCenter)
        self.axis_column_header.setObjectName("axis_column_header")
        self.horizontalLayout_136.addWidget(self.axis_column_header)
        self.work_column_header = StatusLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.work_column_header.sizePolicy().hasHeightForWidth())
        self.work_column_header.setSizePolicy(sizePolicy)
        self.work_column_header.setMinimumSize(QtCore.QSize(100, 17))
        self.work_column_header.setMaximumSize(QtCore.QSize(100, 17))
        self.work_column_header.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 16pt \"Bebas Kai\";\n"
"    padding-left: 6px;\n"
"}")
        self.work_column_header.setAlignment(QtCore.Qt.AlignCenter)
        self.work_column_header.setObjectName("work_column_header")
        self.horizontalLayout_136.addWidget(self.work_column_header)
        self.machine_column_header = QtWidgets.QLabel(self.frame)
        self.machine_column_header.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.machine_column_header.sizePolicy().hasHeightForWidth())
        self.machine_column_header.setSizePolicy(sizePolicy)
        self.machine_column_header.setMinimumSize(QtCore.QSize(100, 17))
        self.machine_column_header.setMaximumSize(QtCore.QSize(100, 17))
        self.machine_column_header.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.machine_column_header.setAlignment(QtCore.Qt.AlignCenter)
        self.machine_column_header.setObjectName("machine_column_header")
        self.horizontalLayout_136.addWidget(self.machine_column_header)
        self.dtg_column_header = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dtg_column_header.sizePolicy().hasHeightForWidth())
        self.dtg_column_header.setSizePolicy(sizePolicy)
        self.dtg_column_header.setMinimumSize(QtCore.QSize(100, 17))
        self.dtg_column_header.setMaximumSize(QtCore.QSize(100, 17))
        self.dtg_column_header.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.dtg_column_header.setAlignment(QtCore.Qt.AlignCenter)
        self.dtg_column_header.setObjectName("dtg_column_header")
        self.horizontalLayout_136.addWidget(self.dtg_column_header)
        self.ref_column_header = StatusLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ref_column_header.sizePolicy().hasHeightForWidth())
        self.ref_column_header.setSizePolicy(sizePolicy)
        self.ref_column_header.setMinimumSize(QtCore.QSize(40, 17))
        self.ref_column_header.setMaximumSize(QtCore.QSize(40, 17))
        self.ref_column_header.setStyleSheet("QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"    font: 16pt \"Bebas Kai\";\n"
"    padding-left: 6px;\n"
"}")
        self.ref_column_header.setAlignment(QtCore.Qt.AlignCenter)
        self.ref_column_header.setObjectName("ref_column_header")
        self.horizontalLayout_136.addWidget(self.ref_column_header)
        self.horizontalLayout_81.addWidget(self.frame)
        self.verticalLayout_55.addLayout(self.horizontalLayout_81)
        self.x_axis_dro_layout = QtWidgets.QHBoxLayout()
        self.x_axis_dro_layout.setContentsMargins(1, 1, 1, 1)
        self.x_axis_dro_layout.setSpacing(7)
        self.x_axis_dro_layout.setObjectName("x_axis_dro_layout")
        self.zero_x_button = MDIButton(self.widget_xyz)
        self.zero_x_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zero_x_button.sizePolicy().hasHeightForWidth())
        self.zero_x_button.setSizePolicy(sizePolicy)
        self.zero_x_button.setMinimumSize(QtCore.QSize(60, 40))
        self.zero_x_button.setMaximumSize(QtCore.QSize(60, 40))
        self.zero_x_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.zero_x_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.zero_x_button.setStyleSheet("MDIButton {\n"
"       font: 17pt \"Bebas Kai\";\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/zero.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zero_x_button.setIcon(icon)
        self.zero_x_button.setIconSize(QtCore.QSize(20, 20))
        self.zero_x_button.setObjectName("zero_x_button")
        self.x_axis_dro_layout.addWidget(self.zero_x_button)
        self.drowidget_x = DROLineEdit(self.widget_xyz)
        self.drowidget_x.setMinimumSize(QtCore.QSize(100, 35))
        self.drowidget_x.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.drowidget_x.setFont(font)
        self.drowidget_x.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.drowidget_x.setStyleSheet("QLineEdit{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    padding-right: 2px;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.drowidget_x.setCursorPosition(10)
        self.drowidget_x.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drowidget_x.setProperty("referenceType", 1)
        self.drowidget_x.setProperty("axisNumber", 0)
        self.drowidget_x.setProperty("latheMode", 0)
        self.drowidget_x.setObjectName("drowidget_x")
        self.x_axis_dro_layout.addWidget(self.drowidget_x)
        self.drolabel_machine_x = DROLabel(self.widget_xyz)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drolabel_machine_x.sizePolicy().hasHeightForWidth())
        self.drolabel_machine_x.setSizePolicy(sizePolicy)
        self.drolabel_machine_x.setMinimumSize(QtCore.QSize(100, 35))
        self.drolabel_machine_x.setMaximumSize(QtCore.QSize(100, 35))
        self.drolabel_machine_x.setStyleSheet("QLabel{\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}\n"
"\n"
"QLabel[style=\"unhomed\"]{\n"
"   color: red;\n"
"}\n"
"\n"
"QLabel[style=\"homing\"]{\n"
"   color: rgb(196, 160, 0);\n"
"}")
        self.drolabel_machine_x.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drolabel_machine_x.setProperty("referenceType", 0)
        self.drolabel_machine_x.setProperty("axisNumber", 0)
        self.drolabel_machine_x.setProperty("latheMode", 0)
        self.drolabel_machine_x.setObjectName("drolabel_machine_x")
        self.x_axis_dro_layout.addWidget(self.drolabel_machine_x)
        self.drolabel_dtg_x = DROLabel(self.widget_xyz)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drolabel_dtg_x.sizePolicy().hasHeightForWidth())
        self.drolabel_dtg_x.setSizePolicy(sizePolicy)
        self.drolabel_dtg_x.setMinimumSize(QtCore.QSize(100, 35))
        self.drolabel_dtg_x.setMaximumSize(QtCore.QSize(100, 35))
        self.drolabel_dtg_x.setStyleSheet("QLabel{\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}")
        self.drolabel_dtg_x.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drolabel_dtg_x.setProperty("referenceType", 2)
        self.drolabel_dtg_x.setProperty("axisNumber", 0)
        self.drolabel_dtg_x.setProperty("latheMode", 0)
        self.drolabel_dtg_x.setObjectName("drolabel_dtg_x")
        self.x_axis_dro_layout.addWidget(self.drolabel_dtg_x)
        self.ref_x_button = ActionButton(self.widget_xyz)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ref_x_button.sizePolicy().hasHeightForWidth())
        self.ref_x_button.setSizePolicy(sizePolicy)
        self.ref_x_button.setMinimumSize(QtCore.QSize(62, 40))
        self.ref_x_button.setMaximumSize(QtCore.QSize(62, 40))
        self.ref_x_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ref_x_button.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.ref_x_button.setObjectName("ref_x_button")
        self.x_axis_dro_layout.addWidget(self.ref_x_button)
        self.verticalLayout_55.addLayout(self.x_axis_dro_layout)
        self.y_axis_dro_layout = QtWidgets.QHBoxLayout()
        self.y_axis_dro_layout.setContentsMargins(1, 1, 1, 1)
        self.y_axis_dro_layout.setSpacing(7)
        self.y_axis_dro_layout.setObjectName("y_axis_dro_layout")
        self.zero_y_button = MDIButton(self.widget_xyz)
        self.zero_y_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zero_y_button.sizePolicy().hasHeightForWidth())
        self.zero_y_button.setSizePolicy(sizePolicy)
        self.zero_y_button.setMinimumSize(QtCore.QSize(60, 40))
        self.zero_y_button.setMaximumSize(QtCore.QSize(60, 40))
        self.zero_y_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.zero_y_button.setStyleSheet("MDIButton {\n"
"       font: 17pt \"Bebas Kai\";\n"
"}")
        self.zero_y_button.setIcon(icon)
        self.zero_y_button.setIconSize(QtCore.QSize(20, 20))
        self.zero_y_button.setObjectName("zero_y_button")
        self.y_axis_dro_layout.addWidget(self.zero_y_button)
        self.drowidget_y = DROLineEdit(self.widget_xyz)
        self.drowidget_y.setMinimumSize(QtCore.QSize(100, 35))
        self.drowidget_y.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.drowidget_y.setFont(font)
        self.drowidget_y.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.drowidget_y.setStyleSheet("QLineEdit{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    padding-right: 2px;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.drowidget_y.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drowidget_y.setProperty("axisNumber", 1)
        self.drowidget_y.setObjectName("drowidget_y")
        self.y_axis_dro_layout.addWidget(self.drowidget_y)
        self.drolabel_machine_y = DROLabel(self.widget_xyz)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drolabel_machine_y.sizePolicy().hasHeightForWidth())
        self.drolabel_machine_y.setSizePolicy(sizePolicy)
        self.drolabel_machine_y.setMinimumSize(QtCore.QSize(100, 35))
        self.drolabel_machine_y.setMaximumSize(QtCore.QSize(100, 35))
        self.drolabel_machine_y.setStyleSheet("QLabel{\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}\n"
"\n"
"QLabel[style=\"unhomed\"]{\n"
"   color: red;\n"
"}\n"
"\n"
"QLabel[style=\"homing\"]{\n"
"   color: rgb(196, 160, 0);\n"
"}")
        self.drolabel_machine_y.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drolabel_machine_y.setProperty("referenceType", 0)
        self.drolabel_machine_y.setProperty("axisNumber", 1)
        self.drolabel_machine_y.setProperty("latheMode", 0)
        self.drolabel_machine_y.setObjectName("drolabel_machine_y")
        self.y_axis_dro_layout.addWidget(self.drolabel_machine_y)
        self.drolabel_dtg_y = DROLabel(self.widget_xyz)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drolabel_dtg_y.sizePolicy().hasHeightForWidth())
        self.drolabel_dtg_y.setSizePolicy(sizePolicy)
        self.drolabel_dtg_y.setMinimumSize(QtCore.QSize(100, 35))
        self.drolabel_dtg_y.setMaximumSize(QtCore.QSize(100, 35))
        self.drolabel_dtg_y.setStyleSheet("QLabel{\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}")
        self.drolabel_dtg_y.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drolabel_dtg_y.setProperty("referenceType", 2)
        self.drolabel_dtg_y.setProperty("axisNumber", 1)
        self.drolabel_dtg_y.setProperty("latheMode", 0)
        self.drolabel_dtg_y.setObjectName("drolabel_dtg_y")
        self.y_axis_dro_layout.addWidget(self.drolabel_dtg_y)
        self.ref_y_button = ActionButton(self.widget_xyz)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ref_y_button.sizePolicy().hasHeightForWidth())
        self.ref_y_button.setSizePolicy(sizePolicy)
        self.ref_y_button.setMinimumSize(QtCore.QSize(62, 40))
        self.ref_y_button.setMaximumSize(QtCore.QSize(62, 40))
        self.ref_y_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ref_y_button.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.ref_y_button.setObjectName("ref_y_button")
        self.y_axis_dro_layout.addWidget(self.ref_y_button)
        self.verticalLayout_55.addLayout(self.y_axis_dro_layout)
        self.z_axis_dro_layout = QtWidgets.QHBoxLayout()
        self.z_axis_dro_layout.setContentsMargins(1, 1, 1, 1)
        self.z_axis_dro_layout.setSpacing(7)
        self.z_axis_dro_layout.setObjectName("z_axis_dro_layout")
        self.zero_z_button = MDIButton(self.widget_xyz)
        self.zero_z_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zero_z_button.sizePolicy().hasHeightForWidth())
        self.zero_z_button.setSizePolicy(sizePolicy)
        self.zero_z_button.setMinimumSize(QtCore.QSize(60, 40))
        self.zero_z_button.setMaximumSize(QtCore.QSize(60, 40))
        self.zero_z_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.zero_z_button.setStyleSheet("MDIButton {\n"
"       font: 17pt \"Bebas Kai\";\n"
"}")
        self.zero_z_button.setIcon(icon)
        self.zero_z_button.setIconSize(QtCore.QSize(20, 20))
        self.zero_z_button.setObjectName("zero_z_button")
        self.z_axis_dro_layout.addWidget(self.zero_z_button)
        self.drowidget_z = DROLineEdit(self.widget_xyz)
        self.drowidget_z.setMinimumSize(QtCore.QSize(100, 35))
        self.drowidget_z.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.drowidget_z.setFont(font)
        self.drowidget_z.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.drowidget_z.setStyleSheet("QLineEdit{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    padding-right: 2px;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.drowidget_z.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drowidget_z.setProperty("axisNumber", 2)
        self.drowidget_z.setObjectName("drowidget_z")
        self.z_axis_dro_layout.addWidget(self.drowidget_z)
        self.drolabel_machine_z = DROLabel(self.widget_xyz)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drolabel_machine_z.sizePolicy().hasHeightForWidth())
        self.drolabel_machine_z.setSizePolicy(sizePolicy)
        self.drolabel_machine_z.setMinimumSize(QtCore.QSize(100, 35))
        self.drolabel_machine_z.setMaximumSize(QtCore.QSize(100, 35))
        self.drolabel_machine_z.setStyleSheet("QLabel{\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}\n"
"\n"
"QLabel[style=\"unhomed\"]{\n"
"   color: red;\n"
"}\n"
"\n"
"QLabel[style=\"homing\"]{\n"
"   color: rgb(196, 160, 0);\n"
"}")
        self.drolabel_machine_z.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drolabel_machine_z.setProperty("referenceType", 0)
        self.drolabel_machine_z.setProperty("axisNumber", 2)
        self.drolabel_machine_z.setProperty("latheMode", 0)
        self.drolabel_machine_z.setObjectName("drolabel_machine_z")
        self.z_axis_dro_layout.addWidget(self.drolabel_machine_z)
        self.drolabel_dtg_z = DROLabel(self.widget_xyz)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drolabel_dtg_z.sizePolicy().hasHeightForWidth())
        self.drolabel_dtg_z.setSizePolicy(sizePolicy)
        self.drolabel_dtg_z.setMinimumSize(QtCore.QSize(100, 35))
        self.drolabel_dtg_z.setMaximumSize(QtCore.QSize(100, 35))
        self.drolabel_dtg_z.setStyleSheet("QLabel{\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}")
        self.drolabel_dtg_z.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drolabel_dtg_z.setProperty("referenceType", 2)
        self.drolabel_dtg_z.setProperty("axisNumber", 2)
        self.drolabel_dtg_z.setProperty("latheMode", 0)
        self.drolabel_dtg_z.setObjectName("drolabel_dtg_z")
        self.z_axis_dro_layout.addWidget(self.drolabel_dtg_z)
        self.ref_z_button = ActionButton(self.widget_xyz)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ref_z_button.sizePolicy().hasHeightForWidth())
        self.ref_z_button.setSizePolicy(sizePolicy)
        self.ref_z_button.setMinimumSize(QtCore.QSize(62, 40))
        self.ref_z_button.setMaximumSize(QtCore.QSize(62, 40))
        self.ref_z_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ref_z_button.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.ref_z_button.setObjectName("ref_z_button")
        self.z_axis_dro_layout.addWidget(self.ref_z_button)
        self.verticalLayout_55.addLayout(self.z_axis_dro_layout)
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setContentsMargins(3, 1, 3, 1)
        self.layout.setSpacing(20)
        self.layout.setObjectName("layout")
        self.zero_all_button = MDIButton(self.widget_xyz)
        self.zero_all_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zero_all_button.sizePolicy().hasHeightForWidth())
        self.zero_all_button.setSizePolicy(sizePolicy)
        self.zero_all_button.setMinimumSize(QtCore.QSize(60, 40))
        self.zero_all_button.setMaximumSize(QtCore.QSize(16777215, 40))
        self.zero_all_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.zero_all_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.zero_all_button.setStyleSheet("MDIButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.zero_all_button.setIconSize(QtCore.QSize(20, 20))
        self.zero_all_button.setObjectName("zero_all_button")
        self.layout.addWidget(self.zero_all_button)
        self.ref_all_button = ActionButton(self.widget_xyz)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ref_all_button.sizePolicy().hasHeightForWidth())
        self.ref_all_button.setSizePolicy(sizePolicy)
        self.ref_all_button.setMinimumSize(QtCore.QSize(62, 40))
        self.ref_all_button.setMaximumSize(QtCore.QSize(16777215, 40))
        self.ref_all_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ref_all_button.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.ref_all_button.setObjectName("ref_all_button")
        self.layout.addWidget(self.ref_all_button)
        self.verticalLayout_55.addLayout(self.layout)
        self.verticalLayout.addWidget(self.widget_xyz)

        self.retranslateUi(dros_xyz)
        QtCore.QMetaObject.connectSlotsByName(dros_xyz)

    def retranslateUi(self, dros_xyz):
        _translate = QtCore.QCoreApplication.translate
        dros_xyz.setWindowTitle(_translate("dros_xyz", "dros_xyz"))
        self.axis_column_header.setText(_translate("dros_xyz", "AXIS"))
        self.axis_column_header.setProperty("rules", _translate("dros_xyz", "[]"))
        self.work_column_header.setProperty("rules", _translate("dros_xyz", "[{\"channels\": [{\"url\": \"status:g5x_index?text\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"ch[0] + \' WORK\'\\n\", \"name\": \"WCS Header\"}]"))
        self.machine_column_header.setText(_translate("dros_xyz", "MACHINE"))
        self.dtg_column_header.setText(_translate("dros_xyz", "DTG"))
        self.ref_column_header.setText(_translate("dros_xyz", "REF"))
        self.ref_column_header.setProperty("rules", _translate("dros_xyz", "[]"))
        self.zero_x_button.setText(_translate("dros_xyz", "X"))
        self.zero_x_button.setProperty("rules", _translate("dros_xyz", "[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]"))
        self.zero_x_button.setProperty("MDICommand", _translate("dros_xyz", "G10 L20 P{ch[0]} X0.0"))
        self.drowidget_x.setText(_translate("dros_xyz", "     0.000"))
        self.drowidget_x.setProperty("inchFormat", _translate("dros_xyz", "%9.4f"))
        self.drowidget_x.setProperty("millimeterFormat", _translate("dros_xyz", "%10.3f"))
        self.drowidget_x.setProperty("degreeFormat", _translate("dros_xyz", "%10.2f"))
        self.drolabel_machine_x.setProperty("inchFormat", _translate("dros_xyz", "%9.4f"))
        self.drolabel_machine_x.setProperty("millimeterFormat", _translate("dros_xyz", "%10.3f"))
        self.drolabel_machine_x.setProperty("degreeFormat", _translate("dros_xyz", "%10.2f"))
        self.drolabel_dtg_x.setProperty("inchFormat", _translate("dros_xyz", "%9.4f"))
        self.drolabel_dtg_x.setProperty("millimeterFormat", _translate("dros_xyz", "%10.3f"))
        self.drolabel_dtg_x.setProperty("degreeFormat", _translate("dros_xyz", "%10.2f"))
        self.ref_x_button.setText(_translate("dros_xyz", "REF X"))
        self.ref_x_button.setProperty("rules", _translate("dros_xyz", "[{\"name\": \"home_prohibit\", \"property\": \"Enable\", \"expression\": \"not (ch[0] or ch[1] or ch[2])\", \"channels\": [{\"url\": \"status:joint.0.homing\", \"trigger\": true}, {\"url\": \"status:joint.1.homing\", \"trigger\": true}, {\"url\": \"status:joint.2.homing\", \"trigger\": true}]}]"))
        self.ref_x_button.setProperty("actionName", _translate("dros_xyz", "machine.home.axis:x"))
        self.zero_y_button.setText(_translate("dros_xyz", "Y"))
        self.zero_y_button.setProperty("rules", _translate("dros_xyz", "[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]"))
        self.zero_y_button.setProperty("MDICommand", _translate("dros_xyz", "G10 L20 P{ch[0]} Y0.0"))
        self.drolabel_machine_y.setProperty("inchFormat", _translate("dros_xyz", "%9.4f"))
        self.drolabel_machine_y.setProperty("millimeterFormat", _translate("dros_xyz", "%10.3f"))
        self.drolabel_machine_y.setProperty("degreeFormat", _translate("dros_xyz", "%10.2f"))
        self.drolabel_dtg_y.setProperty("inchFormat", _translate("dros_xyz", "%9.4f"))
        self.drolabel_dtg_y.setProperty("millimeterFormat", _translate("dros_xyz", "%10.3f"))
        self.drolabel_dtg_y.setProperty("degreeFormat", _translate("dros_xyz", "%10.2f"))
        self.ref_y_button.setText(_translate("dros_xyz", "REF Y"))
        self.ref_y_button.setProperty("rules", _translate("dros_xyz", "[{\"name\": \"home_prohibit\", \"property\": \"Enable\", \"expression\": \"not (ch[0] or ch[1] or ch[2])\", \"channels\": [{\"url\": \"status:joint.0.homing\", \"trigger\": true}, {\"url\": \"status:joint.1.homing\", \"trigger\": true}, {\"url\": \"status:joint.2.homing\", \"trigger\": true}]}]"))
        self.ref_y_button.setProperty("actionName", _translate("dros_xyz", "machine.home.axis:y"))
        self.zero_z_button.setText(_translate("dros_xyz", "Z"))
        self.zero_z_button.setProperty("rules", _translate("dros_xyz", "[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]"))
        self.zero_z_button.setProperty("MDICommand", _translate("dros_xyz", "G10 L20 P{ch[0]} Z0.0"))
        self.drolabel_machine_z.setProperty("inchFormat", _translate("dros_xyz", "%9.4f"))
        self.drolabel_machine_z.setProperty("millimeterFormat", _translate("dros_xyz", "%10.3f"))
        self.drolabel_machine_z.setProperty("degreeFormat", _translate("dros_xyz", "%10.2f"))
        self.drolabel_dtg_z.setProperty("inchFormat", _translate("dros_xyz", "%9.4f"))
        self.drolabel_dtg_z.setProperty("millimeterFormat", _translate("dros_xyz", "%10.3f"))
        self.drolabel_dtg_z.setProperty("degreeFormat", _translate("dros_xyz", "%10.2f"))
        self.ref_z_button.setText(_translate("dros_xyz", "REF Z"))
        self.ref_z_button.setProperty("rules", _translate("dros_xyz", "[{\"name\": \"home_prohibit\", \"property\": \"Enable\", \"expression\": \"not (ch[0] or ch[1] or ch[2])\", \"channels\": [{\"url\": \"status:joint.0.homing\", \"trigger\": true}, {\"url\": \"status:joint.1.homing\", \"trigger\": true}, {\"url\": \"status:joint.2.homing\", \"trigger\": true}]}]"))
        self.ref_z_button.setProperty("actionName", _translate("dros_xyz", "machine.home.axis:z"))
        self.zero_all_button.setText(_translate("dros_xyz", "ZERO ALL"))
        self.zero_all_button.setProperty("rules", _translate("dros_xyz", "[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]"))
        self.zero_all_button.setProperty("MDICommand", _translate("dros_xyz", "G10 L20 P{ch[0]} X0.0 Y0.0 Z0.0"))
        self.ref_all_button.setText(_translate("dros_xyz", "REF ALL"))
        self.ref_all_button.setProperty("rules", _translate("dros_xyz", "[{\"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\'HOMED\' if ch[0] else \'REF ALL\'\", \"name\": \"reference_all\"}, {\"name\": \"home_prohibit\", \"property\": \"Enable\", \"expression\": \"not (ch[0] or ch[1] or ch[2])\", \"channels\": [{\"url\": \"status:joint.0.homing\", \"trigger\": true}, {\"url\": \"status:joint.1.homing\", \"trigger\": true}, {\"url\": \"status:joint.2.homing\", \"trigger\": true}]}]"))
        self.ref_all_button.setProperty("actionName", _translate("dros_xyz", "machine.home.all"))
from qtpyvcp.widgets.button_widgets.action_button import ActionButton
from qtpyvcp.widgets.button_widgets.mdi_button import MDIButton
from qtpyvcp.widgets.display_widgets.dro_label import DROLabel
from qtpyvcp.widgets.display_widgets.status_label import StatusLabel
from qtpyvcp.widgets.input_widgets.dro_line_edit import DROLineEdit
import probe_basic_rc
