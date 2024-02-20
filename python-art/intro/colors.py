import py5

def setup():
    py5.size(800,800)

    py5.fill(0)
    py5.no_stroke()

    for x in range(50, 700, 50):
        d = py5.random(50)
        py5.circle(x, 50, d)
    
    for x in range(50, 700, 50):
        i = py5.random_int(1,4)
        py5.circle(x, 150, i * 10)
    
    for x  in range(50, 700, 50):
        r = py5.random_int(255)
        g = py5.random_int(255)
        b = py5.random_int(255)
        py5.fill(r,g,b)
        py5.circle(x, 250, 45)
    
    for x  in range(50, 700, 50):
        r = py5.random_int(255)
        g = py5.random_int(255)
        b = 0
        py5.fill(r,g,b)
        py5.circle(x, 350, 45)
    
    for x  in range(50, 700, 50):
        r = py5.random_int(128)
        g = 0
        b = py5.random_int(128,255)
        py5.fill(r,g,b)
        py5.circle(x, 450, 45)

    colors = [py5.color(255,200,0),
              py5.color(0,128,255),
              py5.color(128,255,0),]
    
    for x in range(50,700,50):
        py5.fill(py5.random_choice(colors))
        py5.stroke(0)
        py5.circle(x, 550, 45)

    for x in range(50, 800, 100):
        n = py5.random_int(3,7)
        r = py5.random_choice((10,25,40))
        py5.no_stroke()
        draw_star(x, 650,r, 50, n)

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