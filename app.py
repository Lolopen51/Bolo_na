from flask import Flask, request, redirect, url_for, session, render_template

app = Flask(__name__)
app.secret_key = "supersecretkey"  # change this

messages = []
passwords = {
    "Rohan": "1234",
}

# =========================
# Homepage (Login)
# =========================
@app.route("/", methods=["GET", "POST"])
def home():
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in passwords and passwords[username] == password:
            session["logged_in"] = username
            return redirect(url_for("dashboard", username=username))
        else:
            return render_template("home.html", error="❌ Wrong username or password!")

    return render_template("home.html")

# =========================
# Dashboard
# =========================
@app.route("/dashboard/<username>")
def dashboard(username):
    if session.get("logged_in") != username:
        return redirect(url_for("home"))
    return render_template("dashboard.html", username=username)

# =========================
# Public form
# =========================
@app.route("/public/<username>", methods=["GET"])
def public_form(username):
    return render_template("public.html", username=username)

# =========================
# Handle incoming message
# =========================
@app.route("/send/<username>", methods=["POST"])
def send_message(username):
    msg = request.form.get("msg")
    if msg:
        messages.append({"user": username, "text": msg})
    return redirect(url_for("thank_you", username=username))

@app.route("/thankyou/<username>")
def thank_you(username):
    return render_template("thankyou.html", username=username)

# =========================
# Inbox
# =========================
@app.route("/inbox/<username>")
def inbox(username):
    if session.get("logged_in") != username:
        return redirect(url_for("home"))

    user_msgs = [m["text"] for m in messages if m["user"] == username]
    return render_template("inbox.html", username=username, messages=user_msgs)

# =========================
# Logout
# =========================
@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(port=5000, debug=True)
