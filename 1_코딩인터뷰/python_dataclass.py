from dataclasses import dataclass

@dataclass
class Rectangle:
    width: int
    height: int
    
    def area(self):
        return self.width * self.height
    
rect = Rectangle(3,4)
print(rect)
print(rect.area)
    