import streamlit as st
from utils import generate_script

st.title("🎬 视频脚本生成器")
# streamlit run main.py
# 侧边栏
with st.sidebar:
    openai_api_key = st.text_input("请输入OpenAI API密钥：", type="password")
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-keys)")

# 密钥：2b-Jswuf9vZWSba
# 输入
subject = st.text_input("💡 请输入视频的主题")
video_length = st.number_input("⏱️ 请输入视频的大致时长（单位：分钟）", min_value=0.1, step=0.1)
creativity = st.slider("✨ 请输入视频脚本的创造力（数字小更严谨，数字大更多样）", min_value=0.0, max_value=1.0, value=0.2, step=0.1)

# 提交按钮
submit = st.button("生成脚本")

# 判断逻辑
if submit and not openai_api_key:
    st.info("请输入你的OpenAI API密钥")
    st.stop()#到此即停了

if submit and not subject:
    st.info("请输入视频的主题")
    st.stop()

if submit and video_length < 0.1:
    st.info("视频长度需要大于或等于0.1")
    st.stop()

# 生成脚本
if submit:
    with st.spinner("AI正在思考中，请稍等..."):
        search_result, title, script = generate_script(subject, video_length, creativity, openai_api_key)

    st.success("视频脚本已生成！")
    st.subheader("🔥 标题：")
    st.write(title)
    st.subheader("📝 视频脚本：")
    st.write(script)

    with st.expander("维基百科搜索结果 👀"):
        st.info(search_result)