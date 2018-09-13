from flask import Flask,request


app = Flask(__name__)



@app.route("/Get_Stock")
def Get_Stock():

    Stock_Number = request.args.get("st_num")

    return  "股票代碼為：{}".format(Stock_Number)



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5588)
