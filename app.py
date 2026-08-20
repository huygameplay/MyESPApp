from flask import Flask, render_template_string, jsonify
import subprocess
import os

app = Flask(__name__)

HTML = """
<h1 style="font-family:sans-serif">HOST PAPER 1.12.2 FREE - PYTHON</h1>
<p>Trang thai: <b id="status">Dang kiem tra...</b></p>
<button onclick="fetch('/start').then(()=>alert('Dang bat server...'))" style="padding:15px">BAT SERVER</button>
<button onclick="fetch('/stop').then(()=>alert('Da tat server'))" style="padding:15px">TAT SERVER</button>
<pre id="log" style="background:black;color:lime;padding:10px;height:300px;overflow:auto">Log se hien o day...</pre>
<script>
setInterval(()=>{
 fetch('/status').then(r=>r.json()).then(d=>{
  document.getElementById('status').innerText = d.running ? 'DANG CHAY - IP: ' + d.ip : 'DANG TAT'
 })
}, 2000)
</script>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/start")
def start():
    # Chạy paper.jar
    if not os.path.exists("eula.txt"):
        with open("eula.txt","w") as f: f.write("eula=true")
    subprocess.Popen(["java", "-Xmx1500M", "-Xms512M", "-jar", "paper.jar", "nogui"])
    return "ok"

@app.route("/stop")
def stop():
    subprocess.run(["pkill", "-f", "paper.jar"])
    return "ok"

@app.route("/status")
def status():
    running = subprocess.run(["pgrep", "-f", "paper.jar"], capture_output=True).returncode == 0
    return jsonify({"running": running, "ip": os.environ.get("RENDER_EXTERNAL_HOSTNAME","localhost")})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)