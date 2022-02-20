def my_cook_book():
    cook_book = {}
    with open('cookbook.txt') as file:
        for lines in file.read().split('\n\n'):
            name, ing_num, *ingrs = lines.split('\n')
            ingr_list = []
            for ingr in ingrs:
                ingredient_name, quantity, measure = ingr.split(' | ')
                ingr_list.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = ingr_list
    return cook_book


def get_dishes_list(quan, names, cook_book):
    shop_list = {}
    for dish in names:
        for ing in cook_book[dish]:
            if ing['ingredient_name'] not in shop_list:
                shop_list[ing['ingredient_name']] = {'measure': ing['measure'], 'quantity': int(ing['quantity'])*quan}
            else:
                shop_list[ing['ingredient_name']]['quantity'] += int(ing['quantity'])*quan
    return shop_list


def print_shop_list(shop_list):
    for k, v in my_cook_book().items():
        print('{}:{}'.format(k, v))
    print()
    for k, v in shop_list.items():
        print('{}:{}'.format(k, v))


def create_dishes_list():
    quan = int(input('Введите кол-во человек '))
    names = input('Введите блюда через запятую с пробелом ').split(', ')
    shop_list = get_dishes_list(quan, names, my_cook_book())
    print_shop_list(shop_list)


def main():
    my_cook_book()
    create_dishes_list()


main()
