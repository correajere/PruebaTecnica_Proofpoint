import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QTextEdit, QMessageBox
from analizador import limpiar_texto, contar_palabras, obtener_palabras_mas_frecuentes

class AnalizadorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configuración de la ventana
        self.setWindowTitle("Analizador de Frecuencia de Palabras")
        self.setGeometry(100, 100, 600, 400)

        # Layout vertical
        layout = QVBoxLayout()

        # Etiqueta de instrucción
        self.etiqueta = QLabel("Seleccione un archivo de texto para analizar:", self)
        layout.addWidget(self.etiqueta)

        # Botón para seleccionar archivo
        self.boton_seleccionar = QPushButton("Seleccionar Archivo", self)
        self.boton_seleccionar.clicked.connect(self.seleccionar_archivo)
        layout.addWidget(self.boton_seleccionar)

        # Área de texto para mostrar resultados
        self.texto_resultado = QTextEdit(self)
        self.texto_resultado.setReadOnly(True)
        layout.addWidget(self.texto_resultado)

        # Establecer el layout
        self.setLayout(layout)

    def seleccionar_archivo(self):
        # Abrir diálogo para seleccionar archivo
        ruta_archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo de texto", "", "Archivos de texto (*.txt)")

        if ruta_archivo:
            try:
                # Leer el archivo de texto
                with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                    texto = archivo.read()

                # Limpiar el texto
                texto_limpio = limpiar_texto(texto)

                # Contar la frecuencia de las palabras
                contador_palabras = contar_palabras(texto_limpio)

                # Obtener las 10 palabras más frecuentes
                palabras_frecuentes = obtener_palabras_mas_frecuentes(contador_palabras)

                # Mostrar los resultados en el área de texto
                self.texto_resultado.clear()
                self.texto_resultado.append("Las 10 palabras más frecuentes son:\n")
                for palabra, frecuencia in palabras_frecuentes:
                    self.texto_resultado.append(f"{palabra}: {frecuencia}")

            except FileNotFoundError:
                QMessageBox.critical(self, "Error", "El archivo no fue encontrado.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Ocurrió un error: {e}")

# Función principal
def main():
    app = QApplication(sys.argv)
    ventana = AnalizadorApp()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()