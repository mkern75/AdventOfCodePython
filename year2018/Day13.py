from utils import load_grid, tic, toc

INPUT_FILE = "./year2018/data/day13.txt"



class Cart:
    def __init__(self, row, col, drow, dcol, turn=0):
        self.row = row
        self.col = col
        self.drow = drow
        self.dcol = dcol
        self.turn = turn


def load_track_and_carts(filename):
    track = load_grid(filename)
    carts = []
    for row in range(len(track)):
        for col in range(len(track[row])):
            if track[row][col] == ">":
                carts += [Cart(row, col, 0, 1)]
                track[row][col] = "-"
            elif track[row][col] == "<":
                carts += [Cart(row, col, 0, -1)]
                track[row][col] = "-"
            elif track[row][col] == "v":
                carts += [Cart(row, col, 1, 0)]
                track[row][col] = "|"
            elif track[row][col] == "^":
                carts += [Cart(row, col, -1, 0)]
                track[row][col] = "|"
    return track, carts


def get_cart(carts, row, col):
    for cart in carts:
        if cart.row == row and cart.col == col:
            return cart
    return None


def move_cart(cart, track):
    cart.row, cart.col = cart.row + cart.drow, cart.col + cart.dcol
    if track[cart.row][cart.col] == "+":
        if cart.turn == 0:
            cart.drow, cart.dcol = -cart.dcol, cart.drow
        elif cart.turn == 2:
            cart.drow, cart.dcol = cart.dcol, -cart.drow
        cart.turn = (cart.turn + 1) % 3
    elif track[cart.row][cart.col] == "\\":
        if cart.drow == 0:
            cart.drow, cart.dcol = cart.dcol, -cart.drow
        else:
            cart.drow, cart.dcol = -cart.dcol, cart.drow
    elif track[cart.row][cart.col] == "/":
        if cart.drow == 0:
            cart.drow, cart.dcol = -cart.dcol, cart.drow
        else:
            cart.drow, cart.dcol = +cart.dcol, -cart.drow


def move_carts(track, carts):
    row_crash, col_crash = None, None
    carts_to_move = list(carts)
    for row in range(len(track)):
        for col in range(len(track[row])):
            cart = get_cart(carts_to_move, row, col)
            if cart is not None:
                move_cart(cart, track)
                carts_to_move.remove(cart)
                for cart2 in carts:
                    if cart != cart2 and cart.row == cart2.row and cart.col == cart2.col:
                        if row_crash is None and col_crash is None:
                            row_crash, col_crash = cart.row, cart.col
                        carts.remove(cart)
                        carts.remove(cart2)
    return row_crash, col_crash


def get_first_crash(track, carts):
    row_crash, col_crash = None, None
    while row_crash is None and col_crash is None:
        row_crash, col_crash = move_carts(track, carts)
    return row_crash, col_crash


def get_location_last_cart(track, carts):
    while len(carts) > 1:
        move_carts(track, carts)
    return carts[0].row, carts[0].col


tic()
track, carts = load_track_and_carts(INPUT_FILE)
row, col = get_first_crash(track, carts)
print(f"part 1: {col},{row}   ({toc():.3f}s)")

tic()
track, carts = load_track_and_carts(INPUT_FILE)
row, col = get_location_last_cart(track, carts)
print(f"part 2: {col},{row}   ({toc():.3f}s)")
