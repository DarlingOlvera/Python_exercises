import py5

def setup():
    py5.size(800,800)
    py5.background(0)

    colors = [py5.color(95, 15, 64),
              py5.color(251, 139, 36),
              py5.color(227, 100, 20),
              py5.color(154, 3, 30)]
    
    for  x in range(50, 751, 50):
        r = py5.random(10,50)
        w = py5.random(10,40)
        py5.no_stroke()
        for y in range(50, 751, 50):
            py5.fill(py5.random_choice(colors))
            if(y % 100 == 0):
                py5.rect_mode(py5.CENTER)
                py5.square(x,y, w)
            else:
                py5.circle(x, y, r)
    

py5.run_sketch()