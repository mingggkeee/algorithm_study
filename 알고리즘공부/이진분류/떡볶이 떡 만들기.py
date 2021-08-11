# 떡의 개수, 요청한 떡의 길이 입력
n, m = map(int, input().split())
# 떡의 개별 높이
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기
    else:
        result = mid
        start = mid - 1

print(result)
