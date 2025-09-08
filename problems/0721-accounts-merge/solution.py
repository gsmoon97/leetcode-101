class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # union-find approach
        # transitive merging (if a -> b and b -> c, then a -> c)
        # path compression
        
        parent = {}  # key: email, value: parent email
        email_to_name = {}  # to keep track of which name the email belongs to
        def find_root(email):
            if parent[email] != email:
                parent[email] = find_root(parent[email])
            return parent[email]

        def union(email1, email2):
            parent[find_root(email2)] = find_root(email1)

        # initialize union find
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(account[1], email)  # point all emails in the account to the first email of the account
        
        # group emails by root
        groups = defaultdict(set)
        for email in parent:
            groups[find_root(email)].add(email)

        # build result
        result = []
        for root, emails in groups.items():
            name = email_to_name[root]  # find the corresponding name using the root
            account = [name] + sorted(emails)  # concatenate all the emails in sorted order
            result.append(account)
        return result