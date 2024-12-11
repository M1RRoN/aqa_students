import re


def extract_price_from_list(game_info):
    match = re.findall(r'(\d+,\d+)\s?zł', game_info)
    if match:
        final_price = match[-1].replace(',', '.')
        return float(final_price)
    return None
