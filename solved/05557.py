import sys
input = sys.stdin.readline

if __name__ == "__main__" :
    N = int(input())
    nums = list(map(int, input().split()))
    dp = [[0] * 21 for i in range(N)]
    dp[0][nums[0]] = 1
    for i in range(1, N - 1):
        for j in range(21):
            if dp[i - 1][j]:
                plus = j + nums[i]
                minus = j - nums[i]
                if plus <= 20: dp[i][plus] += dp[i - 1][j]
                if minus >= 0 : dp[i][minus] += dp[i - 1][j]
    print(dp[N - 2][nums[-1]])
