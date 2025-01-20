import main


def test_convert_to_morse_code_a():
    assert ". ---" == main.convert_to_morse_code("A")


def test_convert_to_morse_code_b():
    assert "--- . . ." == main.convert_to_morse_code("B")


def test_convert_to_morse_code_c():
    assert "--- . --- ." == main.convert_to_morse_code("C")


def test_convert_to_morse_code_d():
    assert "--- . ." == main.convert_to_morse_code("D")


def test_convert_to_morse_code_e():
    assert "." == main.convert_to_morse_code("E")


def test_convert_to_morse_code_f():
    assert ". . --- ." == main.convert_to_morse_code("F")


def test_convert_to_morse_code_g():
    assert "--- --- ." == main.convert_to_morse_code("G")


def test_convert_to_morse_code_h():
    assert ". . . ." == main.convert_to_morse_code("H")


def test_convert_to_morse_code_i():
    assert ". ." == main.convert_to_morse_code("I")


def test_convert_to_morse_code_j():
    assert ". --- --- ---" == main.convert_to_morse_code("J")


def test_convert_to_morse_code_k():
    assert "--- . ---" == main.convert_to_morse_code("K")


def test_convert_to_morse_code_l():
    assert ". --- . ." == main.convert_to_morse_code("L")


def test_convert_to_morse_code_m():
    assert "--- ---" == main.convert_to_morse_code("M")


def test_convert_to_morse_code_n():
    assert "--- ." == main.convert_to_morse_code("N")


def test_convert_to_morse_code_o():
    assert "--- --- ---" == main.convert_to_morse_code("O")


def test_convert_to_morse_code_p():
    assert ". --- --- ." == main.convert_to_morse_code("P")


def test_convert_to_morse_code_q():
    assert "--- --- . ---" == main.convert_to_morse_code("Q")


def test_convert_to_morse_code_r():
    assert ". --- ." in main.convert_to_morse_code("R")


def test_convert_to_morse_code_s():
    assert ". . ." in main.convert_to_morse_code("S")


def test_convert_to_morse_code_t():
    assert "---" == main.convert_to_morse_code("T")


def test_convert_to_morse_code_u():
    assert ". . ---" == main.convert_to_morse_code("U")


def test_convert_to_morse_code_v():
    assert ". . . ---" == main.convert_to_morse_code("V")


def test_convert_to_morse_code_w():
    assert ". --- ---" == main.convert_to_morse_code("W")


def test_convert_to_morse_code_x():
    assert "--- . . ---" == main.convert_to_morse_code("X")


def test_convert_to_morse_code_y():
    assert "--- . --- ---" in main.convert_to_morse_code("Y")


def test_convert_to_morse_code_z():
    assert "--- --- . ." == main.convert_to_morse_code("Z")


def test_convert_to_morse_code_1():
    assert ". --- --- --- ---" == main.convert_to_morse_code("1")


def test_convert_to_morse_code_2():
    assert ". . --- --- ---" == main.convert_to_morse_code("2")


def test_convert_to_morse_code_3():
    assert ". . . --- ---" == main.convert_to_morse_code("3")


def test_convert_to_morse_code_4():
    assert ". . . . ---" == main.convert_to_morse_code("4")


def test_convert_to_morse_code_5():
    assert ". . . . ." == main.convert_to_morse_code("5")


def test_convert_to_morse_code_6():
    assert "--- . . . ." == main.convert_to_morse_code("6")


def test_convert_to_morse_code_7():
    assert "--- --- . . ." == main.convert_to_morse_code("7")


def test_convert_to_morse_code_8():
    assert "--- --- --- . ." == main.convert_to_morse_code("8")


def test_convert_to_morse_code_9():
    assert "--- --- --- --- ." == main.convert_to_morse_code("9")


def test_convert_to_morse_code_0():
    assert "--- --- --- --- ---" == main.convert_to_morse_code("0")


def test_convert_to_morse_code():
    assert ". ---   . --- . .   . --- . .       ---   . . . .   .       . . --- .   . ---   --- . --- .   ---   . . ." == main.convert_to_morse_code("All the facts")


def test_convert_to_morse_code_empty_word():
    assert "" == main.convert_to_morse_code("")

def test_convert_to_morse_code_unknown_letter():
    assert "?" == main.convert_to_morse_code("#")
