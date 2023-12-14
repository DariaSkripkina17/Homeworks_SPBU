#6. Программа запрашивает два числа, а затем выводит прямоугольник из *, где длины сторон равны данным числам.
height = int(input()) #высота
width = int(input()) #ширина
def draw_box(height, width):    # функция принимает два параметра
    for i in range(height):
        print('*' * width)
draw_box(height, width)

"""более короткое и простое решение: 
a = int(input())
b = int(input())
print(("*" * a + "\n") * b)
"""