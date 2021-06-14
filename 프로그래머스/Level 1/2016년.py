import calendar

def solution(a, b):
    date = {0:'mon', 1:'tue', 2:'wed', 3:'thu', 4:'fri', 5:'sat', 6:'sun'}
    answer = date[calendar.weekday(2016,a,b)]

    return answer.upper()