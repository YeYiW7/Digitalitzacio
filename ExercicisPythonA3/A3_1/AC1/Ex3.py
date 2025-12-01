import requests


# URL de l'endpoint local del servidor
url = "http://localhost:5000/sumar"


# Dades a enviar (Body params)
datos = {"numero": 7}
try:
    # requests.post utilitza l'argument 'json' per enviar les dades
    # com a application/json en el Body
    respuesta = requests.post(url, json=datos)


    # Comprovar el codi de resposta
    if respuesta.status_code == 200:
        # En cas d'èxit, la resposta retorna el resultat processat
        print("✅ Resposta correcta:")
        print(respuesta.json())
    elif respuesta.status_code == 400:
        # 400 Bad Request indica un error del client (p. ex., un paràmetre incorrecte)
        print(f"⚠️ Error {respuesta.status_code}: {respuesta.text}")
    else:
        print(f"⚠️ Error {respuesta.status_code}: {respuesta.text}")


except requests.exceptions.RequestException as e:
    # Captura errors de connexió (per si el servidor no està actiu)
    print(f"❌ Error en la connexió: {e}")
