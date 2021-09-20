import re

new_id = "...!@BaT#*..y.abcdefghijklm"

def solution(new_id):
    answer1 = new_id.lower()
    
    answer2 = re.sub(r'[^a-z0-9-_.]', '', answer1)
    
    answer3 = re.sub('(([.])\\2{1,})','.', answer2)

    answer4 = answer3.strip('.')

    if answer4 == "": answer5 = "a"
    else: answer5 = answer4

    answer6 = answer5[:15].rstrip('.')
    
    if len(str(answer6)) == 1: answer7 = answer6 + answer6[-1]*2
    elif len(str(answer6)) == 2: answer7 = answer6 + answer6[-1]
    else: answer7 = answer6
    
    return answer7

print(solution(new_id))
