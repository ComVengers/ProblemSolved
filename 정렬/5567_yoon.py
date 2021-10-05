#원래 문제: https://www.ioi-jp.org/joi/2009/2010-yo-prob_and_sol/2010-yo-t3/2010-yo-t3.html
#n은 상근이의 동기 수, m은 리스트의 길이, list_a와 list_b는 각각의 입력 저장할 리스트
#my_friend는 상근이 자신의 친구만 저장할 리스트, friend_of_friend는 친구의 친구를 저장할 리스트
#중복을 없애기 위해 추후 my_friend와 friend_of_friend를 집합으로 변환한 뒤 합집합을 만들어 답을 구할 것

n = int(input())
m = int(input())
list_a = list()
list_b = list()
my_friend = list()
friend_of_friend = list()

for i in range(m):
    a, b = map(int, input().split(' '))
    list_a.append(a)
    list_b.append(b)
    if a == 1:
        my_friend.append(b)

for i in range(m):
    for j in my_friend:
        if list_a[i] == j:
            friend_of_friend.append(list_b[i])

my_friend = set(my_friend)
friend_of_friend = set(friend_of_friend)
guest = my_friend.union(friend_of_friend)

#print(list_a)
#print(list_b)
#print(guest)
print(len(guest))
