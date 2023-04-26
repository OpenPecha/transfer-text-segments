[<img src="https://avatars.githubusercontent.com/u/82142807?s=400&amp;u=19e108a15566f3a1449bafb03b8dd706a72aebcd&amp;v=4" alt="OpenPecha" width="150" class="jop-noMdConv">](https://openpecha.org)

### Transfer text segment annotations to the original text

## Usage

### Install using pip.

```
pip install git+https://github.com/OpenPecha/transfer-text-segments.git

```

### Import

```python
from transfer_text_segments import transfer_text
```

### Transfer_text
```python

orginaltext_with_annotation = transfer(Original_text_location,Predicted_tsv_location Column_name)
```

**Original_text_location** := contains location of the original text

**Predicted_tsv_location ** := contains location of the tsv file

**Column_name** := contains column name of the text in the Predicted_tsv (starts from 0)


**Example**


```python
original_text =  "sample/test_orginal_1.txt"
#file contains: མར་པ་ལོ་ཙཱ་བ་ཆོས་ཀྱི་བློ་གྲོས། མར་པ་ཆོས་ཀྱི་བློ་གྲོས་ནི། ཕྱི་ལོ་ ༡༠༡༡ ལོར་བྲག་ཕུག་ཆུ་ཁྱེར་ཞེས་པའི་ས་གནས་སུ་སྐུ་འཁྲུངས།

```

```python
predicted_tsv =  "sample/test_transcription_1.tsv"
#file contains:
#Marpa-ep1-001.wav	1.9	3.65	མར་པ་ཆོས་ཀྱི་ལོ་འགྲོས
#Marpa-ep1-002.wav	5.4	7.2	མར་པ་ཆོས་གོི་སློ་གྲོད་ནི།
#Marpa-ep1-003.wav	7.75	9.65	སཤི་ལོ་རྒྱ་མད་བཅུགས་རྗིས་སལོར་དུ།
#Marpa-ep1-004.wav	9.9	12.55	བགྲ་བུགས་ཆུ་སྐྱིར་ཞེས་བྱ་བའི་ས་ནས་སུ་འདགུ་ཕྲུང༌།
```

```python
column  =  3
# 0.                1    2        3
#Marpa-ep1-001.wav	1.9	   3.65	  མར་པ་ཆོས་ཀྱི་ལོ་འགྲོས
#Marpa-ep1-002.wav	5.4 	 7.2	 མར་པ་ཆོས་གོི་སློ་གྲོད་ནི།
#Marpa-ep1-003.wav	7.75	 9.65  སཤི་ལོ་རྒྱ་མད་བཅུགས་རྗིས་སལོར་དུ།
#Marpa-ep1-004.wav	9.9	   12.55	 བགྲ་བུགས་ཆུ་སྐྱིར་ཞེས་བྱ་བའི་ས་ནས་སུ་འདགུ་ཕྲུང༌།
```

```python
result = transfer_text(original_text, predicted_tsv,3)

extracted text from tsv file..
extracted text from original file..
Annotation transfer started...
Mapping annotations to tofu-IDs
[INFO] Computing diffs ...
source /Users/tenzingayche/Desktop/transfer-text-segments/.venv/bin/activate
[INFO] Diff computed!
Transfering annotations...
```

```python
print(result)
#Note: It returns a dataframe
              0     1      2            3
0  Marpa-ep1-001.wav  1.90   3.65  མར་པ་ལོ་ཙཱ་བ་ཆོས་ཀྱི་བློ་གྲོས།
1  Marpa-ep1-002.wav  5.40   7.20  མར་པ་ཆོས་ཀྱི་བློ་གྲོས་ནི།
2  Marpa-ep1-003.wav  7.75   9.65  ཕྱི་ལོ་ ༡༠༡༡ ལོར་
3  Marpa-ep1-004.wav  9.90  12.55  བྲག་ཕུག་ཆུ་ཁྱེར་ཞེས་པའི་ས་གནས་སུ་སྐུ་འཁྲུངས།
```
## Project owner(s)

<!-- Link to the repo owners' github profiles -->

- [@10zinten](https://github.com/10zinten)
- [@kaldan007](https://github.com/kaldan007)
- [@spsither](https://github.com/spsither)
- [@evanyerburgh](https://github.com/evanyerburgh)
- [@TenzinGayche](https://github.com/TenzinGayche)

## Integrations

<!-- Add any intregrations here or delete `- []()` and write None-->

None
## Docs

<!-- Update the link to the docs -->

Read the docs about antx [here]([https://wiki.openpecha.org/#/dev/coding-guidelines](https://github.com/Esukhia/antx)).
```
