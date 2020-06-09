from requests import get
from operator import itemgetter
from pygal import Bar, style, Config

languages = ['python', 'javascript', 'ruby', 'c', 'java', 'perl', 'haskell', 'go']
all_repositories = []

# получение данных по API GitHub
for language in languages:
    url = f"https://api.github.com/search/repositories?q=language:{language}&sort=stars"
    get_data = get(url)
    if get_data.status_code == 200:
        response_dict = get_data.json()
        all_repositories += response_dict['items']
    else:
        print(f"Не получили информацию по языку {language}.")

# сортируем проекты по убыванию звезд
all_repositories = sorted(all_repositories, key=itemgetter('stargazers_count'), reverse=True)

# получение данных для построения визуализации
names, stars_labels = [], []
for repository in all_repositories[:20]:
    names.append(f"{repository['name']} ({repository['language']})")
    stars_labels.append({'value': repository['stargazers_count'],
                         'label': repository['description'],
                         'xlink': repository['html_url']})

# задание стилей для диаграммы
my_config = Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15  # сокращение длинных названий проектов
my_config.show_y_guides = False  # скроем горизонтальные линии
my_config.width = 1300
my_style = style.LightenStyle('#333366', base_style=style.LightColorizedStyle)
my_style.label_font_size = 16
my_style.major_label_font_size = 20

# построение визуализации
chart = Bar(my_config, style=my_style)
chart.title = "Наиболее популярные проекты на разных языках (GitHub)"
chart.x_labels = names
chart.add('', stars_labels)
chart.render_to_file("popular_projects_on_github.svg")
