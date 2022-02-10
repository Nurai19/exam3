class Rectangle:
    def __init__(self, length: int, width: int):
        self.__length = length
        self.__width = width

    def getWidth(self, width):
        return self.__width

    def getHeight(self):
        return self.__length

    def get_square(self):
        global result_square
        result_square = self.__length * self.__width
        print(f"Площадь прямоугольника: {result_square}")

    def get_perimeter(self):
        global result_perimeter
        result_perimeter = (self.__length + self.__width) * 2
        print(f"Периметр прямоугольника: {result_perimeter}")

    @property
    def get_info_about_rec(self):
        print(f"Ширина прямоугольника: {self.__length}\nДлина прямоугольника: {self.__width}")


rectangle = Rectangle(2, 5)
rectangle.get_square()
rectangle.get_perimeter()
rectangle.get_info_about_rec
