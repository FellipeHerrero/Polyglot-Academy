# filepath: agregar_jlpt.py
import json
import os

archivo = "jlpt.json"
if os.path.exists(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        try:
            jlpt_existente = json.load(f)
        except json.JSONDecodeError:
            jlpt_existente = []
else:
    jlpt_existente = []

# Lote de preguntas adicionales JLPT N5 y N4
nuevas_preguntas = [
    {
        "nivel": "N5",
        "pregunta": "毎日、友達___学校へ行きます。",
        "opciones": ["と", "で", "を", "に"],
        "correcta": "と",
        "frase_completa": "毎日友達と学校へ行きます",
        "lectura_romaji": "maianichi tomodachi to gakkou e ikimashita",
        "explicacion": "La partícula 'と' (to) se traduce como 'con' cuando acompaña a un ser vivo. Indica la compañía con la que se realiza la acción (ir a la escuela con un amigo)."
    },
    {
        "nivel": "N5",
        "pregunta": "部屋の中に猫___います。",
        "opciones": ["が", "を", "に", "は"],
        "correcta": "が",
        "frase_completa": "部屋の中に猫がいます",
        "lectura_romaji": "heya no naka ni neko ga imasu",
        "explicacion": "Para expresar la existencia de seres vivos usando 'います' (imasu), el sujeto existente se marca con la partícula 'が' (ga). El lugar '部屋の中' se marca con 'に'."
    },
    {
        "nivel": "N5",
        "pregunta": "昨日、日本語___勉強しました。",
        "opciones": ["を", "が", "に", "で"],
        "correcta": "を",
        "frase_completa": "昨日日本語を勉強しました",
        "lectura_romaji": "kinou nihongo o benkyou shimashita",
        "explicacion": "La partícula 'を' (o) marca el objeto directo. En este caso, '日本語' (idioma japonés) es el objeto que recibe la acción del verbo transitivo '勉強しました' (estudiar)."
    },
    {
        "nivel": "N5",
        "pregunta": "車の中に傘___あります。",
        "opciones": ["が", "を", "に", "は"],
        "correcta": "が",
        "frase_completa": "車の中に傘があります",
        "lectura_romaji": "kuruma no naka ni kasa ga arimasu",
        "explicacion": "Con el verbo de existencia de objetos inanimados 'あります' (arimasu), el objeto se marca con 'が' (ga). Para seres vivos se usaría 'います' (imasu)."
    },
    {
        "nivel": "N5",
        "pregunta": "一緒に映画に行き___か。",
        "opciones": ["ましょう", "ます", "ません", "たい"],
        "correcta": "ません",
        "frase_completa": "一緒に映画に行きませんか",
        "lectura_romaji": "issho ni eiga ni ikimasen ka",
        "explicacion": "La estructura 'Verbo en forma -masu (sin masu) + ませんか' (-masen ka) es la forma más natural y educada de invitar o proponer un plan a alguien ('¿Por qué no vamos juntos...?')."
    },
    {
        "nivel": "N4",
        "pregunta": "ご飯を___前に、手を洗います。",
        "opciones": ["食べる", "食べて", "食べます", "食べた"],
        "correcta": "食べる",
        "frase_completa": "ご飯を食べる前に手を洗います",
        "lectura_romaji": "gohan o taberu mae ni te o araimasu",
        "explicacion": "Para expresar 'antes de hacer [Acción]', se utiliza siempre el verbo en su forma de diccionario o infinitivo (食べる) seguido de '前に' (mae ni)."
    },
    {
        "nivel": "N4",
        "pregunta": "頭が痛いので、早く寝___ほうがいいです。",
        "opciones": ["た", "て", "ます", "る"],
        "correcta": "た",
        "frase_completa": "頭が痛いので早く寝たほうがいいです",
        "lectura_romaji": "atama ga itai node hayaku neta hou ga ii desu",
        "explicacion": "La estructura para dar un consejo o sugerencia fuerte ('Es mejor que hagas...') se forma con el verbo en pasado informal (forma -ta: 寝た) + 'ほうがいいです'."
    },
    {
        "nivel": "N4",
        "pregunta": "この部屋は、寒___ないです。",
        "opciones": ["く", "に", "で", "くあ"],
        "correcta": "く",
        "frase_completa": "この部屋は寒くないです",
        "lectura_romaji": "kono heya wa samukunai desu",
        "explicacion": "Para negar un adjetivo de tipo -i (寒い - samui, frío), se elimina la 'い' final y se añade 'くないです' (kunai desu), quedando '寒くないです' (no hace frío)."
    },
    {
        "nivel": "N4",
        "pregunta": "昨日、友達に本を貸して___ました。",
        "opciones": ["もらいました", "あげました", "くれました", "やりました"],
        "correcta": "もらいました",
        "frase_completa": "昨日友達に本を貸してもらいました",
        "lectura_romaji": "kinou tomodachi ni hon o kashite moraimashita",
        "explicacion": "La estructura '-te もらう' (te morau) significa que el sujeto recibió el favor de que otra persona hiciera algo por él. Yo recibí el favor de que mi amigo me prestara un libro."
    },
    {
        "nivel": "N4",
        "pregunta": "ニュースによると、明日雨が降る___です。",
        "opciones": ["そうです", "らしい", "みたい", "はず"],
        "correcta": "そうです",
        "frase_completa": "ニュースによると明日雨が降るそうです",
        "lectura_romaji": "nyuusu ni yoru to ashita ame ga furu sou desu",
        "explicacion": "La estructura 'Forma diccionario + そうです' (sou desu) precedida de '～によると' (según...) se utiliza para reportar información de terceros ('He oído que...' / 'Se dice que...')."
    }
]

# Unir listas evitando duplicados en base al campo "pregunta"
preguntas_existentes = {q["pregunta"].lower() for q in jlpt_existente}
nuevos_agregados = 0

for item in nuevas_preguntas:
    if item["pregunta"].lower() not in preguntas_existentes:
        jlpt_existente.append(item)
        nuevos_agregados += 1

# Guardar de nuevo en el archivo JSON
with open(archivo, "w", encoding="utf-8") as f:
    json.dump(jlpt_existente, f, ensure_ascii=False, indent=4)

print("¡PROCESO COMPLETADO!")
print(f"-> Se cargaron {nuevos_agregados} nuevas preguntas oficiales del JLPT.")
print(f"-> Total actual de preguntas en tu app: {len(jlpt_existente)} ejercicios.")