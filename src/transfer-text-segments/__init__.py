from antx import transfer
from pathlib import Path
import pandas as pd
# read the tsv file
tcvFile=pd.read_csv('tests/sample/Marpa-ep1-transcription.tsv',sep='\t',header=None)
predictedText = tcvFile[3].tolist()

