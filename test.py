import os
from dotenv import load_dotenv
import google.generativeai as genai

# .env ファイルから API キーを読み込む
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# API キーを設定
genai.configure(api_key=api_key)

# Gemini Pro モデルを指定してクライアントを作成
model = genai.GenerativeModel('gemini-pro')


response = model.generate_content(
    "What's the weather like in Tokyo?",
    generation_config=genai.types.GenerationConfig(
        temperature=0.7
    )
)

# 出力結果を表示
print(response.text)