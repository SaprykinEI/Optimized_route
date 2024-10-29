


def road(full_addresses: list, list_of_addresses: list):
    # full_addresses = ['Ленина 15а', 'Свободы 9', 'Туполева 9и', 'Ростовская 67', 'Менделеева 3', 'Костромская 13']
    sorted_list = []
    for address in full_addresses:

        if address in list_of_adresses:
            sorted_list.append(address)

    for adr in list_of_addresses:
        if adr not in full_addresses:
            print(f"{adr}, Такого адреса в списке нет!")

    return sorted_list

full_addresses = ['Ленина 15а', 'Свободы 9', 'Туполева 9и', 'Ростовская 67', 'Менделеева 3', 'Костромская 13']
list_of_adresses = ['Менделеева 3', 'Ленина 15а', 'Костромская 13', 'Ростовская 67', 'Петровского 5']

for a in road(full_addresses, list_of_adresses):
    print(a)

def insert_address(new_address, full_addresses: list):
    full_addresses.insert(3, new_address)
    return full_addresses

new_full_addresses = insert_address('Петровского 5', full_addresses)
print(new_full_addresses)

