# import sys

# f=open(sys.argv[1],'r')
# print(f.read())
# # n, m = map(int,input().split())
# # pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
# # print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
# # Enter your code here. Read input from STDIN. Print output to STDOUT
# # from itertools import permutations
# # s,n=input().split()
# # print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')
# # Enter your code here. Read input from STDIN. Print output to STDOUT
# k,n=map(int,input().split())
# maxi=0
# for i in range(0,k):
#     new=map(int,input().split())
#     a=(max(new))
#     maxi=maxi+a**2
# print(maxi%n)
