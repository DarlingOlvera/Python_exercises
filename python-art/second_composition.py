import py5

def setup():
    py5.size(800,800)
    py5.background(0)

    cols = 8
    rows = 4
    off_x = 50 #margin
    off_y = 50
    num_cells = cols * rows
    w = (py5.width - 2 * off_x) / cols #width total del poster tomando en cuenta el margen y el numero de columnas
    h = (py5.height - 2 * off_y) / rows #altura total del poster tomado en cuenta el margen y el numero de filas
    points = []
    colors = [
        py5.color('#265961'),
        py5.color('#227066'),
        py5.color('#76A665'),
        py5.color('#FFDD5C'),
    ]

    for i in range(rows):
        y = off_y + i * h + h / 2 #se suma el margen y la mitad de la altura 
        for j in range(cols):
            x = off_x + j * w + w / 2 #lo mismo que para y
            color = py5.random_choice(colors)
            draw_arcs(8, x, y, w * 0.1, 0, py5.QUARTER_PI, color, False)
   
    
#py5.arc((py5.width / 2), (py5.height /2) + n, 50 * n, 50 * n, 0, py5.QUARTER_PI * n, py5.OPEN )

def draw_arcs(num,cx,cy,r, a1, a2, color, regular):
    """
    Función para dibujar ondas circulares.
    Parametros:
        -num: numero de arcos
        -cx: coordenada x del centro
        -cy: coordenada y del centro
        -r: radio de los arcos
        -a1: angulo inicial
        -a2: angulo final
        -color: color de los arcos
        -regular: todos los arcos son del mismo tamaño

    """
    for n in range(num):
        py5.no_fill()
        py5.stroke(color)
        py5.stroke_weight(2)
        if(regular != True):
            py5.arc(cx, cy + n, r * (n + 1 /2), r * (n + 1 / 2), a1, a2 * n, py5.OPEN )
        py5.arc(cx, cy + n, r * (n + 1 / 2), r * (n + 1 / 2), a1, a2, py5.OPEN )

py5.run_sketch()