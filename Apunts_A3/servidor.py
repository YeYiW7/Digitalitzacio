from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello world!!!"

@app.route('/suma',methods=['GET'])
def suma():
    numero1 = request.args.get('a')
    print(numero1)
    
    numero2 = request.args.get('b')
    print(numero2)
    suma = int (numero1) + int (numero2)
    return "La suma de ", numero1 ,"+", numero2, "és = " ,str (suma)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="10050")


# Para accedir a la pagina tienes que arrangar la maquina i poner IP + /hello 