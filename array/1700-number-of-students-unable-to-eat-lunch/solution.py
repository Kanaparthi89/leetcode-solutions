class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        count = [0, 0]
        
        # Count how many students prefer each type
        for student in students:
            count[student] += 1
        
        # Process sandwiches from the top
        for sandwich in sandwiches:
            if count[sandwich] == 0:
                # No student wants this sandwich
                return count[0] + count[1]
            
            # A student takes this sandwich
            count[sandwich] -= 1
        
        return 0