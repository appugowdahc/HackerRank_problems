"""
There are a number of people who will be attending ACM-ICPC World Finals. 
Each of them may be well versed in a number of topics. Given a list of topics 
known by each attendee, presented as binary strings, determine the maximum number of 
topics a 2-person team can know. Each subject has a column in the binary string, and 
a '1' means the subject is known while '0' means it is not. Also determine the number 
of teams that know the maximum number of topics. Return an integer array with two 
elements. The first is the maximum number of topics known, and the second is the 
number of teams that know that number of topics.

"""
"""
****************steps***************

To solve this problem, we need to determine two things:

1.The maximum number of topics that any 2-person team can know collectively.
2.The number of teams that can achieve this maximum number of topics.

Given the binary strings representing the topics known by each attendee, we can approach the problem as follows:

Steps to Solve the Problem

  -> Understand the Input: Each attendee's knowledge is represented as a binary string, where each bit corresponds to whether they know a specific topic (1 means they know it, 0 means they do not).

  -> Combine Knowledge of Two People: For any two attendees, the combined knowledge of topics can be represented by the bitwise OR operation on their binary strings. The bitwise OR will give a 1 for each topic that is known by either attendee.

  -> Count the Number of Topics Known: Count the number of 1s in the result of the bitwise OR operation. This represents the total number of topics known by that team.

  -> Track the Maximum and Count the Teams: Keep track of the maximum number of topics any team can know and count how many teams can achieve that maximum.


"""
def acm_icpc_team(topic):
    max_topics = 0
    team_count = 0
    
    # Convert binary strings to integers for easier bitwise manipulation
    topic_ints = [int(t, 2) for t in topic]
    n = len(topic_ints)
    
    for i in range(n):
        for j in range(i + 1, n):
            # Perform bitwise OR to find combined topics
            combined_topics = topic_ints[i] | topic_ints[j]
            # Count the number of 1's in the combined topics
            topics_known = bin(combined_topics).count('1')
            
            if topics_known > max_topics:
                max_topics = topics_known
                team_count = 1
            elif topics_known == max_topics:
                team_count += 1
                
    return [max_topics, team_count]

# Example usage
topic = ["10101", "11100", "11010", "00101"]
print(acm_icpc_team(topic))  # Output: [5, 2]
