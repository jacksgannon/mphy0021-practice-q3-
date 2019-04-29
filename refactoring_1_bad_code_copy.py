from numpy import *
import matplotlib.pyplot as plt
import yaml


def get_init_coord(dimension, scale, range, shift, zoom, stretch):
    return scale*(dimension-range/shift)/(zoom*stretch*range)


def update_matrix(t, sharpness, init_x, init_y, limit1, limit2, enhance1, enhance2, contrast, A, x, y):
    while t == True:
        if init_x * init_x + init_y * init_y >= limit1:
            t = False
        if sharpness <= limit2:
            t = False
        a = init_x * init_x - init_y * init_y - contrast
        init_y = enhance1 * init_x * init_y + enhance2
        init_x = a
        sharpness = sharpness - 1
    A[y][x] = sharpness


def plot_julia():



    data_dict = yaml.load(open('config.yaml'))
    print(data_dict)
    xrange=data_dict.get('xrange')[0]
    yrange = data_dict.get('yrange')[0]
    xscale = data_dict.get('xscale')[0]
    yscale = data_dict.get('yrange')[0]
    xshift = data_dict.get('xshift')[0]
    yshift = data_dict.get('yrange')[0]
    xzoom = data_dict.get('xzoom')[0]
    yzoom = data_dict.get('yzoom')[0]
    xstretch = data_dict.get('xstretch')[0]
    ystretch = data_dict.get('ystretch')[0]
    initial_sharpness = data_dict.get('initial_sharpness')[0]
    limit1 = data_dict.get('limit1')[0]
    limit2 = data_dict.get('limit2')[0]
    contrast = data_dict.get('contrast')[0]
    enhance1 = data_dict.get('enhance1')[0]
    enhance2 = data_dict.get('enhance2')[0]
    A = zeros([yrange, xrange])
    for x in range(xrange):
        for y in range(yrange):
            init_x = get_init_coord(x, xscale, xrange, xshift, xzoom, xstretch)
            init_y = get_init_coord(y, yscale, yrange, yshift, yzoom, ystretch)
            sharpness = initial_sharpness
            t=True
            update_matrix(t, sharpness, init_x, init_y, limit1, limit2, enhance1, enhance2, contrast, A, x, y)
    plt.imshow(A)
    plt.show()

plot_julia()