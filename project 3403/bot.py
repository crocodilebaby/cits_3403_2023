from flask import Flask, flash, redirect, render_template, request, url_for
from openai import *
import os
app =(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chatgpt", methods=("GET", "POST"))
def generate(generate2):
    return render_template("chatgpt.html")