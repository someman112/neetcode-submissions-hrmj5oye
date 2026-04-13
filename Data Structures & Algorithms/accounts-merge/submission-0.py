class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj=defaultdict(list)

        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                adj[email].append(i)
        

        
        visited = set()
        def dfs(idx, all_emails):
            if idx in visited: return
            visited.add(idx)

            for email in accounts[idx][1:]:
                all_emails.add(email)
                for nei in adj[email]: dfs(nei, all_emails)
        

        output = []
        for i in range(len(accounts)):
            if i not in visited:
                name = [accounts[i][0]]
                emails = set()
                dfs(i, emails)
                emails = sorted(list(emails))

                output.append(name + emails)
        
        return output




