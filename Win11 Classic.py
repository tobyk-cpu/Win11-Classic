import sys
import subprocess
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox

class MenuManager(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Gestor de Menú Windows 11')
        self.resize(300, 150)

        self.btn_clasico = QPushButton('Activar Menú Clásico')
        self.btn_moderno = QPushButton('Restaurar Menú Original')

        self.btn_clasico.clicked.connect(self.activar_clasico)
        self.btn_moderno.clicked.connect(self.restaurar_original)

        layout = QVBoxLayout()
        layout.addWidget(self.btn_clasico)
        layout.addWidget(self.btn_moderno)
        self.setLayout(layout)

    def ejecutar_comando(self, comando):
        try:
            subprocess.run(comando, shell=True, check=True)
            subprocess.run('taskkill /f /im explorer.exe && start explorer.exe', shell=True)
            QMessageBox.information(self, "Éxito", "Cambios aplicados correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo aplicar: {e}")

    def activar_clasico(self):
        cmd = 'reg add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve'
        self.ejecutar_comando(cmd)

    def restaurar_original(self):
        cmd = 'reg delete "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}" /f'
        self.ejecutar_comando(cmd)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MenuManager()
    ventana.show()
    sys.exit(app.exec())