import py5

def setup():
    py5.size(700, 700)
    #py5.background(0,0,255)

    """
    Primeros pasos
    py5.rect_mode(py5.CENTER) #con esto ahora se toma el centro del rectangulo como referencia para su posicion
    py5.fill(0,0,240) #se pone antes de dibujar la figura
    # py5.no_stroke() quita el trazo
    py5.stroke(255, 0, 0)
    py5.stroke_weight(4)
    py5.rect(py5.width / 2, py5.height / 2, 200, 50)
    py5.no_stroke()
    py5.fill(4,234,120)
    py5.ellipse(200,200, 300, 100) """


    """ for n in range(10,70, 2): # (inicio, final excluido, de cuando en cuanto)
        py5.line(n * 10, 100, n * 5, 490)

    margin = 50
    for i in range(20):
        py5.line(margin + i * 8, 150, margin + i * 16, 600) """
    
     

    star_four_spikes(300, 300, 200, 100)
    star_four_spikes(500, 400, 150, 50)

    
def star_four_spikes(xc,yc,wa,wb):
    """
        wa: is half the width of the whole star
        wb: is the smaller width ot the star
    """
    pts = [(-wa, -wa), (0, -wb),
           (wa, -wa), (wb, 0),
           (wa, wa), (0,wb),
           (-wa, wa), (-wb, 0)]
    
    py5.begin_shape()

    for x,y in pts:
        py5.vertex(xc + x, yc + y)
    py5.end_shape(py5.CLOSE)


def draw_eye(x,y, w):
    """
        Función para dibujar un ojo con pupila roja
    """
    py5.no_stroke()
    py5.fill(255)
    py5.ellipse(x, y, w, w / 3)
    py5.fill(255, 0, 0)
    py5.ellipse(x, y, w / 3, w / 3)
    py5.fill(0)
    py5.ellipse(x, y, w * 0.1, w * 0.1)

def draw_star(cx,cy, ra, rb, np, start_ang = 0):
    """
    parametros:
        -cx: coordenada x del centro
        -cy: coordenada y del centro
        -ra: valor del primer radio
        -rb: valor del segundo radio
        -np: numero de puntos
        -start_ang: angulo inicial (opcional)
    """
    step = py5.TWO_PI / np
    py5.begin_shape()
    for i in range(np):
        ang = start_ang + step * i + py5.frame_count / 50.0 #angle
        ax = cx + py5.cos(ang) * ra
        ay = cy + py5.sin(ang) * ra
        py5.vertex(ax,ay)
        bx = cx + py5.cos(ang + step / 2.0) * rb
        by = cy + py5.sin(ang + step / 2.0) * rb
        py5.vertex(bx,by) 
    py5.end_shape(py5.CLOSE)


py5.run_sketch()