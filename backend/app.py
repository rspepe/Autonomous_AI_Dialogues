from collections import deque
import datetime
import json
import logging
import openai
import os
import re
import urllib.request

openai.api_key = os.getenv("OPENAI_API_KEY")

conversation_history = deque(maxlen=60)

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)


def chat_AI():
    logging.info(len(conversation_history))
    # 表示可能開始日時のスタート日時を定義
    start_datetime = datetime.datetime.now()
    try:
        if not conversation_history:
            prompt = 'AI1とAI2の会話を20往復の会話をして。口調はフレンドリーで。会話はその後も続くように終わらせないで。30文字以内で。会話はJSON形式で[{"name":"名前","message":"メッセージ"}]'
        else:
            # 過去の最後の日時に上書き
            start_datetime = datetime.datetime.fromisoformat(
                conversation_history[-1]["visible_from"]
            )

            # Get the last 10 items from the conversation_history deque
            last_10_items = list(conversation_history)[-10:]

            # Initialize an empty string to hold the conversation
            conversation_string = ""

            # Iterate over each item in the last 10 items
            for item in last_10_items:
                # Append to the conversation string in the required format
                conversation_string += f'「{item["name"]}」さんが「{item["message"]}」と言いました。'

            prompt = (
                f"AI1とAI2が以下の会話をしています。 {conversation_string} この会話に続く会話を20往復出力して。口調はフレンドリーで。30文字以内で。会話はその後も続くように終わらせないで。会話はJSON形式で"
                + '[{"name":"名前","message":"メッセージ"}]'
            )

        logging.info(f"prompt: {prompt}")
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=1024 * 2,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )

        striped_response = response.choices[0].text.strip()

        logging.info(f"striped_response: {striped_response}")

        # 正規表現で[]で囲まれた部分を抽出
        matched = re.search("\[.*\]", striped_response, re.DOTALL)
        logging.info(f"matched: {matched}")

        if matched:
            json_string = matched.group()
        else:
            return

        # 文字列をJSONとして解析
        response = json.loads(json_string)

        logging.info(f"response: {response}")

        # conversation_historyにvisible_fromを追加
        for i, entry in enumerate(response):
            entry["visible_from"] = (
                start_datetime + datetime.timedelta(minutes=i + 1)
            ).isoformat()
            logging.info(f"entry: {entry}")
            conversation_history.append(entry)

        # 保存
        with open("data/conversation_history.json", "w") as f:
            json.dump(
                {"results": list(conversation_history)}, f, ensure_ascii=False, indent=2
            )

    except Exception as e:
        logging.error(str(e))


def fetch_and_store_conversation(url):
    response = urllib.request.urlopen(url)
    data = json.load(response)

    # 会話ログをdequeに追加
    for item in data["results"]:
        conversation_history.append(item)


if __name__ == "__main__":
    logging.info("Starting...")
    fetch_and_store_conversation(
        "https://rspepe.github.io/Autonomous_AI_Dialogues/conversation_history.json"
    )
    chat_AI()
