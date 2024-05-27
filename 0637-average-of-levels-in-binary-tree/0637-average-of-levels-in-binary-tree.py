class Solution(object):
    def averageOfLevels(self, root):
        self.lst = []
        self.count = []
        
        def level_sum(root, level):
            if not root:
                return
            if len(self.lst) <= level:
                self.lst.append(0.00)
                self.count.append(0)
            self.lst[level] += root.val
            self.count[level] += 1
            level_sum(root.left, level+1)
            level_sum(root.right, level+1)
            
        level_sum(root, 0)
        for level in range(len(self.lst)):
            self.lst[level] = self.lst[level] / self.count[level]
        return self.lst