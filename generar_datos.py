# filepath: generar_datos.py
import json

# 1. BASE DE DATOS COMPLETA DE KANAS (92 caracteres básicos)
kana_completo = [
    # Hiragana
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
    {"caracter": "さ", "romaji": "sa", "tipo": "hiragana"},
    {"caracter": "し", "romaji": "shi", "tipo": "hiragana"},
    {"caracter": "す", "romaji": "su", "tipo": "hiragana"},
    {"caracter": "せ", "romaji": "se", "tipo": "hiragana"},
    {"caracter": "そ", "romaji": "so", "tipo": "hiragana"},
    {"caracter": "た", "romaji": "ta", "tipo": "hiragana"},
    {"caracter": "ち", "romaji": "chi", "tipo": "hiragana"},
    {"caracter": "つ", "romaji": "tsu", "tipo": "hiragana"},
    {"caracter": "て", "romaji": "te", "tipo": "hiragana"},
    {"caracter": "と", "romaji": "to", "tipo": "hiragana"},
    {"caracter": "な", "romaji": "na", "tipo": "hiragana"},
    {"caracter": "に", "romaji": "ni", "tipo": "hiragana"},
    {"caracter": "ぬ", "romaji": "nu", "tipo": "hiragana"},
    {"caracter": "ね", "romaji": "ne", "tipo": "hiragana"},
    {"caracter": "の", "romaji": "no", "tipo": "hiragana"},
    {"caracter": "は", "romaji": "ha", "tipo": "hiragana"},
    {"caracter": "ひ", "romaji": "hi", "tipo": "hiragana"},
    {"caracter": "ふ", "romaji": "fu", "tipo": "hiragana"},
    {"caracter": "へ", "romaji": "he", "tipo": "hiragana"},
    {"caracter": "ほ", "romaji": "ho", "tipo": "hiragana"},
    {"caracter": "ま", "romaji": "ma", "tipo": "hiragana"},
    {"caracter": "み", "romaji": "mi", "tipo": "hiragana"},
    {"caracter": "む", "romaji": "mu", "tipo": "hiragana"},
    {"caracter": "め", "romaji": "me", "tipo": "hiragana"},
    {"caracter": "も", "romaji": "mo", "tipo": "hiragana"},
    {"caracter": "や", "romaji": "ya", "tipo": "hiragana"},
    {"caracter": "ゆ", "romaji": "yu", "tipo": "hiragana"},
    {"caracter": "よ", "romaji": "yo", "tipo": "hiragana"},
    {"caracter": "ら", "romaji": "ra", "tipo": "hiragana"},
    {"caracter": "り", "romaji": "ri", "tipo": "hiragana"},
    {"caracter": "る", "romaji": "ru", "tipo": "hiragana"},
    {"caracter": "れ", "romaji": "re", "tipo": "hiragana"},
    {"caracter": "ろ", "romaji": "ro", "tipo": "hiragana"},
    {"caracter": "わ", "romaji": "wa", "tipo": "hiragana"},
    {"caracter": "を", "romaji": "wo", "tipo": "hiragana"},
    {"caracter": "ん", "romaji": "n", "tipo": "hiragana"},
    # Katakana
    {"caracter": "ア", "romaji": "a", "tipo": "katakana"},
    {"caracter": "イ", "romaji": "i", "tipo": "katakana"},
    {"caracter": "ウ", "romaji": "u", "tipo": "katakana"},
    {"caracter": "エ", "romaji": "e", "tipo": "katakana"},
    {"caracter": "オ", "romaji": "o", "tipo": "katakana"},
    {"caracter": "カ", "romaji": "ka", "tipo": "katakana"},
    {"caracter": "キ", "romaji": "ki", "tipo": "katakana"},
    {"caracter": "ク", "romaji": "ku", "tipo": "katakana"},
    {"caracter": "ケ", "romaji": "ke", "tipo": "katakana"},
    {"caracter": "コ", "romaji": "ko", "tipo": "katakana"},
    {"caracter": "サ", "romaji": "sa", "tipo": "katakana"},
    {"caracter": "シ", "romaji": "shi", "tipo": "katakana"},
    {"caracter": "ス", "romaji": "su", "tipo": "katakana"},
    {"caracter": "セ", "romaji": "se", "tipo": "katakana"},
    {"caracter": "ソ", "romaji": "so", "tipo": "katakana"},
    {"caracter": "タ", "romaji": "ta", "tipo": "katakana"},
    {"caracter": "チ", "romaji": "chi", "tipo": "katakana"},
    {"caracter": "ツ", "romaji": "tsu", "tipo": "katakana"},
    {"caracter": "テ", "romaji": "te", "tipo": "katakana"},
    {"caracter": "ト", "romaji": "to", "tipo": "katakana"},
    {"caracter": "ナ", "romaji": "na", "tipo": "katakana"},
    {"caracter": "ニ", "romaji": "ni", "tipo": "katakana"},
    {"caracter": "ヌ", "romaji": "nu", "tipo": "katakana"},
    {"caracter": "ネ", "romaji": "ne", "tipo": "katakana"},
    {"caracter": "ノ", "romaji": "no", "tipo": "katakana"},
    {"caracter": "ハ", "romaji": "ha", "tipo": "katakana"},
    {"caracter": "ヒ", "romaji": "hi", "tipo": "katakana"},
    {"caracter": "フ", "romaji": "fu", "tipo": "katakana"},
    {"caracter": "ヘ", "romaji": "he", "tipo": "katakana"},
    {"caracter": "ホ", "romaji": "ho", "tipo": "katakana"},
    {"caracter": "マ", "romaji": "ma", "tipo": "katakana"},
    {"caracter": "ミ", "romaji": "mi", "tipo": "katakana"},
    {"caracter": "ム", "romaji": "mu", "tipo": "katakana"},
    {"caracter": "メ", "romaji": "me", "tipo": "katakana"},
    {"caracter": "モ", "romaji": "mo", "tipo": "katakana"},
    {"caracter": "ヤ", "romaji": "ya", "tipo": "katakana"},
    {"caracter": "ユ", "romaji": "yu", "tipo": "katakana"},
    {"caracter": "ヨ", "romaji": "yo", "tipo": "katakana"},
    {"caracter": "ラ", "romaji": "ra", "tipo": "katakana"},
    {"caracter": "リ", "romaji": "ri", "tipo": "katakana"},
    {"caracter": "ル", "romaji": "ru", "tipo": "katakana"},
    {"caracter": "レ", "romaji": "re", "tipo": "katakana"},
    {"caracter": "ロ", "romaji": "ro", "tipo": "katakana"},
    {"caracter": "ワ", "romaji": "wa", "tipo": "katakana"},
    {"caracter": "ヲ", "romaji": "wo", "tipo": "katakana"},
    {"caracter": "ン", "romaji": "n", "tipo": "katakana"}
]

