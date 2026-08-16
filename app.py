from flask import Flask, render_template, request,session,redirect,url_for
from yua_core import create_reply
from profile import (
    load_profile,
    analyze_profile,
    save_profile
)
from memory import load_memory

app = Flask(__name__)
app.secret_key = "yua_secret_key"


@app.route("/", methods=["GET", "POST"])
def index():

    profile = load_profile()
    print(profile)

    profile["favorite_food"] = "、".join(profile["favorite_food"])
    profile["goal"] = "、".join(profile["goal"])

    if "chat" not in session:
        session["chat"] = []

    user_text = ""
    reply = ""

    if request.method == "POST":

        if "clear" in request.form:
            session["chat"] = []
            session.modified = True

            return redirect(url_for("index"))
            
        user_text = request.form["message"]
        reply = create_reply(user_text)

        memory = load_memory()

        profile = analyze_profile(memory)

        save_profile(profile)

        profile["favorite_food"] = "、".join(profile["favorite_food"])
        profile["goal"] = "、".join(profile["goal"])
      
        session["chat"].append(
            {
                "user":user_text,
                "reply":reply
            }
        )
        session.modified = True       

    return render_template(
        "index.html",
        user_text=user_text,
        reply=reply,
        chat=session["chat"],
        profile=profile
)

if __name__ == "__main__":
    app.run(debug=False)
