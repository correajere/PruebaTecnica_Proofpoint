import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QTextEdit, QMessageBox
from servicios import leer_csv, limpiar_datos, eliminar_duplicados, organizar_datos

class BibliotecaApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configuración de la ventana
        self.setWindowTitle("Limpieza de Catálogo de Biblioteca")
        self.setGeometry(100, 100, 600, 400)

        # Layout vertical
        layout = QVBoxLayout()

        # Etiqueta de instrucción
        self.etiqueta = QLabel("Cargue un archivo CSV con el catálogo de la biblioteca:", self)
        layout.addWidget(self.etiqueta)

        # Botón para cargar archivo
        self.boton_cargar = QPushButton("Cargar Archivo CSV", self)
        self.boton_cargar.clicked.connect(self.cargar_archivo)
        layout.addWidget(self.boton_cargar)

        # Área de texto para mostrar resultados
        self.texto_resultado = QTextEdit(self)
        self.texto_resultado.setReadOnly(True)
        layout.addWidget(self.texto_resultado)

        # Establecer el layout
        self.setLayout(layout)

    def cargar_archivo(self):
        # Abrir diálogo para seleccionar archivo
        ruta_archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo CSV", "", "Archivos CSV (*.csv)")

        if ruta_archivo:
            try:
                # Leer y procesar el archivo CSV
                catalogo = leer_csv(ruta_archivo)
                if catalogo is not None:
                    catalogo = limpiar_datos(catalogo)
                    catalogo = eliminar_duplicados(catalogo)
                    catalogo = organizar_datos(catalogo)

                    # Mostrar los datos limpios en el área de texto
                    self.texto_resultado.setText(catalogo.to_string(index=False))
                    QMessageBox.information(self, "Éxito", "Catálogo limpiado y organizado correctamente.")
                else:
                    QMessageBox.critical(self, "Error", "No se pudo leer el archivo CSV.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Ocurrió un error: {e}")

# Función principal
def main():
    app = QApplication(sys.argv)
    ventana = BibliotecaApp()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()