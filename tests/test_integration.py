from quick_calc_gui import CalculatorCore


def test_full_user_flow_addition():
    calc = CalculatorCore()
    calc.press("5")
    calc.press("+")
    calc.press("3")
    assert calc.press("=") == "8"


def test_clear_after_calculation_resets_display():
    calc = CalculatorCore()
    calc.press("9")
    calc.press("*")
    calc.press("2")
    calc.press("=")
    assert calc.press("C") == "0"

