"""
Problem Link: https://leetcode.com/problems/accounts-merge/

Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, 
and the rest of the elements are emails representing emails of the account.
Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email 
that is common to both accounts. Note that even if two accounts have the same name, they may belong to different 
people as people could have the same name. A person can have any number of accounts initially, but all of their 
accounts definitely have the same name.
After merging the accounts, return the accounts in the following format: the first element of each account is the name, 
and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], 
["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], 
["Mary", "mary@mail.com"]]

Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

Note:
The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
"""
class DSU:
    def __init__(self, n):
        self.s = list(range(n))
        
    def find(self, index):
        if self.s[index] != index:
            return self.find(self.s[index])
        return index
    
    def union(self, index1, index2):
        if index1 == index2:
            return self.find(index1)
        
        p1 = self.find(index1)
        p2 = self.find(index2)
        if p1 > p2:
            p1, p2 = p2, p1
        self.s[p2] = self.s[p1]
        return p1
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails = {}
        
        dsu = DSU(len(accounts)) 
        for account_index in range(len(accounts)):
            
            if accounts[account_index][1] in emails:
                p1 = emails.get(accounts[account_index][1])
            else:
                emails[accounts[account_index][1]] = account_index
                p1 = account_index
                
            for email_index in range(2, len(accounts[account_index])):
                dsu.s[account_index] = dsu.union(p1, emails.get(accounts[account_index][email_index], account_index))
                emails[accounts[account_index][email_index]] = dsu.s[account_index]
        
        res = []
        
        for i in range(len(dsu.s)):
            index = dsu.find(dsu.s[i])
            if index == dsu.s[i] and index >= len(res):
                res.append([accounts[i][0], set()])
            else:
                res.append([])
            
            for email in accounts[i][1:]:
                res[index][1].add(email)
        
        
        for i in range(len(res)):
            if res[i]:
                res[i] = [res[i][0]] + sorted(res[i][1])
        return [r for r in res if r]


class Solution1:    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails = {}
        
        for account_index in range(len(accounts)):
            for email_index in range(1, len(accounts[account_index])):
                email = accounts[account_index][email_index]
                if email in emails:
                    emails[email].append(account_index)
                else:
                    emails[email] = [account_index]
        
        visited = set()
        res = []
        for i in range(len(accounts)):
            if i not in visited:
                res.append([accounts[i][0]])
                temp_set = set()
                temp_email = accounts[i][1]
                stack = emails[temp_email]
                while stack:
                    new_level = []
                    for index in stack:
                        if index not in visited:
                            visited.add(index)
                            for e in accounts[index][1:]:
                                temp_set.add(e)
                                new_level.extend(emails[e])
                    stack = new_level if new_level else None
                res[-1].extend(sorted(temp_set))
        
        return res