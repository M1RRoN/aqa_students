from utils.price_utils import extract_price_from_list


def parse_and_sort_games(filtered_games):
    games_parsed = []
    for game in filtered_games:
        game_info = game.text.split('\n')
        price = extract_price_from_list(game_info[-1])
        games_parsed.append((game_info, price))

    sorted_games = sorted(games_parsed, key=lambda x: x[1] if x[1] is not None else -float('inf'), reverse=True)

    return [game[0] for game in sorted_games]
