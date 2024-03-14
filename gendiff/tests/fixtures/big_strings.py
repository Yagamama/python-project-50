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


def tree_stylish():
    return '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}
'''


def tree_plain():
    return '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to [complex value]
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From 'too much' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
Property 'group4.default' was updated. From null to ''
Property 'group4.foo' was updated. From 0 to null
Property 'group4.isNested' was updated. From false to 'none'
Property 'group4.key' was added with value: false
Property 'group4.nest.bar' was updated. From '' to 0
Property 'group4.nest.isNested' was removed
Property 'group4.someKey' was added with value: true
Property 'group4.type' was updated. From 'bas' to 'bar'
'''
