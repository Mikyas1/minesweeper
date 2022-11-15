import settings


def calc_percentage(percentage, of):
    return (of / 100) * percentage


def height_prct(percentage):
    return calc_percentage(percentage=percentage, of=settings.HEIGHT)


def width_prct(percentage):
    return calc_percentage(percentage=percentage, of=settings.WIDTH)
