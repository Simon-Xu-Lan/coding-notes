class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        if not source:
            return -1

        sp = 0
        tp = 0
        while sp + tp < len(source):
            if tp < len(target):
                if source[sp + tp] == target[tp]:
                    tp += 1
                else:
                    sp += 1
                    tp = 0
            if tp == len(target):
                return sp

        return -1


