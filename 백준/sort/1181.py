N = int(input())
words = []
for i in range(N):
    words.append(str(input()))
words = list(set(words))
words.sort(key=lambda x : (len(x),x))

for word in words:
    print(word)