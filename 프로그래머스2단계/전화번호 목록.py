def solution(phone_book):
    answer = True
    book = sorted(phone_book)
    
    for j in range(len(book)-1):
        if book[j] in book[j+1][:len(book[j])]:
            return False
            
    return True
