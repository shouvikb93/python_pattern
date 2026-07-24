# if __name__ == '__main__':
#     n = int(input())
#    # integer_list = map(int, input().split())
    
#     t1 = ()
#     lst = list(t1)
#     for i in range(1, n+1):
#         lst.append(i)
#         t2 = tuple(lst)
#     print(t2)
#     print(hash(t2))
        
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    t = tuple(integer_list)
    print(hash(t))