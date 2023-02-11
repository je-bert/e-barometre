type QuestionID = string;
type Operator = '>' | '<' | '>=' | '<=' | '=';
type NumberToCompare = number;

type ParsedConditional = [QuestionID, Operator, NumberToCompare];

export class ConditionalParser {
  parse(statement: string): ParsedConditional[] {
    const statements = statement.split('and');
    return statements.map(this.parseCondition);
  }

  parseCondition(condition: string): ParsedConditional {
    if (!condition) {
      throw new Error('No condition provided');
    }

    if (typeof condition !== 'string') {
      throw new Error('Condition must be a string');
    }

    const conditionalOperators: string[] = [];

    // todo cleanup this part
    for (let i = 0; i < condition.length; i++) {
      if (
        i < condition.length &&
        condition[i] === '>' &&
        condition[i + 1] === '='
      ) {
        conditionalOperators.push('>=');
        i++;
        continue;
      }
      if (
        i < condition.length &&
        condition[i] === '<' &&
        condition[i + 1] === '='
      ) {
        conditionalOperators.push('<=');
        i++;
        continue;
      }
      if (condition[i] === '>') {
        conditionalOperators.push('>');
        continue;
      }

      if (condition[i] === '<') {
        conditionalOperators.push('<');
        continue;
      }

      if (condition[i] === '=') {
        conditionalOperators.push('=');
        continue;
      }
    }

    // const conditionalOperators = condition.match(/>|<|>=|<=|=/g);

    if (!conditionalOperators || conditionalOperators.length == 0) {
      throw new Error(
        "condition argument must contain '>', '<', '>=', '<=' or '='"
      );
    }

    if (conditionalOperators.length > 1) {
      console.error(condition);
      throw new Error(
        'condition argument must contain exactly one of ">", "<", ">=", "<=" or "="'
      );
    }

    const conditionalOperator = conditionalOperators[0] as Operator;

    const [questionId, numberToCompare] = condition.split(
      new RegExp(conditionalOperator)
    );

    if (!questionId) {
      console.error(condition);
      throw new Error('questionId must be defined');
    }

    if (!numberToCompare) {
      console.error(condition);
      throw new Error('numberToCompare must be defined');
    }

    // https://regex101.com/

    if (!/^\d+(\.\d+)?$/.test(numberToCompare)) {
      console.error(condition);
      throw new Error(
        'numberToCompare must be a number in the standard decimal format (At least one number, followed by an optional group starting with one dot and 1 or more numbers. Ex : 5, 1.1, 1.05)'
      );
    }

    return [questionId, conditionalOperator, +numberToCompare];
  }
}

/* 

ID   operator        string|number

A1    > < >= <= =     

*/
