import sys
from os import getcwd, listdir, stat, path
from os.path import dirname, isdir, isfile, join
from time import localtime, strftime
from editFileExplorer import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem
from PyQt5.QtGui import QIcon

try:
    # Windows.
    from os import startfile
except ImportError:
    # Otras plataformas.
    from webbrowser import open as startfile





class Window(QMainWindow):
    
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Explorador de archivos y carpetas")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



        self.back_history = []
        self.forward_history = []        
        

        # Back clicked   
        self.ui.pushButton.clicked.connect(self.back_clicked)
        self.ui.pushButton.setEnabled(False)
        
        # Forward clicked
        self.ui.pushButton_3.clicked.connect(self.forward_clicked)
        self.ui.pushButton_3.setEnabled(False)       
        
        #Refresh cliked        
        self.ui.pushButton_2.clicked.connect(self.pushButton_2_clicked)

        # Parent folder, up
        self.ui.pushButton_4.clicked.connect(self.up_button_clicked)
        
        
        self.ui.treeWidget.setRootIsDecorated(False)
        self.ui.treeWidget.itemDoubleClicked.connect(self.item_double_clicked)
        
        # Iniciar en el directorio actual.
        
        self.load_path(getcwd())
        #Address edit                
        self.ui.address_edit.returnPressed.connect(self.enter_add)

    def enter_add(self):
        add = self.ui.address_edit.text()                
        if path.isdir(add):
            self.load_path(add)
        else:
            print("Wrong path, change the path to an existing one")
            
        
    def back_clicked(self, checked):
        """Vira para atrás cuando se da click en el botón.
        """
        if self.back_history and len(self.back_history) > 1:
            # Obtener el útimo elemento.
            path = self.back_history[-2]           
            self.forward_history.append(self.back_history[-1])

            # Remover el directorio actual.
            del self.back_history[-1]
            self.load_path(path, False)
    
    def forward_clicked(self, checked):
        """Avanza cuando se da click en el botón.
        """
        if self.forward_history:
            path = self.forward_history[-1]
            self.back_history.append(path)
            del self.forward_history[-1]
            self.load_path(path, False)
    
    def item_double_clicked(self, item, column):
        """Evento que maneja los dobles clik sobre los archivos o carpetas
        """
        filepath = join(self.current_path, item.text(0))
        if isdir(filepath):
            self.load_path(filepath)
        else:
            # Iniciar archivo con el programa predeterminado.

            startfile(filepath)
    
    def up_button_clicked(self, checked):
        """Redirige hacia el directorio padre.
        """
        parent = dirname(self.current_path)
        if parent != self.current_path:
            self.load_path(parent)
    
    def load_path(self, path, use_history=True):
        """Esta es la funcion principal ya que se encarga de
        cargar los archivos y carpetas de un directorio dado.
        """
        # Obtener archivos y carpetas.
        items = listdir(path)
        # Eliminar el contenido anterior.
        self.ui.treeWidget.clear()
        
        for i in items:
            # Omitir archivos ocultos.
            if i.startswith("."):
                continue
            filepath = join(path, i)
            # Obtener informacion del archivo.
            stats = stat(filepath)
            # Crear el control item.
            item_widget = QTreeWidgetItem(
                (i, strftime("%c", localtime(stats.st_mtime)),
                 str(stats.st_size) if isfile(filepath) else "")
            )
            # Establecer el icono correspondiente.
            item_widget.setIcon(0, QIcon(f"images/{'file' if isfile(filepath) else 'folder'}.png"))
            # Anhadir elemento.
            self.ui.treeWidget.addTopLevelItem(item_widget)
        
        # Ajustar el tamanho de las columnas.
        for i in range(2):
            self.ui.treeWidget.resizeColumnToContents(i)
        
        self.current_path = path
        self.ui.address_edit.setText(self.current_path)
        
        # Anhadir al historial.
        if use_history:
            self.back_history.append(self.current_path)
        
        # Habilitar / dehabilitar botones del historial.
        # Back button
        if self.back_history and len(self.back_history) > 1 and not self.ui.pushButton.isEnabled():
            self.ui.pushButton.setEnabled(True)                

        elif self.ui.pushButton.isEnabled():
            self.forward_history = []
            self.ui.pushButton.setEnabled(False)
            
                
        
        # Forward button
        if self.forward_history and not self.ui.pushButton_3.isEnabled():
            self.ui.pushButton_3.setEnabled(True)

        elif self.ui.pushButton_3.isEnabled():
            self.ui.pushButton_3.setEnabled(False)
                
    
    def pushButton_2_clicked(self, checked):
        """Actualizar, accion correspondiente
        al boton de igual nombre.
        """
        self.load_path(self.current_path)



if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec_())