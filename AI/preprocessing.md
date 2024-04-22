# 전처리

---

## Text Preprocessing

데이터를 용도에 맞게 사용하기 위해선 토큰화, 정제, 정규화의 과정을 거쳐야 함

### 단어 토큰화

> **Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop.**
> 

다음 문장의 경우, Don’t나 Mr.Jone’s를 어떻게 토큰화할지에 대한 여러가지 선택지가 있음.

```python
from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer
from tensorflow.keras.preprocessing.text import text_to_word_sequence

# text_to_word_sequence(text) 
# ["don't", 'be', 'fooled', 'by', 'the', 'dark', 'sounding', 'name', 
#    'mr', "jone's", 'orphanage', 'is', 'as', 'cheery', 'as', 'cheery', 
#    'goes', 'for', 'a', 'pastry', 'shop']
```

이 중 `text_to_word_sequence` 를 사용하면 마침표나 콤마, 느낌표 등의 구두점을 제외하고  토큰화함.

### 문장 토큰화

토큰의 단위가 문장일 경우, 물음표, 느낌표, 마침표로 문장을 분리하면 될 것 같지만 Mr.Jones와 같이 단어에서 마침표를 활용하는 경우가 있음 → 라이브러리 갖다 쓰면 알아서 잘 해줌👍

```python
from nltk.tokenize import sent_tokenize     # 영어
import kss                                  # 한국어
```

### 형태소

한국어는 영어와 다르게 띄어쓰기에 민감하지 않고, 조사라는 것이 존재하기 때문에 같은 단어라도 조사가 붙어 다른 단어로 인식되는 것을 주의 → 형태소의 종류로 구분

- **자립 형태소** : 접사, 어미, 조사와 상관없이 자립하여 사용할 수 있는 형태소. 그 자체로 단어가 된다. 체언(명사, 대명사, 수사), 수식언(관형사, 부사), 감탄사 등이 있다.
- **의존 형태소** : 다른 형태소와 결합하여 사용되는 형태소. 접사, 어미, 조사, 어간을 말한다.

이러한 형태소를 분석해주는 라이브러리로 `Okt`, `Mecab`, `Komoran`, `Hannanum`, `Kkma` 가 있으며 결론적으로 말하자면, 성능 우선이면 `Hannanum`, `Kkma` 를 선택하고, 속도 우선이면 `Mecab` 사용할 것.

### 정제

자연어가 아니면서 아무 의미가 없는 글자들이나 분석하고자 하는 목적에 맞지 않는 불필요 단어들을 정제해야 함 → 불용어, 등장빈도 적은 단어, 길이 짧은 단어

### 정규화

정규화 기법 중 단어의 개수를 줄이는 기법으로 표제어 추출과 어간 추출이 있음.

- **표제어 추출**

단어들로부터 표제어를 찾아가는 과정 → 단어들이 다른 형태를 가지더라도 그 뿌리 단어를 찾아가서 단어의 개수를 줄일 수 있는지 파악.

이를 위해서 단어들을 형태소 단위로 분리하여 구분하는 과정을 거쳐야 함. 형태소의 종류로는 어간(stem)과 접사(affix)가 있음.

- **어간** : 단어의 의미를 담고 있는 핵심 부분 ex) cats의 ‘cat’
- **접사** : 단어의 추가적인 의미를 주는 부분 ex) cats의 ‘s’

‘cat’과 ‘cats’ 두 단어가 제시되었을 때 형태소 분리를 통해 같은 단어임을 파악할 수 있다.

- **어간 추출**

형태소로 분리하는 과정을 단순화한 것 → 어림짐작으로 비슷한 형태의 단어를 변환하는 알고리즘을 적용함.

예를 들면, 왼쪽의 알고리즘을 단어에 적용하면 오른쪽과 같은 결과가 나온다.

**알고리즘**

```python
ALIZE → AL
ANCE → 제거
ICAL → IC
```

**적용 결과**

```python
formalize → formal
allowance → allow
electricical → electric
```