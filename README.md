# Simple Question Answering System

### Description:
This is HCMUT natural language processing (NLP) course mini assignment about question answering system <br> for simple intercity train database.

### Folder hierachy:
* "main.py": Program entry point.
* "Input/database": Intercity train data save as text file (replace database system).
* "Input/question": Simple question.
* "Models": Program modules.
* "Output": Associate with each questions.

### Implementation:
Process with following step (output of current step is input of the next step):
1. Tokenize sentences and get type of each phrase.
2. Perform dependency parsing.
3. Transform into grammartical relation.
4. Transform into logical form.
5. Transform into procedure semantics.
6. Execute procedure semantics to answer the question.

Write to output file result of step 2 -> 6.

### Run application:
```
python main.py
```
> or
```
python3 main.py
```
