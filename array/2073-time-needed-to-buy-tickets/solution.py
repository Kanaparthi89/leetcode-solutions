class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        time = 0
        
        for i in range(len(tickets)):
            if i <= k:
                # People before or at k can buy up to tickets[k] times
                time += min(tickets[i], tickets[k])
            else:
                # People after k get one less chance because k finishes earlier
                time += min(tickets[i], tickets[k] - 1)
        
        return time