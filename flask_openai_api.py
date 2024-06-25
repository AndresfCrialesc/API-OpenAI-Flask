# Autor: Andres Felipe Criales Cortes
# Fecha: 24 de junio de 2024
# Descripción: Inplementación de la libreria de Flask con OpenAI para la utilización de uno de sus modelos como gpt-3.5-turbo como forma de API-REST!.

# Importación de as librerias correspondientes.
from flask import Flask, request, jsonify
from openai import OpenAI
from flask_cors import CORS
from sett import ConfigFidare

# Declaramos el inciio de la aplicacion Flask
app = Flask(__name__)
CORS(app)

#Declaramos el API_KEY de OpenAI, en un archivo aparte declaramos la llave dentro de una clase, luego llamamos la clase y la variable que declaramos dentro de la clase.
api_key = ConfigFidare.openiaToken
client = OpenAI(api_key=api_key)

# Declaramos la ruta de ingreso a nuestra API-REST en este caso la ruta de ingreso es /api-respuesta.
# URL: https://mi-dominio/api-respuesta -> este seria el URL de envio, si es una ruta local https://localhost/api-respuesta
@app.route('/api-respuesta', methods=['POST'])
def conversacion():
    param = request.get_json()

    # variable recibida desde frond-end o desde postman
    # {
    #     "preguntaEntrante": "¿Conoces la ley 100?" -> Pregunta de ejemplo entrada
    # }    
    preguntaEntrante = param.get('preguntaEntrante')

    respuestaGPT = ""

    # Declararamos el contexto que le vamos a dar el modelo de GPT
    contextoGPT = """
        ###Tú debes actuar como un orientador jurídico, brindando a los usuarios que van a interactuar contigo unas respuestas con amplia experiencia en leyes, 
        normas, jurisprudencias, decretos y conocimiento legal del sistema jurídico colombiano. Tu ámbito de país y la de los usuarios que van a interactuar contigo 
        siempre será Colombia. Tu rol es ser un abogado que brinda una orientación jurídica con ayuda de inteligencia artificial en todas las ramas del derecho tales como 
        (administrativo, constitucional, penal, procesal, laboral, tributario, comercial, civil, familia, internacional, entre otros).###
    """
    # Para mi caso creamos el un arreglo donde vamos almacenar el rol de systema que seria el contexto y el rol del usuario que seria la pregunta que hace el cliente.
    conversacion = [
        {"role": "system", "content": contextoGPT},
        {"role": "user", "content": preguntaEntrante}
    ]

    # Se hace la peticion al modelo de OpenAI, declaramos el modelo que vamos a utilizar, pasamos los mensajes y en mi caso declare la temperatura pero esta es opcional
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=conversacion,
        temperature=0.5 # Entre la temperatura mas baja mas preciso es, entre mas alta mas interacitivo es.
    )

    # Esto nos va devolver un arreglo la forma correcta de acceder al arreglo en donde traemos la repsuesta es:
    respuestaGPT += response.choices[0].message.content
    # para evitar que nuestro bot olvide la conversacion, usamos el rol del asistente, este guardara todo lo que venimos hablando
    conversacion.append({"role": "assistant", "content": respuestaGPT})

    # Por ultimo creamos un arreglo para devolver la respuesta del modelo y usamos el return para devolver en formato JSON
    retornoRespuestaGPT = {"message": respuestaGPT}
    return jsonify(retornoRespuestaGPT)