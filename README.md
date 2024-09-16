# Data Engineering Coding Challenges

## Judgment Criteria

- Beauty of the code (beauty lies in the eyes of the beholder)
- Testing strategies
- Basic Engineering principles

## Problem 1

### Parse fixed width file

- Generate a fixed width file using the provided spec (offset provided in the spec file represent the length of each field).
- Implement a parser that can parse the fixed width file and generate a delimited file, like CSV for example.
- DO NOT use python libraries like pandas for parsing. You can use the standard library to write out a csv file (If you feel like)
- Language choices (Python or Scala)
- Deliver source via github or bitbucket
- Bonus points if you deliver a docker container (Dockerfile) that can be used to run the code (too lazy to install stuff that you might use)
- Pay attention to encoding

## Problem 2

### Data processing

- Generate a csv file containing first_name, last_name, address, date_of_birth
- Process the csv file to anonymise the data
- Columns to anonymise are first_name, last_name and address
- You might be thinking  that is silly
- Now make this work on 2GB csv file (should be doable on a laptop)
- Demonstrate that the same can work on bigger dataset
- Hint - You would need some distributed computing platform

## Choices

- Any language, any platform
- One of the above problems or both, if you feel like it.

## Problem 1: Fixed Width File Parser

This solution parses a fixed-width file and converts it into a delimited CSV file.

### Steps to execute problem-1

1. Navigate to the `problem_1` directory.
2. Ensure you have Python installed.
3. Run the script:

    ```bash
    ./fixed_width_parser.sh
    ```

### Input/Output

- Input: `input.txt` (fixed-width file)
- Output: `output.csv` (delimited CSV)

---

## Problem 2: Data Anonymization with PySpark

This solution processes a CSV file containing personal data and anonymizes the `first_name`, `last_name`, and `address` columns using PySpark.

### Steps to execute problem-2

1. Ensure you have Python and PySpark installed.
2. Navigate to the `problem_2` directory.
3. Run the script:

    ```bash
    ./anonymize_data.sh
    ```

### Input/Output

- Input: `input.csv` (CSV file with sensitive data)
- Output: `out_anonym.csv` (anonymized CSV)
