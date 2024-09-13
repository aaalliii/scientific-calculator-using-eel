import eel
import math

eel.init('web')

current_input = ""

@eel.expose
def handleClick(button_id):
    global current_input

    functions_map = {
        'sin': 'math.sin(math.radians',
        'cos': 'math.cos(math.radians',
        'tg': 'math.tan(math.radians',
        'ctg': '1/math.tan(math.radians',
        'arcsin': 'math.degrees(math.asin',
        'arccos': 'math.degrees(math.acos',
        'arctg': 'math.degrees(math.atan',
        'arcctg': '(math.pi/2) - math.atan(math.radians',
        '^2': '**2',
        '^3': '**3',
        '^4': '**4',
        '^5': '**5',
        '2√': '**(1/2)',
        '3√': '**(1/3)',
        '4√': '**(1/4)',
        '5√': '**(1/5)',
        'PI': 'math.pi',
        '(': '(',
        ')': ')'
    }

    def append_to_input(value):
        global current_input
        if value in functions_map:
            current_input += functions_map[value]
        else:
            current_input += value

    if button_id == "clear":
        current_input = ""
    elif button_id == "equals":
        try:
            if current_input.count('(') > current_input.count(')'):
                current_input += ')' * (current_input.count('(') - current_input.count(')'))
            current_input = str(eval(current_input, {"math": math, "__builtins__": {}}))
        except Exception as e:
            current_input = "Error"
    else:
        if button_id in functions_map or button_id in {'+', '-', '*', '/'}:
            if current_input and (current_input[-1] in {'+', '-', '*', '/'}):
                current_input = current_input[:-1]
            append_to_input(button_id)
        else:
            append_to_input(button_id)

    eel.updateDisplay(current_input)

eel.start('index.html', size=(840, 600))