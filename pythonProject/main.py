def road(full_adresses: list, list_of_adresses: list):
    # full_adresses = ['Ленина 15а', 'Свободы 9', 'Туполева 9и', 'Ростовская 67', 'Менделеева 3', 'Костромская 13']
    sorted_list = []
    for adress in full_adresses:

        if adress in list_of_adresses:
            sorted_list.append(adress)

    for adr in list_of_adresses:
        if adr not in full_adresses:
            print(f"{adr}, Такого адреса в списке нет!")

    return sorted_list


for a in road(['Ленина 15а', 'Свободы 9', 'Туполева 9и', 'Ростовская 67', 'Менделеева 3', 'Костромская 13'],
              ['Менделеева 3', 'Ленина 15а', 'Костромская 13', 'Ростовская 67', 'Петровского 5'], ):
    print(a)

