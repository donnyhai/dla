
start = 0
boundx = [-200, 200]
boundy = [-200, 200]
colors = ["111111", "222222", "333333"]
color_pos = 0
color_step = 10

particle_coords = [] #import
particles_colored = []

def move(r,k):
    if r.real == k:
        if r.imag == -k: r.real -= 1
        else: r.imag -= 1

    elif r.imag == -k:
        if r.real == -k: r.imag += 1
        else: r.real -= 1

    elif r.real == -k:
        if r.imag == k: r.real += 1
        else: r.imag += 1
    
    elif r.imag == k:
        if r.real == k: r.imag -= 1
        else: r.real += 1

    return r

def color_surface(pos):
    pass


def main():
    for k in range(boundx[1]):
        print(k)

        r = 0
        for j in range(2 * k + 1):
            color_step += 1

            pos = k + k*1j + r
            if pos in particle_coords or pos in particles_colored:
                r = move(r,k)
                continue

            color_surface(pos)














if __name__ == "__main__":
    main()