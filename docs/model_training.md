# 모델 학습
### 모델 학습 요약
```sh
 본 모델(Gemma3-1B)은 Colab 환경에서 V2 TPU 8개를 활용하여 학습하였으며, gemma 3.0.2 라이브러리를 사용하였습니다. 학습 데이터는 kaggle의 파워리프팅 데이터셋과 teacher model인 GPT-4o-mini를 활용하여 제작하였습니다.
# 모델 학습
 LoRA를 활용하여 학습하였으며, '531 프로그램 이해', '531 프로그램 루틴 추천'을 목표로 두 번의 학습을 하였습니다.
 1차적으로 Feedback-in-the-loop 구조로 모델 학습을 수행했습니다. teacher modle을 활용하여 531 프로그램 정보 데이터를 생성한 후, 해당 데이터로 모델을 학습합니다. 학습된 모델을 teacher model이 평가하고, 학습이 더욱 잘 수행될 수 있도록 개선된 데이터를 생성합니다. 이 과정을 반복하여 모델 성능을 향상시킵니다.
 2차적으로는 kaggle의 파워리프팅 대회 데이터셋과 teacher model을 활용하여, 531 프로그램 루틴 추천 데이터를 생성 및 모델 학습을 수행했습니다. 파워리프팅 대회 데이터셋을 활용하여, 실제 유저들의 신체 정보와 1RM 데이터 등을 확보하였습니다. 해당 데이터와 teacher model을 활용하여, 유저의 상황과 운동 목표에 따른 531 프로그램 루틴 추천 데이터를 생성합니다. 생성된 데이터로 모델 학습을 수행합니다.
# 모델 평가
 모델에게 531 프로그램 루틴 추천을 100회 요청한 후, 두 가지 방식으로 모델을 평가합니다. 
    (1) 100회의 요청에 대한 20%의 답변을 사람이 직접 검수하여 모델의 정확도, 할루시네이션 여부 등을 판별합니다.
    (2) 100회의 요청에 대한 모든 답변을 teacher model(GPT-4o-mini)이 평가하여 모델의 정확도, 할루시네이션 여부 등을 판별합니다.
# 모델 학습 비용
모델 학습을 위한 데이터 생성 과정에서 X만큼
모델 학습 과정에서 비용 X만큼
모델 평가 과정에서 X만큼
# 결론


```

- 모델 정보 : Gemma3-1B
    - 모델 선정 사유 :
        - 다양한 언어 지원
        - 경량화    
- 학습 환경 : Colab(V2 TPU 8개)
- 학습 설정 :
    - Lora fine-tuning1
        - Batch Size : 8
        - Epochs : 300
        - Learning Rate :
        - Optimizer :
    - Lora fine-tuning2
        - Batch Size : 8
        - Epochs : 300
        - Learning Rate :
        - Optimizer :

