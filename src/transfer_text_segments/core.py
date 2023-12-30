from antx import transfer
from pathlib import Path
import pandas as pd

def extract_tsv_text(tsvFile,ColumnNumber):
    # read the tsv file
    predictedText = tsvFile[ColumnNumber].tolist()
    # to avoid unwanted splits in a word we replace space with _
    for count,text in enumerate(predictedText):
        predictedText[count] = predictedText[count].replace(' ','_') 
    predictedText =  "\n".join(" ".join(predictedText).split())
    # write the text to a file
    Path('tests/sample/test_extracted_tsv.txt').write_text(predictedText,encoding='utf-8')

    return predictedText

def get_original_text(OriginalText):
    target = Path(f'{OriginalText}').read_text(encoding='utf-8')
    #remove unwanted characters
    target = target.replace('“','').replace('”','')
    Path('tests/sample/test_get_original_text.txt').write_text(target,encoding='utf-8')
    return target

def transfer_text(OriginalText,PredictedTSV,ColumnNumber):

    tsvFile=pd.read_csv(f'{PredictedTSV}',sep='\t',header=None)

    source = extract_tsv_text(tsvFile,ColumnNumber)
    target = get_original_text(OriginalText)

    annotation = [['segment', '(\n)']]

    transferedText=transfer(source,annotation,target).split('\n')
    tsvFile[ColumnNumber]=transferedText
    #returns a dataframe
    return tsvFile

