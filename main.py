from Models.API import *
from Models.IO import *

def main() -> None:
    io = IO.getInstance()
    preprocess = PreProcessing.getInstance()
    process = Process.getInstance()

    sentences = io.loadData("Input/question/")

    for i, text in enumerate(sentences):
        tokens = preprocess.tokenize(text)
        types = preprocess.getWordTypes(tokens)

        io.writeData(f"Output/output_{i+1}.txt", "w+", f"##### OUTPUT OF QUERY QUESTION {i+1} #####\n\n")
        for result in process.pipeline(tokens, types):
            io.writeData(f"Output/output_{i+1}.txt", "a+", str(result))


if __name__ == '__main__':
    main()