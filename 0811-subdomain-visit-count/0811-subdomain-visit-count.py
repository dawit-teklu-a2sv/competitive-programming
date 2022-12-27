class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        output = Counter()
        
        for domain in cpdomains:
            n,s = domain.split()
            output[s] += int(n)
            
            for i in range(len(s)):
                if s[i] == '.':
                    output[s[i+1:]] += int(n)
        return [f"{value} {key}" for key,value in output.items()]
            