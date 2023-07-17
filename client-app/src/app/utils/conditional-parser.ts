type QuestionID = string;
type Operator = '>' | '<' | '>=' | '<=' | '=';
type NumberToCompare = number;

type ParsedConditional = [QuestionID, Operator, NumberToCompare];

export class ConditionalParser {
  // parse(statement: string): ParsedConditional[] {
  //   const statements = statement.split('and');
  //   return statements.map(this.parseCondition);
  // }

  parseCondition(condition: string): Array<{
    questionID: string;
    operator: Operator;
    conditionAnswer: number;
    logicalOperator?: string;
  }> {
    if (!condition) {
      throw new Error('No condition provided');
    }

    if (typeof condition !== 'string') {
      throw new Error('Condition must be a string');
    }

    const logicalOperators = condition.match(/&&|\|\|/g) || [];
    const conditions = condition.split(/&&|\|\|/g);

    if (conditions.length - 1 !== logicalOperators.length) {
      throw new Error('Syntax error in condition string');
    }

    return conditions.map((condition, index) => {
      const conditionalOperators: string[] = [];

      for (let i = 0; i < condition.length; i++) {
        if (condition[i] === '>' && condition[i + 1] === '=') {
          conditionalOperators.push('>=');
          i++;
          continue;
        }
        if (condition[i] === '<' && condition[i + 1] === '=') {
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

      if (!conditionalOperators || conditionalOperators.length === 0) {
        throw new Error(
          "condition argument must contain '>', '<', '>=', '<=' or '='"
        );
      }

      if (conditionalOperators.length > 1) {
        console.error(condition);
        throw new Error(
          'Each condition must contain exactly one of ">", "<", ">=", "<=" or "="'
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

      if (!/^\d+(\.\d+)?$/.test(numberToCompare)) {
        console.error(condition);
        throw new Error(
          'numberToCompare must be a number in the standard decimal format (At least one number, followed by an optional group starting with one dot and 1 or more numbers. Ex : 5, 1.1, 1.05)'
        );
      }

      return {
        questionID: questionId.trim(),
        operator: conditionalOperator,
        conditionAnswer: +numberToCompare,
        logicalOperator: logicalOperators[index],
      };
    });
  }

  // TODO (simon) -> old method
  // parseCondition(condition: string): ParsedConditional {
  //   if (!condition) {
  //     throw new Error('No condition provided');
  //   }

  //   if (typeof condition !== 'string') {
  //     throw new Error('Condition must be a string');
  //   }

  //   const conditionalOperators: string[] = [];

  //   // todo cleanup this part
  //   for (let i = 0; i < condition.length; i++) {
  //     if (
  //       i < condition.length &&
  //       condition[i] === '>' &&
  //       condition[i + 1] === '='
  //     ) {
  //       conditionalOperators.push('>=');
  //       i++;
  //       continue;
  //     }
  //     if (
  //       i < condition.length &&
  //       condition[i] === '<' &&
  //       condition[i + 1] === '='
  //     ) {
  //       conditionalOperators.push('<=');
  //       i++;
  //       continue;
  //     }
  //     if (condition[i] === '>') {
  //       conditionalOperators.push('>');
  //       continue;
  //     }

  //     if (condition[i] === '<') {
  //       conditionalOperators.push('<');
  //       continue;
  //     }

  //     if (condition[i] === '=') {
  //       conditionalOperators.push('=');
  //       continue;
  //     }
  //   }

  //   // const conditionalOperators = condition.match(/>|<|>=|<=|=/g);

  //   if (!conditionalOperators || conditionalOperators.length == 0) {
  //     throw new Error(
  //       "condition argument must contain '>', '<', '>=', '<=' or '='"
  //     );
  //   }

  //   if (conditionalOperators.length > 1) {
  //     console.error(condition);
  //     throw new Error(
  //       'condition argument must contain exactly one of ">", "<", ">=", "<=" or "="'
  //     );
  //   }

  //   const conditionalOperator = conditionalOperators[0] as Operator;

  //   const [questionId, numberToCompare] = condition.split(
  //     new RegExp(conditionalOperator)
  //   );

  //   if (!questionId) {
  //     console.error(condition);
  //     throw new Error('questionId must be defined');
  //   }

  //   if (!numberToCompare) {
  //     console.error(condition);
  //     throw new Error('numberToCompare must be defined');
  //   }

  //   // https://regex101.com/

  //   if (!/^\d+(\.\d+)?$/.test(numberToCompare)) {
  //     console.error(condition);
  //     throw new Error(
  //       'numberToCompare must be a number in the standard decimal format (At least one number, followed by an optional group starting with one dot and 1 or more numbers. Ex : 5, 1.1, 1.05)'
  //     );
  //   }

  //   return [questionId, conditionalOperator, +numberToCompare];
  // }
}

/* 

ID   operator        string|number

A1    > < >= <= =     

*/
