import { ConditionalParser } from './conditional-parser';

describe('ConditionalParser should work as expected', () => {
  describe('parseConditional method should return the expected value', () => {
    it('should not work with an empty string', () => {
      expect(() => {
        const parser = new ConditionalParser();
        parser.parseCondition('');
      }).toThrowError('No condition provided');
    });

    it('should not work if the type of condition is not a string', () => {
      expect(() => {
        const parser = new ConditionalParser();

        //@ts-ignore
        parser.parseCondition(1);
      }).toThrowError('Condition must be a string');
    });

    it('should trow an error if no conditional operator exists in the condition', () => {
      expect(() => {
        const parser = new ConditionalParser();
        parser.parseCondition('1');
      }).toThrowError(
        "condition argument must contain '>', '<', '>=', '<=' or '='"
      );
    });

    it('should throw an error if multiple conditional operators are present in the condition', () => {
      expect(() => {
        const parser = new ConditionalParser();
        parser.parseCondition('1>2>3');
      }).toThrowError(
        'condition argument must contain exactly one of ">", "<", ">=", "<=" or "="'
      );

      expect(() => {
        const parser = new ConditionalParser();
        parser.parseCondition('1>2>=3');
      }).toThrowError(
        'condition argument must contain exactly one of ">", "<", ">=", "<=" or "="'
      );

      expect(() => {
        const parser = new ConditionalParser();
        parser.parseCondition('1>2>3');
      }).toThrowError(
        'condition argument must contain exactly one of ">", "<", ">=", "<=" or "="'
      );

      expect(() => {
        const parser = new ConditionalParser();
        parser.parseCondition('1<2>3');
      }).toThrowError(
        'condition argument must contain exactly one of ">", "<", ">=", "<=" or "="'
      );

      expect(() => {
        const parser = new ConditionalParser();
        parser.parseCondition('1<<2');
      }).toThrowError(
        'condition argument must contain exactly one of ">", "<", ">=", "<=" or "="'
      );

      expect(() => {
        const parser = new ConditionalParser();
        parser.parseCondition('1>=2>4');
      }).toThrowError(
        'condition argument must contain exactly one of ">", "<", ">=", "<=" or "="'
      );

      expect(() => {
        const parser = new ConditionalParser();
        parser.parseCondition('1=2>=3');
      }).toThrowError(
        'condition argument must contain exactly one of ">", "<", ">=", "<=" or "="'
      );
    });

    it('should throw an error if the condition is missing a question id at the left hand side of the operator', () => {
      expect(() => {
        const parser = new ConditionalParser();
        parser.parseCondition('>2');
      }).toThrowError('questionId must be defined');
    });

    it('should throw an error if there is no number to compare the answer to at the right of the condtional operator', () => {
      expect(() => {
        const parser = new ConditionalParser();
        parser.parseCondition('1>');
      }).toThrowError('numberToCompare must be defined');
    });

    it('should throw an error if the number to compare is not a number', () => {
      expect(() => {
        const parser = new ConditionalParser();
        parser.parseCondition('1>a');
      }).toThrowError(
        'numberToCompare must be a number in the standard decimal format (At least one number, followed by an optional group starting with one dot and 1 or more numbers. Ex : 5, 1.1, 1.05)'
      );
    });

    it('ab>1.112', () => {
      const parser = new ConditionalParser();
      const result = parser.parseCondition('h1a>1.112');

      expect(result).toEqual(['h1a', '>', 1.112]);
    });

    it('ab>1.112a', () => {
      expect(() => {
        const parser = new ConditionalParser();
        parser.parseCondition('ab>1.112a');
      }).toThrowError(
        'numberToCompare must be a number in the standard decimal format (At least one number, followed by an optional group starting with one dot and 1 or more numbers. Ex : 5, 1.1, 1.05)'
      );
    });

    it('ab>1.', () => {
      expect(() => {
        const parser = new ConditionalParser();
        const result = parser.parseCondition('ab>1.');
      }).toThrowError(
        'numberToCompare must be a number in the standard decimal format (At least one number, followed by an optional group starting with one dot and 1 or more numbers. Ex : 5, 1.1, 1.05)'
      );
    });

    it('1>2', () => {
      const parser = new ConditionalParser();

      const result = parser.parseCondition('1>2');
      expect(result).toEqual(['1', '>', 2]);
    });

    it('1>=2', () => {
      const parser = new ConditionalParser();

      const result = parser.parseCondition('1>=2');
      expect(result).toEqual(['1', '>=', 2]);
    });

    it('1<=2', () => {
      const parser = new ConditionalParser();

      const result = parser.parseCondition('1<=2');
      expect(result).toEqual(['1', '<=', 2]);
    });

    it('1=1', () => {
      const parser = new ConditionalParser();

      const result = parser.parseCondition('1=1');
      expect(result).toEqual(['1', '=', 1]);
    });

    it('1<2', () => {
      const parser = new ConditionalParser();
      const result = parser.parseCondition('1<2');
      expect(result).toEqual(['1', '<', 2]);
    });

    it('ab>1.1', () => {
      const parser = new ConditionalParser();
      const result = parser.parseCondition('ab>1.1');
      expect(result).toEqual(['ab', '>', 1.1]);
    });
  });
});
