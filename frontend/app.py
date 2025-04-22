from flask import Flask, render_template, request, session, redirect, url_for
import requests

app = Flask(__name__)
app.secret_key = "your_super_secret_key"
FASTAPI_URL = "http://localhost:8000"

@app.route("/", methods=["GET", "POST"])
def index():
    if "chat_history" not in session:
        session["chat_history"] = []
    if "log" not in session:
        session["log"] = []

    uploaded_files = []
    try:
        files_resp = requests.get(f"{FASTAPI_URL}/uploaded_files/")
        uploaded_files = files_resp.json().get("uploaded_files", [])
    except Exception:
        uploaded_files = ["(Failed to fetch uploaded files)"]

    if request.method == "POST":
        if "file" in request.files:
            f = request.files["file"]
            files = {"file": (f.filename, f.stream, f.mimetype)}
            try:
                upload_resp = requests.post(f"{FASTAPI_URL}/upload/", files=files)
                session["log"].append(f"Uploaded: {f.filename}")
            except Exception:
                session["log"].append("Upload failed.")
        elif "question" in request.form:
            question = request.form["question"]
            try:
                resp = requests.post(f"{FASTAPI_URL}/ask/", data={"question": question})
                answer = resp.json().get("answer", "Error: No answer returned.")
                session["chat_history"].append({"user": question, "bot": answer})
            except Exception:
                session["chat_history"].append({"user": question, "bot": "Error: Failed to get response."})

        session.modified = True
        return redirect(url_for("index"))

    return render_template(
        "index.html",
        uploaded_files=uploaded_files,
        chat_history=session["chat_history"],
        logs=session["log"]
    )

@app.route("/clear/<target>")
def clear_session(target):
    if target == "chat":
        session["chat_history"] = []
    elif target == "logs":
        session["log"] = []
    session.modified = True
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(port=5000, debug=True)
