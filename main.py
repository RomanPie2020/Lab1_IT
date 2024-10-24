# Model: відповідає за роботу з даними (файлом)
class TextModel:
    def __init__(self, file_path, lines_per_page=25):
        self.file_path = file_path
        self.lines_per_page = lines_per_page
        self.pages = []
        self.current_page_index = 0
        self._load_file()

    def _load_file(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                # Розбиваємо файл на сторінки по 25 ліній
                for i in range(0, len(lines), self.lines_per_page):
                    self.pages.append(lines[i:i + self.lines_per_page])
        except FileNotFoundError:
            print(f"Файл {self.file_path} не знайдено!")

    def get_current_page(self):
        return self.pages[self.current_page_index]

    def next_page(self):
        if self.current_page_index < len(self.pages) - 1:
            self.current_page_index += 1

    def previous_page(self):
        if self.current_page_index > 0:
            self.current_page_index -= 1

    def get_page_count(self):
        return len(self.pages)

# View: відповідає за відображення сторінок
class TextView:
    def display_page(self, page_content, current_page, total_pages):
        print(f"\n--- Сторінка {current_page + 1} з {total_pages} ---")
        for line in page_content:
            print(line, end="")
        print("\n" + "-" * 30)

# Controller: керує логікою програми
class TextController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_page(self):
        current_page_content = self.model.get_current_page()
        current_page = self.model.current_page_index
        total_pages = self.model.get_page_count()
        self.view.display_page(current_page_content, current_page, total_pages)

    def next_page(self):
        self.model.next_page()
        self.show_page()

    def previous_page(self):
        self.model.previous_page()
        self.show_page()

    def run(self):
        self.show_page()
        while True:
            command = input("\nВведіть 'n' для наступної сторінки, 'p' для попередньої сторінки або 'q' для виходу: ").strip().lower()
            if command == 'n':
                self.next_page()
            elif command == 'p':
                self.previous_page()
            elif command == 'q':
                print("Вихід з програми.")
                break
            else:
                print("Невідома команда! Спробуйте ще раз.")

# Ініціалізація та запуск програми
if __name__ == "__main__":
    file_path = input("Введіть шлях до текстового файлу: ")
    model = TextModel(file_path)
    view = TextView()
    controller = TextController(model, view)
    controller.run()
