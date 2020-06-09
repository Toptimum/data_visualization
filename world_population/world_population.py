from json import load
from pygal import style
from pygal_maps_world import maps

from export_countries.country_codes import get_country_code

# извлекаем данные из файла
with open('population_data.json') as file_obj:
    pop_data = load(file_obj)

# выводим население каждой страны за 2018 год
cc_population = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == 2018:
        country_name = pop_dict["Country Name"]
        population = int(pop_dict['Value'])
        code = get_country_code(country_name)
        if code:
            cc_population[code] = population
        else:
            print(f"{country_name}")

# сгруппируем страны по уровням населения
cc_pops_1, cc_pops_2, cc_pops_3, = {}, {}, {}
for cc, pop in cc_population.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# визуализируем данные на карте мира
wm_style = style.RotateStyle('#336699')
world_map = maps.World(style=wm_style)
world_map.title = "Численность населения стран мира в 2018 году"
world_map.add("0-10m", cc_pops_1)
world_map.add("10m-1b", cc_pops_2)
world_map.add(">1b", cc_pops_3)
world_map.render_to_file('world_population.svg')
