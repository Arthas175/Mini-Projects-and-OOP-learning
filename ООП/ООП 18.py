class Geom:
    name = "Geom"

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    name = 'Line'

    def draw(self):
        print("Рисование линии")

class Rect(Geom):
    def draw(self):
        print("Рисование прямоугольника")


g = Geom()
g.set_coords(0, 0, 0, 0)
l = Line()
r = Rect()
print(l.name)
print(r.name)