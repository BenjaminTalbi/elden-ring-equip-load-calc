import math

weight = 30.0
threshold = 0.299
 

talisman_list_1 = [
    ('', 1, 0),
    ('Erdtree-favor', 1.05, 1.5),
    ('Erdtree-favor+1', 1.065, 1.5),
    ('Erdtree-favor+2',1.08, 1.5)]
    
talisman_list_2 = [
    ('', 1, 0),
    ('Arsenal', 1.15, 1.5),
    ('Arsenal+1', 1.17, 1.5),
    ('Great-Jar', 1.19, 1.5)]
 
def with_talisman(
    weight, 
    threshold, 
    talisman1=1, 
    talisman2=1):
    return math.ceil(100 * weight / threshold / (talisman1 * talisman2))/ 100


def cross_talisman_calculation(
    weight, 
    list_1, 
    list_2,
    add_talisman_weight=True,
    sort_by=lambda element: element[2]):
    combinations = []
    for talisman_1, effect_1, talisman_weight_1 in list_1:
        for talisman_2, effect_2, talisman_weight_2 in list_2:
            combinations.append((
                talisman_1,
                talisman_2,
                with_talisman(
                    weight +(talisman_weight_1 + talisman_weight_2 if add_talisman_weight else 0), 
                    threshold, 
                    effect_1, 
                    effect_2
                )
            ))
    return sorted(combinations, key=sort_by)


    
def print_talisman_table(matrix):
    print('| {:<16} | {:<16} | {:<4}'.format('Talisman 1', 'Talisman 2', 'Minimum Equip Load'))
    for row in matrix:
        print('| {:<16} | {:<16} | {:<4}'.format(*row))

print("WEIGHT IS SET TO", weight, '\n')
print('Needed Equip load for fast roll', '\n')
print('Table with added weight of used Talismans')
print_talisman_table(
    cross_talisman_calculation(
        weight, 
        talisman_list_1, 
        talisman_list_2))
print('\nTable without added weight of used Talismans')
print_talisman_table(
    cross_talisman_calculation(
        weight, 
        talisman_list_1, 
        talisman_list_2,
        add_talisman_weight=False
        ))
