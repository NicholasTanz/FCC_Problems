

'''FCC Problem 1 --> Arithmetic Formatter'''
def arithmetic_formatter(problem_list, display_results=False):
    problem_list_broken_down = []
    for problem in problem_list:
        problem_list_broken_down.append(problem.split())

    for problem in problem_list_broken_down:
        if problem[1] != "-" and problem[1] != "+":
            print("Operators other than addition or subtraction are not allowed")
            return False
        if len(problem[0]) > 4 or len(problem[2]) > 4:
            print("Number length cannot be greater than four")
            return False
        try:
            check = int(problem[0])
            check = int(problem[2])
        except:
            print("The Numbers must be integers")
            return False
        if len(problem[0]) >= len(problem[2]):
            line_below = len(problem[0]) + 2
        else:
            line_below = len(problem[2]) + 2
        line_char = "-" * line_below

        print('{message: >{width}}'.format(message=problem[0], width=line_below))
        print("{operator:<{width}}{message}".format(operator=problem[1], message=problem[2], width=line_below - len(problem[2])))
        print(line_char)

        if display_results:
                if problem[1] == "+":
                    result = int(problem[0]) + int(problem[2])
                    print('{result: >{width}}'.format(result=result, width=line_below))
                    print("\n")
                else:
                    result = int(problem[0]) - int(problem[2])
                    print('{result: >{width}}'.format(result=result, width=line_below))
                    print("\n")

'''FCC Problem 5 --> Probability Calculator'''
from collections import Counter
import random 
import copy

class Hat():
    def __init__(self, **colors):
        List_colors = []
        self.List_colors = List_colors
        for color in colors:
            for i in range(colors[color]):
                List_colors.append(color)
    def draw(self, draw_amnt):
        List_copy = copy.deepcopy(self.List_colors)
        List_return = []
        for i in range(draw_amnt):
            if draw_amnt >= len(List_copy):
                return List_copy
            random_choice = random.choice(List_copy)
            List_return.append(random_choice)
            List_copy.remove(random_choice)
        return List_return

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    probability = 0
    expected_balls_list = []
    num_occurences_expected_balls = 0
    for key, value in expected_balls.items():
        for i in range(value):
            expected_balls_list.append(key)

    expected_balls_list_copy = copy.deepcopy(expected_balls_list)
    #probability should be calculated using the number of times you manage to get the expected balls / number experiments
    for i in range(num_experiments):
        random_draw = hat.draw(num_balls_drawn)
        expected_balls_list = copy.deepcopy(expected_balls_list_copy)
        for draw in random_draw:
            if draw in expected_balls_list:
                expected_balls_list.remove(draw)
                if len(expected_balls_list) == 0:
                    num_occurences_expected_balls+=1
                    break

    probability = num_occurences_expected_balls / num_experiments
    print(probability)
    return probability