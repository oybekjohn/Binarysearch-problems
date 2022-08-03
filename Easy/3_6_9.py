class Solution:
    def solve(self, n):
        li = []
        for i in range(1, n+1):
            t = [int(x) for x in str(i)]
            if i%3==0:
               li.append("clap")
            elif 3 in t:
                li.append("clap")
            elif 6 in t:
                li.append("clap")
            elif 9 in t:
                li.append("clap")
            else:
                li.append(str(i))
        return li


#  n = 16
#  ["1", "2", "clap", "4", "5", "clap", "7", "8", "clap", "10", "11", "clap", "clap", "14", "clap", "clap"]