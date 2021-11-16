def repaint(a): #a는 중첩 리스트 (크기 8*8인 2차원 배열)
    b_start = list('BWBWBWBW')
    w_start = list('WBWBWBWB')
    b_cnt = w_cnt = cnt = 0
    #맨 왼쪽 윗칸이 black인 경우
    for i in range(8):
        for j in range(8):
            if i % 2 == 0: #짝수 행
                if b_start[j] != a[i][j]:
                    b_cnt += 1
            else: #홀수 행
                if w_start[j] != a[i][j]:
                    b_cnt += 1
    #맨 왼쪽 윗칸이 white인 경우
    for i in range(8):
        for j in range(8):
            if i % 2 == 0: #짝수 행
                if w_start[j] != a[i][j]:
                    w_cnt += 1
            else: #홀수 행
                if b_start[j] != a[i][j]:
                    w_cnt += 1
    #어느 경우에 더 적게 셀 수 있는지
    cnt = min(b_cnt, w_cnt)
    return cnt

N, M = map(int, input().split())
real_min = 10000
#사용자의 입력에 따른 중첩 리스트 생성
a = []
for i in range(N):
    a.append(list(input()))
#8*8 크기로 잘라서 repaint 함수의 인자로 보내기, min 계속 업데이트
for i in range(N-7):
    for j in range(M-7):
        real_min = min(real_min, repaint(a[i:i+8][j:j+8]))
print(real_min)
