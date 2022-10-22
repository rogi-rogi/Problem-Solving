if __name__ == "__main__" :
    N = int(input())
    SHU_list = sorted([*map(int, input().split())])
    MOD = int(1e9 + 7)
    res = 0
    for i in range(N) :
        jooheon_pain_level = pow(2, i, MOD) - pow(2, N - i - 1, MOD)
        res = (res + SHU_list[i] * jooheon_pain_level) % MOD
    print(res)
    
