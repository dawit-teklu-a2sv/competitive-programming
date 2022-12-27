class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for path in paths:
            files = path.split()
            root = files[0]
            for i in range(1,len(files)):
                file_name, content= files[i].split('(')
                d[content[:-1]].append(f'{root}/{file_name}')
        return [value for key,value in d.items() if len(value) > 1]
       