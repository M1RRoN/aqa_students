import re


def extract_price_from_list(game_info):
    match = re.findall(r'(\d+,\d+)\s?zł', game_info)
    if match:
        final_price = match[-1].replace(',', '.')
        return float(final_price)
    return None


def parse_and_sort_games(filtered_games):
    games_parsed = []
    for game in filtered_games:
        game_info = game.text.split('\n')
        price = extract_price_from_list(game_info[-1])
        games_parsed.append((game_info, price))

    sorted_games = sorted(games_parsed, key=lambda x: x[1] if x[1] is not None else -float('inf'), reverse=True)

    return [game[0] for game in sorted_games]
