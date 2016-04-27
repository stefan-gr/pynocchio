# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/bookmark_manager_dialog.ui'
#
# Created: Wed Apr 27 03:26:39 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Bookmark_Dialog(object):
    def setupUi(self, Bookmark_Dialog):
        Bookmark_Dialog.setObjectName("Bookmark_Dialog")
        Bookmark_Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Bookmark_Dialog.resize(750, 436)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Bookmark_Dialog.sizePolicy().hasHeightForWidth())
        Bookmark_Dialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/apps/48/office-database.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Bookmark_Dialog.setWindowIcon(icon)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Bookmark_Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bookmark_table = QtGui.QTableView(Bookmark_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookmark_table.sizePolicy().hasHeightForWidth())
        self.bookmark_table.setSizePolicy(sizePolicy)
        self.bookmark_table.setAutoFillBackground(False)
        self.bookmark_table.setFrameShape(QtGui.QFrame.StyledPanel)
        self.bookmark_table.setAutoScroll(True)
        self.bookmark_table.setAutoScrollMargin(9)
        self.bookmark_table.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed|QtGui.QAbstractItemView.EditKeyPressed|QtGui.QAbstractItemView.SelectedClicked)
        self.bookmark_table.setTabKeyNavigation(True)
        self.bookmark_table.setProperty("showDropIndicator", False)
        self.bookmark_table.setDragDropOverwriteMode(False)
        self.bookmark_table.setAlternatingRowColors(True)
        self.bookmark_table.setSelectionMode(QtGui.QAbstractItemView.ContiguousSelection)
        self.bookmark_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.bookmark_table.setShowGrid(True)
        self.bookmark_table.setSortingEnabled(True)
        self.bookmark_table.setWordWrap(True)
        self.bookmark_table.setObjectName("bookmark_table")
        self.horizontalLayout.addWidget(self.bookmark_table)
        self.verticalFrame = QtGui.QFrame(Bookmark_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy)
        self.verticalFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.verticalFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.page_image_label = QtGui.QLabel(self.verticalFrame)
        self.page_image_label.setText("")
        self.page_image_label.setPixmap(QtGui.QPixmap(":/icons/pynocchio_icon_2.png"))
        self.page_image_label.setScaledContents(True)
        self.page_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.page_image_label.setObjectName("page_image_label")
        self.verticalLayout.addWidget(self.page_image_label)
        self.page_preview_label = QtGui.QLabel(self.verticalFrame)
        self.page_preview_label.setEnabled(True)
        font = QtGui.QFont()
        font.setItalic(True)
        self.page_preview_label.setFont(font)
        self.page_preview_label.setAlignment(QtCore.Qt.AlignCenter)
        self.page_preview_label.setObjectName("page_preview_label")
        self.verticalLayout.addWidget(self.page_preview_label)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.verticalFrame)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.line_edit_path = QtGui.QLineEdit(Bookmark_Dialog)
        self.line_edit_path.setReadOnly(True)
        self.line_edit_path.setObjectName("line_edit_path")
        self.verticalLayout_3.addWidget(self.line_edit_path)
        self.grid_layout = QtGui.QGridLayout()
        self.grid_layout.setObjectName("grid_layout")
        self.button_remove = QtGui.QPushButton(Bookmark_Dialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/stock_delete.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_remove.setIcon(icon1)
        self.button_remove.setObjectName("button_remove")
        self.grid_layout.addWidget(self.button_remove, 1, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacerItem2, 1, 2, 1, 1)
        self.button_cancel = QtGui.QPushButton(Bookmark_Dialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/dialog-cancel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_cancel.setIcon(icon2)
        self.button_cancel.setObjectName("button_cancel")
        self.grid_layout.addWidget(self.button_cancel, 1, 3, 1, 1)
        self.button_load = QtGui.QPushButton(Bookmark_Dialog)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/dialog-apply.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_load.setIcon(icon3)
        self.button_load.setDefault(True)
        self.button_load.setObjectName("button_load")
        self.grid_layout.addWidget(self.button_load, 1, 4, 1, 1)
        self.verticalLayout_3.addLayout(self.grid_layout)

        self.retranslateUi(Bookmark_Dialog)
        QtCore.QObject.connect(self.button_cancel, QtCore.SIGNAL("clicked()"), Bookmark_Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Bookmark_Dialog)

    def retranslateUi(self, Bookmark_Dialog):
        Bookmark_Dialog.setWindowTitle(QtGui.QApplication.translate("Bookmark_Dialog", "Bookmark manager", None, QtGui.QApplication.UnicodeUTF8))
        self.page_preview_label.setText(QtGui.QApplication.translate("Bookmark_Dialog", "Page Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.button_remove.setText(QtGui.QApplication.translate("Bookmark_Dialog", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cancel.setText(QtGui.QApplication.translate("Bookmark_Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.button_load.setText(QtGui.QApplication.translate("Bookmark_Dialog", "Load", None, QtGui.QApplication.UnicodeUTF8))

import main_window_view_rc
import main_window_view_rc
import main_window_view_rc
import main_window_view_rc
import main_window_view_rc
