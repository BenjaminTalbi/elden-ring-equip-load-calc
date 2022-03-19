import math

weight = 30.0
threshold = 0.299

erd1 = 1.05
erd2 = 1.065
erd3 = 1.08

arsenal1 = 1.15
arsenal2 = 1.17
arsenal3 = 1.19
 
def ceil2(n):
    return math.ceil(100 * n) / 100
 
def with_talisman(weight, threshold, talisman1=1, talisman2=1):
    return ceil2(weight / threshold / (talisman1 * talisman2))

talisman_list_1 = [
    ('None           ', 1),
    ('Erdtree-favor  ', erd1),
    ('Erdtree-favor+1', erd2),
    ('Erdtree-favor+2',erd3)]
    
talisman_list_2 = [
    ('None     ', 1),
    ('Arsenal  ', arsenal1),
    ('Arsenal+1', arsenal2),
    ('Great-Jar', arsenal3)]

def talisman_matrix(weight, talisman_list1, talisman_list2):
    for name1, effect1 in talisman_list1:
        for name2, effect2 in talisman_list2:
            print(name1, '\t', name2, '\t', with_talisman(weight, threshold, effect1, effect2), '\n')        

print(
    'Needed Equip load for fast roll', '\n',
    'Talisman 1     \t','Talisman 2     \n'
)

talisman_matrix(weight, talisman_list_1, talisman_list_2)