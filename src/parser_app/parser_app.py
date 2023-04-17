import re
from collections import Counter

from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)


def parse(data):
    pattern = '\d{1,3}-\d{1,3}-\d{1,3}-\d{1,3}'
    ips = re.findall(pattern=pattern, string=data)
    results = Counter(ips).most_common(10)
    return results



@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        log = request.files["log_file"].read()
        txt = str(log, "utf8")
        result = parse(txt)
                # for the recommended bans list of ip addresses
        ban = []
        for key, value in result:
            if value > 0:
                ban.append({"ip": key, "counts": value})
        return render_template("index.html", ips=ban)


    else:
        return render_template("index.html")



# def main():
#     with open("log") as f:
#         data = f.read()
#     pattern = '\d{1,3}-\d{1,3}-\d{1,3}-\d{1,3}'
#     ips = re.findall(pattern=pattern, string=data)

#     results = Counter(ips).most_common(10)
#     # print(results)
#     for key, value in results:
#         print(f"{key} - {value}")

if __name__ == '__main__':
    app.run(debug=True, port=8000)
    # main()