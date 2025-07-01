# 리스트로 관리하면 안되고 이래서 hash를 써야되는구나!!
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i]==phone_book[i+1][:len(phone_book[i])]:
            return False
    return True