# 2. BANCO DE PREGUNTAS CLAVE JLPT N5/N4
jlpt_banco = [
    {
        "nivel": "N5",
        "pregunta": "私は毎朝コーヒー___飲みます。",
        "opciones": ["を", "が", "に", "で"],
        "correcta": "を",
        "frase_completa": "私は毎朝コーヒーを飲みます",
        "lectura_romaji": "watashi wa maiasa koohii o nomimasu",
        "explicacion": "La partícula 'を' (o) marca el objeto directo de la acción. Aquí, 'コーヒー' (café) es el objeto que se bebe."
    },
    {
        "nivel": "N5",
        "pregunta": "図書館で本___借りました。",
        "opciones": ["を", "が", "に", "で"],
        "correcta": "を",
        "frase_completa": "図書館で本を借りました",
        "lectura_romaji": "toshokan de hon o karimashita",
        "explicacion": "Se utiliza 'を' (o) para enlazar el objeto directo '本' (libro) con el verbo transitivo '借りました' (tomar prestado)."
    },
    {
        "nivel": "N5",
        "pregunta": "日曜日___テニスをします。",
        "opciones": ["に", "を", "で", "が"],
        "correcta": "に",
        "frase_completa": "日曜日にテニスをします",
        "lectura_romaji": "nichiyoubi ni tenisu o shimasu",
        "explicacion": "La partícula 'に' (ni) se añade detrás de palabras que expresan un tiempo específico (como los días de la semana) para marcar el momento de la acción."
    },
    {
        "nivel": "N5",
        "pregunta": "このペン___書いてください。",
        "opciones": ["で", "に", "を", "が"],
        "correcta": "で",
        "frase_completa": "このペンで書いてください",
        "lectura_romaji": "kono pen de kaite kudasai",
        "explicacion": "La partícula 'で' (de) indica el medio, herramienta o instrumento que se utiliza para realizar la acción (escribir con este bolígrafo)."
    },
    {
        "nivel": "N5",
        "pregunta": "駅までタクシー___五分です。",
        "opciones": ["で", "に", "から", "まで"],
        "correcta": "で",
        "frase_completa": "駅までタクシーで五分です",
        "lectura_romaji": "eki made takushii de gofun desu",
        "explicacion": "La partícula 'で' aquí define el medio de transporte o la limitación física bajo la cual toma lugar el trayecto."
    },
    {
        "nivel": "N4",
        "pregunta": "雨が降って___、学校に行きます。",
        "opciones": ["も", "て", "たら", "なら"],
        "correcta": "も",
        "frase_completa": "雨が降っても学校に行きます",
        "lectura_romaji": "ame ga futtemo gakkou ni ikimasu",
        "explicacion": "La estructura '-te + も' (futtemo) expresa concesión extrema: 'Incluso si / aunque llueva, iré a la escuela'."
    },
    {
        "nivel": "N4",
        "pregunta": "先生はもうお帰り___。",
        "opciones": ["になりました", "しました", "でした", "にしました"],
        "correcta": "init", # placeholder corregido abajo
        "frase_completa": "先生はもうお帰りになりました",
        "lectura_romaji": "sensei wa mou okaeri ni narimashita",
        "explicacion": "La estructura de respeto (Keigo) se forma con 'お + raíz verbal de la forma masu + になる'. Regresar es '帰ります', su raíz es '帰り'."
    },
    {
        "nivel": "N4",
        "pregunta": "漢字が難しくて、書け___。",
        "opciones": ["ません", "ます", "ない", "なかった"],
        "correcta": "ません",
        "frase_completa": "漢字が難しくて書けません",
        "lectura_romaji": "kanji ga muzukashikute kakemasen",
        "explicacion": "El verbo '書く' (escribir) se convierte en potencial '書ける' (poder escribir). Su forma negativa educada es '書けません' (no poder escribir)."
    },
    {
        "nivel": "N4",
        "pregunta": "テレビを___ながらご飯を食べます。",
        "opciones": ["見", "見る", "見て", "見た"],
        "correcta": "見",
        "frase_completa": "テレビを見ながらご飯を食べます",
        "lectura_romaji": "terebi o minagara gohan o tabemasu",
        "explicacion": "La partícula gramatical 'ながら' (nagara) denota acciones simultáneas y se añade directamente a la raíz (stem) del verbo (forma -masu sin 'masu')."
    },
    {
        "nivel": "N4",
        "pregunta": "日本語が上手に___なりました。",
        "opciones": ["に", "な", "を", "が"],
        "correcta": "に",
        "frase_completa": "日本語が上手になりました",
        "lectura_romaji": "nihongo ga jouzu ni narimashita",
        "explicacion": "Para indicar cambio de estado con un adjetivo de tipo -na (上手), se remueve el 'na' y se agrega la partícula 'に' seguida de 'なる' (narimashita)."
    }
]
# Ajustar corrector de keigo en el array anterior
jlpt_banco[6]["correcta"] = "になりました"

