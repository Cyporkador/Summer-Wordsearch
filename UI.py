import pygame
import sys
import WordGenerator
import time

pygame.init()
pygame.font.init()
pygame.display.set_caption("Summer Word Search")

WIDTH = 595
HEIGHT = 770

BACKGROUND_COLOR = (255, 255, 204)
BLACK = (0, 0, 0)
SELECTED_COLOR = (255, 204, 153)
COMPLETED_COLOR = (255, 128, 0)

start_time = time.time()
time_sunken = start_time

selected_indices = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

completed_indices = selected_indices

DATA = None
found_words = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

screen = pygame.display.set_mode((WIDTH, HEIGHT))


def clear_selected_squares():
    global selected_indices
    selected_indices = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def draw_selected_squares(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == 1:
                pygame.draw.rect(screen, SELECTED_COLOR, (105.25 + 25 * j, 57.25 + 25 * i + 50, 25, 25))


def draw_completed_squares(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == 1:
                pygame.draw.rect(screen, COMPLETED_COLOR, (105.25 + 25 * j, 57.25 + 25 * i + 50, 25, 25))


# rounds to the nearest multiple of base
def myround(x, base=25):
    return base * round(x/base)


def new_puzzle():
    global DATA, time_sunken, found_words, completed_indices, completed_words, finished_time
    DATA = WordGenerator.generate_new_puzzle(15)
    time_sunken = time.time()
    found_words = [False, False, False, False, False, False, False,
                   False, False, False, False, False, False, False, False]
    completed_indices = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    completed_words = []
    finished_time = None


def draw_board():
    pygame.draw.line(screen, BLACK, (100, 50 + 50), (490, 50 + 50), 3)
    pygame.draw.line(screen, BLACK, (100, 440 + 50), (490, 440 + 50), 3)
    pygame.draw.line(screen, BLACK, (100, 50 + 50), (100, 440 + 50), 3)
    pygame.draw.line(screen, BLACK, (490, 50 + 50), (490, 440 + 50), 3)

    board = DATA[0]
    my_font = pygame.font.SysFont('comicsans', 25)
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            text = board[i][j]
            label = my_font.render(text, 1, BLACK)

            added_space = 0
            if text == "I":
                added_space = 4
            elif text == "M":
                added_space = -1
            elif text == "W":
                added_space = -2

            screen.blit(label, (112.5 + 25*i + added_space, 62.5 + 25*j + 50))


def draw_border():
    pygame.draw.rect(screen, COMPLETED_COLOR, (0, 0, 595, 15))
    pygame.draw.rect(screen, COMPLETED_COLOR, (0, 755, 595, 15))
    pygame.draw.rect(screen, COMPLETED_COLOR, (0, 0, 25, 800))
    pygame.draw.rect(screen, COMPLETED_COLOR, (570, 0, 25, 800))


def draw_words():
    words = DATA[1]
    my_font = pygame.font.SysFont('comicsans', 25)
    for i in range(0, len(words)):
        label = my_font.render(words[i], 1, BLACK)

        y_add = i // 3
        x_add = 0
        if i % 3 != 0:
            x_add = i % 3

        screen.blit(label, (110 + 150 * x_add, 467 + 30 * y_add + 50))


def draw_replay_button():
    pygame.draw.rect(screen, COMPLETED_COLOR, (100, 630 + 50, 250, 40))
    my_font = pygame.font.SysFont('comicsans', 30)
    text = "Bring on a new puzzle!"
    label = my_font.render(text, 1, BLACK)
    screen.blit(label, (110, 640 + 50))


def draw_time():
    my_font = pygame.font.SysFont('comicsans', 30)
    total_seconds = (time.time() - time_sunken) // 1
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)
    if seconds < 10:
        text = "Time: " + str(minutes) + ":" + "0" + str(seconds)
    else:
        text = "Time: " + str(minutes) + ":" + str(seconds)
    label = my_font.render(text, 1, BLACK)
    screen.blit(label, (390, 640 + 50))


def update_selected_squares(pos):
    global selected_indices, guessed_word, previous_square
    if 105.25 < pos[0] < 480.25 and 57.25 + 50 < pos[1] < 432.25 + 50:
        if (pos[0] - 105.25) % 25 < 6 or (pos[0] - 105.25) % 25 > 19:
            return 0
        else:
            if (pos[0] - 105.25) >= myround(pos[0] - 105.25):
                x_pos = myround(pos[0] - 105.25) // 25
            else:
                x_pos = myround(pos[0] - 105.25) // 25 - 1
        if (pos[1] - 57.25 - 50) % 25 < 6 or (pos[1] - 57.25 - 50) % 25 > 19:
            return 0
        else:
            if (pos[1] - 57.25 - 50) >= myround(pos[1] - 57.25 - 50):
                y_pos = myround(pos[1] - 57.25 - 50) // 25
            else:
                y_pos = myround(pos[1] - 57.25 - 50) // 25 - 1
        selected_indices[y_pos][x_pos] = 1
        if not (x_pos, y_pos) == previous_square:
            guessed_word = guessed_word + DATA[0][x_pos][y_pos]
            guessed_word_indices.append((y_pos, x_pos))
        previous_square = (x_pos, y_pos)


def check_guessed_word(word, indices):
    global finished_time
    if word in DATA[1] and word not in completed_words:
        for point in indices:
            completed_indices[point[0]][point[1]] = 1
        completed_words.append(word)
        if len(completed_words) == 15:
            finished_time = (time.time() - time_sunken) // 1
            puzzle_finished()


def draw_crossed_out_words(words):
    for word in words:
        index = DATA[1].index(word)
        y_add = index // 3
        x_add = 0
        if index % 3 != 0:
            x_add = index % 3
        pygame.draw.rect(screen, BLACK, (102 + 150 * x_add, 476 + 30 * y_add + 48, len(word) * 15, 3))


def draw_title():
    my_font = pygame.font.SysFont('comicsans', 50)
    text = "HACKY SUMMER"
    label = my_font.render(text, 1, BLACK)
    screen.blit(label, (155, 40))


def puzzle_finished():
    pygame.draw.rect(screen, BACKGROUND_COLOR, (105, 55 + 50, 380, 380))
    my_font = pygame.font.SysFont('comicsans', 40)
    text = "CONGRATULATIONS!"
    text2 = "PUZZLE COMPLETE!"
    label = my_font.render(text, 1, BLACK)
    label2 = my_font.render(text2, 1, BLACK)
    screen.blit(label, (140, 200 + 50))
    screen.blit(label2, (150, 240 + 50))
    total_seconds = finished_time
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)
    if seconds < 10:
        text = "Time: " + str(minutes) + ":" + "0" + str(seconds)
    else:
        text = "Time: " + str(minutes) + ":" + str(seconds)
    label = my_font.render(text, 1, BLACK)
    screen.blit(label, (230, 300 + 50))


