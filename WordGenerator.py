import random

words = "august, baseball, beach, berries, bikini, blistering, camp, camping, canoeing, frisbee, grass, hot, humidity, july, june, bright, muggy, ocean, outdoors, outings, outside, park, picnic, play, popsicle, recreation, relax, sailing, sandals, shorts, sightseeing, summer, sunflowers, sunhat, sunny, sunscreen, swim, swimsuit, travel, trip, vacation, visit, voyage, warm, watermelon, waterpark, waterski, zoris, hack, hackathon, code, coding, codefest, hacker, program, bug, debug, computer, software, website, developer, github, discord, active, allergic, boiling, breezy, burning, cheerful, clear, clouds, dreamy, endless, happy, hazy, lakeside, lake, lazy, magical, moist, outdoor, poolside, pool, teams, lifeguard, scorching, season, seasonal, tropical, steamy, sweaty, starry, activities, adventure, backyard, lounging, fresh, fun, barbecue, midsummer, surf".upper()
word_list = []

word = ""
for w in words:
    if w == ",":
        word_list.append(word)
        word = ""
    elif w == " ":
        pass
    else:
        word = word[:] + w

word_list = sorted(word_list)

search_matrix = [['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']]

solution_list = []


def generate_new_puzzle(amount):
    global solution_list
    new_board = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    copy_board(new_board, search_matrix)
    new_word_list = generate_words(amount)
    solution_list = []
    for i in range(0, amount):
        place_word(new_word_list[i], new_board)
    fill_remaining_space(new_board)
    return [new_board, new_word_list, solution_list]


# Requires: cannot be negative, cannot be over 100
def generate_words(amount):
    generated_words = []
    list_copy = word_list[:]
    for i in range(0, amount):
        index = random.randrange(0, len(list_copy) - 1)
        generated_words.append(list_copy[index])
        del list_copy[index]
    return generated_words


def print_word_search(word_search):
    for i in range(len(word_search)):
        for j in range(len(word_search[0])):
            if j != len(word_search[0]) - 1:
                if word_search[i][j] == "":
                    print("@" + " ", end="")
                else:
                    print(word_search[i][j] + " ", end="")
            else:
                if word_search[i][j] == "":
                    print("@")
                else:
                    print(word_search[i][j])


def place_words_on_matrix(list_of_words, matrix):
    for item in list_of_words:
        place_word(item, matrix)
    return matrix


# flips board 90 degrees to the left so you can use vertical as horizontal and same for diagonal
def flip_board(matrix):
    new_board = []
    row = []
    for i in range(0, len(matrix)):
        for each_row in matrix:
            row.append(each_row[len(matrix) - 1 - i])
        new_board.append(row)
        row = []
    copy_board(matrix, new_board)


# helper for flip_board
def copy_board(matrix, new_board):
    for i in range(0, len(matrix)):
        matrix[i] = new_board[i][:]


def place_word(item, matrix):
    orientation = random.randrange(0, 3)
    # reverse = random.randrange(0, 2)
    # if reverse == 0:
    #     item = item[::-1]
    # horizontal
    if orientation == 0:
        place_horizontal(item, matrix, False)
    # vertical
    elif orientation == 1:
        flip_board(matrix)
        place_horizontal(item, matrix, True)
        # flips it back to normal
        flip_board(matrix)
        flip_board(matrix)
        flip_board(matrix)
    # diagonal
    else:
        flip = random.randrange(0, 2)
        if flip == 1:
            place_diagonal(item, matrix, False)
        else:
            flip_board(matrix)
            place_diagonal(item, matrix, True)
            # flips it back to normal
            flip_board(matrix)
            flip_board(matrix)
            flip_board(matrix)


# flips the indices as if the board wasn't rotated
def flip_indices(coords):
    new_pos_list = []
    for coord in coords:
        new_board = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        copy_board(new_board, search_matrix)
        new_board[coord[0]][coord[1]] = "here"
        flip_board(new_board)
        flip_board(new_board)
        flip_board(new_board)
        for i in range(0, len(new_board)):
            if "here" in new_board[i]:
                new_pos_list.append((i, new_board[i].index("here")))
    return new_pos_list


