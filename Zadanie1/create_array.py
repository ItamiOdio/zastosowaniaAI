def read_data(filename: str):
    f = open("Datasets/" + filename, "r")
    data = [[int(n) for n in line.split()] for line in f]
    return data


def get_city_count(data: list):
    city_count = data[0][0]
    return city_count


def create_arr(data: list):
    count = get_city_count(data)
    del data[0]

    for i in range(0, count):
        for j in range(count - len(data[i])):
            data[i].append(0)

    for i in range(0, count):
        for j in range(count):
            if i < j:
                data[i][j] = data[j][i]

    return data
