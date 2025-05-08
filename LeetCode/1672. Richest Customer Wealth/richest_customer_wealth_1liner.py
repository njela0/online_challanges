def maximumWealth(accounts: list[list[int]]) -> int:

    return max(sum(account) for account in accounts)

accounts1 = [[1,2,3],[3,2,1]]
accounts2 = [[1,5],[7,3],[3,5]]
accounts3 = [[2,8,7],[7,1,3],[1,9,5]]

print(maximumWealth(accounts3))