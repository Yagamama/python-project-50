def files1_and_2():
    return '''{
  - follow: false
    host: hexlet.io
  + hostess: mrs. Bar
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def files1_and_1():
    return '''{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}'''


def f1_2_plain():
    return '''Property 'follow' was removed
Property 'hostess' was added with value: 'mrs. Bar'
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true
'''


def yml3_4():
    return '''{
  - attaks: ['bite', 'push']
  + attaks: ['shot', 'iceball']
  - clan: Grmr
  + healings: ['selfheal']
  - health: 216
  + health: 188
    level: 12
  + name: Oorin
  - race: orc
  + race: elf
}'''


def yml4_4():
    return '''{
    attaks: ['shot', 'iceball']
    healings: ['selfheal']
    health: 188
    level: 12
    name: Oorin
    race: elf
}'''


def yml3_4_plain():
    s = "Property 'attaks' was updated. "
    s += '''From ['bite', 'push'] to ['shot', 'iceball']
Property 'clan' was removed
Property 'healings' was added with value: ['selfheal']
Property 'health' was updated. From 216 to 188
Property 'name' was added with value: 'Oorin'
Property 'race' was updated. From 'orc' to 'elf'
'''
    return s
