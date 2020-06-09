from pygal import Config, style, Bar
from requests import get
from operator import itemgetter

# получение данных по API
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
get_data = get(url)
if get_data.status_code != 200:
    print("Сервер ответил с ошибкой.")

# обработка полученной информации
ids_articles = get_data.json()
articles = []
# получаем информацию по каждой статье отдельно и добавляем в общий список
for id_article in ids_articles[:15]:
    url_article = f"https://hacker-news.firebaseio.com/v0/item/{id_article}.json"
    get_article = get(url_article)
    if get_article.status_code != 200:
        print(f"Не удалось получить статью по id {id_article}.")
    else:
        read_article = get_article.json()
        about_article = {'value': read_article.get('descendants', 0),
                         'label': read_article['title'],
                         'xlink': f"https://news.ycombinator.com/item?id={id_article}"}
        articles.append(about_article)

# сортируем список статей по кол-ву комментариев
articles = sorted(articles, key=itemgetter('value'), reverse=True)
print(articles)

# формируем список из названий статей
names = []
for article in articles:
    names.append(article['label'])

# задание стилей для диаграммы
my_config = Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 25  # сокращение длинных названий проектов
my_config.show_y_guides = False  # скроем горизонтальные линии
my_config.width = 1300
my_style = style.LightenStyle('#333366', base_style=style.LightColorizedStyle)
my_style.label_font_size = 16
my_style.major_label_font_size = 20

# построение визуализации
chart = Bar(my_config, style=my_style)
chart.title = "Активные обсуждения на Hack News"
chart.x_labels = names
chart.add('', articles)
chart.render_to_file("popular_articles_hack_news.svg")
