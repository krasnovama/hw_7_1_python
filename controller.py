from view import get_data, get_chois, get_rezult
from mod1 import div, init1
from mod2 import mod, init2
from log import get_log


def button_click():
    v_a, v_b = get_data()
    x = get_chois()

    if x == 1:
        init1(v_a, v_b)
        rezult = div()

    elif x == 2:
        init2(v_a, v_b)
        rezult = mod()

    else:
        rezult = "Не верно выбрана операция"

    get_log(x, rezult)
    get_rezult(rezult)
