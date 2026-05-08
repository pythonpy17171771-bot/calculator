
import math
import streamlit as st

st.set_page_config(
    page_title="다기능 계산기",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 다기능 계산기")
st.write("사칙연산, 모듈러연산, 지수연산, 로그연산을 지원합니다.")

# 계산 기록 저장
if "history" not in st.session_state:
    st.session_state.history = []

operations = [
    "덧셈 (+)",
    "뺄셈 (-)",
    "곱셈 (×)",
    "나눗셈 (÷)",
    "모듈러 (%)",
    "지수 (a^b)",
    "로그 (log_b(a))"
]

with st.form("calculator_form"):
    operation = st.selectbox("연산을 선택하세요", operations)

    st.subheader("입력값")
    num1 = st.number_input("첫 번째 값 (a)", value=0.0, format="%.6f")
    num2 = st.number_input("두 번째 값 (b)", value=0.0, format="%.6f")

    submitted = st.form_submit_button("계산하기")

if submitted:
    try:
        result = None
        expression = ""

        if operation == "덧셈 (+)":
            result = num1 + num2
            expression = f"{num1} + {num2}"

        elif operation == "뺄셈 (-)":
            result = num1 - num2
            expression = f"{num1} - {num2}"

        elif operation == "곱셈 (×)":
            result = num1 * num2
            expression = f"{num1} × {num2}"

        elif operation == "나눗셈 (÷)":
            if num2 == 0:
                st.error("0으로 나눌 수 없습니다.")
            else:
                result = num1 / num2
                expression = f"{num1} ÷ {num2}"

        elif operation == "모듈러 (%)":
            if num2 == 0:
                st.error("0으로 나눈 나머지는 정의되지 않습니다.")
            else:
                # 모듈러는 보통 정수 느낌이 강하지만,
                # 파이썬에서는 실수에도 % 연산이 가능합니다.
                result = num1 % num2
                expression = f"{num1} % {num2}"

        elif operation == "지수 (a^b)":
            result = num1 ** num2
            expression = f"{num1}^{num2}"

        elif operation == "로그 (log_b(a))":
            # log_b(a)는 a > 0, b > 0, b != 1 이어야 함
            if num1 <= 0:
                st.error("로그의 진수 a는 0보다 커야 합니다.")
            elif num2 <= 0 or num2 == 1:
                st.error("로그의 밑 b는 0보다 크고 1이 아니어야 합니다.")
            else:
                result = math.log(num1, num2)
                expression = f"log_{num2}({num1})"

        if result is not None:
            st.success(f"결과: {result}")

            st.session_state.history.insert(
                0,
                {
                    "expression": expression,
                    "result": result
                }
            )

    except OverflowError:
        st.error("값이 너무 커서 계산할 수 없습니다.")
    except ValueError:
        st.error("입력값 범위를 확인해주세요.")
    except Exception as e:
        st.error(f"오류가 발생했습니다: {e}")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("사용 방법")
    st.markdown(
        """
        - **a, b** 값을 입력합니다.
        - 원하는 연산을 선택합니다.
        - **계산하기** 버튼을 누릅니다.

        **로그 연산**
        - `a = 진수`
        - `b = 밑`
        - 즉, `log_b(a)`를 계산합니다.
        """
    )

with col2:
    st.subheader("계산 기록")
    if st.session_state.history:
        for i, item in enumerate(st.session_state.history[:10], start=1):
            st.write(f"{i}. {item['expression']} = {item['result']}")
    else:
        st.write("아직 계산 기록이 없습니다.")

if st.button("기록 지우기"):
    st.session_state.history = []
    st.success("계산 기록을 지웠습니다.")
