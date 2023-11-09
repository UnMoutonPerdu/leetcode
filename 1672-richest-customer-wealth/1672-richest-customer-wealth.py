class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        for i in range(len(accounts)):
            sum_account = 0
            for j in range(len(accounts[0])):
                sum_account += accounts[i][j]
            wealth = max(wealth, sum_account)

        return wealth