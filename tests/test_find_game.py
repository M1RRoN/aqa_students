import pytest

from config.utils import parse_and_sort_games
from pages.main_page import MainPage
from pages.result_search_page import ResultSearch, SEARCH_RESULT_CONTAINER, WAIT
from config.driver import driver


@pytest.mark.parametrize("driver", ["en", "ru"], indirect=True)
@pytest.mark.parametrize("game_name", ["The Witcher", "Fallout"])
def test_find_game(driver, game_name):
    main_page = MainPage(driver)
    main_page.open_main_page()
    assert driver.execute_script("return document.readyState") == "complete", \
        (f"Страница не загрузилась полностью. "
         f"Получено: {driver.execute_script('return document.readyState')}, ожидаемо: 'complete'")
    main_page.search_on_main_page(game_name)
    main_page.find_visibility_element(SEARCH_RESULT_CONTAINER, WAIT)
    assert driver.execute_script("return document.readyState") == "complete", \
        (f"Страница не загрузилась полностью. "
         f"Получено: {driver.execute_script('return document.readyState')}, ожидаемо: 'complete'")
    result_search = ResultSearch(driver)
    search_text = result_search.text_input()
    assert search_text == game_name, (
        f"Ошибка: Текст в строке поиска не совпадает с названием игры. "
        f"Получено: '{search_text}', ожидаемо: '{game_name}'."
    )
    result_search.sorted_results_price_desc()
    if game_name == "The Witcher":
        quantity = 10
        filtered_games = result_search.get_n_games(quantity)
        result = parse_and_sort_games(filtered_games)
        assert len(result) == quantity
        print(result)
    elif game_name == "Fallout":
        quantity = 20
        filtered_games = result_search.get_n_games(quantity)
        result = parse_and_sort_games(filtered_games)
        assert len(result) == quantity
        print(result)