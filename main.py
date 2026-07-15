# filepath: main.py
import customtkinter as ctk
import speech_recognition as sr
import threading
import json
import os
import random

# Configuración global de la interfaz
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class AppIdiomas(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Polyglot Academy - C1 English & JLPT N4 Japanese")
        self.geometry("1000x650")
        self.resizable(False, False)

        # Inicializar bases de datos locales
        self.inicializar_bases_de_datos()

        # ---- CONFIGURACIÓN DE GRID ----
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # ---- MENÚ LATERAL (SIDEBAR) ----
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="POLYGLOT\nACADEMY", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=20)

        # Botones del Menú
        self.btn_inicio = ctk.CTkButton(self.sidebar_frame, text="🏠 Inicio", command=self.mostrar_inicio, fg_color="transparent", anchor="w")
        self.btn_inicio.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.btn_vocab = ctk.CTkButton(self.sidebar_frame, text="📖 Vocabulario C1", command=self.mostrar_vocabulario, fg_color="transparent", anchor="w")
        self.btn_vocab.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.btn_kana = ctk.CTkButton(self.sidebar_frame, text="⛩️ Hiragana/Katakana", command=self.mostrar_kana, fg_color="transparent", anchor="w")
        self.btn_kana.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        self.btn_jlpt = ctk.CTkButton(self.sidebar_frame, text="📝 JLPT N5/N4", command=self.mostrar_jlpt, fg_color="transparent", anchor="w")
        self.btn_jlpt.grid(row=4, column=0, padx=20, pady=10, sticky="ew")

        # ---- ÁREA DE CONTENIDO PRINCIPAL ----
        self.content_frame = ctk.CTkFrame(self, corner_radius=15, fg_color="#1E1E1E")
        self.content_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
        self.mostrar_inicio()

    def inicializar_bases_de_datos(self):
        """Crea o expande los archivos JSON con abundante contenido didáctico."""
        # 1. Base de datos de Vocabulario Inglés C1 (Se mantiene)
        if not os.path.exists("vocab_c1.json"):
            datos_vocab = [
                {
                    "es": "Hacer de tripas corazón / Aceptar una situación difícil con valor",
                    "pt": "Engolir o sapo / Aguentar firme e aceitar uma situação difícil",
                    "en": "bite the bullet",
                    "explicacion": "'Bite the bullet' significa enfrentar una situación inevitable y dolorosa con valentía. Proviene de la antigua práctica militar de morder una bala para soportar el dolor físico."
                },
                {
                    "es": "Dejar de trabajar en algo por el resto del día / Dar algo por terminado",
                    "pt": "Encerrar os trabalhos por hoje / Dar por terminado",
                    "en": "call it a day",
                    "explicacion": "'Call it a day' se usa para dar por terminada una jornada de trabajo o estudio porque se ha hecho suficiente."
                },
                {
                    "es": "Irse a dormir",
                    "pt": "Ir dormir / Ir para a cama",
                    "en": "hit the sack",
                    "explicacion": "'Hit the sack' es un modismo muy común. El 'sack' (saco) hace referencia al saco de paja que se usaba antiguamente como colchón."
                }
            ]
            with open("vocab_c1.json", "w", encoding="utf-8") as f:
                json.dump(datos_vocab, f, ensure_ascii=False, indent=4)

        # 2. Base de datos de Hiragana/Katakana expandida
        if not os.path.exists("kana.json"):
            datos_kana = [
                {"caracter": "あ", "romaji": "a", "tipo": "hiragana"},
                {"caracter": "い", "romaji": "i", "tipo": "hiragana"},
                {"caracter": "う", "romaji": "u", "tipo": "hiragana"},
                {"caracter": "え", "romaji": "e", "tipo": "hiragana"},
                {"caracter": "お", "romaji": "o", "tipo": "hiragana"},
                {"caracter": "か", "romaji": "ka", "tipo": "hiragana"},
                {"caracter": "き", "romaji": "ki", "tipo": "hiragana"},
                {"caracter": "く", "romaji": "ku", "tipo": "hiragana"},
                {"caracter": "け", "romaji": "ke", "tipo": "hiragana"},
                {"caracter": "こ", "romaji": "ko", "tipo": "hiragana"},
                {"caracter": "ア", "romaji": "a", "tipo": "katakana"},
                {"caracter": "イ", "romaji": "i", "tipo": "katakana"},
                {"caracter": "ウ", "romaji": "u", "tipo": "katakana"},
                {"caracter": "エ", "romaji": "e", "tipo": "katakana"},
                {"caracter": "オ", "romaji": "o", "tipo": "katakana"},
                {"caracter": "カ", "romaji": "ka", "tipo": "katakana"}
            ]
            with open("kana.json", "w", encoding="utf-8") as f:
                json.dump(datos_kana, f, ensure_ascii=False, indent=4)

        # 3. Base de datos de JLPT N5/N4 expandida
        if not os.path.exists("jlpt.json"):
            datos_jlpt = [
                {
                    "nivel": "N5",
                    "pregunta": "あそこに犬___います。",
                    "opciones": ["は", "が", "を", "に"],
                    "correcta": "が",
                    "frase_completa": "あそこに犬がいます",
                    "lectura_romaji": "asoko ni inu ga imasu",
                    "explicacion": "La partícula 'が' (ga) se utiliza para marcar el sujeto que existe (犬 - perro). Con verbos de existencia como 'います' (imasu), el sujeto se indica con 'が'."
                },
                {
                    "nivel": "N4",
                    "pregunta": "日本語を勉強___始めました。",
                    "opciones": ["し", "する", "して", "した"],
                    "correcta": "し",
                    "frase_completa": "日本語を勉強し始めました",
                    "lectura_romaji": "nihongo o benkyou shi hajimemashita",
                    "explicacion": "Para decir 'comenzar a hacer algo', usamos la raíz del verbo en forma -masu (し) + 始める (hajimeru). Por tanto: '勉強し始めました' (comencé a estudiar)."
                },
                {
                    "nivel": "N5",
                    "pregunta": "昨日、デパート___行きました。",
                    "opciones": ["を", "が", "へ", "は"],
                    "correcta": "へ",
                    "frase_completa": "昨日デパートへ行きました",
                    "lectura_romaji": "kinou depaato e ikimashita",
                    "explicacion": "La partícula 'へ' (leída como 'e') indica la dirección del movimiento hacia un lugar, en este caso, hacia el centro comercial (デパート)."
                }
            ]
            with open("jlpt.json", "w", encoding="utf-8") as f:
                json.dump(datos_jlpt, f, ensure_ascii=False, indent=4)


    # ---- MÉTODOS DE NAVEGACIÓN ----
    def limpiar_pantalla(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def resaltar_boton(self, boton_activo):
        botones = [self.btn_inicio, self.btn_vocab, self.btn_kana, self.btn_jlpt]
        for btn in botones:
            if btn == boton_activo:
                btn.configure(fg_color="#1F6AA5")
            else:
                btn.configure(fg_color="transparent")

    def mostrar_inicio(self):
        self.limpiar_pantalla()
        self.resaltar_boton(self.btn_inicio)

        titulo = ctk.CTkLabel(self.content_frame, text="¡Bienvenido a tu Academia de Idiomas!", font=ctk.CTkFont(size=24, weight="bold"))
        titulo.pack(pady=(40, 20))

        subtitulo = ctk.CTkLabel(self.content_frame, text="Tu puente nativo: Español ➡️ Fluido: Portugués\nMetas: Inglés C1 | Japonés JLPT N4", font=ctk.CTkFont(size=14))
        subtitulo.pack(pady=10)

        descripcion = ctk.CTkLabel(self.content_frame, text="Utiliza el menú de la izquierda para navegar por los módulos.\nCada sección interactúa con tu voz para garantizar tu aprendizaje práctico.", font=ctk.CTkFont(size=12), text_color="gray")
        descripcion.pack(pady=40)

    # ---- MÓDULO INGLÉS C1 (Fase 5) ----
    def mostrar_vocabulario(self):
        self.limpiar_pantalla()
        self.resaltar_boton(self.btn_vocab)
        
        with open("vocab_c1.json", "r", encoding="utf-8") as f:
            self.lista_vocab = json.load(f)
        
        self.tarjeta_actual = random.choice(self.lista_vocab)

        titulo = ctk.CTkLabel(self.content_frame, text="Módulo: Vocabulario & Expresiones Avanzadas C1", font=ctk.CTkFont(size=20, weight="bold"))
        titulo.pack(pady=(20, 10))

        instruccion = ctk.CTkLabel(self.content_frame, text="¿Cómo se dice esta expresión en inglés avanzado (C1)?", font=ctk.CTkFont(size=14, slant="italic"), text_color="#A0A0A0")
        instruccion.pack(pady=5)

        self.lang_card = ctk.CTkFrame(self.content_frame, corner_radius=10, fg_color="#2D2D2D")
        self.lang_card.pack(pady=15, fill="x", padx=40)

        lbl_es = ctk.CTkLabel(self.lang_card, text=f"🇪🇸 Español: {self.tarjeta_actual['es']}", font=ctk.CTkFont(size=15, weight="bold"), anchor="w")
        lbl_es.pack(pady=10, padx=20, anchor="w")

        lbl_pt = ctk.CTkLabel(self.lang_card, text=f"🇵🇹 Português: {self.tarjeta_actual['pt']}", font=ctk.CTkFont(size=15, weight="bold"), anchor="w", text_color="#34A853")
        lbl_pt.pack(pady=(0, 10), padx=20, anchor="w")

        self.lbl_estado = ctk.CTkLabel(self.content_frame, text="Presiona el botón para responder hablando en inglés...", font=ctk.CTkFont(size=13), text_color="gray")
        self.lbl_estado.pack(pady=10)

        self.btn_grabar = ctk.CTkButton(self.content_frame, text="Responder con Voz 🎙️", command=self.escuchar_respuesta_c1, fg_color="#10B981", hover_color="#059669")
        self.btn_grabar.pack(pady=10)

        self.btn_siguiente = ctk.CTkButton(self.content_frame, text="Siguiente Expresión ➡️", command=self.mostrar_vocabulario, fg_color="#3B82F6", hover_color="#2563EB")
        self.btn_siguiente.pack(pady=5)

        self.txt_explicacion = ctk.CTkTextbox(self.content_frame, height=120, width=650, corner_radius=10, fg_color="#181818")
        self.txt_explicacion.pack(pady=15, padx=40)
        self.txt_explicacion.insert("1.0", "La explicación gramatical aparecerá aquí después de responder.")
        self.txt_explicacion.configure(state="disabled")

    def escuchar_respuesta_c1(self):
        self.btn_grabar.configure(state="disabled", text="Escuchando...")
        self.lbl_estado.configure(text="Sintonizando micrófono... ¡Habla ahora en inglés!", text_color="#FBBF24")
        self.update()
        threading.Thread(target=self.procesar_voz_c1, daemon=True).start()

    def procesar_voz_c1(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                r.adjust_for_ambient_noise(source, duration=0.8)
                audio = r.listen(source, timeout=6)
                respuesta_usuario = r.recognize_google(audio, language="en-US").strip().lower()
                respuesta_correcta = self.tarjeta_actual["en"].strip().lower()

                respuesta_usuario_limpia = respuesta_usuario.replace(".", "").replace(",", "").replace("'", "")
                respuesta_correcta_limpia = respuesta_correcta.replace(".", "").replace(",", "").replace("'", "")

                if respuesta_usuario_limpia == respuesta_correcta_limpia:
                    self.lbl_estado.configure(text=f"¡EXCELENTE! Pronunciaste perfectamente:\n\"{respuesta_usuario}\"", text_color="#10B981")
                else:
                    self.lbl_estado.configure(text=f"Casi... Entendí: \"{respuesta_usuario}\"\nLa respuesta correcta es: \"{self.tarjeta_actual['en']}\"", text_color="#EF4444")
                
                self.txt_explicacion.configure(state="normal")
                self.txt_explicacion.delete("1.0", "end")
                self.txt_explicacion.insert("1.0", f"Respuesta esperada: {self.tarjeta_actual['en'].upper()}\n\n{self.tarjeta_actual['explicacion']}")
                self.txt_explicacion.configure(state="disabled")

            except Exception as e:
                self.lbl_estado.configure(text="Error de reconocimiento de voz o micrófono desconectado.", text_color="#EF4444")
            finally:
                self.btn_grabar.configure(state="normal", text="Responder con Voz 🎙️")


    # ---- FASE 6: MÓDULO HIRAGANA/KATAKANA ----
    def mostrar_kana(self):
        self.limpiar_pantalla()
        self.resaltar_boton(self.btn_kana)

        with open("kana.json", "r", encoding="utf-8") as f:
            self.lista_kana = json.load(f)

        self.kana_actual = random.choice(self.lista_kana)

        titulo = ctk.CTkLabel(self.content_frame, text="Módulo: Escritura y Sonido (Hiragana & Katakana)", font=ctk.CTkFont(size=20, weight="bold"))
        titulo.pack(pady=(20, 10))

        # Cuadro de carácter grande
        self.kana_card = ctk.CTkFrame(self.content_frame, width=150, height=150, corner_radius=15, fg_color="#2D2D2D")
        self.kana_card.pack(pady=15)
        self.kana_card.pack_propagate(False)

        lbl_caracter = ctk.CTkLabel(self.kana_card, text=self.kana_actual['caracter'], font=ctk.CTkFont(size=70, weight="bold"))
        lbl_caracter.pack(expand=True)

        lbl_tipo = ctk.CTkLabel(self.content_frame, text=f"Tipo de silabario: {self.kana_actual['tipo'].upper()}", font=ctk.CTkFont(size=13), text_color="#34A853")
        lbl_tipo.pack(pady=5)

        # Generar opciones de respuesta aleatorias
        respuestas_incorrectas = list(set([k['romaji'] for k in self.lista_kana if k['romaji'] != self.kana_actual['romaji']]))
        opciones = random.sample(respuestas_incorrectas, 3)
        opciones.append(self.kana_actual['romaji'])
        random.shuffle(opciones)

        # Contenedor de botones
        self.opciones_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        self.opciones_frame.pack(pady=15)

        self.botones_opciones = []
        for i, opc in enumerate(opciones):
            btn = ctk.CTkButton(self.opciones_frame, text=opc, width=110, height=45, font=ctk.CTkFont(size=16, weight="bold"),
                                command=lambda o=opc: self.verificar_kana(o))
            btn.grid(row=0, column=i, padx=10)
            self.botones_opciones.append(btn)

        self.lbl_feedback_kana = ctk.CTkLabel(self.content_frame, text="Selecciona la romanización (romaji) correcta.", font=ctk.CTkFont(size=14))
        self.lbl_feedback_kana.pack(pady=10)

        # Siguiente
        self.btn_next_kana = ctk.CTkButton(self.content_frame, text="Siguiente Carácter ➡️", command=self.mostrar_kana, fg_color="#3B82F6")
        self.btn_next_kana.pack(pady=10)

    def verificar_kana(self, opcion):
        for btn in self.botones_opciones:
            btn.configure(state="disabled")
            if btn.cget("text") == self.kana_actual['romaji']:
                btn.configure(fg_color="#10B981") # Verde el correcto
            elif btn.cget("text") == opcion:
                btn.configure(fg_color="#EF4444") # Rojo el incorrecto si falló

        if opcion == self.kana_actual['romaji']:
            self.lbl_feedback_kana.configure(text=f"¡Correcto! '{self.kana_actual['caracter']}' se pronuncia '{self.kana_actual['romaji']}'.", text_color="#10B981")
        else:
            self.lbl_feedback_kana.configure(text=f"Incorrecto. '{self.kana_actual['caracter']}' se pronuncia '{self.kana_actual['romaji']}'.", text_color="#EF4444")


    # ---- FASE 6: MÓDULO JLPT N5/N4 CON MICRÓFONO JAPONÉS ----
    def mostrar_jlpt(self):
        self.limpiar_pantalla()
        self.resaltar_boton(self.btn_jlpt)

        with open("jlpt.json", "r", encoding="utf-8") as f:
            self.lista_jlpt = json.load(f)

        self.pregunta_actual = random.choice(self.lista_jlpt)

        titulo = ctk.CTkLabel(self.content_frame, text=f"Módulo: Práctica Oficial JLPT - {self.pregunta_actual['nivel']}", font=ctk.CTkFont(size=20, weight="bold"))
        titulo.pack(pady=(20, 10))

        # Pregunta
        self.lbl_pregunta = ctk.CTkLabel(self.content_frame, text=self.pregunta_actual['pregunta'], font=ctk.CTkFont(size=24, weight="bold"), text_color="#60A5FA")
        self.lbl_pregunta.pack(pady=20)

        # Botones de opciones
        self.opciones_jlpt_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        self.opciones_jlpt_frame.pack(pady=10)

        self.botones_jlpt = []
        for i, opc in enumerate(self.pregunta_actual['opciones']):
            btn = ctk.CTkButton(self.opciones_jlpt_frame, text=opc, width=120, height=45, font=ctk.CTkFont(size=16),
                                command=lambda o=opc: self.verificar_jlpt(o))
            btn.grid(row=0, column=i, padx=10)
            self.botones_jlpt.append(btn)

        self.lbl_feedback_jlpt = ctk.CTkLabel(self.content_frame, text="Selecciona la partícula o conjugación que va en el espacio vacío.", font=ctk.CTkFont(size=13), text_color="gray")
        self.lbl_feedback_jlpt.pack(pady=10)

        # Módulo de Micrófono Japonés (Oculto hasta responder correctamente)
        self.micro_frame = ctk.CTkFrame(self.content_frame, fg_color="#2D2D2D", corner_radius=10)
        
        self.lbl_micro_instruccion = ctk.CTkLabel(self.micro_frame, text="¡Nivel Desbloqueado! Lee la frase completa en voz alta:", font=ctk.CTkFont(size=13, weight="bold"))
        self.lbl_micro_instruccion.pack(pady=(10, 2))

        self.lbl_romaji = ctk.CTkLabel(self.micro_frame, text=f"Lectura: {self.pregunta_actual['lectura_romaji']}", font=ctk.CTkFont(size=14, slant="italic"), text_color="#FBBF24")
        self.lbl_romaji.pack(pady=5)

        self.btn_grabar_ja = ctk.CTkButton(self.micro_frame, text="Leer en Japonés 🎙️", command=self.escuchar_respuesta_ja, fg_color="#10B981", hover_color="#059669")
        self.btn_grabar_ja.pack(pady=10)

        # Cuadro de explicación
        self.txt_explicacion_jlpt = ctk.CTkTextbox(self.content_frame, height=90, width=650, corner_radius=10, fg_color="#181818")
        self.txt_explicacion_jlpt.pack(pady=10, padx=40)
        self.txt_explicacion_jlpt.insert("1.0", "La explicación gramatical de la partícula aparecerá aquí.")
        self.txt_explicacion_jlpt.configure(state="disabled")

        # Siguiente pregunta
        self.btn_next_jlpt = ctk.CTkButton(self.content_frame, text="Siguiente Pregunta ➡️", command=self.mostrar_jlpt, fg_color="#3B82F6")
        self.btn_next_jlpt.pack(pady=10)

    def verificar_jlpt(self, opcion):
        for btn in self.botones_jlpt:
            btn.configure(state="disabled")
            if btn.cget("text") == self.pregunta_actual['correcta']:
                btn.configure(fg_color="#10B981")
            elif btn.cget("text") == opcion:
                btn.configure(fg_color="#EF4444")

        # Rellenar el espacio en blanco con la respuesta correcta para visualizarla mejor
        frase_resuelta = self.pregunta_actual['pregunta'].replace("___", f" [{self.pregunta_actual['correcta']}] ")
        self.lbl_pregunta.configure(text=frase_resuelta)

        # Mostrar la explicación gramatical
        self.txt_explicacion_jlpt.configure(state="normal")
        self.txt_explicacion_jlpt.delete("1.0", "end")
        self.txt_explicacion_jlpt.insert("1.0", f"Respuesta: {self.pregunta_actual['correcta']}\n\n{self.pregunta_actual['explicacion']}")
        self.txt_explicacion_jlpt.configure(state="disabled")

        if opcion == self.pregunta_actual['correcta']:
            self.lbl_feedback_jlpt.configure(text="¡EXCELENTE! Respuesta correcta.", text_color="#10B981")
            # Desbloqueamos el panel para interactuar con la voz en japonés
            self.micro_frame.pack(pady=10, fill="x", padx=40)
        else:
            self.lbl_feedback_jlpt.configure(text="Respuesta incorrecta. Revisa la explicación gramatical.", text_color="#EF4444")

    def escuchar_respuesta_ja(self):
        self.btn_grabar_ja.configure(state="disabled", text="Escuchando japonés...")
        self.lbl_feedback_jlpt.configure(text="Micrófono encendido... Lee la frase completa.", text_color="#FBBF24")
        self.update()
        threading.Thread(target=self.procesar_voz_ja, daemon=True).start()

    def procesar_voz_ja(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                r.adjust_for_ambient_noise(source, duration=0.8)
                audio = r.listen(source, timeout=6)
                # Sintonizamos el reconocedor para que escuche idioma JAPONÉS
                voz_usuario = r.recognize_google(audio, language="ja-JP").strip()
                
                # Quitar espacios vacíos del resultado (el japonés no usa espacios)
                voz_usuario_limpia = voz_usuario.replace(" ", "").replace(" ", "")
                objetivo_limpio = self.pregunta_actual['frase_completa'].replace(" ", "").replace(" ", "")

                # Como la API a veces escribe en Kanji, Hiragana o Katakana indistintamente,
                # mostramos lo que escuchamos para que el usuario aprenda a modular.
                if voz_usuario_limpia in objetivo_limpio or objetivo_limpio in voz_usuario_limpia:
                    self.lbl_feedback_jlpt.configure(text=f"¡Perfecto! Pronunciaste excelente:\n「{voz_usuario}」", text_color="#10B981")
                else:
                    self.lbl_feedback_jlpt.configure(text=f"Escuché: 「{voz_usuario}」\nIntenta leerlo fluido de nuevo.", text_color="#FBBF24")

            except Exception as e:
                self.lbl_feedback_jlpt.configure(text="No logré capturar el audio claramente en japonés.", text_color="#EF4444")
            finally:
                self.btn_grabar_ja.configure(state="normal", text="Leer en Japonés 🎙️")


if __name__ == "__main__":
    app = AppIdiomas()
    app.mainloop()