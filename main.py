from controller import TextController
from model import TextModel
from view import TextView

# Ініціалізація та запуск програми
if __name__ == "__main__":
    file_path = input("Введіть шлях до текстового файлу: ")
    model = TextModel(file_path)
    view = TextView()
    controller = TextController(model, view)
    controller.run()
# end

