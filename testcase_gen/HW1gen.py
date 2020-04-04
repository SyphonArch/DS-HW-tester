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
normal_testcases = 999 # 정상적 (한글 주석이다 낄낄낄)
small_testcases = 500 # -99~99
cross_testcases = 500 # 큰 수랑 작은 수
# Total number of testcases = normal_testcases + small_testcases + big_testcases + 1
operations_per_testcase = 100

slash = '/'
testset_path = f"..{slash}testcases{slash}1-BigInteger{slash}testset{slash}"

testcase_name_pattern = "custom-{}"
terminator = 'quit'

operators = [Add(), Subtract(), Multiply()]


def rand_num():
    return randint(min_num, max_num)

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

#for rand_small_num()
average = (max_num + min_num) // 2
length = isqrt(min(max_num - average, average - min_num))
def rand_small_num():
    return randint(average - length, average + length)

def rand_blank():
    return ' ' * randint(1, 9)

def blank_string(blank_index, blank_type):
    return "" if (blank_type // (2 ** blank_index)) % 2 == 0 else rand_blank()

def num_string(num, num_type):
    if num_type == 1:
        return '+' + str(num)
    elif num_type == 2:
        return '+' + rand_blank() + str(num)
    elif num_type == 4:
        return '-' + rand_blank() + str(-num)
    else:
        return str(num)

if __name__ == '__main__':
    testcases = 0
    for i in range(normal_testcases):
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

        with open(testset_path + 'input' + slash + testcase_name_pattern.format(testcases + i) + '.txt', 'w', encoding='utf-8') as f:
            f.write(input_str)
        with open(testset_path + 'output' + slash + testcase_name_pattern.format(testcases + i) + '.txt', 'w', encoding='utf-8') as f:
            f.write(output_str)

    testcases += normal_testcases

    for i in range(small_testcases):
        input_list = []
        output_list = []
        for j in range(operations_per_testcase):
            num1 = randint(-99, 99)
            num2 = randint(-99, 99)
            operator = choice(operators)

            expected = operator.operate(num1, num2)

            input_list.append("{} {} {}".format(num1, operator, num2))
            output_list.append(str(expected))
        input_list.append(terminator)

        input_str = '\n'.join(input_list) + '\n'
        output_str = '\n'.join(output_list) + '\n'

        with open(testset_path + 'input' + slash + testcase_name_pattern.format(testcases + i) + '.txt', 'w', encoding='utf-8') as f:
            f.write(input_str)
        with open(testset_path + 'output' + slash + testcase_name_pattern.format(testcases + i) + '.txt', 'w', encoding='utf-8') as f:
            f.write(output_str)

    testcases += small_testcases

    for i in range(cross_testcases):
        input_list = []
        output_list = []
        for j in range(operations_per_testcase):
            num1 = rand_small_num() if j < operations_per_testcase // 2 else rand_num()
            num2 = rand_num() if j < operations_per_testcase // 2 else rand_small_num()
            operator = choice(operators)

            expected = operator.operate(num1, num2)

            input_list.append("{} {} {}".format(num1, operator, num2))
            output_list.append(str(expected))
        input_list.append(terminator)

        input_str = '\n'.join(input_list) + '\n'
        output_str = '\n'.join(output_list) + '\n'

        with open(testset_path + 'input' + slash + testcase_name_pattern.format(testcases + i) + '.txt', 'w', encoding='utf-8') as f:
            f.write(input_str)
        with open(testset_path + 'output' + slash + testcase_name_pattern.format(testcases + i) + '.txt', 'w', encoding='utf-8') as f:
            f.write(output_str)

    testcases += cross_testcases

    input_list = []
    output_list = []
    for j in range(400):
        tempj = j
        blank_type = tempj % 16
        tempj //= 16
        num1_type = tempj % 5
        num2_type = tempj // 5

        num1 = 5 if num1_type < 3 else -5
        num2 = 2 if num2_type < 3 else -2
        operator = choice(operators)

        expected = operator.operate(num1, num2)

        input_list.append("{}{}{}{}{}{}{}".format(blank_string(0, blank_type), num_string(num1, num1_type), blank_string(1, blank_type), operator, blank_string(2, blank_type), num_string(num2, num2_type), blank_string(3, blank_type)))
        output_list.append(str(expected))
    input_list.append(terminator)

    input_str = '\n'.join(input_list) + '\n'
    output_str = '\n'.join(output_list) + '\n'

    with open(testset_path + 'input' + slash + testcase_name_pattern.format(testcases) + '.txt', 'w', encoding='utf-8') as f:
        f.write(input_str)
    with open(testset_path + 'output' + slash + testcase_name_pattern.format(testcases) + '.txt', 'w', encoding='utf-8') as f:
        f.write(output_str)

    testcases += 1

    print("{} custom testcases generated and written to file.".format(testcases))
