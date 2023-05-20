import json
import sys


def ipv6_expand(ipv6: str) -> str:
    permitted_chars = [chr(x) for x in range(48, 59)] + \
                      [chr(x) for x in range(65, 71)] + \
                      [chr(x) for x in range(97, 103)]
    for item in ipv6:
        if item not in permitted_chars:
            raise Exception(f"Incorrect address, {item} cannot be included in ipv6 address")

    result_first = []
    result_second = []
    if '::' in ipv6:
        main_list = ipv6.split('::')
        first = main_list[0].split(':')
        second = main_list[1].split(':')
        for item in first:
            if len(item) == 4:
                result_first.append(item)
                continue
            else:
                liczba_do_dodania = 4 - len(item)
                result_first.append('0' * liczba_do_dodania + item)

        for item in second:
            if len(item) == 4:
                result_second.append(item)
                continue
            else:
                liczba_do_dodania = 4 - len(item)
                result_second.append('0' * liczba_do_dodania + item)

        to_add = 8 - (len(result_first) + len(result_second))
        return_list = result_first + ['0000'] * to_add + result_second
        ipv6 = ':'.join(return_list)

    else:
        main_list = ipv6.split(':')
        for item in main_list:
            if len(item) == 4:
                result_first.append(item)
                continue
            else:
                liczba_do_dodania = 4 - len(item)
                result_first.append('0' * liczba_do_dodania + item)
        return_list = result_first
        ipv6 = ':'.join(return_list)

    correctness = True if ipv6.count(':') == 7 else False
    if not correctness:
        raise Exception(f'{ipv6} address is incorrect')
    return ipv6


def ipv6_compress(ipv6: str) -> str:
    permitted = [chr(x) for x in range(48, 59)] + \
                [chr(x) for x in range(65, 71)] + \
                [chr(x) for x in range(97, 103)]
    for item in ipv6:
        if item not in permitted:
            raise Exception(f"Incorrect address, {item} cannot be included in ipv6 address")

    return ipv6


def script(path: str, method):
    with open(path, 'r') as file:
        data = (json.load(file))
    for interface in data['interfaces']:
        interface['address'] = method(interface['address'])
    with open(path, 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    args = sys.argv
    path = args[1]
    function_name = args[2]
    if function_name == 'expand':
        script(path, ipv6_expand)
    elif function_name == 'compress':
        script(path, ipv6_compress)
