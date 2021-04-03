with open('1.txt', 'r') as old_file:
    with open('1.txt', 'r+') as new_file:
        current_line = 0
        for line in old_file.readlines():
            if current_line == 1:
                line = ""
            new_file.write(line)
            current_line += 1