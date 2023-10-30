class Button:
    def display(self):
        pass


class Frame:
    def display(self):
        pass


class WindowsButton(Button):
    def display(self):
        return "Отображение кнопки Windows"


class LinuxButton(Button):
    def display(self):
        return "Отображение кнопки Linux"


class WindowsFrame(Frame):
    def display(self):
        return "Отображение фрейма Windows"


class LinuxFrame(Frame):
    def display(self):
        return "Отображение фрейма Linux"


# Абстрактная фабрика
class GUIFactory:
    def create_button(self):
        pass

    def create_frame(self):
        pass


# Конкретные фабрики
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_frame(self):
        return WindowsFrame()


class LinuxFactory(GUIFactory):
    def create_button(self):
        return LinuxButton()

    def create_frame(self):
        return LinuxFrame()


# Клиентский код
def create_gui(factory):
    button = factory.create_button()
    frame = factory.create_frame()
    return button, frame


def main():
    # Использование
    windows_gui = create_gui(WindowsFactory())
    linux_gui = create_gui(LinuxFactory())

    print(windows_gui[0].display())  # Отображение кнопки Windows
    print(windows_gui[1].display())  # Отображение фрейма Windows

    print(linux_gui[0].display())  # Отображение кнопки Linux
    print(linux_gui[1].display())  # Отображение фрейма Linux


if __name__ == "__main__":
    main()
