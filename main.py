import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
sub_pattern = r'+7(\2)-\3-\4-\5 \6\7'

def main(contact_list: list):
    new_list = list()
    for item in contact_list:
        full_name = ' '.join(item[:3]).split(' ')
        result = [full_name[0], full_name[1], full_name[2], item[3], item[4], re.sub(pattern, sub_pattern, item[5]), item[6]]
        new_list.append(result)
    return union(new_list)

def union(contacts: list):
    unique_contacts = {}
    for contact in contacts:
        key = tuple(contact[:2])
        if key not in unique_contacts:
            unique_contacts[key] = contact
        else:
            for i in range(0, len(contact)):
                if contact[i]:
                    unique_contacts[key][i] = contact[i]
    return list(unique_contacts.values())

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(main(contacts_list))


