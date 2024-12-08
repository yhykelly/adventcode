import numpy as np

def horizontal(letter_array):

    KEYWORD = 'XMAS'

    horizontal_strings = []
    horizontal_count = 0

    # get all possible horizontal string combos
    for line in letter_array:
        line_rev = line[::-1]
        for n in range(len(line) - 3):
            candidate_word = line[n:n+4]
            candidate_word_rev = line_rev[n:n+4]
            horizontal_strings.append(candidate_word)
            horizontal_strings.append(candidate_word_rev)

    for item in horizontal_strings:
        if item == KEYWORD:
            horizontal_count+=1

    print(horizontal_count)

def vertical(letter_array):
    KEYWORD = 'XMAS'

    vertical_strings = []
    vertical_count = 0

    array = []

    # split the string into separate characters and store them in 2D array + transpose to make it vertically doable
    for line in letter_array:
        # print(line)
        line = list(line)
        array.append(line)
    # print(array)
    vertical_array = np.array(array).transpose()
    
    x = 0

    # find words
    for line in vertical_array:
        
            vertical_line = ''.join(line) # join the split element into one string
            # vertical_line_rev = vertical_line[::-1]
            
            for n in range(len(vertical_line) - 3):
                candidate_word = vertical_line[n:n+4]
                # candidate_word_rev = vertical_line_rev[n:n+4]
                vertical_strings.append(candidate_word)
                # vertical_strings.append(candidate_word_rev)
        

    for item in vertical_strings:
        if item == KEYWORD or item == 'SAMX':
            vertical_count+=1

    print(vertical_count)


def diagonal(letter_array):
    KEYWORD = 'XMAS'
    array = []
    for line in letter_array:
        line = list(line)
        array.append(line)
    array_2d = np.array(array)
    array_2d_flip = np.flipud(array_2d)

    num_rows, _ = array_2d.shape

    diagonal_array = []
    diagonal_strings = []
    diagonal_count = 0

    diagonal_array.append(array_2d.diagonal().tolist())
    diagonal_array.append(array_2d_flip.diagonal().tolist())

    for n in range(1, num_rows):
        diagonal_upper = array_2d.diagonal(n)
        diagonal_lower = array_2d.transpose().diagonal(n)
        diagonal_upper_flip = array_2d_flip.diagonal(n)
        diagonal_lower_flip = array_2d_flip.transpose().diagonal(n)
        diagonal_array.append(diagonal_upper.tolist())
        diagonal_array.append(diagonal_lower.tolist())
        diagonal_array.append(diagonal_upper_flip.tolist())
        diagonal_array.append(diagonal_lower_flip.tolist())

    for line in diagonal_array:
        if len(line) >= 4:
            diagonal_line = ''.join(line) # join the split element into one string
            diagonal_line_rev = diagonal_line[::-1]
            for n in range(len(diagonal_line) - 3):
                candidate_word = diagonal_line[n:n+4]
                diagonal_strings.append(candidate_word)
            # for n in range(len(diagonal_line_rev) - 3):
            #     candidate_word_rev = diagonal_line_rev[n:n+4]
            #     diagonal_strings.append(candidate_word_rev)

    for item in diagonal_strings:
        if item == KEYWORD or item == 'SAMX':
            diagonal_count+=1

    print(diagonal_count)


if __name__ == "__main__":
    letter_array = []

    with open('input-dec4.txt', 'r') as reader:
        lines = reader.readlines()
        for line in lines:
            letter_array.append(list(line.strip()))
    
    letter_array_2d = np.array(letter_array)
    num_row, num_col = letter_array_2d.shape
    # print(num_row)

    # print(letter_array_2d[0][1])

    keywords = ['MAS', 'SAM']

    num_match = 0

    iteration = 0
    for row in range(num_row):
        for col in range(num_col):
            if row == 0 or row == num_row - 1 or col == 0 or col == num_row - 1:
                continue
            center = letter_array_2d[row][col]
            top_left = letter_array_2d[row-1][col-1]
            top_right = letter_array_2d[row-1][col+1]
            bottom_left = letter_array_2d[row+1][col-1]
            bottom_right = letter_array_2d[row+1][col+1]
            print("iteration:", iteration)
            diagonal1 = top_left+center+bottom_right
            diagonal2 = top_right+center+bottom_left
            if diagonal1 in keywords and diagonal2 in keywords:
                num_match+=1
            iteration += 1
    print(num_match)

