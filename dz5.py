import colorama
import inspect

for name, data in inspect.getmembers(colorama):
        if inspect.ismodule(data):
            print(f"Модуль: {name}")
        elif inspect.isfunction(data):
            print(f"Функція: {name}")
        elif inspect.isclass(data):
            print(f"Клас: {name}")
