def hello(name):
    print(f"Hello {name}")


def area(width, height):
    total = width*height
    return total


def show_info(name="", salary=0.00, lang="not define"):
    print(f"Name:{name}")
    print(f"Salary:{salary}")
    print(f"Language:{lang}")


hello('ติว')
print(area(4, 5))
show_info()
print()
show_info('สุกฤษ', 350000, 'JAVA')
