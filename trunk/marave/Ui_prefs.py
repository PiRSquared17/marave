# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prefs.ui'
#
# Created: Thu Feb 18 00:04:55 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(390, 257)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.close = QtGui.QToolButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close.setIcon(icon)
        self.close.setAutoRaise(True)
        self.close.setObjectName("close")
        self.verticalLayout.addWidget(self.close)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem1 = QtGui.QSpacerItem(56, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.themeList = QtGui.QComboBox(self.tab)
        self.themeList.setObjectName("themeList")
        self.horizontalLayout.addWidget(self.themeList)
        self.saveTheme = QtGui.QToolButton(self.tab)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveTheme.setIcon(icon1)
        self.saveTheme.setObjectName("saveTheme")
        self.horizontalLayout.addWidget(self.saveTheme)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_5)
        self.styleList = QtGui.QComboBox(self.tab)
        self.styleList.setObjectName("styleList")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.styleList)
        self.spelling = QtGui.QRadioButton(self.tab)
        self.spelling.setChecked(True)
        self.spelling.setObjectName("spelling")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.spelling)
        self.langBox = QtGui.QComboBox(self.tab)
        self.langBox.setObjectName("langBox")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.langBox)
        self.syntax = QtGui.QRadioButton(self.tab)
        self.syntax.setObjectName("syntax")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.syntax)
        self.syntaxList = QtGui.QComboBox(self.tab)
        self.syntaxList.setEnabled(False)
        self.syntaxList.setObjectName("syntaxList")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.syntaxList)
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName("label")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label)
        self.schemeList = QtGui.QComboBox(self.tab)
        self.schemeList.setEnabled(False)
        self.schemeList.setObjectName("schemeList")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.schemeList)
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_3)
        self.buttonStyle = QtGui.QComboBox(self.tab)
        self.buttonStyle.setObjectName("buttonStyle")
        self.buttonStyle.addItem("")
        self.buttonStyle.addItem("")
        self.buttonStyle.addItem("")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.buttonStyle)
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_4)
        self.opacity = QtGui.QSlider(self.tab)
        self.opacity.setMaximum(100)
        self.opacity.setOrientation(QtCore.Qt.Horizontal)
        self.opacity.setObjectName("opacity")
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.opacity)
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_6)
        self.autoSave = QtGui.QSpinBox(self.tab)
        self.autoSave.setObjectName("autoSave")
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.autoSave)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pluginContainer = QtGui.QScrollArea(self.tab_2)
        self.pluginContainer.setWidgetResizable(True)
        self.pluginContainer.setObjectName("pluginContainer")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.pluginContainer)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 259, 204))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pluginLayout = QtGui.QVBoxLayout()
        self.pluginLayout.setObjectName("pluginLayout")
        self.verticalLayout_5.addLayout(self.pluginLayout)
        self.pluginContainer.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.pluginContainer)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        spacerItem2 = QtGui.QSpacerItem(55, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_2.setBuddy(self.themeList)
        self.label_5.setBuddy(self.styleList)
        self.label_3.setBuddy(self.buttonStyle)
        self.label_4.setBuddy(self.opacity)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.close.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.close.setShortcut(QtGui.QApplication.translate("Form", "Esc", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "&Theme:", None, QtGui.QApplication.UnicodeUTF8))
        self.saveTheme.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "St&yle:", None, QtGui.QApplication.UnicodeUTF8))
        self.spelling.setText(QtGui.QApplication.translate("Form", "&Spell Checking:", None, QtGui.QApplication.UnicodeUTF8))
        self.syntax.setText(QtGui.QApplication.translate("Form", "Syntax Highlight:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Color Scheme:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "&Buttons:", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonStyle.setItemText(0, QtGui.QApplication.translate("Form", "Icons", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonStyle.setItemText(1, QtGui.QApplication.translate("Form", "Text", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonStyle.setItemText(2, QtGui.QApplication.translate("Form", "Text + Icons", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "&Editor Opacity:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Auto save (minutes):", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Form", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Form", "Plugins", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

