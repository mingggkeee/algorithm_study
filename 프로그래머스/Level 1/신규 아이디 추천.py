import re
def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    # 2단계
    new_id = re.sub('[^a-z0-9-_.]','', new_id)
    # 3단계
    temp = ''
    for i in range(len(new_id)):
        if i == 0:
            temp += new_id[i]
            continue
        if new_id[i] == '.':
            if new_id[i] != new_id[i-1]:
                temp += new_id[i]
        else:
            temp += new_id[i]
    new_id = temp
    #4단계
    if new_id[0] == '.' and new_id[-1] == '.':
        new_id = new_id[1:-1]
    elif new_id[0] == '.':
        new_id = new_id[1:]
    elif new_id[-1] == '.':
        new_id = new_id[:-1]
    else:
        pass
    #5단계
    if len(new_id) < 1:
        new_id += 'a'
    #6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    # 7단계
    while(len(new_id)<3):
        new_id += new_id[-1]
    return new_id