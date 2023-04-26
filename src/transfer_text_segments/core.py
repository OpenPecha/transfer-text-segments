from pathlib import Path

import pandas as pd
from antx import transfer


def extract_tsv_text(tsvFile, ColumnNumber):
    # read the tsv file
    predictedText = tsvFile[ColumnNumber].tolist()
    # to avoid unwanted splits in a word we replace space with _
    for count, text in enumerate(predictedText):
        predictedText[count] = predictedText[count].replace(" ", "_")
    predictedText = "\n".join(" ".join(predictedText).split())
    print("extracted text from tsv file..")
    return predictedText


def get_original_text(OriginalText):
    target = Path(f"{OriginalText}").read_text(encoding="utf-8")
    # remove unwanted characters
    target = target.replace("“", "").replace("”", "")
    print("extracted text from original file..")

    return target


def transfer_text(OriginalText, PredictedTSV, ColumnNumber):

    tsvFile = pd.read_csv(f"{PredictedTSV}", sep="\t", header=None)
    source = extract_tsv_text(tsvFile, ColumnNumber)
    target = get_original_text(OriginalText)

    annotation = [["segment", "(\n)"]]

    transferedText = transfer(source, annotation, target).split("\n")
    tsvFile[ColumnNumber] = transferedText
    # returns a dataframe
    return tsvFile


print(
    transfer_text(
        "tests/sample/test_get_original_text.txt",
        "tests/sample/test-transcription_1.tsv",
        3,
    )
)
