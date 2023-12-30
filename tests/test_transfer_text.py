import pytest
import pandas as pd
from pathlib import Path

from transfer_text_segments.core import transfer_text
from transfer_text_segments.core import extract_tsv_text
from transfer_text_segments.core import get_original_text

def test_transfer():
    assert str(transfer_text('tests/sample/test_orginal_1.txt','tests/sample/test-transcription_1.tsv',3)) == str(pd.read_csv('tests/sample/resultTSV_1.tsv',sep='\t',header=None))
def test_extract_tvs():
    tsvFile=pd.read_csv('tests/sample/test-transcription_1.tsv',sep='\t',header=None)
    assert str(extract_tsv_text(tsvFile,3)) == str(Path('tests/sample/test_extracted_tsv.txt').read_text(encoding='utf-8'))
def test_get_original_text():
    assert str(get_original_text('tests/sample/test_orginal_1.txt')) == str(Path('tests/sample/test_get_original_text.txt').read_text(encoding='utf-8'))