# solves all but one word for you
def view_answers():
    global completed_words
    index = 0
    while len(completed_words) < 14:
        if not DATA[1][index] in completed_words:
            completed_words.append(DATA[1][index])
        index += 1
    coords = DATA[2][0:len(DATA[2]) - 1 - len(DATA[1][-1])]
    for coord in coords:
        completed_indices[coord[1]][coord[0]] = 1
    print(DATA[2][-1])


game_quit = False
mouse_down = False
# used for not adding the same square to guessed_word
previous_square = (-1, -1)
guessed_word = ""
guessed_word_indices = []
completed_words = []
finished_time = None

new_puzzle()

while not game_quit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_quit = True
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if 350 >= mouse_pos[0] >= 100 and 670 + 50 >= mouse_pos[1] >= 630 + 50:
                new_puzzle()
            elif 284 >= mouse_pos[0] >= 150 and 76 >= mouse_pos[1] >= 36:
                view_answers()
            else:
                mouse_down = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
            check_guessed_word(guessed_word, guessed_word_indices)
            guessed_word = ""
            guessed_word_indices = []

    mouse_pos = pygame.mouse.get_pos()
    if mouse_down:
        update_selected_squares(mouse_pos)
    else:
        clear_selected_squares()

    screen.fill(BACKGROUND_COLOR)
    draw_completed_squares(completed_indices)
    draw_selected_squares(selected_indices)
    draw_board()

    if 284 >= mouse_pos[0] >= 150 and 76 >= mouse_pos[1] >= 36:
        if not mouse_down:
            pygame.draw.rect(screen, SELECTED_COLOR, (150, 36, 134, 40))
        else:
            pygame.draw.rect(screen, COMPLETED_COLOR, (150, 36, 134, 40))

    draw_border()
    draw_words()
    draw_replay_button()
    draw_time()
    draw_title()
    draw_crossed_out_words(completed_words)
    if finished_time is not None:
        puzzle_finished()
    pygame.display.update()
