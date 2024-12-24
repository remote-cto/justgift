from flask import Flask, render_template, request, jsonify
from openai import OpenAI

# Initialize Flask app
app = Flask(__name__)

client = OpenAI(
    add actual code
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():

    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"error": "Message cannot be empty"}), 400

    try:
        print(f"its here now - {user_input}")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        print(response)
        # bot_response = response['choices'][0]['message']['content']
        bot_response = response.choices[0].message.content

        return jsonify({"response": bot_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
