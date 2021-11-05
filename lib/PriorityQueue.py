import heapq


class PriorityQueue:
    """
    優先度付きキュー
    """

    class Reverse:
        def __init__(self, val):
            self.val = val

        def __lt__(self, other):
            return self.val > other.val

        def __str__(self):
            return str(self.val)

        def __repr__(self):
            return repr(self.val)

    def __init__(self, a=None, desc=False):
        self.__container = []
        if a:
            self.__container = a[:]

        if desc:
            for i, item in enumerate(self.__container):
                self.__container[i] = self.Reverse(item)
            self.pop = self.__pop_desc
            self.push = self.__push_desc
            self.top = self.__top_desc
        else:
            self.pop = self.__pop_asc
            self.push = self.__push_asc
            self.top = self.__top_asc
        heapq.heapify(self.__container)

    def __pop_asc(self):
        return heapq.heappop(self.__container)

    def __pop_desc(self):
        return heapq.heappop(self.__container).val

    def __push_asc(self, item):
        heapq.heappush(self.__container, item)

    def __push_desc(self, item):
        heapq.heappush(self.__container, self.Reverse(item))

    def __top_asc(self):
        return self.__container[0]

    def __top_desc(self):
        return self.__container[0].val

    def sum(self):
        return sum(self.__container)

    def __len__(self):
        return len(self.__container)

    def __str__(self):
        return str(sorted(self.__container))

    def __repr__(self):
        return self.__str__()
