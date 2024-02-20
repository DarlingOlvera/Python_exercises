import py5

s = 1 

def setup():
    py5.size(700,980)
    py5.background('#2B3A55')



def draw():
    py5.random_seed(s)
    for _ in range(3):
        grid(100,6,8)




def grid(off_x, cols, rows):
    py5.stroke(255)
    w = py5.width - 2 * off_x
    wc = (py5.width - 2 * off_x) / cols
    off_y = (py5.height - wc * rows) / 2
    h = py5.height - 2 * off_y

    hc = (py5.height - 2 * off_y) / rows

    for j in range(rows):
        y = off_y + j * wc + wc / 2
        r = py5.random_int(128,255)
        g = py5.random_int(0,100)
        b = py5.random_int(0, 50)
        for i in range(cols):
            x  = off_x + i * wc + wc / 2
            m = py5.random_int(1,6)
            if m == 1:
                ra = py5.random(wc / 20, wc / 2)
                rb = py5.random(1, wc / 2)
                np = py5.random_int(4, 10)
                py5.fill(r,g,b, 128)
                draw_star(x, y, ra, rb, np)
            elif 1 < m < 4:
                py5.fill(255,64)
                dr = py5.random_int(0,1) * wc / 2
                py5.rect(x - dr, y - dr, wc /2, wc / 2)
            elif 4 <= m < 6:
                py5.fill(200,64)
                py5.rect(x - wc /2, y - wc / 2, wc, wc)
            else:
                py5.fill(r,g,b,64)
                py5.circle(x, y, py5.random_int(1,2) * wc / 4)

#FUNCIONES
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
        ang = start_ang + step * i  #angle
        ax = cx + py5.cos(ang) * ra
        ay = cy + py5.sin(ang) * ra
        py5.vertex(ax,ay)
        bx = cx + py5.cos(ang + step / 2.0) * rb
        by = cy + py5.sin(ang + step / 2.0) * rb
        py5.vertex(bx,by) 
    py5.end_shape(py5.CLOSE)

def mouse_pressed():
    global s
    s = s + 1
    print(f'random seed: {s}')

def key_pressed():
    if py5.key == 's':
        py5.save_frame(f'results/output-{s}.png')
        print('saved png')
        
py5.run_sketch()