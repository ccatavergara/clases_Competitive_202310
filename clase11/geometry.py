from dataclasses import dataclass
from typing import List
import math
# import numpy IS NOT STANDARD

EPS = 1E-8

@dataclass
class point:
    x: float
    y: float

    def __add__(self, t):
        return point(self.x + t.x, self.y + t.y)

    def __sub__(self, t):
        return point(self.x - t.x, self.y - t.y)

    def dot(self, a):
        return self.x*a.x + self.y*a.y

    def norm(self):
        return math.sqrt(self.dot(self))

    def rotate(self, theta):
        return point(self.x*math.cos(theta) + self.y*math.sin(theta),
                    self.x*math.sin(theta) - self.y*math.cos(theta))
        
    def angle(self, a, b):
        s1 = a - self
        d1 = s1.norm()

        s2 = b - self
        d2 = s2.norm()
        
        return math.acos(s1.dot(s2)/(d1*d2))
    
    def cross(self, p):
        return self.x*p.y - p.x*self.y

@dataclass
class line:
    a: float
    b: float
    c: float
    
    @staticmethod
    def from_points(p1, p2):
        if abs(p1.x - p2.x) < EPS:
            return line(1.0, 0.0, -p1.x)
        else:
            a = -(p1.y - p2.y) / (p1.x - p2.x)
            b = 1.0
            c = -(a * p1.x) - p1.y
            return line(a, b, c)
    
    def slope(self):
        return -self.a / self.b
    def y_cross(self):
        return -self.c / self.b
    def x_cross(self):
        return -self.c / self.a
    
    def normal(self):
        return point(self.a / math.sqrt(self.a**2 + self.b**2),
                    self.b / math.sqrt(self.a**2 + self.b**2))
    def d(self):
        return self.c / math.sqrt(self.a**2 + self.b**2)
    
    def intersect(self, l):
        return point((-self.b*l.c + l.b*self.c)/ (self.a*l.b - l.a*self.b),(-self.a*l.c + l.a*self.c)/ (self.a*l.b - l.a*self.b))
    
    def are_parallel(self, line):
        return abs((self.a*line.a + self.b*line.b)
               / (math.sqrt(self.a**2 + self.b**2)*math.sqrt(line.a**2 + line.b**2))
               - 1.0) < EPS
        
    def angle(self, line):
        return math.acos((self.a*line.a + self.b*line.b)
                     / (math.sqrt(self.a**2 + self.b**2)*math.sqrt(line.a**2 + line.b**2)))
        
@dataclass
class segment:
    p: point
    q: point

    def does_intersect(seg1, seg2, *, include_p=False, include_q=False):
        cross1 = (seg2.q - seg1.p).cross(seg1.q - seg1.p)
        cross2 = (seg2.p - seg1.p).cross(seg1.q - seg1.p)
        cross3 = (seg1.q - seg2.p).cross(seg2.q - seg2.p)
        cross4 = (seg1.p - seg2.p).cross(seg2.q - seg2.p)
        return (cross1 * cross2 < 0 or (include_p and math.fabs(cross2) < EPS) or (include_q and math.fabs(cross1) < EPS))\
            and (cross3 * cross4 < 0 or (include_p and math.fabs(cross4) < EPS) or (include_q and math.fabs(cross3) < EPS))
