from collections import Counter


def can_make_ladybugs_happy(board):

    ladybug_count = Counter(board)
    if '_' in ladybug_count:
        del ladybug_count['_']

    if any(count == 1 for count in ladybug_count.values()):
        return "NO"

    if '_' not in board:
        for i in range(1, len(board) - 1):
            if board[i] != board[i - 1] and board[i] != board[i + 1]:
                return "NO"
        if board[0] != board[1] or board[-1] != board[-2]:
            return "NO"

    return "YES"

games = ["RBY_YBR", "X_Y__X", "__", "B_RRBR"]
results = [can_make_ladybugs_happy(game) for game in games]
print(results)  # Output: ['YES', 'NO', 'YES', 'YES']


