import streamlit as at
from utils import generate_script

at.title("🎬 视频脚本生成器")
# streamlit run main.py

with at.sidebar:
    openai_api_key = at.text_input("请输入OpenAI API密钥：",type="password")
    at.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-keys)")
# 密钥：2b-Jswuf9vZWSba

subject = at.text_input("💡 请输入视频的主题")
video_length = at.number_input("⏱️ 请输入视频的大致时长（单位：分钟）",min_value=0.1,step=0.1)
creativity = at.slider("✨ 请输入视频脚本的创造力（数字小说明更严谨，数字大说明更多样）",min_value=0.0,max_value=1.0,value=0.2,step=0.1)

submit = at.button("生成脚本")
if submit and not openai_api_key:
    at.info("请输入你的OpenAI API密钥")
    at.stop()
#到此即停了
if submit and not subject:
    at.info("请输入视频的主题")
    at.stop()
if submit and not video_length >= 0.1:
    at.info("视频长度需要大于或等于0.1")
    at.stop()

if submit:
    with at.spinner(("AI正在思考中，请稍等...")):
        search_result,title,script = generate_script(subject,video_length,creativity,openai_api_key)

        at.success("视频脚本已生成！")
        at.subheader("🔥 标题：")
        at.write(title)
        at.subheader("📝 视频脚本：")
        at.write(script)

        with at.expander("维基百科搜索结果 👀"):
            at.info(search_result)