def scrambled(orig):
    dest = orig[:]
    random.shuffle(dest)
    return dest


def place_horizontal(item, matrix, is_flipped):
    check_order = scrambled(make_list(len(matrix)))
    separated = random.randrange(0, 4)
    if separated != 1 and place_horizontal_crossed(item, matrix, is_flipped):
        pass
    else:
        for i in check_order:
            for j in check_order:
                if has_space_horizontal(i, j, item, matrix):
                    for k in range(0, len(item)):
                        matrix[i][j + k] = item[k]
                        if not is_flipped:
                            solution_list.append((i, j+k))
                        else:
                            solution_list.append(flip_indices([(i, j+k)])[0])
                    return 0


def make_list(num):
    temp = []
    for i in range(0, num):
        temp.append(i)
    return temp


def place_horizontal_crossed(item, matrix, is_flipped):
    check_order = scrambled(make_list(len(matrix)))
    for index in check_order:
        for i in range(0, len(item)):
            if item[i] in matrix[index] and has_space_horizontal(index, matrix[index].index(item[i]) - i, item, matrix):
                for k in range(0, len(item)):
                    matrix[index][matrix[index].index(item[i]) - i + k] = item[k]
                    if not is_flipped:
                        solution_list.append((index, matrix[index].index(item[i]) - i + k))
                    else:
                        solution_list.append(flip_indices([(index, matrix[index].index(item[i]) - i + k)])[0])
                return True
    return False


def place_diagonal(item, matrix, is_flipped):
    separated = random.randrange(0, 4)
    if separated != 1 and place_diagonal_crossed(item, matrix, is_flipped):
        pass
    else:
        check_order = scrambled(make_list(len(matrix)))
        check_order2 = scrambled(make_list(len(matrix)))
        for i in check_order:
            for j in check_order2:
                if has_space_diagonal(i, j, item, matrix):
                    for k in range(0, len(item)):
                        matrix[i + k][j + k] = item[k]
                        if not is_flipped:
                            solution_list.append((i+k, j+k))
                        else:
                            solution_list.append(flip_indices([(i+k, j+k)])[0])
                    return 0


def place_diagonal_crossed(item, matrix, is_flipped):
    check_order = scrambled(make_list(len(matrix)))
    for index in check_order:
        for i in range(0, len(item)):
            if item[i] in matrix[index] and has_space_diagonal(index - i, matrix[index].index(item[i]) - i, item, matrix):
                for k in range(0, len(item)):
                    matrix[index - i + k][matrix[index].index(item[i]) - i + k] = item[k]
                    if not is_flipped:
                        solution_list.append((index - i + k, matrix[index].index(item[i]) - i + k))
                    else:
                        solution_list.append(flip_indices([(index - i + k, matrix[index].index(item[i]) - i + k)])[0])
                return True
    return False


def has_space_diagonal(i, j, item, matrix):
    if len(matrix[0]) - len(item) >= j >= 0 and len(matrix) - len(item) >= i >= 0:
        for k in range(0, len(item)):
            if not matrix[i + k][j + k] == "" and not matrix[i + k][j + k] == item[k]:
                return False
        return True
    else:
        return False


def has_space_horizontal(i, j, item, matrix):
    if len(matrix[0]) - len(item) >= j >= 0:
        for k in range(0, len(item)):
            if not matrix[i][j + k] == "" and not matrix[i][j + k] == item[k]:
                return False
        return True
    else:
        return False


def fill_remaining_space(matrix):
    # increase probability of generating vowels
    letters = "aaaabcdeeeefghiiiijklmnoooopqrstuuuuvwxyz".upper()
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if matrix[i][j] == "":
                index = random.randrange(0, len(letters))
                matrix[i][j] = letters[index]

