# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import sqlHandler as sqlHandler


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1004, 789)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(-1, 10, -1, -1)
        self.formLayout.setObjectName("formLayout")
        self.nomeLabel = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.nomeLabel.setFont(font)
        self.nomeLabel.setObjectName("nomeLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nomeLabel)
        self.nome_lbl_new = QtWidgets.QLineEdit(self.tab)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.nome_lbl_new.setFont(font)
        self.nome_lbl_new.setObjectName("nome_lbl_new")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nome_lbl_new)
        self.label_2 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.genero_lbl_new = QtWidgets.QLineEdit(self.tab)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.genero_lbl_new.setFont(font)
        self.genero_lbl_new.setObjectName("genero_lbl_new")
        self.gridLayout_4.addWidget(self.genero_lbl_new, 0, 1, 1, 1)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.gridLayout_4)
        self.label_3 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.ano_lbl_new = QtWidgets.QLineEdit(self.tab)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ano_lbl_new.setFont(font)
        self.ano_lbl_new.setObjectName("ano_lbl_new")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ano_lbl_new)
        self.plataformasLabel = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.plataformasLabel.setFont(font)
        self.plataformasLabel.setObjectName("plataformasLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.plataformasLabel)
        self.plataforma_lbl_new = QtWidgets.QLineEdit(self.tab)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.plataforma_lbl_new.setFont(font)
        self.plataforma_lbl_new.setObjectName("plataforma_lbl_new")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.plataforma_lbl_new)
        self.classificaOIndicativaLabel = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.classificaOIndicativaLabel.setFont(font)
        self.classificaOIndicativaLabel.setObjectName("classificaOIndicativaLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.classificaOIndicativaLabel)
        self.classificacao_lbl_new = QtWidgets.QLineEdit(self.tab)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.classificacao_lbl_new.setFont(font)
        self.classificacao_lbl_new.setObjectName("classificacao_lbl_new")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.classificacao_lbl_new)
        self.nDaMesaLabel = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.nDaMesaLabel.setFont(font)
        self.nDaMesaLabel.setObjectName("nDaMesaLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.nDaMesaLabel)
        self.mesa_lbl_new = QtWidgets.QLineEdit(self.tab)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.mesa_lbl_new.setFont(font)
        self.mesa_lbl_new.setObjectName("mesa_lbl_new")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.mesa_lbl_new)
        self.gridLayout_3.addLayout(self.formLayout, 1, 0, 1, 1)
        self.cadastrar_btn = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cadastrar_btn.sizePolicy().hasHeightForWidth())
        self.cadastrar_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.cadastrar_btn.setFont(font)
        self.cadastrar_btn.setObjectName("cadastrar_btn")
        self.cadastrar_btn.clicked.connect(self.cadastrar)# connect button clicked with action
        self.gridLayout_3.addWidget(self.cadastrar_btn, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 2, 0, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(-1, 15, -1, 15)
        self.formLayout_2.setObjectName("formLayout_2")
        self.nomeLabel_2 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.nomeLabel_2.setFont(font)
        self.nomeLabel_2.setObjectName("nomeLabel_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nomeLabel_2)
        self.nome_lbl_search = QtWidgets.QLineEdit(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.nome_lbl_search.setFont(font)
        self.nome_lbl_search.setObjectName("nome_lbl_search")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nome_lbl_search)
        self.genRoLabel = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.genRoLabel.setFont(font)
        self.genRoLabel.setObjectName("genRoLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.genRoLabel)
        self.genero_lbl_search = QtWidgets.QLineEdit(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.genero_lbl_search.setFont(font)
        self.genero_lbl_search.setObjectName("genero_lbl_search")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.genero_lbl_search)
        self.anoDeLanAmentoLabel = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.anoDeLanAmentoLabel.setFont(font)
        self.anoDeLanAmentoLabel.setObjectName("anoDeLanAmentoLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.anoDeLanAmentoLabel)
        self.ano_lbl_search = QtWidgets.QLineEdit(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ano_lbl_search.setFont(font)
        self.ano_lbl_search.setObjectName("ano_lbl_search")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ano_lbl_search)
        self.plataformaLabel = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.plataformaLabel.setFont(font)
        self.plataformaLabel.setObjectName("plataformaLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.plataformaLabel)
        self.plataforma_lbl_search = QtWidgets.QLineEdit(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.plataforma_lbl_search.setFont(font)
        self.plataforma_lbl_search.setObjectName("plataforma_lbl_search")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.plataforma_lbl_search)
        self.classificaOIndicativaLabel_2 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.classificaOIndicativaLabel_2.setFont(font)
        self.classificaOIndicativaLabel_2.setObjectName("classificaOIndicativaLabel_2")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.classificaOIndicativaLabel_2)
        self.classificacao_lbl_search = QtWidgets.QLineEdit(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.classificacao_lbl_search.setFont(font)
        self.classificacao_lbl_search.setObjectName("classificacao_lbl_search")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.classificacao_lbl_search)
        self.nDaMesaLabel_2 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.nDaMesaLabel_2.setFont(font)
        self.nDaMesaLabel_2.setObjectName("nDaMesaLabel_2")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.nDaMesaLabel_2)
        self.mesa_lbl_search = QtWidgets.QLineEdit(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.mesa_lbl_search.setFont(font)
        self.mesa_lbl_search.setObjectName("mesa_lbl_search")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.mesa_lbl_search)
        self.gridLayout_6.addLayout(self.formLayout_2, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 1, 0, 1, 1)
        self.search_btn = QtWidgets.QPushButton(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.search_btn.setFont(font)
        self.search_btn.setObjectName("search_btn")
        self.gridLayout_6.addWidget(self.search_btn, 4, 0, 1, 1)
        self.search_btn.clicked.connect(self.pesquisar)
        self.tableView = QtWidgets.QTableView(self.tab_2)
        self.tableView.setObjectName("tableView")
        self.gridLayout_6.addWidget(self.tableView, 5, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1004, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def cadastrar(self):
        name = self.nome_lbl_new.text().strip()
        genero = self.genero_lbl_new.text().strip()
        mesa = self.mesa_lbl_new.text().strip()
        ano = self.ano_lbl_new.text().strip()
        classificacao = self.classificacao_lbl_new.text().strip()
        plataforma = self.plataforma_lbl_new.text().strip()

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setWindowTitle("Erro")

        if len(name) > 15:
            msg.setText("Campo: Nome")
            msg.setInformativeText("Nome deve ter no máximo 15 caracteres")
            msg.exec_()
            return
        if len(name) == 0:
            msg.setText("Campo: Nome")
            msg.setInformativeText("Nome não pode ser nulo")
            msg.exec_()
            return

        if len(genero) > 20:
            msg.setText("Campo: Genêro(s)")
            msg.setInformativeText("Gênero(s) deve ter no máximo 20 caracteres")
            msg.exec_()
            return
        if len(genero) == 0:
            msg.setText("Campo: Gênero(s)")
            msg.setInformativeText("Gênero(s) não pode ser nulo")
            msg.exec_()
            return
        
        if len(mesa) > 2:
            msg.setText("Campo: Nº da Mesa")
            msg.setInformativeText("Nº da Mesa deve ter no máximo 2 caracteres")
            msg.exec_()
            return
        if len(mesa) == 0:
            msg.setText("Campo: Nº da Mesa")
            msg.setInformativeText("Nº da Mesa não pode ser nulo")
            msg.exec_()
            return
        if len(mesa) <= 2 and len(mesa) != 0:
            try: 
                int(mesa)
            except ValueError:
                msg.setText("Campo: Nº da Mesa")
                msg.setInformativeText("Nº da Mesa deve ser um inteiro positivo")
                msg.exec_()
                return
            if int(mesa) < 0:
                msg.setText("Campo: Nº da Mesa")
                msg.setInformativeText("Nº da Mesa deve ser um inteiro positivo")
                msg.exec_()
                return


        if len(ano) > 4:
            msg.setText("Campo: Ano de Lançamento")
            msg.setInformativeText("Ano de Lançamento deve ter no máximo 4 caracteres")
            msg.exec_()
            return

        if len(ano) <= 4:
            try: 
                int(ano)
            except ValueError:
                msg.setText("Campo: Ano de Lançamento")
                msg.setInformativeText("Ano de Lançamento deve ser um inteiro positivo")
                msg.exec_()
                return
            if int(ano) < 0:
                msg.setText("Campo: Ano de Lançamento")
                msg.setInformativeText("Ano de Lançamento deve ser um inteiro positivo")
                msg.exec_()
                return

        if len(classificacao) > 2:
            msg.setText("Campo: Classificação Indicativa")
            msg.setInformativeText("Classificação Indicativa deve ter no máximo 2 caracteres")
            msg.exec_()
            return

        if len(classificacao) <= 2:
            try: 
                int(classificacao)
            except ValueError:
                msg.setText("Campo: Classificação Indicativa")
                msg.setInformativeText("Classificação Indicativa deve ser um inteiro positivo")
                msg.exec_()
                return
            if int(classificacao) < 0:
                msg.setText("Campo: Classificação Indicativa")
                msg.setInformativeText("Classificação Indicativa deve ser um inteiro positivo")
                msg.exec_()
                return

        if len(plataforma) > 2:
            msg.setText("Campo: Plataforma(s)")
            msg.setInformativeText("Plataforma(s) deve ter no máximo 2 caracteres")
            msg.exec_()
            return
        if len(plataforma) == 0:
            msg.setText("Campo: Plataforma(s)")
            msg.setInformativeText("Plataforma(s) não pode ser nulo")
            msg.exec_()
            return

        sqlHandler.insert_new_data('jogo', [mesa, nome, ano, classificacao])
        sqlHandler.insert_new_data('plataforma_jogo', [mesa, plataforma])
        sqlHandler.insert_new_data('genero_jogo', [mesa, genero])

        #reset fields after insert
        self.nome_lbl_new.setText("")
        self.genero_lbl_new.setText("")
        self.mesa_lbl_new.setText("")
        self.ano_lbl_new.setText("")
        self.classificacao_lbl_new.setText("")
        self.plataforma_lbl_new.setText("")
              
    def pesquisar(self):
        name = self.nome_lbl_search.text().strip()
        genero = self.genero_lbl_search.text().strip()
        mesa = self.mesa_lbl_search.text().strip()
        ano = self.ano_lbl_search.text().strip()
        classificacao = self.classificacao_lbl_search.text().strip()
        plataforma = self.plataforma_lbl_search.text().strip()

        columns = []
        values = []
        
        if len(name) > 0:
            columns.append('J.nome')
            values.append(name)

        if len(genero) > 0:
            columns.append('GJ.genero')
            values.append(genero)

        if len(mesa) > 0:
            columns.append('J.numero_mesa')
            values.append(mesa)

        if len(ano) > 0:
            columns.append('J.ano_lancamento')
            values.append(ano)

        if len(classificacao) > 0:
            columns.append('J.classificacao_indicativa')
            values.append(classificacao)

        if len(plataforma) > 0:
            columns.append('PJ.plataforma')
            values.append(plataforma)

        self.table_data = sqlHandler.search_game(values,columns)
        
        header = ['numero_mesa', 'nome', 'ano', 'classif', 'jogo', 'genero', 'jogo', 'plataforma']
        table_model = MyTableModel(self.table_data, header, self)
        self.tableView.setModel(tablemodel)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Cadastrar novo Jogo"))
        self.nomeLabel.setText(_translate("MainWindow", "Nome"))
        self.label_2.setText(_translate("MainWindow", "Gênero(s)"))
        self.label_3.setText(_translate("MainWindow", "Ano de Lançamento"))
        self.plataformasLabel.setText(_translate("MainWindow", "Plataforma(s)"))
        self.classificaOIndicativaLabel.setText(_translate("MainWindow", "Classificação Indicativa"))
        self.nDaMesaLabel.setText(_translate("MainWindow", "Nº da mesa"))
        self.cadastrar_btn.setText(_translate("MainWindow", "Cadastrar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Cadastrar"))
        self.label_6.setText(_translate("MainWindow", "Campos em branco serão ignorados na pesquisa"))
        self.nomeLabel_2.setText(_translate("MainWindow", "Nome"))
        self.genRoLabel.setText(_translate("MainWindow", "Genêro"))
        self.anoDeLanAmentoLabel.setText(_translate("MainWindow", "Ano de Lançamento"))
        self.plataformaLabel.setText(_translate("MainWindow", "Plataforma"))
        self.classificaOIndicativaLabel_2.setText(_translate("MainWindow", "Classificação Indicativa"))
        self.nDaMesaLabel_2.setText(_translate("MainWindow", "N° da Mesa"))
        self.label_4.setText(_translate("MainWindow", "Pesquisar Jogos existentes"))
        self.label_5.setText(_translate("MainWindow", "Utilize os campos abaixo para realizar sua busca"))
        self.search_btn.setText(_translate("MainWindow", "Pesquisar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Listagem"))

class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self, datain, headerdata, parent=None):
        """
        Args:
            datain: a list of lists\n
            headerdata: a list of strings
        """
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.arraydata = datain
        self.headerdata = headerdata

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        if len(self.arraydata) > 0: 
            return len(self.arraydata[0]) 
        return 0

    def data(self, index, role):
        if not index.isValid():
            return QtCore.QVariant()
        elif role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        return QtCore.QVariant(self.arraydata[index.row()][index.column()])
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
