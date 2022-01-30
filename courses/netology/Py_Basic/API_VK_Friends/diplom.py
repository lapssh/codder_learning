import requests
import time
import json
import pickle
from pprint import pprint

# TASK: Вывести список групп в ВК в которых состоит пользователь, но не состоит никто из его друзей.
token = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
victim = 'https://vk.com/eshmargunov'
set_of_groups = set()
name_gid_members_count = dict()
params = {
    'access_token': token,
    'v': '5.103'
}


def get_params():
    return dict(
        access_token=token,
        v='5.103'
    )


def data_save(data):
    with open('data_temp_save.dump', 'wb') as f:
        pickle.dump(data, f)
    print('Запись сырых данных в файл закончена.')


def data_load():
    with open('data_temp_save.dump', 'rb') as f:
        data = set(pickle.load(f))
    print('Загрузка сырых данных из файла завершена')
    return data


def get_list_of_groups(id):
    """
    Функция возвращает список групп по id пользователя
    """
    params = get_params()
    params['user_id'] = id
    params['extended'] = 1
    params['fields'] = 'members_count'
    try:
        response = requests.get('https://api.vk.com/method/groups.get', params)
        # params['count'] = 1000
        # print(response.json())

        return response.json()['response']['items']
    except:
        print('\nУ пользователя с id', id, 'закрытый профиль, пропускаем....')
        return False


def get_friens_by_id(id):
    """
    Функция возвращает список друзей по id
    """
    params = get_params()
    params['user_ids'] = id
    response = requests.get('https://api.vk.com/method/friends.get', params)
    return response.json()['response']['items']


def create_set_of_grups(id):
    get_params()
    friends_victim = get_friens_by_id(id)
    for friend in friends_victim:
        try:
            friend_groups = get_list_of_groups(friend)
            if friend_groups == False:
                continue
        except:
            print('\nВозникло исключение на пользователе', friend)
        time.sleep(0.35)
        for group in friend_groups:
            try:
                group_name = group['name']
                group_id = group['id']
                group_members_count = group['members_count']
                # print(group_id, group_name, group_members_count)
                set_of_groups.add((group_id, group_name, group_members_count))
                print('*', end='')
            except:
                print('\n', group_name, '- Закрытая группа, данные не предоставлены.')
    return set_of_groups


id = '392307838'
id_shmargunov = '171691064'
friends_victim = get_friens_by_id(id_shmargunov)
victim_groups = get_list_of_groups(id_shmargunov)
set_of_victim = set()
for group in victim_groups:
    group_name = group['name']
    group_id = group['id']
    group_members_count = group['members_count']
    set_of_victim.add((group_id, group_name, group_members_count))
set_of_groups = create_set_of_grups(id_shmargunov)
# set_of_groups = data_load()
# data_save(set_of_groups)
print('\nВсе сообщества:')
print(set_of_groups)
print()
print('Сообщества жертвы:')
print(set_of_victim)
print()
diff_groups = set_of_victim - set_of_groups
print('Отличия: ')
js_data = []
for i in diff_groups:
    elem = {
        "name": i[1],
        "gid": i[0],
        "members_count": i[2]
    }
    js_data.append(elem)
pprint(diff_groups)
with open('groups.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(js_data, ensure_ascii=False))
print('\nДанные сохранены в файле "groups.json"')
