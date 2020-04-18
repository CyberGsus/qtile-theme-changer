import numpy as np
from PIL import Image
import json

def getindex(inp, arr):
    for i, it in enumerate(arr):
           if list(it) == list(inp): return i
    return -1

def get_config_key(dict_o, val):
    could_keys = [ ]
    for k, (v1, v2) in dict_o.items():
        if all(val[i] == v1[i] for i in range(3)) and all(val[i] == v2[i] for i in range(3)):
            could_keys.append(k)
    return could_keys[0], getindex(val, dict_o[could_keys[0]])if could_keys else None

def convert_config(config):
    def hex_to_rgb(string):
        string = string[1:] # remove the '#'
        n = int(string, 16)
        return np.array([
            (n & 0xff0000) >> 16,
            (n & 0xff00) >> 8,
            n & 0xff,
            ], dtype=np.uint8)
    new_dict = {}
    for key, (c1, c2) in config.items():
        new_dict[key] = [
                hex_to_rgb(c1),
                hex_to_rgb(c2)
        ]
    return new_dict

def load_pattern(image_name, config, get_shape=False):
    colors = []
    arr = np.array(
            Image.open(image_name)
    )
    for x in range(arr.shape[0]):
        for y in range(arr.shape[1]):
            colors.append(get_config_key(config, arr[x][y][:-1]))
    return colors if not get_shape else colors, arr.shape

def write_pattern(image_path, pattern, config, shape):
    arr = np.zeros(shape)
    pattern_it = iter(pattern)
    for x in range(shape[0]):
        for y in range(shape[1]):
            next_key = next(pattern_it)
            next_list = list(config[next_key])
            print(f'{next_list=}')
            new_arr = [ 255, *next_list ]
            arr[x][y] = np.array(new_arr)
    Image.fromarray(arr).save(image_path)


if __name__ == '__main__':

    print('Loading configuration...')
    config_file = '/home/cyber/.config/qtile/themes/dracula/colors.json'
    image_file = '/home/cyber/.config/qtile/themes/dracula/img/bg-to-secondary.png'
    default_config = convert_config({ 
        'dark' : [ '#333333', '#333333' ], 
        'grey' : [ '#444444', '#444444' ],
        'light' : [ '#555555', '#555555' ],
        'primary' : [ '#000000', '#000000' ],
        'secondary' : [ '#ffffff', '#ffffff' ],
    })
    with open(config_file) as f:
        image_config = convert_config(json.loads(f.read()))
    print('Loading pattern from image...')
    pattern, shape = load_pattern(image_file, image_config, get_shape=True)
    print(pattern)
    # print('Writing pattern to new image...')
    # write_pattern('test-bg-to-secondary.png', pattern, default_config, shape)
    # print('Write successful')


