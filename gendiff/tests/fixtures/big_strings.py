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
