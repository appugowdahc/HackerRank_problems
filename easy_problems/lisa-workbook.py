

def count_special_problems(n, k, problems):
    page_number = 1
    special_problems = 0
    
    for chapter in range(n):
        num_problems = problems[chapter]
        
        for problem_index in range(1, num_problems + 1):
            if problem_index == page_number:
                special_problems += 1
            
            if problem_index % k == 0 or problem_index == num_problems:
                page_number += 1
    
    return special_problems

# Example usage
n = 5  # Number of chapters
k = 3  # Maximum problems per page
problems = [4, 2, 6, 1, 10]  # Problems in each chapter

print(count_special_problems(n, k, problems))  # Output: 4

def count_special_problems(n, k, problems):
    page_number = 1
    special_problems = 0

    for chapter in range(n):
        num_problems = problems[chapter]
        
        for i in range(1, num_problems + 1, k):
            end = min(i + k - 1, num_problems)
            if page_number >= i and page_number <= end:
                special_problems += 1
            page_number += 1

    return special_problems

n = 5  # Number of chapters
k = 3  # Maximum problems per page
problems = [4, 2, 6, 1, 10]  # Problems in each chapter

print(count_special_problems(n, k, problems))  # Output: 4

