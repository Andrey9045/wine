from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas
import collections
import argparse
import os


def calculate_years_together(delta):
    if delta % 100 > 10 and delta % 100 < 20:
        return f'Уже {delta} лет вместе'
    elif delta % 10 == 1:
        return f'Уже {delta} год вместе'
    elif delta % 10 > 1 and delta % 10 < 5:
        return f'Уже {delta} года вместе'
    else:
        return f'Уже {delta} лет вместе'


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )

    start_date = datetime.date(1920, 1, 1)
    date_today = datetime.date.today()
    delta = date_today.year - start_date.year
    age_vinery = calculate_years_together(delta)

    parser = argparse.ArgumentParser(description='Загрузите из Excel.')
    parser.add_argument(
        'filepath',
        nargs='?',
        type=str,
        default='wine3.xlsx',
        help='Путь к файлу Excel (по умолчанию: wine3.xlsx)'
    )
    args = parser.parse_args()
    filepath = args.filepath or os.getenv('WINE_FILEPATH')
    if filepath is None:
        raise KeyError("Переменная окружения 'WINE_FILEPATH' не задана и не передан аргумент.")

    template = env.get_template('template.html')

    excel_data_df = pd.read_excel(
        args.filepath,
        na_values=['N/A', 'NA'],
        keep_default_na=False
    )
    wine_collection = excel_data_df.to_dict(orient='records')
    wine_info = collections.defaultdict(list)

    for one_wine in wine_collection:
        wine_info[one_wine['Категория']].append(one_wine)

    rendered_page = template.render(wine_info=wine_info, age_vinery=age_vinery)

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
