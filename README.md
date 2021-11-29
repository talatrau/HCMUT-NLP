# Simple Question Answering System

### Description:
This is HCMUT natural language processing (NLP) course mini assignment about question answering system <br> for simple intercity train database.

### Requirement:
1. Build the grammar parsing of dependency grammar.
2. Parsing and output the relations of each query questions.
3. Create grammartical relation from output of previous step.
4. Create logical form from output of previous step.
5. Create procedure semantics from output of previous step.
6. Query database to get the right answer for each query questions.

### Folder hierachy:
* "main.py": Program entry point.
* "Input/database": Intercity train data save as text file (replace database system).
* "Input/question": Simple question.
* "Models": Program modules.
* "Output": Associate with each query questions.

### Implementation:
Process with following step (output of current step is the input of the next step):
1. Tokenize sentences and get type of each phrase.
2. Perform dependency parsing.
3. Transform into grammartical relation.
4. Transform into logical form.
5. Transform into procedure semantics.
6. Execute procedure semantics to answer the question.

Write to output file result of step 2 -> 6 associate with each query questions.

### Run application:
```
python main.py
```
> or
```
python3 main.py
```
