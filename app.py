from flask import Flask, request, render_template_string
import requests
import json

app = Flask(__name__)

API_URL = "https://promql-gateway.service.newrelic.com/api/v1/translate"
API_KEY = "xxxx"  # Replace with your actual API key

template = '''
<!DOCTYPE html>
<html>
<head>
    <title>PromQL to NRQL Translator</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.3.1/styles/default.min.css">
    <script src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.3.1/highlight.min.js"></script>
    <style>
        .hljs {
            display: block;
            overflow-x: auto;
            padding: 0.5em;
            color: #333;
            background: #f8f8f8;
            position: relative;
            max-width: 90%; /* Set maximum width */
            margin: auto; /* Center the block */
            text-align: left; /* Align text to the left */
            white-space: pre-wrap; /* Allow wrapping of long lines */
            word-wrap: break-word; /* Break long words */
        }
        .copy-icon {
            position: absolute;
            top: 0.5em;
            right: 0.5em;
            cursor: pointer;
            background: white;
            padding: 0.2em;
            border-radius: 4px;
            border: 1px solid #ccc;
        }
        .code-container {
            position: relative;
            max-width: 50%; /* Set maximum width */
            margin: left; /* Center the block */
            text-align: left; /* Align text to the left */


        }
    </style>
    <script>
        function copyToClipboard() {
            var codeElement = document.getElementById("nrql-code");
            var range = document.createRange();
            range.selectNode(codeElement);
            window.getSelection().removeAllRanges();
            window.getSelection().addRange(range);
            document.execCommand("copy");
            window.getSelection().removeAllRanges();
            alert("Copied the NRQL query!");
        }
    </script>
</head>
<body>
    <h1>PromQL to NRQL Translator</h1>
    <form method="POST" action="/">
        <label for="promql">PromQL Query:</label><br>
        <textarea id="promql" name="promql" rows="4" cols="50"></textarea><br><br>
        <input type="submit" value="Translate">
    </form>
    {% if result %}
    <h2>Translated NRQL:</h2>
    <div class="code-container">
        <pre><code id="nrql-code" class="hljs">{{ result }}</code></pre>
        <i class="fas fa-copy copy-icon" onclick="copyToClipboard()"></i>
    </div>
    {% endif %}
    <script>hljs.highlightAll();</script>
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def translate():
    result = None
    if request.method == "POST":
        promql = request.form["promql"]
        
        # Set up the translation request payload
        req_payload = {
            "step": "1",
            "isRange": True,
            #"end": "1690318730919",
            "account_id": "",
            "promql": promql,
            #"start": "1690316930919"
        }

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Api-Key": API_KEY
        }

        response = requests.post(API_URL, headers=headers, data=json.dumps(req_payload))
        
        if response.status_code == 200:
            result = response.json().get("nrql", "No NRQL result found")
        else:
            result = f"Error: {response.text}"

    return render_template_string(template, result=result)

if __name__ == "__main__":
    app.run(debug=True)