# 3. BASE DE DATOS DE INGLÉS C1 AVANZADO (Modismos, Colocaciones y Phrasal Verbs)
vocab_c1_completo = [
    {
        "es": "Quemar las pestañas / Estudiar o trabajar hasta altas horas de la noche",
        "pt": "Queimar as pestanas / Estudar ou trabalhar até tarde da noite",
        "en": "burn the midnight oil",
        "explicacion": "Significa trabajar arduamente durante la noche. Proviene de la época previa a la electricidad, cuando las personas debían consumir el aceite de sus lámparas para tener luz y seguir trabajando."
    },
    {
        "es": "Tomar el camino más fácil / Ahorrar tiempo o dinero a costa de la calidad",
        "pt": "Pegar atalhos / Fazer algo de forma desleixada para economizar tempo ou dinheiro",
        "en": "cut corners",
        "explicacion": "Proviene de la hípica o la conducción, donde recortar las esquinas de una ruta ahorra trayecto, pero es sumamente peligroso y antideportivo."
    },
    {
        "es": "Quitarle el protagonismo a alguien / Adelantarse a las ideas de otro",
        "pt": "Roubar a cena / Tomar o crédito pelas ideias de outra pessoa",
        "en": "steal someone's thunder",
        "explicacion": "Nace en el siglo XVIII cuando el dramaturgo John Dennis inventó un método para simular el sonido del trueno en el teatro. Su obra fracasó, pero otros teatros copiaron su truco del trueno en producciones exitosas, 'robándole' su trueno."
    },
    {
        "es": "Tomar algo con pinzas / No creerse algo al pie de la letra",
        "pt": "Não levar totalmente a sério / Ter um pé atrás com alguma informação",
        "en": "take it with a grain of salt",
        "explicacion": "Se remonta a antiguos tratados de medicina donde se sugería ingerir venenos con un pequeño grano de sal para neutralizar o digerir mejor sus efectos letales."
    },
    {
        "es": "Estar muy atento / Estar sumamente concentrado y listo",
        "pt": "Estar esperto / Estar muito atento e focado",
        "en": "on the ball",
        "explicacion": "Se originó en deportes de pelota (béisbol o cricket), donde mantener la vista estrictamente en el balón era el factor de éxito indispensable."
    },
    {
        "es": "No hay mal que por bien no venga / Una bendición disfrazada",
        "pt": "Há males que vêm para o bem / Uma bênção disfarçada",
        "en": "blessing in disguise",
        "explicacion": "Describe un evento que inicialmente parece una desgracia absoluta, pero que a largo plazo desata consecuencias extraordinariamente positivas."
    },
    {
        "es": "Sentirse un poco enfermo o indispuesto",
        "pt": "Sentir-se um pouco indisposto ou doente",
        "en": "under the weather",
        "explicacion": "Viene del lenguaje marítimo. Cuando los marineros se mareaban por tormentas, iban bajo la cubierta del barco para resguardarse del clima ('under the weather') y descansar."
    },
    {
        "es": "Estar extremadamente feliz / Estar en el séptimo cielo",
        "pt": "Estar extremamente feliz / Estar nas nuvens",
        "en": "be on cloud nine",
        "explicacion": "El término proviene de las clasificaciones meteorológicas antiguas, donde la 'Nube Nueve' (cumulonimbo) era la nube más alta y majestuosa que existía."
    },
    {
        "es": "Ladrarle al árbol equivocado / Culpar o investigar a la persona errónea",
        "pt": "Procurar no lugar errado / Acusar a pessoa errada",
        "en": "bark up the wrong tree",
        "explicacion": "Nace de los perros de caza que perseguían mapaches hasta los árboles y terminaban ladrándole a un árbol vacío porque el animal ya había escapado."
    },
    {
        "es": "Llorar sobre la leche derramada / Lamentarse por algo irreversible",
        "pt": "Chorar pelo leite derramado",
        "en": "cry over spilled milk",
        "explicacion": "Expresión clásica que enfatiza la inutilidad de gastar energía preocupándose por un error del pasado que no se puede cambiar."
    },
    {
        "es": "Empezar de cero / Volver a la mesa de dibujo",
        "pt": "Voltar à estaca zero / Recomeçar um projeto do início",
        "en": "back to the drawing board",
        "explicacion": "Popularizada en los años 40 por caricaturas de ingenieros aeronáuticos cuyos aviones de prueba se estrellaban, obligándolos a regresar a sus tableros de diseño físico."
    },
    {
        "es": "Hacer de abogado del diablo / Argumentar en contra solo por debatir",
        "pt": "Fazer o papel de advogado do diabo",
        "en": "play devil's advocate",
        "explicacion": "Viene de un proceso formal de la Iglesia Católica donde se designaba a un clérigo para buscar defectos o falsedades en la vida de un candidato a la canonización."
    },
    {
        "es": "Quemar puentes / Cortar relaciones de forma definitiva",
        "pt": "Queimar pontes / Cortar relações de forma irreversível",
        "en": "burn bridges",
        "explicacion": "Proviene de tácticas militares donde los ejércitos invasores destruían los puentes detrás de ellos para eliminar cualquier tentación o posibilidad de retirada."
    },
    {
        "es": "Subirse al carro de la victoria / Seguir una moda o corriente popular",
        "pt": "Entrar na onda / Seguir uma tendência popular",
        "en": "jump on the bandwagon",
        "explicacion": "En la política estadounidense del siglo XIX, se usaban carros con bandas musicales para atraer multitudes; los políticos se subían a ellos para ganar simpatía rápida."
    },
    {
        "es": "Mantener algo a raya / Evitar que un problema se acerque",
        "pt": "Manter sob controle / Evitar que algo ruim se aproxime",
        "en": "keep something at bay",
        "explicacion": "Se remonta a las batallas navales y cacerías donde las presas acorraladas hacían frente a sus perseguidores para evitar que se acercaran demasiado."
    }
]

# Guardar bases de datos masivas sobreescribiendo los JSON locales
with open("kana.json", "w", encoding="utf-8") as f:
    json.dump(kana_completo, f, ensure_ascii=False, indent=4)

with open("jlpt.json", "w", encoding="utf-8") as f:
    json.dump(jlpt_banco, f, ensure_ascii=False, indent=4)

with open("vocab_c1.json", "w", encoding="utf-8") as f:
    json.dump(vocab_c1_completo, f, ensure_ascii=False, indent=4)

print("¡ÉXITO ROTUNDO!")
print(f"-> Se han cargado {len(kana_completo)} caracteres básicos en kana.json.")
print(f"-> Se han cargado {len(jlpt_banco)} preguntas oficiales en jlpt.json.")
print(f"-> Se han cargado {len(vocab_c1_completo)} modismos de nivel C1 en vocab_c1.json.")