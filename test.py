from io import StringIO
from unittest.mock import MagicMock, patch

import pytest

from main import TextController, TextModel, TextView


# Тест для моделі TextModel
class TestTextModel:
    @pytest.fixture
    def small_file(self, tmp_path):
        file_content = "Line1\nLine2\nLine3\nLine4\nLine5\n"
        file_path = tmp_path / "test_file.txt"
        file_path.write_text(file_content)
        return file_path


    def test_load_file(self, small_file):
        model = TextModel(small_file, lines_per_page=2)
        assert model.pages == [['Line1\n', 'Line2\n'], ['Line3\n', 'Line4\n'], ['Line5\n']]

    def test_get_current_page(self, small_file):
        model = TextModel(small_file, lines_per_page=2)
        assert model.get_current_page() == ['Line1\n', 'Line2\n']

    def test_next_page(self, small_file):
        model = TextModel(small_file, lines_per_page=2)
        model.next_page()
        assert model.get_current_page() == ['Line3\n', 'Line4\n']

    def test_previous_page(self, small_file):
        model = TextModel(small_file, lines_per_page=2)
        model.next_page()  # Move to page 2
        model.previous_page()  # Move back to page 1
        assert model.get_current_page() == ['Line1\n', 'Line2\n']

    def test_get_page_count(self, small_file):
        model = TextModel(small_file, lines_per_page=2)
        assert model.get_page_count() == 3  # 5 lines, 2 lines per page


# Тест для відображення TextView
class TestTextView:
    @patch("builtins.print")
    def test_display_page(self, mock_print):
        view = TextView()
        page_content = ['Line1\n', 'Line2\n']
        view.display_page(page_content, current_page=0, total_pages=3)
        mock_print.assert_any_call("\n--- Сторінка 1 з 3 ---")
        mock_print.assert_any_call("Line1\n", end="")
        mock_print.assert_any_call("Line2\n", end="")
        mock_print.assert_any_call("\n" + "-" * 30)


# Тест для контролера TextController
class TestTextController:
    @pytest.fixture
    def mock_model(self):
        model = MagicMock()
        model.get_current_page.return_value = ['Line1\n', 'Line2\n']
        model.current_page_index = 0
        model.get_page_count.return_value = 3
        return model

    @pytest.fixture
    def mock_view(self):
        return MagicMock()

    def test_show_page(self, mock_model, mock_view):
        controller = TextController(mock_model, mock_view)
        controller.show_page()
        mock_view.display_page.assert_called_once_with(['Line1\n', 'Line2\n'], 0, 3)

    def test_next_page(self, mock_model, mock_view):
        controller = TextController(mock_model, mock_view)
        controller.next_page()
        mock_model.next_page.assert_called_once()
        mock_view.display_page.assert_called()

    def test_previous_page(self, mock_model, mock_view):
        controller = TextController(mock_model, mock_view)
        controller.previous_page()
        mock_model.previous_page.assert_called_once()
        mock_view.display_page.assert_called()

    @patch("builtins.input", side_effect=['n', 'p', 'q'])
    @patch("builtins.print")
    def test_run(self, mock_print, mock_input, mock_model, mock_view):
        controller = TextController(mock_model, mock_view)
        controller.run()
        assert mock_input.call_count == 3  # Called for 'n', 'p', 'q'
        mock_print.assert_any_call("Вихід з програми.")
