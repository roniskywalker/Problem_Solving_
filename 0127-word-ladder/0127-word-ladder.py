from collections import defaultdict
class Solution:
    def ladderLength(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        if begin_word not in word_list:
            word_list.append(begin_word)
        patterns = defaultdict(set)
        for word in word_list:
            for i in range(len(word)):
                form = word[:i] + "*" + word[i+1:]
                patterns[form].add(word)
        graph = defaultdict(list)
        for word in word_list:
            local_set = set()
            for i in range(len(word)):
                form = word[:i] + "*" + word[i+1:]
                local_set |= patterns[form]
            graph[word] = list(local_set)
        queue = deque([begin_word])
        step = 0
        visit = set([begin_word])
        while queue:
            step += 1
            for _ in range(len(queue)):
                choosen_word = queue.popleft()
                if choosen_word == end_word:
                    return step
                for next_word in graph[choosen_word]:
                    if next_word in visit:
                        continue
                    visit.add(next_word)
                    queue.append(next_word)
        return 0