import yaml

from conftest import BASE_DIR


def bulid_login_data():
    with open(BASE_DIR + '/data/login_data.yml', encoding='utf-8')as f:
        data = yaml.safe_load(f)
        data_list = list()
        for i in data:
            data_list.append((i.get('num'), i.get('pwd')))
        return data_list
