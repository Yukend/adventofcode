sum_of_games = 0

for game in open("input.txt", "r").readlines():
    _game = game.split(':')
    game_ = _game[1].replace('\n', '').split(';')
    red = 0
    green = 0
    blue = 0
    for cubes in game_:
        cubes = cubes.split(',')
        for cube in cubes:
            cube = cube.split(' ')
            if "red" == cube[2]:
                red = int(cube[1]) if int(cube[1]) > red else red
            if "green" == cube[2]:
                green = int(cube[1]) if int(cube[1]) > green else green
            if "blue" == cube[2]:
                blue = int(cube[1]) if int(cube[1]) > blue else blue
    print(red, green, blue, sum_of_games)
    if red <= 12 and green <= 13 and blue <= 14:
        sum_of_games += int(_game[0].split(' ')[1])

print(sum_of_games)


