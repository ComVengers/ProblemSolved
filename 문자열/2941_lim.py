word = input()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# croatia 문자열 중 일치하는 것이 word에 있으면 *로 교체
for i in croatia:
    word = word.replace(i,'*')

print(len(word))
#print(word)