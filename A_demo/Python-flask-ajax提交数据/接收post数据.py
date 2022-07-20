#参考：https://blog.csdn.net/pandora_madara/article/details/46293903
from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
#跨域
CORS(app, supports_credentials=True)

@app.route('/')
def hello_world():
    return 'hello world'

#http://127.0.0.1:8888/username
@app.route( "/username", methods = [ "POST", "GET" ] )
def index():
    if request.method == "POST":
        first_name = request.form.get("first_name", "null")
        last_name = request.form.get("last_name", "null")
        return jsonify(name = first_name + "-" + last_name)

    listdata = [{"name":"king", "password":"123456"}, {"name":"bob", "password":"88888"}]
    return jsonify(listdata) #GET提交会出现这个
    #return jsonify(error="不是post请求")

if __name__ == '__main__':
    app.run(port=8888, debug=True) #http://127.0.0.1:8888