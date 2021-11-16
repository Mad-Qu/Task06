def parse_parameters(query: str) -> dict:
    result = {}
    count = query.count('=')
    query = query[query.find('?') + 1:] if query.find('?') != -1 else ''

    for number in range(count):
        key = query[:query.find('=')]
        item = query[query.find('=') + 1:query.find('&')] if number + 1 != count \
            else query[query.rfind('=') + 1:]
        result[key] = item
        query = query[query.find('&') + 1:] if number + 1 != count else ''

    return result


def parse_cookies(query: str) -> dict:
    result = {}
    count = query.count('=')

    for number in range(count):
        key = query[:query.find('=')]
        item = query[query.find('=') + 1:query.find(';')] if number + 1 != count \
            else query[query.find('=') + 1:] if query[-1] != ';' else query[query.find('=') + 1: -1]
        result[key] = item
        query = query[query.find(';') + 1:] if number + 1 != count else ''

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
    assert parse_cookies('ipaddress=179.12.011.19;browser=GoogleChrome') == {'ipaddress': '179.12.011.19', 'browser': 'GoogleChrome'}
    assert parse_cookies('date=12/12/2020;time=18:33:20;country=Ukraine') == {'date': '12/12/2020', 'time': '18:33:20', 'country': 'Ukraine'}
    assert parse_cookies('first=0000001;second=0000002;') == {'first': '0000001', 'second': '0000002'}
