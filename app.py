import streamlit as st

# 1. 앱 제목 및 설명
st.title("💬 실시간 의사소통 기능 분석기")
st.write("분석하고 싶은 발화를 아래에 입력하고 '분석하기' 버튼을 눌러보세요.")

# 2. 사용자 입력창 (멀티라인 입력 가능)
user_input = st.text_area("발화 내용 입력:", placeholder="예: 오늘 점심 뭐 먹을까?")

# 3. 분석 버튼
if st.button("의사소통 기능 분석"):
    if user_input.strip() == "":
        st.warning("내용을 입력해주세요!")
    else:
        # 여기에 분석 로직 추가 (예시: 간단한 키워드 매칭 또는 LLM API 호출)
        # 지금은 간단한 예시 결과를 보여줍니다.
        st.subheader("📌 분석 결과")
        
        # 임시 분석 로직 (Vibe Coding으로 LLM을 연결하면 더 정확해집니다)
        if "?" in user_input:
            function = "질문하기 (Request Information)"
        elif "!" in user_input:
            function = "감정 표현 (Expression)"
        else:
            function = "정보 제공 (Reporting)"
            
        st.info(f"입력한 발화: **{user_input}**")
        st.success(f"추정되는 의사소통 기능: **{function}**")
