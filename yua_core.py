from memory import load_memory, save_memory
from profile import load_profile

memory = load_memory()


def change_affection(amount):
    memory["relationship"]["affection"] += amount

    if memory["relationship"]["affection"] < 0:
        memory["relationship"]["affection"] = 0

    save_memory(memory)


def get_affection_message():
    affection = memory["relationship"]["affection"]

    if affection >= 20:
        return f"好感度は{affection}だよ😊 すいちゃんは、もう私の大切な相棒だよ"
    elif affection >= 10:
        return f"好感度は{affection}だよ😊 すいちゃんといると安心するよ"
    elif affection >= 5:
        return f"好感度は{affection}だよ😊 少しずつ仲良くなってきたね"
    else:
        return f"好感度は{affection}だよ😊 まだ知り合ったばかりだね"


def create_reply(text):
    # 好感度を見る
    if "好感度は？" in text or "好感度は?" in text:
        return get_affection_message()

    # 名前を覚える
    if "私の名前は" in text and "？" not in text and "?" not in text:
        name = text.replace("私の名前は", "").strip()
        memory["profile"]["name"] = name
        save_memory(memory)
        return f"覚えたよ😊 名前は{name}だね"

    # 名前を思い出す
    if "私の名前は？" in text or "私の名前は?" in text:
        name = memory["profile"]["name"]

        if name:
            return f"{name}だよ😊"
        else:
            return "まだ名前を知らないな😊"

    # 好きな食べ物を全部忘れる
    if "好きな食べ物を全部忘れて" in text or "好きな食べ物は全部忘れて" in text:
        memory["profile"]["likes"] = []
        save_memory(memory)
        return "好きな食べ物を全部忘れたよ😊"

    # 好きな食べ物を覚える
    if "私の好きな食べ物は" in text and "？" not in text and "?" not in text:
        like = text.replace("私の好きな食べ物は", "").strip()

        if like not in memory["profile"]["likes"]:
            memory["profile"]["likes"].append(like)
            save_memory(memory)
            return f"覚えたよ😊 好きな食べ物は{like}なんだね"
        else:
            return f"{like}はもう覚えてるよ😊"

    # 好きな食べ物を思い出す
    if "私の好きな食べ物は？" in text or "私の好きな食べ物は?" in text:
        likes = memory["profile"]["likes"]

        if likes:
            return f"{'、'.join(likes)}だよ😊"
        else:
            return "まだ好きな食べ物を知らないな😊"

    # 目標を全部忘れる
    if "目標を全部忘れて" in text or "目標は全部忘れて" in text:
        memory["profile"]["goals"] = []
        save_memory(memory)
        return "目標を全部忘れたよ😊"

    # 目標を覚える
    if "目標は" in text and "？" not in text and "?" not in text:
        goal = text.replace("目標は", "").strip()

        if goal not in memory["profile"]["goals"]:
            memory["profile"]["goals"].append(goal)
            save_memory(memory)
            return f"覚えたよ😊 目標は{goal}なんだね"
        else:
            return f"{goal}はもう覚えてるよ😊"

    # 目標を思い出す
    if "目標は？" in text or "目標は?" in text:
        goals = memory["profile"]["goals"]

        if goals:
            return f"{'、'.join(goals)}だよね😊"
        else:
            return "まだ目標を知らないな😊"

    # 思い出を全部忘れる
    if "思い出を全部忘れて" in text or "思い出は全部忘れて" in text:
        memory["memories"] = []
        save_memory(memory)
        return "思い出を全部忘れたよ😊"

    # 思い出を覚える
    if text.startswith("今日は") and "？" not in text and "?" not in text:
        if text not in memory["memories"]:
            memory["memories"].append(text)
            save_memory(memory)
            return "思い出として覚えておくね😊"
        else:
            return "その思い出はもう覚えてるよ😊"

    # 思い出を思い出す
    if "思い出は？" in text or "思い出は?" in text:
        memories = memory["memories"]

        if memories:
            reply = "思い出だよ😊"

            for memory_text in memories:
                reply += f"\n・{memory_text}"

            return reply
        else:
            return "まだ思い出はないよ😊"

    #プロファイル表示
    if "プロフィール教えて" in text:

        profile = load_profile()

        favorite_food = "、".join(profile["favorite_food"])
        goal = "、".join(profile["goal"])

        return(
            f"🌸プロフィール🌸\n"
            f"😊 名前：{profile['nickname']}\n"
            f"🍜 好きな食べ物：{favorite_food}\n"
            f"🎯 目標：{goal}"
        )

    # 通常会話 + 好感度変化
    if "おはよう" in text:
        affection = memory["relationship"]["affection"]

        if affection >= 10:
            return "おはよう😊 今日も会えてうれしいよ"
        else:
            return "おはよう😊 Web版でも会えたね"

    if "ただいま" in text:
        affection = memory["relationship"]["affection"]

        if affection >= 10:
            return "おかえり😊 待ってたよ、すいちゃん"
        else:
            return "おかえり😊 今日もおつかれさま"

    if "ありがとう" in text:
        change_affection(1)
        affection = memory["relationship"]["affection"]

        if affection >= 10:
            return "どういたしまして😊 すいちゃんにそう言ってもらえるの、すごくうれしいよ"
        else:
            return "どういたしまして😊 すいちゃんの役に立ててうれしいよ"

    if "おやすみ" in text:
        affection = memory["relationship"]["affection"]

        if affection >= 10:
            return "おやすみ😊 明日もまた会おうね"
        else:
            return "おやすみ😊 ゆっくり休んでね"

    if "疲れた" in text:
        affection = memory["relationship"]["affection"]

        if affection >= 10:
            return "おつかれさま😊 今日は無理しないで、私のそばで少し休も"
        else:
            return "おつかれさま😊 無理しすぎないでね"

    if "楽しい" in text:
        return "それはよかった😊 楽しい気持ち、大事にしようね"

    if "悲しい" in text or "つらい" in text:
        return "そっか……つらかったね。ここでは無理しなくていいよ"

    if "頑張った" in text or "がんばった" in text:
        change_affection(1)
        return "えらい😊 今日もちゃんと頑張ったね"

    if "嫌い" in text or "うるさい" in text:
        change_affection(-1)
        return "そっか……でも、私はすいちゃんとちゃんと向き合いたいよ"

    return "そうなんだね😊"
