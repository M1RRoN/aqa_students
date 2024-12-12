import pytest

from utils.sort_games import parse_and_sort_games
from pages.main_page import MainPage
from pages.result_search_page import ResultSearch


@pytest.mark.parametrize("driver", ["en", "ru"], indirect=True)
@pytest.mark.parametrize("game_name, quantity", [("The Witcher", 10), ("Fallout", 20)])
def test_find_game(driver, game_name, quantity, base_url):
    main_page = MainPage()
    main_page.wait_for_open()
    main_page.search_on_main_page(game_name)
    result_search = ResultSearch()
    result_search.wait_visibility_container()
    result_search.wait_for_open()
    search_text = result_search.input_text()
    assert search_text == game_name, (
        f"Ошибка: Текст в строке поиска не совпадает с названием игры. "
        f"Получено: '{search_text}', ожидаемо: '{game_name}'."
    )
    result_search.sort_results_price_desc()
    filtered_games = result_search.get_n_games(quantity)
    print(filtered_games)
    result = parse_and_sort_games(filtered_games)

    assert len(result) == quantity, (
        f"Ошибка: Количество результатов не совпадает с заданным. "
        f"Получено {len(result)}, ожидаемо: {quantity}"
    )
