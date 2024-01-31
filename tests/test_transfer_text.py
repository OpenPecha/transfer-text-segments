from pathlib import Path

import pandas as pd

from transfer_text_segments.core import (
    extract_tsv_text,
    get_original_text,
    transfer_text,
)


def test_transfer():
    assert str(
        pd.read_csv("tests/sample/resultTSV_1.tsv", sep="\t", header=None)
    ) == str(pd.read_csv("tests/sample/resultTSV_1.tsv", sep="\t", header=None))


def test_extract_tvs():
    tsvFile = pd.read_csv(
        "tests/sample/test-transcription_1.tsv", sep="\t", header=None
    )
    assert str(
        Path("tests/sample/test_extracted_tsv.txt").read_text(encoding="utf-8")
    ) == str(Path("tests/sample/test_extracted_tsv.txt").read_text(encoding="utf-8"))


def test_get_original_text():
    assert str(
        Path("tests/sample/test_get_original_text.txt").read_text(encoding="utf-8")
    ) == str(
        Path("tests/sample/test_get_original_text.txt").read_text(encoding="utf-8")
    )
