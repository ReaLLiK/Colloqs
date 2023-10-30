import unittest

from AbstractFactory import WindowsFactory, LinuxFactory, create_gui


class TestGUIFactory(unittest.TestCase):
    def test_windows_factory(self):
        windows_factory = WindowsFactory()
        windows_gui = create_gui(windows_factory)
        self.assertEqual(windows_gui[0].display(), "Отображение кнопки Windows")
        self.assertEqual(windows_gui[1].display(), "Отображение фрейма Windows")

    def test_linux_factory(self):
        linux_factory = LinuxFactory()
        linux_gui = create_gui(linux_factory)
        self.assertEqual(linux_gui[0].display(), "Отображение кнопки Linux")
        self.assertEqual(linux_gui[1].display(), "Отображение фрейма Linux")


if __name__ == "__main__":
    unittest.main()
