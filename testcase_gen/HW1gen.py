from random import randint, choice


class Operand:
    @staticmethod
    def operate(a, b):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError


class Add(Operand):
    @staticmethod
    def operate(a, b):
        return a + b

    def __repr__(self):
        return '+'


class Subtract(Operand):
    @staticmethod
    def operate(a, b):
        return a - b

    def __repr__(self):
        return '-'


class Multiply(Operand):
    @staticmethod
    def operate(a, b):
        return a * b

    def __repr__(self):
        return '*'


max_num = 10 ** 100 - 1
min_num = - max_num
testcases = 1000
operations_per_testcase = 100

slash = '/'
testset_path = f"..{slash}testcases{slash}1-BigInteger{slash}testset{slash}"

testcase_name_pattern = "custom-{}"
terminator = 'quit'

operators = [Add(), Subtract(), Multiply()]


def rand_num():
    return randint(min_num, max_num)


if __name__ == '__main__':
    for i in range(testcases):
        input_list = []
        output_list = []
        for j in range(operations_per_testcase):
            num1 = rand_num()
            num2 = rand_num()
            operator = choice(operators)

            expected = operator.operate(num1, num2)

            input_list.append("{} {} {}".format(num1, operator, num2))
            output_list.append(str(expected))
        input_list.append(terminator)

        input_str = '\n'.join(input_list) + '\n'
        output_str = '\n'.join(output_list) + '\n'

        with open(testset_path + 'input' + slash + testcase_name_pattern.format(i) + '.txt', 'w', encoding='utf-8') as f:
            f.write(input_str)
        with open(testset_path + 'output' + slash + testcase_name_pattern.format(i) + '.txt', 'w', encoding='utf-8') as f:
            f.write(output_str)

    print("{} custom testcases generated and written to file.".format(testcases))
