import py5

def setup():
    py5.size(800,800)
    py5.background(100)

    cols = 4
    rows = 4
    off_x = 50 #margin
    off_y = 50
    w = (py5.width - 2 * off_x) / cols #width total del poster tomando en cuenta el margen y el numero de columnas
    h = (py5.height - 2 * off_y) / rows #altura total del poster tomado en cuenta el margen y el numero de filas


    for i in range(rows):
        y = off_y + i * h + h / 2 #se suma el margen y la mitad de la altura 
        for j in range(cols):
            x = off_x + j * w + w / 2 #lo mismo que para y
            py5.rect_mode(py5.CENTER) 
            py5.fill(255)
            py5.rect(x, y, w, h) #(x,y) es el centro
    
    #identificar cada esquina de las celdas del  grid
    for y in range(rows + 1):
        for x in range(cols + 1):
            point(off_x + x * w, off_y + y * h)

def point(x,y):
    py5.no_stroke
    py5.fill(0)
    py5.circle(x,y, 10)

py5.run_sketch()