def get_user_input():
    w = float(input('w = '))
    h = int(input('h = '))
    return (w,h)


def calc_bmi(w,h):
    print(f'w={w}, h={h}')
    return w/h*2



user_data  = get_user_input()

# bmi = calc_bmi(user_data[0], user_data[1])
bmi = calc_bmi( *user_data )
print(bmi)