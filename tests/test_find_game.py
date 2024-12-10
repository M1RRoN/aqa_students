import pytest

from utils.sort_games import parse_and_sort_games
from pages.main_page import MainPage
from pages.result_search_page import ResultSearch
from conftest import driver
from conftest import wait
from conftest import base_url


@pytest.mark.parametrize("driver", ["en", "ru"], indirect=True)
@pytest.mark.parametrize("game_name, quantity", [("The Witcher", 10), ("Fallout", 20)])
def test_find_game(driver, game_name, quantity, wait, base_url):
    main_page = MainPage(wait, base_url)
    main_page.open_main_page()
    main_page.wait_for_open()
    main_page.search_on_main_page(game_name)
    result_search = ResultSearch(wait, base_url)
    result_search.visibility_container()
    result_search.wait_for_open()
    search_text = result_search.text_input()
    assert search_text == game_name, (
        f"Ошибка: Текст в строке поиска не совпадает с названием игры. "
        f"Получено: '{search_text}', ожидаемо: '{game_name}'."
    )
    result_search.sorted_results_price_desc()
    filtered_games = result_search.get_n_games(quantity)
    result = parse_and_sort_games(filtered_games)

    assert len(result) == quantity, (
        f"Ошибка: Количество результатов не совпадает с заданным. "
        f"Получено {len(result)}, ожидаемо: {quantity}"
    )
