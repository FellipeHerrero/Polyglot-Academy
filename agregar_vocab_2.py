# filepath: agregar_vocab_2.py
import json
import os

archivo = "vocab_c1.json"
if os.path.exists(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        try:
            vocab_existente = json.load(f)
        except json.JSONDecodeError:
            vocab_existente = []
else:
    vocab_existente = []

# Lote 2: 50 Expresiones C1 (Phrasal Verbs Avanzados y Vocabulario Profesional)
nuevo_lote = [
    {
        "es": "Mencionar o introducir un tema en una conversación",
        "pt": "Mencionar / Trazer um assunto à tona",
        "en": "bring up",
        "explicacion": "Phrasal verb C1 esencial. Significa introducir un tema difícil o delicado en una discusión de negocios o personal. Ejemplo: 'Don't bring up the budget during the meeting'."
    },
    {
        "es": "Apostar por la vía dura / Negociar de forma agresiva",
        "pt": "Jogar pesado / Negociar de forma agressiva",
        "en": "play hardball",
        "explicacion": "Viene del béisbol (donde la pelota es rígida y peligrosa, a diferencia del sóftbol). En el mundo de los negocios, significa adoptar una postura estricta, implacable y sin concesiones para ganar una negociación."
    },
    {
        "es": "Ponerse en contacto con alguien para una actualización rápida",
        "pt": "Fazer contato / Conversar rapidamente para alinhar as coisas",
        "en": "touch base",
        "explicacion": "Modismo corporativo muy común en inglés americano. Significa contactar brevemente a un colega o cliente para asegurarse de que ambos están en la misma sintonía sobre un proyecto."
    },
    {
        "es": "Ir directo al grano / Dejar de dar rodeos",
        "pt": "Ir direto ao ponto / Cortar o blá-blá-blá",
        "en": "cut to the chase",
        "explicacion": "Proviene de la época del cine mudo. Los productores de Hollywood notaron que el público se aburría con los diálogos lentos y prefería que la película saltara directamente a la escena de persecución ('the chase')."
    },
    {
        "es": "Empezar con fuerza y dinamismo desde el primer día",
        "pt": "Começar com força total / Começar a trabalhar sem perder tempo",
        "en": "hit the ground running",
        "explicacion": "Originalmente se refería a las tropas paracaidistas que debían correr inmediatamente al tocar tierra en territorio enemigo para no ser blanco fácil. En el ámbito laboral, significa ser productivo desde el inicio."
    },
    {
        "es": "Ponerse al día con una información o habilidad",
        "pt": "Atualizar-se / Ficar a par de uma situação",
        "en": "get up to speed",
        "explicacion": "Significa aprender u obtener toda la información necesaria para alcanzar el nivel de conocimiento o rendimiento requerido en un proyecto."
    },
    {
        "es": "Poner en marcha un proceso o proyecto",
        "pt": "Dar o pontapé inicial / Começar um processo",
        "en": "get the ball rolling",
        "explicacion": "Viene del fútbol u otros deportes donde poner el balón en movimiento da inicio formal al juego. Significa tomar la iniciativa para que un grupo comience a trabajar."
    },
    {
        "es": "Leer entre líneas / Captar un mensaje oculto o implícito",
        "pt": "Ler nas entrelinhas / Entender o que não foi dito abertamente",
        "en": "read between the lines",
        "explicacion": "Habilidad avanzada de comunicación que consiste en descifrar la verdadera intención o significado detrás de las palabras escritas o habladas de alguien."
    },
    {
        "es": "Dar algo por sentado / No valorar algo por tenerlo siempre disponible",
        "pt": "Não dar o devido valor / Dar algo como garantido",
        "en": "take for granted",
        "explicacion": "Error cognitivo común de asumir que una persona, recurso o situación siempre estará allí disponible sin necesidad de cuidarlo o agradecerlo."
    },
    {
        "es": "Llegar a fin de mes (económicamente)",
        "pt": "Dar um jeito de pagar as contas / Sobreviver com o orçamento",
        "en": "make ends meet",
        "explicacion": "Viene del viejo inglés donde 'ends' hacía referencia a los extremos de una cuerda de ingresos y gastos; lograr que se unan ('meet') significa no quedar con deudas al final del mes."
    },
    {
        "es": "Un secreto vergonzoso que se oculta de los demás",
        "pt": "Um segredo de família vergonhoso / Um esqueleto no armário",
        "en": "skeleton in the closet",
        "explicacion": "Metáfora oscura sobre ocultar un hecho del pasado sumamente grave o vergonzoso que arruinaría la reputación de una persona o familia si saliera a la luz."
    },
    {
        "es": "Una gota en el océano / Algo insignificante ante un gran problema",
        "pt": "Uma gota no oceano / Algo insignificante",
        "en": "a drop in the ocean",
        "explicacion": "Se utiliza para ilustrar que un esfuerzo, cantidad de dinero o ayuda es ridículamente pequeña en comparación con la magnitud total de lo que se requiere resolver."
    },
    {
        "es": "Resolver o solucionar un malentendido o problema",
        "pt": "Resolver um problema / Esclarecer um mal-entendido",
        "en": "iron out",
        "explicacion": "Metafóricamente significa 'planchar' las arrugas de una situación para dejarla completamente lisa, fluida y sin asperezas entre las partes."
    },
    {
        "es": "Afrontar un problema con paciencia y resignación",
        "pt": "Aguentar o tranco / Aceitar uma situação difícil",
        "en": "bear with",
        "explicacion": "Phrasal verb formal que se usa mucho en servicio al cliente ('Please bear with me') para pedirle paciencia a alguien mientras resuelves un inconveniente técnico."
    },
    {
        "es": "Hacerse cargo de una responsabilidad o puesto de trabajo",
        "pt": "Assumir o controle / Tomar a liderança de algo",
        "en": "take over",
        "explicacion": "Significa asumir el control de una empresa, departamento o tarea que antes lideraba otra persona."
    },
    {
        "es": "Echarse atrás en un compromiso o acuerdo",
        "pt": "Dar para trás / Voltar atrás em um acordo",
        "en": "back out",
        "explicacion": "Phrasal verb que describe cuando alguien decide romper una promesa, trato comercial o contrato justo antes de que se ejecute por miedo o conveniencia."
    },
    {
        "es": "Destacar sobre la multitud por ser excelente",
        "pt": "Chamar a atenção / Destacar-se pela excelência",
        "en": "stand out",
        "explicacion": "En el nivel C1, este verbo define a candidatos o productos cuya calidad sobresaliente hace imposible que pasen desapercibidos ante los reclutadores."
    },
    {
        "es": "Posponer un evento o reunión para una fecha posterior",
        "pt": "Adiar / Deixar para depois",
        "en": "put off",
        "explicacion": "Equivalente común de 'procrastinar' o 'reprogramar'. Ejemplo: 'We decided to put off the meeting until next Monday'."
    },
    {
        "es": "Cancelar definitivamente un evento planeado",
        "pt": "Cancelar / Chamar de volta",
        "en": "call off",
        "explicacion": "A diferencia de 'put off' (posponer), 'call off' significa suspender por completo un evento, boda, huelga o reunión sin intención de reprogramarla."
    },
    {
        "es": "Descartar una opción o posibilidad de una investigación",
        "pt": "Descartar uma possibilidade / Eliminar uma opção",
        "en": "rule out",
        "explicacion": "Verbo clave para debates analíticos. Significa excluir un factor, sospechoso o teoría tras examinar la evidencia disponible."
    },
    {
        "es": "Enfocarse con absoluta precisión en un objetivo",
        "pt": "Focar totalmente em algo / Mirar de perto",
        "en": "zero in on",
        "explicacion": "Proviene de la calibración de miras telescópicas de precisión, donde ajustar el visor al centro (el cero) garantiza dar en el blanco. Significa concentrar toda la atención en un punto crítico."
    },
    {
        "es": "Reforzar o mejorar la potencia o seguridad de algo",
        "pt": "Reforçar / Tornar algo mais forte ou seguro",
        "en": "beef up",
        "explicacion": "Jerga empresarial de nivel C1 que significa robustecer un sistema de seguridad, un argumento legal o un equipo de trabajo añadiendo más recursos."
    },
    {
        "es": "Repasar o refrescar el conocimiento sobre un tema olvidado",
        "pt": "Dar uma espanada / Relembrar ou praticar um assunto",
        "en": "brush up on",
        "explicacion": "Perfecto para el contexto de idiomas. Significa volver a estudiar algo que ya sabías en el pasado pero que has dejado de practicar por mucho tiempo."
    },
    {
        "es": "Planificar detalladamente los pasos de un proyecto",
        "pt": "Planejar detalhadamente / Traçar um plano",
        "en": "map out",
        "explicacion": "Significa estructurar, diseñar o esquematizar de forma gráfica y organizada el camino que seguirá un negocio o desarrollo de software en el futuro."
    },
    {
        "es": "Encontrarse con alguien de forma casual e inesperada",
        "pt": "Esbarrar com alguém por acaso",
        "en": "run into",
        "explicacion": "Sinónimo informal de 'meet by chance'. Se usa cuando te topas en la calle o supermercado con un conocido sin haber agendado una cita previa."
    },
    {
        "es": "Resolver un problema complejo organizando sus partes",
        "pt": "Resolver uma situação / Organizar uma bagunça",
        "en": "sort out",
        "explicacion": "Significa poner orden en un caos de cables, documentos, finanzas o resolver un malentendido personal de manera madura."
    },
    {
        "es": "Tratar un tema por encima sin profundizar demasiado",
        "pt": "Passar de raspão / Mencionar superficialmente um assunto",
        "en": "touch on",
        "explicacion": "Significa hablar brevemente de un punto específico durante una presentación o informe antes de pasar al tema principal."
    },
    {
        "es": "Terminar en una situación o lugar no planeado originalmente",
        "pt": "Acabar em uma situação inesperada / Ir parar em algum lugar",
        "en": "wind up",
        "explicacion": "Significa el desenlace final de una serie de decisiones caóticas. Ejemplo: 'If you don't save money, you'll wind up broke'."
    },
    {
        "es": "Llevar a cabo una tarea, investigación o experimento",
        "pt": "Executar / Realizar um experimento ou tarefa",
        "en": "carry out",
        "explicacion": "Verbo formal académico C1 de alta frecuencia. Significa ejecutar instrucciones, planes, órdenes militares o análisis científicos."
    },
    {
        "es": "Contar con alguien / Confiar plenamente en su apoyo",
        "pt": "Contar com alguém / Confiar em alguém",
        "en": "count on",
        "explicacion": "Expresa la certeza de que una persona estará allí para ayudarte y respaldarte en los momentos en que más lo necesites."
    },
    {
        "es": "Pensar obsesivamente en un error o arrepentimiento del pasado",
        "pt": "Ficar remoendo o passado / Pensar demais em algo ruim",
        "en": "dwell on",
        "explicacion": "Significa quedarse estancado mentalmente sufriendo por una mala situación o un fracaso que ya no se puede modificar."
    },
    {
        "es": "Recurrir a un plan B o reserva de dinero ante una emergencia",
        "pt": "Recorrer a algo em caso de emergência / Ter uma reserva",
        "en": "fall back on",
        "explicacion": "Estrategia de supervivencia financiera o logística: utilizar un colchón de ahorros o un sistema alternativo cuando el plan principal falla por completo."
    },
    {
        "es": "Superar una enfermedad, ruptura amorosa o trauma emocional",
        "pt": "Superar uma situação difícil ou doença / Superar um ex",
        "en": "get over",
        "explicacion": "Significa recuperar la salud física o el equilibrio emocional tras un evento doloroso que te tuvo inactivo o deprimido."
    },
    {
        "es": "Investigar a fondo un misterio, queja o problema técnico",
        "pt": "Investigar / Analisar detalhadamente um problema",
        "en": "look into",
        "explicacion": "Promesa formal en entornos profesionales: indica que vas a indagar los hechos detalladamente antes de proponer una solución. Ejemplo: 'We will look into this issue immediately'."
    },
    {
        "es": "Reprimir una emoción, risa o lágrimas",
        "pt": "Segurar as emoções / Conter-se",
        "en": "hold back",
        "explicacion": "Significa evitar mostrar lo que sientes o contener tu verdadero potencial por culpa del miedo, timidez o protocolo social."
    },
    {
        "es": "Desglosar o explicar algo paso a paso de forma detallada",
        "pt": "Explicar detalhadamente / Detalhar passo a passo",
        "en": "break down",
        "explicacion": "Significa dividir un concepto masivo o un presupuesto grande en partes más pequeñas y digeribles para que el cliente lo entienda fácilmente."
    },
    {
        "es": "Compensar un error o retraso realizando una buena acción",
        "pt": "Compensar um erro / Redimir-se",
        "en": "make up for",
        "explicacion": "Significa balancear el daño provocado por una mala acción inicial entregando un valor extra. Ejemplo: 'I'll buy you dinner to make up for being late'."
    },
    {
        "es": "Ceder en una discusión / Retirarse de una postura testaruda",
        "pt": "Ceder / Voltar atrás em uma exigência",
        "en": "back down",
        "explicacion": "Significa admitir que estabas equivocado o retirar tus demandas agresivas ante una negociación cuando te das cuenta de que vas a perder."
    },
    {
        "es": "Despedir a trabajadores de forma definitiva por problemas económicos de la empresa",
        "pt": "Demitir funcionários por razões econômicas / Fazer cortes de pessoal",
        "en": "lay off",
        "explicacion": "A diferencia de despedir por mal comportamiento ('fire'), 'lay off' se usa cuando la causa de la desvinculación es estrictamente financiera o de reestructuración corporativa."
    },
    {
        "es": "Seleccionar a una sola persona de un grupo para criticarla o premiarla",
        "pt": "Destacar ou escolher alguém especificamente",
        "en": "single out",
        "explicacion": "Significa apuntar o discriminar (positiva o negativamente) a un individuo dentro de un colectivo para darle un trato especial."
    },
    {
        "es": "Ceder ante la presión o exigencias de otra persona",
        "pt": "Render-se / Ceder à pressão de alguém",
        "en": "yield to",
        "explicacion": "Verbo formal C1 que denota sumisión o aceptación forzosa de las condiciones impuestas por una fuerza superior en un debate o conflicto."
    },
    {
        "es": "Eliminar o filtrar elementos indeseables de un grupo",
        "pt": "Filtrar / Eliminar o que não serve de um grupo",
        "en": "weed out",
        "explicacion": "Metáfora agrícola que significa arrancar la 'maleza' (weeds). En recursos humanos o procesos de selección, significa descartar a los candidatos no calificados."
    },
    {
        "es": "Ignorar o restarle importancia a un error grave en una conversación",
        "pt": "Minimizar um erro / Passar pano por cima de algo ruim",
        "en": "gloss over",
        "explicacion": "Significa tratar de ocultar un fallo, una mala noticia o un defecto cosmético mencionándolo de forma rápida y descuidada para que nadie lo note."
    },
    {
        "es": "El punto clave / La conclusión más importante de un negocio",
        "pt": "O ponto principal / O resultado final de uma discussão",
        "en": "bottom line",
        "explicacion": "Proviene de la última línea de un estado financiero de pérdidas y ganancias, donde se muestra el balance final real de dinero obtenido."
    },
    {
        "es": "Una cifra estimada aproximada",
        "pt": "Uma estimativa aproximada / Um valor estimado",
        "en": "ballpark figure",
        "explicacion": "Viene del béisbol. Si una pelota cae dentro de los límites del estadio ('the ballpark'), está cerca del objetivo. Significa dar un presupuesto aproximado cuando aún no tienes los costos exactos."
    },
    {
        "es": "Mantener a alguien informado de las novedades",
        "pt": "Manter alguém informado / Deixar a par das novidades",
        "en": "keep posted",
        "explicacion": "Viene de la época del correo postal rápido. Significa enviar reportes periódicos a tu jefe o equipo para que conozcan el avance de una situación."
    },
    {
        "es": "Volver al punto de partida / Empezar todo de cero otra vez",
        "pt": "Voltar à estaca zero / Recomeçar do absoluto zero",
        "en": "back to square one",
        "explicacion": "Viene de los juegos de mesa antiguos donde caer en la casilla número uno obligaba al jugador a reiniciar todo su recorrido desde el comienzo."
    },
    {
        "es": "Lo que ocurre de forma privada detrás del escenario o de la oficina",
        "pt": "Nos bastidores / Por trás das câmeras",
        "en": "behind the scenes",
        "explicacion": "Hace referencia al trabajo técnico invisible en el teatro o televisión. En negocios, denota el esfuerzo administrativo que el cliente final no ve."
    },
    {
        "es": "Lo último en tecnología / Lo más moderno que existe",
        "pt": "Tecnologia de ponta / O que há de mais moderno",
        "en": "state of the art",
        "explicacion": "Término técnico de patentes del siglo XX que describe el nivel máximo de desarrollo científico alcanzado en una industria en el momento actual."
    },
    {
        "es": "Publicidad boca a boca / Recomendaciones directas de clientes",
        "pt": "De boca em boca / Recomendação pessoal",
        "en": "word of mouth",
        "explicacion": "La forma de marketing más poderosa y orgánica del mundo, donde el producto se vende gracias a las recomendaciones de los propios consumidores."
    }
]

en_existentes = {item["en"].lower() for item in vocab_existente}
nuevos_agregados = 0

for item in nuevo_lote:
    if item["en"].lower() not in en_existentes:
        vocab_existente.append(item)
        nuevos_agregados += 1

with open(archivo, "w", encoding="utf-8") as f:
    json.dump(vocab_existente, f, ensure_ascii=False, indent=4)

print("¡PROCESO COMPLETADO!")
print(f"-> Se cargaron {nuevos_agregados} nuevas expresiones C1 del Lote 2.")
print(f"-> Total actual de vocabulario C1 en tu app: {len(vocab_existente)} expresiones.")