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

