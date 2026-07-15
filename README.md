# Manual de Usuario y Guía de Desarrollo - Polyglot Academy

Este documento contiene toda la información necesaria para instalar, ejecutar, actualizar y compilar tu aplicación de escritorio para el aprendizaje de idiomas (Inglés C1 y Japonés JLPT N5/N4).

## ¿Qué es este proyecto?

Es una aplicación de escritorio interactiva para Windows que te permite practicar:
1. **Inglés C1 (Avanzado):** Traducciones inversas desde el español y portugués hacia modismos y verbos compuestos avanzados en inglés, evaluando tu pronunciación con micrófono.
2. **Hiragana y Katakana (Japonés Básico):** Tarjetas de memoria visuales para memorizar los silabarios.
3. **JLPT N5/N4 (Examen de Japonés):** Preguntas reales de gramática japonesa con explicación técnica y un sistema interactivo de lectura en voz alta para evaluar tu pronunciación en japonés.

## Instalación de Requisitos

Para que el programa funcione, tu computadora debe tener instalado Python 3.12 (o superior). 

Abre la terminal de Visual Studio Code (puedes abrirla presionando las teclas Ctrl + Ñ) dentro de tu carpeta "MiAppIdiomas" e instala las librerías necesarias ejecutando el siguiente comando:

py -m pip install customtkinter SpeechRecognition pyaudio pyinstaller

## Cómo Ejecutar la Aplicación

Tienes dos opciones para abrir y usar el programa en tu computadora:

### Opción A: Ejecutar desde la Terminal de VS Code (Para Pruebas)

Utiliza esta opción si estás editando el código o quieres ver si la terminal arroja algún error mientras usas el programa:

1. Abre Visual Studio Code en tu carpeta "MiAppIdiomas".
2. Abre la terminal presionando Ctrl + Ñ.
3. Escribe este comando y presiona Enter:
py main.py

4. La aplicación se abrirá en tu pantalla. Si cierras la terminal, el programa se cerrará.

### Opción B: Ejecutar como Programa de Escritorio (.exe)

Utiliza esta opción si quieres abrir la aplicación con un doble clic en tu pantalla de Windows sin tener que usar comandos ni abrir VS Code:

1. Abre la terminal de VS Code y escribe el siguiente comando de compilación:
py -m PyInstaller --noconsole --onefile --collect-all customtkinter main.py

2. Espera a que el proceso termine (puede tardar un par de minutos). Sabrás que finalizó cuando veas el texto "Build complete!" en la terminal.
3. Ve a tu carpeta "MiAppIdiomas" usando el explorador de archivos de Windows y entra a la carpeta llamada "dist".
4. Copia el archivo llamado "main.exe" (o "main") de esa carpeta y pégalo en tu carpeta principal "MiAppIdiomas" (es obligatorio que esté en la misma carpeta que tus archivos JSON).
5. Crea un acceso directo en tu escritorio para abrirlo cómodamente:
* Haz clic derecho sobre el archivo "main.exe" que acabas de pegar en la carpeta principal.
* Selecciona "Mostrar más opciones" (si estás en Windows 11) -> "Enviar a" -> "Escritorio (crear acceso directo)".
6. Ahora puedes abrir tu app haciendo doble clic en el acceso directo de tu escritorio.

## Cómo Cargar y Actualizar los Datos (JSON)

La aplicación utiliza tres bases de datos locales independientes. Para llenarlas con el contenido masivo de estudio que hemos diseñado, ejecuta los siguientes comandos en la terminal de VS Code:

* **Para cargar todo el silabario de Hiragana/Katakana y preguntas iniciales del JLPT:**
py generar_datos.py

* **Para cargar el Lote 1 de vocabulario avanzado en inglés C1 (50 expresiones):**
py agregar_vocab.py

* **Para cargar el Lote 2 de vocabulario avanzado en inglés C1 (50 expresiones adicionales):**
py agregar_vocab_2.py

* **Para cargar el banco extendido de preguntas oficiales de examen JLPT N5/N4:**
py agregar_jlpt.py

## Estructura de la Carpeta del Proyecto

Para que el ejecutable y los scripts funcionen sin dar errores, los archivos de tu carpeta "MiAppIdiomas" deben estar organizados exactamente de esta forma:

MiAppIdiomas/
├── main.py                # Código fuente de la aplicación
├── generar_datos.py       # Script de datos iniciales
├── agregar_vocab.py       # Script de vocabulario C1 (Lote 1)
├── agregar_vocab_2.py     # Script de vocabulario C1 (Lote 2)
├── agregar_jlpt.py        # Script de preguntas JLPT
├── main.exe               # Tu aplicación de escritorio ejecutable
├── vocab_c1.json          # Archivo de base de datos de inglés
├── kana.json              # Archivo de base de datos de silabarios
├── jlpt.json              # Archivo de base de datos del simulador
└── README.md              # Este manual de instrucciones

## Cómo Añadir Más Preguntas o Palabras Manualmente

Si quieres seguir expandiendo tus listas de vocabulario o exámenes sin usar la consola de comandos:

1. Ve a tu carpeta "MiAppIdiomas".
2. Haz clic derecho sobre cualquiera de los archivos con extensión ".json" (por ejemplo, "vocab_c1.json").
3. Selecciona "Abrir con" -> "Bloc de notas" (o ábrelo en VS Code).
4. Copia una de las preguntas existentes, escribe una coma (,) después de la llave de cierre (}) de la pregunta anterior, pega el bloque y edita los textos respetando las comillas y las llaves.
5. Guarda el documento (Ctrl + G en Bloc de notas) y abre tu aplicación. Los cambios se reflejarán de inmediato.