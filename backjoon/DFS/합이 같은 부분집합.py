'''
N개의 원소로 구성된 자연수 집합이 주어지면, 이 집합을 두 개의 부분집합으로 나누었을 때 두 부분집합의 원소의 합이 서로 같은 경우가 존재하면 “YES"를 출력하고, 그렇지 않으면 ”NO"를 출력하는 프로그램을 작성하세요.
둘로 나뉘는 두 부분집합은 서로소 집합이며, 두 부분집합을 합하면 입력으로 주어진 원래의 집합이 되어 합니다.
예를 들어 {1, 3, 5, 6, 7, 10}이 입력되면 {1, 3, 5, 7} = {6, 10} 으로 두 부분집합의 합이 16으로 같은 경우가 존재하는 것을 알 수 있다.

▣ 입력설명®
첫 번째 줄에 자연수 N(1<=N<=10)이 주어집니다.
두 번째 줄에 집합의 원소 N개가 주어진다. 각 원소는 중복되지 않는다.

▣ 출력설명
첫 번째 줄에 “YES" 또는 ”NO"를 출력한다.

▣ 입력예제 1 6
1 3 5 6 7 10
▣ 출력예제 1 YES
'''
# def solved(sumNum, nu):
#    index = len(numList)-1
#    for i in range(index):
#         if numList[-(index+1)] > sumNum:
#             continue
#
#         divNum = sumNum - numList[-(index+1)]
#         if divNum in numList:
#             return "YES"
#         else:
#             solved(sumNum, nu+1)
#
#    return "NO"
#
#
#
# n = int(input())
# numList= list(map(int, input().split()))
# sumNum = sum(numList)/2
# nu = 0
# print(solved(sumNum, nu))



def can_partition(index, current_sum, total_sum, numList, n):
    if current_sum == total_sum / 2:
        return True
    if index == n or current_sum > total_sum / 2:
        return False

    # Include the current element in the subset and move to the next element
    if can_partition(index + 1, current_sum + numList[index], total_sum, numList, n):
        return True

    # Exclude the current element from the subset and move to the next element
    if can_partition(index + 1, current_sum, total_sum, numList, n):
        return True

    return False

def solve():
    n = int(input())
    numList = list(map(int, input().split()))
    total_sum = sum(numList)

    if total_sum % 2 != 0:
        print("NO")
    else:
        if can_partition(0, 0, total_sum, numList, n):
            print("YES")
        else:
            print("NO")

solve()

