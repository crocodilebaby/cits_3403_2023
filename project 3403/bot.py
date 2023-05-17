import flask from Flask,redirect, render_template, request, url_for
import openai from openai

app =(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chatgpt", methods=("GET", "POST"))
def generate:

