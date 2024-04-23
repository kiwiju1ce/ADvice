RNN(Recurrent Neural Network)
---

<aside>
💡 가장 기본적인 인공 신경망 시퀀스 모델

</aside>

순환 신경망으로, 재귀 신경망(Recursive Neural Network)과는 다른 개념임.



### RNN의 특징 세가지

- **메모리 기능**

일반적으로 신경망들은 은닉층에서 출력층 방향으로 상태 값을 보내지만, 순환 신경망은 **`출력층`** 뿐만 아니라 **`은닉층의 노드`**도 보낼 수 있다는 특징이 있음.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/6d5bed8f-ebf3-4ada-b901-fc60fee8319e/c140f05c-e1da-4c7a-b84e-d34b3240404c/Untitled.png)

이 때문에 각각의 노드는 이전의 값을 기억하기 위해 메모리 역할을 수행해야 하며 이를 수행하는 노드를 메모리 셀이라고 함 → 메모리 셀은 t시점에 은닉 상태를 계산하기 위해 t-1시점의 상태 값도 포함.

- **입출력 길이의 다양성**

RNN은 입력과 출력의 길이를 다르게 설계하여 다양한 용도로 사용할 수 있음.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/6d5bed8f-ebf3-4ada-b901-fc60fee8319e/6b8b6503-ffad-477e-9933-384bcdf4089e/Untitled.png)

- **One-to-Many** : 입력층이 하나, 출력층이 여러 개일 때
- 하나의 이미지에 사진의 제목 출력 - 단어의 나열인 제목(여러 개의 출력)
- **Many-to-One** : 입력층이 여러 개, 출력층이 하나일 때
- 문장이 긍정적인지 부정적인지 판별하는 감성 분류
- **Many-to-Many** : 입력층이 여러 개, 출력층이 여러 개일 때
- 챗봇, 번역기, 품사 태깅

- **순차적 데이터 처리**

입력받은 순서에 따라 순차적으로 은닉층의 입력 값으로 들어감 → 문장이나 시계열 데이터 처리

### 양방향 순환 신경망

```markdown
운동을 열심히 하는 것은 [        ]을 늘리는데 효과적이다.

1) 근육
2) 지방
3) 스트레스
```

단방향 순환 신경망의 경우, 과거 시점의 입력만 고려하여 결과를 도출하기 때문에 “운동을 열심히 하는 것은” 이라는 문장만 보고 빈 칸을 채워야 함.

하지만 빈 칸에 들어갈 단어를 찾기 위해선 단순히 앞의 문장을 파악하는 것이 아닌 앞뒤 문맥을 파악해야 하므로 과거 시점과 미래 시점의 입력 모두 고려하는 양방향 순환 신경망을 제안

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/6d5bed8f-ebf3-4ada-b901-fc60fee8319e/97525cc5-f78e-45f3-9e3d-3517bd392647/Untitled.png)

### RNN의 한계

RNN은 비교적 짧은 시퀀스에 대해서만 효과를 보인다는 단점이 있음.

중요한 정보가 입력의 앞 쪽에 위치하고 있을 경우, 뒤로 갈수록 앞의 정보가 희석되어버림.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/6d5bed8f-ebf3-4ada-b901-fc60fee8319e/e40df1ad-9fbb-4ed7-994c-4f00455d2cb7/Untitled.png)

이러한 문제를 **장기 의존성 문제**라 하며 이를 해결하고자 LSTM(Long Short-Term Memory), GRU(Gated Recurrent Unit)가 제안되었음.

- LSTM의 장기 의존성 문제 해결책을 유지하고 구조를 간단화시킨 것이 GRU임.