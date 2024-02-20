import py5

#variable global
s = 1

def setup():
    py5.size(980, 980)
    


def draw(): #draw dibuja a 60 fps automaticamente si no se pone el no_loop
    py5.background(200)
    py5.random_seed(s)
    d = py5.random_int(100,200)
    py5.fill(py5.random_int(255), py5.random_int(255), py5.random_int(255))
    py5.circle(py5.width /2, py5.height / 2, d)

def mouse_pressed():
    #py5.redraw() #se aplica draw otra vez
    global s #para poder manipular la variable global
    s = s + 1
    print(s)

py5.run_sketch()