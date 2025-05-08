def maximumWealth(accounts: list[list[int]]) -> int:

    account_sums = [0] * len(accounts)

    for index, account in enumerate(accounts):
        account_sum = sum(account)
        account_sums[index] = account_sum

    max_sum = max(account_sums)

    return max_sum

accounts1 = [[1,2,3],[3,2,1]]
accounts2 = [[1,5],[7,3],[3,5]]
accounts3 = [[2,8,7],[7,1,3],[1,9,5]]

print(maximumWealth(accounts3))