## 모델 학습
### Lora fine-tuning1
```mermaid
graph LR
  A(소수 seed 프롬프트) --> B(teacher LLM)
  B --> |531 프로그램 정보 데이터| C(Gemma3-1B LoRA fine-tune)
```
- 목표 : 모델에게 531 프로그램에 대하여 학습시킨다.
0. teacher LLM을 활용하여, 531 운동 프로그램 학습용 데이터 생성 : `00_generate_training_data_with_llm(GPT-4o-mini).ipynb`
0. teacher LLM을 활용하여, `Gemma3-1B`모델 학습 및 평가용 데이터 생성 : [01_training-generate_eval_data.ipynb (Colab 링크)](https://colab.research.google.com/drive/1ytDXXEpQELN29wcKBOxL4jgsN9sIUQKy?usp=sharing)
0. teacher 모델을 활용하여, 생성된 데이터 평가 및 개선된 학습 데이터 제시 : `02_eval-generate_data_with_llm(GPT-4o-mini).ipynb`
0. (1 ~ 2 단계 5회 반복)

### Lora fine-tuning2
```mermaid
graph LR
  A(소수 seed 프롬프트 + 파워리프팅 데이터) --> |Few-shot| B(teacher LLM)
  B --> |531 프로그램 루틴 추천 데이터| C(Gemma3-1B LoRA fine-tune)
```
- 목표 : 모델이 사용자의 입력에 대해 531 프로그램 루틴을 추천할 수 있게 한다.
0. kaggle의 파워리프팅 데이터 수집 및 간단한 데이터 시각화 : `00_dataset_setup.ipynb`
0. 데이터 전처리 수행 : `01_preprocess_data.ipynb`
0. teacher LLM을 활용하여, 학습용 데이터 생성 : `02_generate_training_data_with_llm.ipynb`
0. `Gemma3-1B`모델 학습 : [(Colab 링크)]()

## 모델 평가
- 평가 방식1 
    - Gemma3-1B 모델의 출력 데이터 직접 검수(20%)
        - 표본 갯수 : 100개
        - 표본 비율 : 
        - 표준 오차 : 
        - 신뢰 구간 : 
- 평가 방식2
    - teacher LLM을 활용한, Gemma3-1B 모델의 출력 데이터 검수
        - 표본 갯수 : 100개
        - 표본 비율 : 
        - 표준 오차 : 
        - 신뢰 구간 : 

## 모델 학습 비용 :
- 모델 학습 및 평가를 위한 데이터 생성 (OpenAI API)
    - OpenAI API input tokens : 
    - OpenAI API output tokens : 
- 모델 학습 (Colab)
    - 연산 장비 : V2 TPU 8개
    - 연산 비용 XX개

- 모델 학습에 사용된 리소스 (시행착오 포함) :
    - 모델 학습 및 평가를 위한 데이터 생성 (OpenAI API)
        - OpenAI API input tokens : 
        - OpenAI API output tokens : 
    - 모델 학습 (Colab)
        - 연산 장비 : V2 TPU 8개, A100 GPU
        - 연산 비용 XX개

# 결론


---

## 시행착오 내용
- 시도1
    - seed 프롬프트 생성
    - 파워리프팅 데이터로 teacher model이 생성한 데이터로 모델 학습
- 문제점 1: 답변이 구조적이지 못함. (주차가 계속 반복되는 문제 발생) `### 1주차: ....(무한 반복)`
- 문제점2 : Gemma3-1B 모델의 경우, 답변의 부정확도가 높음. Gemma3-4B 모델의 경우, 답변의 정확도가 향상되지만, 모델 크기 제한사항에 맞지 않음.
- 문제점3 : Gemma3 기술문서 참고 -> small teacher 모델로 부터 지식 증류는 받는 것이 더 낫다는 주장.
- 해결 방법
  - 작은 teacher 모델로 Sambanova Cloud의 Llama모델을 선정한다.

- 시도2
    - 위키피디아, 나무위키 데이터로 모델 학습
- 531 운동 프로그램에 대하여, 학습을 하지 않은 경우, 할루시네이션 답변 발생 `<input>531 by jim wendler에 대해서 설명해줘. -> <output>Jim Wendler의 "531"은 다양한 게임, 특히 RPG (Role-Playing ....`

- 해결 방법
    - 위키피디아, 나무위키로 파워리프팅, 웨이트 트레이닝 도메인 데이터 수집 및 모델 학습
- 문제점1 : 나무위키, 위키피디아의 설명하는 말투를 그대로 사용.
- 문제점2 : 학습 데이터 수집에 어려움이 있음. (저작권, 데이터의 갯수 부족)


- 시도3
    - teacher model로 531 운동 프로그램에 대한 지도학습 데이터 생성
    - 해당 데이터로 학습
    - teacher model을 활용한 모델 평가
- 문제점1 : 데이터 생성 비용
- 문제점2 : 모델의 답변 형식이 운동 루틴을 추천하는 것이 아닌, 531 운동 프로그램에 대하여 설명형식임.

- 시도4
    - 시도1 + 시도3
    - 시도3으로 531 운동 프로그램에 대하여 모델 학습 수행
    - 시도1의 teacher model로 지도학습 데이터 생성(프롬프트 엔지니어링을 활용하여, 할루시네여션 감소, COT 적용(?) - TM 계산 과정 명시)
    - 학습된 모델에 생성한 데이터로 모델 학습 수행
    - 답변이 일정 형식을 띔(과적합). 하지만, 루틴 추천에만 사용하는 모델이라면, 문제가 없을 것으로 예상

