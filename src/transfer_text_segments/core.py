from pathlib import Path

import pandas as pd
from antx import transfer


def extract_tsv_text(tsvFile, ColumnNumber):
    """extracts text from dataframe using column number
    Args:
        tsvFile (Dataframe): dataframe of predicted tsv file
        ColumnNumber (integer/string):column name of the text to be extracted

    Returns:
        string: extracted text from tsv file
    """
    # read the tsv file
    predictedText = tsvFile[ColumnNumber].tolist()
    # to avoid unwanted splits in a word we replace space with _
    for count, text in enumerate(predictedText):
        predictedText[count] = predictedText[count].replace(" ", "_")
    predictedText = "\n".join(" ".join(predictedText).split())
    print("extracted text from tsv file..")
    return predictedText


def get_original_text(OriginalText):
    """reads the original text and removes unwanted characters

    Args:
        OriginalText (string): location of the original text file

    Returns:
        string: original text without unwanted characters
    """
    target = Path(f"{OriginalText}").read_text(encoding="utf-8")
    # remove unwanted characters
    target = target.replace("“", "").replace("”", "")
    print("extracted text from original file..")

    return target


def transfer_text(OriginalText, PredictedTSV, ColumnNumber='sentence'):
    """transfers the annotation from predicted text to original text and returns a dataframe

    Args:
        OriginalText (string): location of the original string
        PredictedTSV (string): location of the predicted tsv file
        ColumnNumber (int/string): name of the coloumn in which transcripted text is there in .tsv file

    Returns:
        dataframe: dataframe that contains transfered annotation on original text
    """
    tsvFile = pd.read_csv(f"{PredictedTSV}", sep="\t")
    source = extract_tsv_text(tsvFile, ColumnNumber)
    target = get_original_text(OriginalText)
    annotation = [["segment", "(\n)"]]
    transferedText = transfer(source, annotation, target).split("\n")
    if len(transferedText) > len(tsvFile):
        transferedText = transferedText[:len(tsvFile)]
        tsvFile[ColumnNumber] = transferedText
    elif len(transferedText) < len(tsvFile):
        transferedText = transferedText + [np.nan]*(len(tsvFile) - len(transferedText))
        tsvFile[ColumnNumber] = transferedText
    else:
        tsvFile[ColumnNumber] = transferedText
    # returns a dataframe
    return tsvFile
