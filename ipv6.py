import json
import sys


def ipv6_expand(ipv6: str) -> str:
    permitted_chars = [chr(x) for x in range(48, 59)] + \
                      [chr(x) for x in range(65, 71)] + \
                      [chr(x) for x in range(97, 103)]
    for item in ipv6:
        if item not in permitted_chars:
            raise Exception(f"Incorrect address, {item} cannot be included in ipv6 address")

    result_first_section = []
    result_second_section = []
    if '::' in ipv6:
        sections = ipv6.split('::')
        first_section = sections[0].split(':')
        second_section = sections[1].split(':')
        for item in first_section:
            if len(item) == 4:
                result_first_section.append(item)
                continue
            else:
                to_add = 4 - len(item)
                result_first_section.append('0' * to_add + item)

        for item in second_section:
            if len(item) == 4:
                result_second_section.append(item)
                continue
            else:
                to_add = 4 - len(item)
                result_second_section.append('0' * to_add + item)

        to_add = 8 - (len(result_first_section) + len(result_second_section))
        return_list = result_first_section + ['0000'] * to_add + result_second_section
        ipv6 = ':'.join(return_list)

    else:
        sections = ipv6.split(':')
        for item in sections:
            if len(item) == 4:
                result_first_section.append(item)
                continue
            else:
                to_add = 4 - len(item)
                result_first_section.append('0' * to_add + item)
        return_list = result_first_section
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

    if '::' in ipv6:
        return ipv6
    else:
        return_list = []
        sections = ipv6.split(':')
        for section in sections:
            count = 0
            for i in range(len(section)):
                if i == 0 and section[i] != '0':
                    break
                else:
                    if section[i] =='0':
                        count += 1
                    else:
                        break

            return_list.append(section[count:])
        for i in range(len(return_list)):
            if return_list[i] == '':
                return_list[i] = '0'
        return ':'.join(return_list)


def start(path: str, method):
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
        start(path, ipv6_expand)
    elif function_name == 'compress':
        start(path, ipv6_compress)

