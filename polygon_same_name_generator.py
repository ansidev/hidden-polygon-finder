def translative_name(name):
    return name[1:] + name[0]


def get_same_names_of_polygon(name):
    names = list()
    new_name = translative_name(name)
    while name != new_name:
        names.append(new_name)
        new_name = translative_name(new_name)
    reverse_names = list()
    for n in names:
        reverse_names.append(n[0] + n[1:][::-1])
    names.append(name[0] + name[1:][::-1])
    return names + reverse_names


def main():
    print(str(get_same_names_of_polygon("ABFD")))


if __name__ == '__main__':
    main()
