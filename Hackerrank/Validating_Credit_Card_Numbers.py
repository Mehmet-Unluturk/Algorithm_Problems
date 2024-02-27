#https://www.hackerrank.com/challenges/validating-credit-card-number/problem



import re

for i in range(int(input())):
    
    card = input()
    
    try:
        assert re.search(r'^[456]', card)
        assert re.search(r'^(-?\d{4}){4}$', card)
        assert not re.search(r'(\d)(-?\1){3}', card)
    
    except:
        print('Invalid')
    else:
        print('Valid')
