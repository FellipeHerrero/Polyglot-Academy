# filepath: agregar_vocab.py
import json
import os

# Cargar la base de datos existente si existe, si no, empezar vacía
archivo = "vocab_c1.json"
if os.path.exists(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        try:
            vocab_existente = json.load(f)
        except json.JSONDecodeError:
            vocab_existente = []
else:
    vocab_existente = []

# Lote 1: 50 Expresiones C1 Avanzadas (Idioms, Phrasal Verbs y Business English)
nuevo_lote = [
    {
        "es": "Irse por las ramas / No ir al grano",
        "pt": "Ficar enrolando / Não ir direto ao ponto",
        "en": "beat around the bush",
        "explicacion": "Significa evitar hablar de un tema importante o doloroso. Proviene de la caza medieval: los ayudantes golpeaban los arbustos ('beat the bushes') para hacer salir a las aves antes de que los cazadores dispararan, retrasando el momento de la acción directa."
    },
    {
        "es": "Asumir las consecuencias de tus actos / 'Dar la cara'",
        "pt": "Encarar as consequências / Assumir a responsabilidade",
        "en": "face the music",
        "explicacion": "Significa aceptar el castigo o la crítica por algo que hiciste mal. Su origen es militar: cuando un soldado era expulsado del ejército deshonrosamente, se realizaba una ceremonia donde se tocaban tambores de fondo ('la música') mientras marchaba hacia afuera."
    },
    {
        "es": "Dar en el clavo / Acertar exactamente",
        "pt": "Acertar na mosca / Acertar em cheio",
        "en": "hit the nail on the head",
        "explicacion": "Expresa que alguien ha descrito una situación o resuelto un problema de la manera más precisa posible, tal como un carpintero experimentado que golpea el clavo exactamente en su cabeza."
    },
    {
        "es": "Revelar un secreto sin querer / 'Irse de la lengua'",
        "pt": "Dar com a língua nos dentes / Revelar um segredo",
        "en": "let the cat out of the bag",
        "explicacion": "Proviene de los mercados antiguos donde se vendían cerdos pequeños dentro de sacos. Los vendedores fraudulentos a veces metían gatos callejeros en su lugar. El secreto se revelaba cuando el comprador abría el saco en casa y salía el gato."
    },
    {
        "es": "Muy rara vez / Una vez cada mil años",
        "pt": "Uma vez na vida, outra na morte / Muito raramente",
        "en": "once in a blue moon",
        "explicacion": "Hace referencia a un fenómeno astronómico real: la aparición de una segunda luna llena en un mismo mes calendario, un evento inusual que ocurre aproximadamente cada 2.7 años."
    },
    {
        "es": "Perder la oportunidad por actuar tarde",
        "pt": "Perder o bonde / Perder a oportunidade",
        "en": "miss the boat",
        "explicacion": "Se utiliza cuando alguien es demasiado lento para aprovechar una gran oferta, un negocio o una situación favorable, quedándose metafóricamente en el muelle."
    },
    {
        "es": "No escatimar esfuerzos / Buscar por todos lados",
        "pt": "Não poupar esforços / Investigar minuciosamente",
        "en": "leave no stone unturned",
        "explicacion": "Tiene origen en una antigua leyenda griega sobre un general que enterró un tesoro en su tienda de campaña tras ser derrotado. El oráculo aconsejó al buscador 'no dejar ninguna piedra sin voltear' para hallarlo."
    },
    {
        "es": "Por los pelos / Por un pelo de rana",
        "pt": "Por um triz / De raspão",
        "en": "by the skin of my teeth",
        "explicacion": "Significa escapar de un peligro o lograr algo por un margen extremadamente estrecho. Proviene de una traducción literal del Libro de Job en la Biblia ('He escapado con la piel de mis dientes'), sugiriendo que los dientes no tienen piel, por lo tanto, el margen fue casi nulo."
    },
    {
        "es": "Tomar el pelo a alguien / Bromear",
        "pt": "Tirar onda com alguém / Brincar ou zoar",
        "en": "pull someone's leg",
        "explicacion": "Hoy significa bromear, pero en el Londres del siglo XIX era un método de los ladrones callejeros, quienes usaban bastones o cuerdas para hacer tropezar ('pull the leg') a las personas y robarles mientras caían."
    },
    {
        "es": "Estar indeciso / No tomar una postura",
        "pt": "Ficar em cima do muro / Indeciso",
        "en": "on the fence",
        "explicacion": "Describe a alguien que no apoya a ninguno de los dos bandos en una discusión. Metafóricamente, la persona está sentada sobre la cerca, mirando ambos lados de la propiedad sin cruzarse a ninguno."
    },
    {
        "es": "En las buenas y en las malas",
        "pt": "Na alegria e na tristeza / Custe o que custar",
        "en": "through thick and thin",
        "explicacion": "Se refiere a mantener la lealtad absoluta bajo cualquier circunstancia. Nace en los bosques feudales de Inglaterra, donde los viajeros debían avanzar a través de vegetación despejada ('thin') o follaje denso y peligroso ('thick')."
    },
    {
        "es": "Tirar la toalla / Rendirse",
        "pt": "Jogar a toalha / Desistir",
        "en": "throw in the towel",
        "explicacion": "Modismo tomado directamente del boxeo. Cuando los entrenadores veían que su boxeador ya no podía resistir más golpes y querían detener la pelea para protegerlo, arrojaban la toalla de secar el sudor al centro del ring."
    },
    {
        "es": "Trabajar en exceso de día y de noche / Agotarse",
        "pt": "Trabalhar até a exaustão / Queimar a vela nas duas pontas",
        "en": "burn the candle at both ends",
        "explicacion": "Significa gastar tus energías desmesuradamente levantándote muy temprano y acostándote muy tarde. Encender una vela por ambos extremos hace que se consuma el doble de rápido, destruyéndose a sí misma."
    },
    {
        "es": "Jugárselo todo a una sola carta / Arriesgar todo en un solo plan",
        "pt": "Apostar todas as fichas em uma coisa só",
        "en": "put all your eggs in one basket",
        "explicacion": "Advertencia clásica de negocios y finanzas: si pones todos los huevos en una misma canasta y esta se cae, los perderás absolutamente todos sin tener un respaldo."
    },
    {
        "es": "El problema obvio del que nadie quiere hablar",
        "pt": "O problema óbvio que todo mundo finge não ver",
        "en": "the elephant in the room",
        "explicacion": "Se refiere a una verdad incómoda, obvia y gigantesca que todos los presentes conocen perfectamente, pero que evitan mencionar activamente para no generar tensión o discusiones."
    },
    {
        "es": "Costar un ojo de la cara / Ser extremadamente caro",
        "pt": "Custar os olhos da cara / Extremamente caro",
        "en": "cost an arm and a leg",
        "explicacion": "Se popularizó tras las guerras del siglo XX, donde los soldados que regresaban mutilados sin un brazo o una pierna pagaban un 'costo' físico incalculable por sobrevivir al conflicto."
    },
    {
        "es": "En el último minuto / A última hora",
        "pt": "Na última hora / No último segundo",
        "en": "at the eleventh hour",
        "explicacion": "Proviene de una parábola bíblica sobre los trabajadores contratados para trabajar en un viñedo; los que llegaron a la hora número 11 (la última hora laboral del día) recibieron el mismo pago que los que trabajaron todo el día."
    },
    {
        "es": "Estar de acuerdo con alguien / Compartir la misma opinión",
        "pt": "Concordar plenamente / Estar em sintonia",
        "en": "see eye to eye",
        "explicacion": "Significa mirar directamente a los ojos de otra persona desde una misma altura física, simbolizando igualdad de pensamiento y entendimiento mutuo sin conflictos."
    },
    {
        "es": "¡Mucho éxito! / ¡Rompe una pierna! (Teatro)",
        "pt": "Boa sorte! / Quebre a perna! (Teatro)",
        "en": "break a leg",
        "explicacion": "Expresión de buena suerte usada exclusivamente en el teatro. Los actores creen que desear la suerte directamente atrae a los malos espíritus, por lo que desear algo terrible (romperse una pierna) invoca el efecto contrario."
    },
    {
        "es": "Estar al mando / Tomar las decisiones importantes",
        "pt": "Dar as cartas / Estar no comando",
        "en": "call the shots",
        "explicacion": "Proviene de la jerga de los tiradores de precisión o billaristas de alto nivel, quienes antes de realizar un tiro, anunciaban públicamente en qué parte exacta del objetivo o qué tronera golpearía la bola ('calling the shot')."
    },
    {
        "es": "De vanguardia / Lo último en tecnología",
        "pt": "De última geração / Tecnologia de ponta",
        "en": "cutting-edge",
        "explicacion": "Hace referencia a la parte más afilada de una herramienta de corte (como un bisturí o espada), la cual abre camino primero. En negocios denota innovación disruptiva."
    },
    {
        "es": "Echarse atrás en el último momento por miedo",
        "pt": "Amarelar / Desistir na última hora por medo",
        "en": "get cold feet",
        "explicacion": "Término de origen militar. Los soldados cuyos pies sufrían de congelación en las trincheras no podían marchar ni combatir, usándose luego como metáfora para quien se paraliza por el pánico escénico antes de actuar."
    },
    {
        "es": "Improvisar sobre la marcha",
        "pt": "Improvisar / Ver o que acontece no momento",
        "en": "play it by ear",
        "explicacion": "Viene del mundo de la música clásica. Tocar una pieza 'de oído' ('by ear') significa interpretarla directamente sin partitura física al frente, improvisando y adaptando las notas según el sonido."
    },
    {
        "es": "La gota que colmó el vaso",
        "pt": "A gota d'água / O limite",
        "en": "the last straw",
        "explicacion": "Abreviatura de la frase histórica: 'Es la última paja la que rompe el lomo del camello'. Describe un pequeño problema adicional que, sumado a una gran carga acumulada, provoca un colapso definitivo."
    },
    {
        "es": "Hacer algo de forma ilegal, secreta o con sobornos",
        "pt": "Por debaixo dos panos / Fazer algo ilegal ou secreto",
        "en": "under the table",
        "explicacion": "Se refiere a transacciones de dinero en efectivo o acuerdos corruptos que se realizan físicamente bajo el nivel de la mesa de reuniones para que los inspectores u otras personas no puedan ver el intercambio."
    },
    {
        "es": "Para abreviar / En pocas palabras",
        "pt": "Para encurtar a história / Resumindo",
        "en": "make a long story short",
        "explicacion": "Frase de transición utilizada para omitir detalles innecesarios de una anécdota larga y aburrida, saltando directamente al desenlace o conclusión relevante."
    },
    {
        "es": "Las acciones valen más que las palabras",
        "pt": "Ações valem mais que palavras / Atitude é tudo",
        "en": "actions speak louder than words",
        "explicacion": "Filosofía pragmática inglesa del siglo XVII. Expresa que el verdadero carácter y las intenciones de una persona se demuestran con lo que hace, no con sus promesas o discursos vacíos."
    },
    {
        "es": "Dar una falsa alarma / Mentir repetidamente hasta perder credibilidad",
        "pt": "Mentir muito até ninguém mais acreditar / Dar alarme falso",
        "en": "cry wolf",
        "explicacion": "Proviene directamente de la famosa fábula de Esopo sobre el joven pastor mentiroso que se divertía engañando a los aldeanos gritando que venía el lobo, hasta que el lobo real llegó y nadie acudió a salvarlo."
    },
    {
        "es": "Tener los pies sobre la tierra / Persona realista y humilde",
        "pt": "Pé no chão / Pessoa realista e sensata",
        "en": "down-to-earth",
        "explicacion": "Adjetivo altamente valorado en el ámbito profesional C1. Describe a una persona práctica, directa, honesta y libre de pretensiones o arrogancia intelectual."
    },
    {
        "es": "Salirse de control / Perder el orden",
        "pt": "Sair do controle / Fugir do controle",
        "en": "get out of hand",
        "explicacion": "Proviene de la equitación. Si el jinete soltaba las riendas o las perdía de las manos ('out of hand'), el caballo corría desbocado y sin control alguno."
    },
    {
        "es": "Dar el beneficio de la duda",
        "pt": "Dar o benefício da dúvida / Acreditar na pessoa",
        "en": "give someone the benefit of the doubt",
        "explicacion": "Término legal adoptado en el inglés cotidiano. Significa elegir creer la versión de una persona sobre un hecho dudoso mientras no existan pruebas irrefutables de que está mintiendo."
    },
    {
        "es": "Fracasar estrepitosamente",
        "pt": "Ir por água abaixo / Fracassar totalmente",
        "en": "go down in flames",
        "explicacion": "Originalmente hacía referencia a los aviones de combate que eran derribados y caían incendiados de forma irreversible. Hoy se usa para proyectos o presentaciones que terminan en desastre absoluto."
    },
    {
        "es": "Estar al tanto / Mantenerse informado en un grupo",
        "pt": "Estar por dentro / Estar informado",
        "en": "in the loop",
        "explicacion": "Viene de los diagramas de flujo de ingeniería y sistemas de comunicación militar, donde estar dentro del lazo cerrado ('loop') significaba recibir la información de primera mano en el círculo de decisiones."
    },
    {
        "es": "Vigilar de cerca / Echar un ojo",
        "pt": "Ficar de olho em algo / Vigiar atentamente",
        "en": "keep an eye on",
        "explicacion": "Expresión de supervisión activa que denota responsabilidad protectora sobre un objeto, niño o proceso comercial para que nada falle."
    },
    {
        "es": "Perder la habilidad o el talento que se tenía",
        "pt": "Perder o jeito / Perder o talento para algo",
        "en": "lose your touch",
        "explicacion": "Originalmente aplicada a pianistas, cirujanos o magos cuya sensibilidad táctil ('touch') en las manos disminuía con la edad, impidiéndoles ejecutar su arte con la precisión de antes."
    },
    {
        "es": "Sonarme familiar / Traer algo a la memoria",
        "pt": "Soar familiar / Trazer alguma lembrança",
        "en": "ring a bell",
        "explicacion": "Viene del uso de campanas y timbres en experimentos de condicionamiento clásico (como los de Pávlov) o alarmas domésticas destinadas a despertar un recuerdo o activar la atención inmediata."
    },
    {
        "es": "Saber algo de primera fuente / Directo de la fuente original",
        "pt": "Saber direto da fonte / Informação direta e confiável",
        "en": "straight from the horse's mouth",
        "explicacion": "Proviene del mundo de las apuestas hípicas. Para conocer la edad o el verdadero estado de salud de un caballo de carreras, la única fuente 100% confiable era examinar directamente su dentadura ('la boca del caballo')."
    },
    {
        "es": "Echar más leña al fuego / Empeorar una mala situación",
        "pt": "Piorar ainda mais a situação / Jogar sal na ferida",
        "en": "add insult to injury",
        "explicacion": "Se remonta a una antigua fábula romana donde un calvo intenta aplastar a un mosquito en su cabeza, falla, se propina un golpe doloroso a sí mismo, y el mosquito se burla de él, sumando la humillación ('insult') al daño físico ('injury')."
    },
    {
        "es": "Tener lo mejor de dos opciones distintas al mismo tiempo",
        "pt": "O melhor dos dois mundos / Aproveitar o melhor de tudo",
        "en": "the best of both worlds",
        "explicacion": "Se usa cuando un individuo logra disfrutar de las ventajas de dos situaciones totalmente opuestas sin tener que sufrir los inconvenientes de ninguna."
    },
    {
        "es": "Pensar fuera de la caja / Ser creativo e innovador",
        "pt": "Pensar fora da caixa / Ser criativo",
        "en": "think outside the box",
        "explicacion": "Nace del famoso acertijo de los nueve puntos, donde la única forma de unirlos a todos con solo cuatro líneas rectas continuas es dibujando líneas que se extiendan más allá de los límites visuales del cuadrado imaginario."
    },
    {
        "es": "Situación incierta, peligrosa o inestable",
        "pt": "Uma situação instável ou incerta / No fio da navalha",
        "en": "touch and go",
        "explicacion": "Viene del lenguaje de navegación rápida. Cuando un barco navegaba en aguas poco profundas, tocaba el fondo de arena ('touch') y debía salir de inmediato a toda velocidad ('go') antes de encallar definitivamente."
    },
    {
        "es": "Estar en el aire / Algo pendiente de decidir",
        "pt": "Estar no ar / Indeciso ou pendente",
        "en": "up in the air",
        "explicacion": "Se asocia a la imagen de hacer malabares con varios objetos. Mientras los objetos estén flotando en el aire, no se sabe con certeza cuál caerá primero ni dónde terminarán."
    },
    {
        "es": "Tú sabes tanto como yo / No tengo idea",
        "pt": "O seu palpite é tão bom quanto o meu / Não faço ideia",
        "en": "your guess is as good as mine",
        "explicacion": "Frase de camaradería C1 que se utiliza para admitir honesta y llanamente que no se tiene la menor idea de la respuesta ante un problema o pregunta difícil."
    },
    {
        "es": "Estar pisando hielo fino / Arriesgarse demasiado en una situación tensa",
        "pt": "Andar em ovos / Estar pisando em gelo fino",
        "en": "skating on thin ice",
        "explicacion": "Metáfora sumamente gráfica sobre realizar una acción sumamente peligrosa, donde el más mínimo paso en falso quebrará el soporte y te hundirá en aguas heladas de consecuencias fatales."
    },
    {
        "es": "Común y corriente / Del montón",
        "pt": "Comum / Nada de especial ou extraordinário",
        "en": "run-of-the-mill",
        "explicacion": "Originalmente se refería a los productos textiles o de madera fabricados en serie por un molino ('mill') común sin ningún tipo de control de diseño o personalización exclusiva."
    },
    {
        "es": "Desahogarse / Soltar la presión acumulada",
        "pt": "Desabafar / Soltar o estresse acumulado",
        "en": "let off steam",
        "explicacion": "Proviene de la era industrial de las locomotoras de vapor. Si los motores acumulaban demasiada presión interna de calor, debían abrir una válvula para liberar vapor libremente y evitar una explosión masiva."
    },
    {
        "es": "Pasar la noche en vela / Estudiar de forma intensiva a última hora",
        "pt": "Virar a noite estudando ou trabalhando",
        "en": "cram",
        "explicacion": "Verbo avanzado C1 que define la acción de meter a la fuerza gran cantidad de información en la memoria a corto plazo justo antes de rendir un examen importante."
    },
    {
        "es": "Tomar un atajo / Tomar el camino más corto",
        "pt": "Pegar um atalho",
        "en": "take a shortcut",
        "explicacion": "Define la acción de desviarse de la ruta oficial o del procedimiento estándar para ahorrar tiempo en completar una tarea de negocios."
    },
    {
        "es": "Poner las cartas sobre la mesa / Ser completamente honesto",
        "pt": "Jogar limpo / Colocar as cartas na mesa",
        "en": "lay one's cards on the table",
        "explicacion": "Proviene de los juegos de cartas de apuestas donde, al finalizar la ronda, todos los jugadores deben mostrar sus cartas boca arriba de manera transparente para definir al ganador legal."
    },
    {
        "es": "Cambiar de opinión en el último minuto",
        "pt": "Mudar de ideia na última hora",
        "en": "have a change of heart",
        "explicacion": "Expresa una transformación profunda y honesta en la actitud, opinión o sentimientos de una persona respecto a una decisión crucial tomada previamente."
    }
]

# Unir listas evitando duplicados en base al campo "en"
en_existentes = {item["en"].lower() for item in vocab_existente}
nuevos_agregados = 0

for item in nuevo_lote:
    if item["en"].lower() not in en_existentes:
        vocab_existente.append(item)
        nuevos_agregados += 1

# Guardar de nuevo en el archivo JSON
with open(archivo, "w", encoding="utf-8") as f:
    json.dump(vocab_existente, f, ensure_ascii=False, indent=4)

print("¡PROCESO COMPLETADO!")
print(f"-> Se cargaron {nuevos_agregados} nuevas expresiones C1.")
print(f"-> Total actual de vocabulario C1 en tu app: {len(vocab_existente)} expresiones.")