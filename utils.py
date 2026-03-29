from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import wikipediaapi
import os


def generate_script(subject, Video_length, creativity, api_key):
    title_template = ChatPromptTemplate.from_messages([
        ("human", "请为'{subject}'这个主题的视频想一个吸引人的标题")
    ])

    script_template = ChatPromptTemplate.from_messages([
        ("human",
         """你是一位短视频频道的博主。根据以下标题和相关信息，为短视频脚本创作。
         视频标题：{title}，时长：{duration}分钟。
         格式：【开头、中间、结尾】，风格轻松有趣，吸引年轻人。
         参考资料：```{wikipedia_search}```""")
    ])

    model = ChatOpenAI(
        model="gpt-3.5-turbo",
        api_key=api_key,
        base_url="https://api.shubiaobiao.com/v1",
        temperature=creativity
    )

    tit_chain = title_template | model
    script_chain = script_template | model

    title = tit_chain.invoke({"subject": subject}).content

    # ✅ 修复：必须加 user_agent 参数，否则云端报错
    wiki = wikipediaapi.Wikipedia(
        user_agent="MyApp/1.0",
        language='zh',
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )

    page = wiki.page(subject)
    search_result = page.text if page.exists() else "未找到相关内容"

    script = script_chain.invoke({
        "title": title,
        "duration": Video_length,
        "wikipedia_search": search_result
    }).content

    return search_result, title, script