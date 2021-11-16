def parse_parameters(query: str) -> dict:
    result = {}
    temp_str = query[query.find('?'):] if query.find('?') != -1 else ''

    for number in range(temp_str.count('=')):
        key = temp_str[temp_str.find('?') + 1:temp_str.find('=')]
        item = temp_str[temp_str.find('=') + 1:temp_str.find('&')] if number + 1 != query.count('=') \
            else query[query.rfind('=') + 1:]
        result[key] = item
        temp_str = '?' + temp_str[temp_str.find('&') + 1:] if number + 1 != query.count('=') else ''

    return result


def parse_cookies(query: str) -> dict:
    result = {}
    return result


if __name__ == '__main__':
    # Tests for function "parse_parameters"
    assert parse_parameters('http://example.com/?') == {}
    assert parse_parameters('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse_parameters('http://goole.com/ru/room?name=central&size=large&access=true') == {'name': 'central', 'size': 'large', 'access': 'true'}
    assert parse_parameters('https://name.ua/lol/t?one=two&pip3=install') == {'one': 'two', 'pip3': 'install'}
    assert parse_parameters('https://yandex.ru/asd/234/ad/23/sdf/?left=right') == {'left': 'right'}

    # Tests for function "parse_cookies"
    assert parse_cookies('') == {}
    assert parse_cookies('name=Dima;') == {'name': 'Dima'}
