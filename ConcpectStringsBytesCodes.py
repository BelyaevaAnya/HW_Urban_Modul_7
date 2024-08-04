print('hello')  # ASCII
print(ord('a'))
print(ord('A'))
# # 97
# # 65
print(ord('h'))
print(ord('e'))
print(ord('l'))
print(ord('l'))
print(ord('o'))
# # 104
# # 101
# # 108
# # 108
# # 111
chars = []
a = 'hello'
for i in a:
    chars.append(ord(i))
print(chars)
s = ''
for i in chars:
    s += chr(i)
print(s)
for i in range(128):
    print(chr(i))
# UNICOD
for i in range(1000, 1200):
    print(chr(i))
print(hex(ord('h')))
bb = b'\x68'
print(type(bb))
print(bb.decode())