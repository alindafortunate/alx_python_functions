count = 0  # global count


def increment_global():
    global count
    count += 1


increment_global()


print(count)
