import re

def parse_conditional_intensity(data, answers):
    def evaluate_condition(condition, answers_dict):
        variable = None
        # Extracting variable and operator from the condition
        for operator in ['==', '<=', '>=', '<', '>', '!=']:
            if operator in condition:
                variable, op, value = condition.partition(operator)
                break
        
        variable = variable.strip()
        op = op.strip()
        value = value.strip()

        # Parsing values from answers_dict based on variable
        if variable not in answers_dict:
            return False
        values = answers_dict[variable].value.split(',') if hasattr(answers_dict[variable], 'value') else answers_dict[variable]['value'].split(',')
        values = [int(val) for val in values if val.isdigit()]

        # Evaluating the condition
        if op == '==':
            return any(int(val) == int(value) for val in values)
        elif op == '!=':
            return all(int(val) != int(value) for val in values)
        elif op == '<=':
            return any(int(val) <= int(value) for val in values)
        elif op == '>=':
            return any(int(val) >= int(value) for val in values)
        elif op == '<':
            return any(int(val) < int(value) for val in values)
        elif op == '>':
            return any(int(val) > int(value) for val in values)

    def shunting_yard(tokens):
        output_queue = []
        operator_stack = []
        precedence = {'&&': 1, '||': 1}

        for token in tokens:
            if token in ['&&', '||']:
                while operator_stack and operator_stack[-1] in precedence and precedence[operator_stack[-1]] >= precedence[token]:
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                operator_stack.pop()
            else:
                output_queue.append(token)

        while operator_stack:
            output_queue.append(operator_stack.pop())

        return output_queue

    intensity = data['intensity']
    conditions = data['conditional_intensity'].split(';')
    condition_met = False

    for condition in conditions:
        i, expression = condition.split(':')
        tokens = expression.split()
        postfix_tokens = shunting_yard(tokens)
        stack = []
        for token in postfix_tokens:
            if token in ['&&', '||']:
                right_operand = stack.pop()
                left_operand = stack.pop()
                if token == '&&':
                    stack.append(left_operand and right_operand)
                elif token == '||':
                    stack.append(left_operand or right_operand)
            else:
                stack.append(evaluate_condition(token, answers))

        if stack and stack[0]:
            condition_met = True
            return int(i)

    if not condition_met:
        return intensity



def is_valid_condition_syntax(condition):
    num_conditions = 0
    last_token = None
    num_parentheses = 0
    operators = set(['<=', '>=', '!=', '==', '<', '>'])
    logical_operators = set(['&&', '||'])
    tokens = condition.split()

    for token in tokens:
        if last_token is None or last_token == ";":
          if re.match(r'^\d+:$', token) is None:
            return False
        elif token == ";":
            if last_token is None or not any(op in last_token for op in operators):
              return False
        elif any(log_op == token for log_op in logical_operators):
            if not any(op in last_token for op in operators):
                return False
        elif any(op in token for op in operators):
            variable = None
            found = False
            for operator in operators:
                if operator in token:
                    variable, op, value = token.partition(operator)
                    if variable is not None and op is not None and value is not None and value.isdigit():
                        found = True
                        num_conditions += 1
                        break
            if not found:
                return False
        elif token == "(":
          if last_token is not None and not any(op in last_token for op in operators):
            num_parentheses += 1
          else:
              return False
        elif token == ")":
            if not any(op in last_token for op in operators) or num_parentheses <= 0:
                return False
            else:
                num_parentheses -= 1
        else:
            return False

        last_token = token
        
    return num_conditions > 0 and num_parentheses == 0 and last_token != ";"

def is_valid_data(data):
    # Check if 'intensity' and 'conditional_intensity' keys exist in data
    if 'intensity' not in data or 'conditional_intensity' not in data:
        return False

    # Check if 'conditional_intensity' value is a non-empty string and has valid syntax
    if not isinstance(data['conditional_intensity'], str) or not data['conditional_intensity'].strip():
        return False
    

    return is_valid_condition_syntax(data['conditional_intensity'])