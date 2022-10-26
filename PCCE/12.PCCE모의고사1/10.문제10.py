# # 문자열은 할당(저장)이 불가능합니다.
# text="Hello"
# text[0]="P"
# # 이동 또한 문자열 안에서 할 수 없어요. 그래서 다른 자료형의 도움을 받아야 합니다.

def solution(text,anagram,sw):
    answer=[""]*len(text)

    if sw==True:
        for i in range(len(anagram)):
            answer[anagram[i]]=text[i]
    else:
        for i in range(len(anagram)):
            answer[i]=text[anagram[i]]

    return "".join(answer)

print(solution("Hello",[4,2,0,1,3],True))   # "lleoH"
print(solution("lleoH",[4,2,0,1,3],False))  # "Hello"