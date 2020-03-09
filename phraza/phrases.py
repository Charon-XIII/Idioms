import json

##################################################################################

def label():
    label = ['"Фразеологизмдердегі лексикалық көп мәнділікті және синонимиялықты анықтау тәсілін зерттеу және программалық жүзеге асыру"',
             'Еңгізілген фразеологизм жоқ']
    return label

##################################################################################

def open_file(filename):
    filename = 'Base/' + filename
    with open(filename, 'r', encoding='utf-8') as f_obj:
        idioms = json.load(f_obj)
    return idioms

def write_file(filename, idiom):
    filename = 'Base/' + filename
    with open(filename, 'w', encoding='utf-8') as f_obj:
        json.dump(idiom, f_obj)

##################################################################################

def search(idiom):
    write_file('show_last_idiom.json', idiom)

    if idiom in open_file('idioms_items.json'):
        return open_file('idioms.json')[idiom]
    else:
        return 'Not found'

##################################################################################

def show_last_idiom():
    return open_file('show_last_idiom.json')

##################################################################################

def masks(value=""):
    obj = ''
    for word in value.split(","):
        if value.split(",")[-1] == word:
            obj += word.strip().lower()
        else:
            obj += word.strip().lower() + ' <--> '
    return obj

##################################################################################

def create(idiom, value, example, sin="", pol=""):
    sin = masks(sin)
    pol = masks(pol)

    idioms = open_file('idioms.json')
    idioms[idiom] = [value, example, sin, pol]
    write_file('idioms.json', idioms)

    idioms_items = open_file('idioms_items.json')
    idioms_items.append(idiom)
    idioms_items.sort()
    write_file('idioms_items.json', idioms_items)

    write_file('show_last_idiom.json', idiom)

    return search(idiom)

##################################################################################

def edit(idiom, value, example, sin="", pol=""):
    delete()
    write_file('show_last_idiom.json', idiom)

    idioms = open_file('idioms.json')
    del idioms

    return create(idiom, value, example, sin, pol)

##################################################################################

def delete():
    idiom_for_delete = show_last_idiom()

    idioms = open_file('idioms.json')
    del idioms[idiom_for_delete]
    write_file('idioms.json', idioms)

    idioms_items = open_file('idioms_items.json')
    index_idiom_for_delete = idioms_items.index(idiom_for_delete)
    del idioms_items[index_idiom_for_delete]
    write_file('idioms_items.json', idioms_items)

##################################################################################





