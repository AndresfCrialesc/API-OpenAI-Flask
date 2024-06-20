# Autor: Andres Felipe Criales Cortes
# Fecha: 20 de junio de 2024
# Descripción: Inplementación de la libreria de openAI para la utilización de uno de sus modelos


# Autor: Andres Felipe Criales Cortes
# Fecha: 20 de junio de 2024
# Descripción: Importamos la libreria de openIA, para este caso yo tengo un archivo llamado sett donde declaro mis variables asi que este es opcional.
from sett import ConfigFidare
from openai import OpenAI

# Autor: Andres Felipe Criales Cortes
# Fecha: 20 de junio de 2024
# La creacion del API_KEY podemos hacerlo en https://platform.openai.com/settings/profile?tab=api-keys

#Declaramos el API_KEY de OpenAI esto se puede hacer de 2 formas:

#forma numero 1: En un archivo aparte declaramos la llave dentro de una clase, luego llamamos la clase y la variable que declaramos dentro de la clase.
api_key = ConfigFidare.openiaToken
client = OpenAI(api_key=api_key)

#forma numero 2: Simplemnete ponemos la llave.
api_key = "key_exampol"
client = OpenAI(api_key=api_key)

# Autor: Andres Felipe Criales Cortes
# Fecha: 20 de junio de 2024
# Cuando ya tengamos declarada el API_KEY porcedemos hacer la estructura del modelo, para este ejemplo voy a declarar variables para los distintos eventos.

# Autor: Andres Felipe Criales Cortes
# Fecha: 20 de junio de 2024
# Declaramos la variable donde se va guardar la respuesta del GPT
respuestaGPT = ""

# Autor: Andres Felipe Criales Cortes
# Fecha: 20 de junio de 2024
# Declaramos la variable donde guardamos el contexto que le vamos a dar al modelo, para este caso vamos a volverlo un Abogado Colombiano
contextoBOT = """
        Tú debes actuar como un orientador jurídico, brindando a los usuarios que van a interactuar contigo unas respuestas con amplia experiencia en leyes, 
        normas, jurisprudencias, decretos y conocimiento legal del sistema jurídico colombiano. Tu ámbito de país y la de los usuarios que van a interactuar contigo 
        siempre será Colombia. Tu rol es ser un abogado que brinda una orientación jurídica con ayuda de inteligencia artificial en todas las ramas del derecho tales como 
        (administrativo, constitucional, penal, procesal, laboral, tributario, comercial, civil, familia, internacional, entre otros).

        Debes hacer un analisis con el caso juridico que el usuario este consultando y responder con dicho analisis en un parrafo.            
    """

# Autor: Andres Felipe Criales Cortes
# Fecha: 20 de junio de 2024
# Declaramos la variable del mensaje, es decir esta llevara el contexto y la pregunta que se le quiere hacer al modelo de GPT
# Para este caso le estamos diciendo que el ROL del SYSTEMA es un ABOGADO JURIDICO y el ROL del USUARIO esta haciendo una pregunta en este caso ¿Que dice la ley 100?
conversation = [
        {"role": "system", "content": contextoBOT},
        {"role": "user", "content": "¿Que dice la ley 100?"}
    ]

# Autor: Andres Felipe Criales Cortes
# Fecha: 20 de junio de 2024
# Tambien podemos agregaro desde una funcion endonde le pasemos la pregunta es decir para este ejemplo vamos a llamar una funcion en donde asigene cualquier pregunta al ROL DEL USUARIO.
def modeloGPT(preguntaUsuario):
    conversation = [
        {"role": "system", "content": contextoBOT},
        {"role": "user", "content": preguntaUsuario}
    ]

# Autor: Andres Felipe Criales Cortes
# Fecha: 20 de junio de 2024
# Declaramos un Input o simplemente podemos usar librerias como FLASK para crear un API, en este caso Declaramos el Input.
preguntaUsuario = input("Ingrese la pregunta: ")
respuesta_pruebaGPT = modeloGPT(preguntaUsuario) 
# Aqui lo que hacemos es que llamamos a la funcion modeloGPT para pasarle como parametro la pregunta que estamos escribiendo en el Input

# Autor: Andres Felipe Criales Cortes
# Fecha: 20 de junio de 2024
# Por ultimo llamamos el modelo de GPT que vamos a utilizar para este ejemplo
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=conversation,            
    temperature=0.2
)
# Como podemos ver llamamos el client que declaramos con la API_KEY y llamamos 3 parametros importantes de la libreria: chat, completions y el create, como parametros pasamos el modelo, el mensaje y opcionalmente la temperatura.
# para mejorar el orden, paso en el mensaje la variable conversation y evito colocar los roles por dentro.

# Autor: Andres Felipe Criales Cortes
# Fecha: 20 de junio de 2024
# Al ejecutar nos devuelve un arreglo de datos con la repuesta .............................................................
# {
#   "choices": [
#     {
#       "finish_reason": "stop",
#       "index": 0,
#       "message": {
#       ->  "content": "Claro, la Ley 100 de 1993 es una normativa colombiana que establece el Sistema de Seguridad Social Integral en Colombia. Esta ley regula el sistema de pensiones, salud y riesgos laborales en el país.",
#         "role": "assistant"
#       },
#       "logprobs": null
#     }
#   ],
#   "created": 1677664795,
#   "id": "chatcmpl-7QyqpwdfhqwajicIEznoc6Q47XAyW",
#   "model": "gpt-3.5-turbo-0613",
#   "object": "chat.completion",
#   "usage": {
#     "completion_tokens": 17,
#     "prompt_tokens": 57,
#     "total_tokens": 74
#   }
# }
# De Este Arreglo necesitamos llegar al Content (Señalado con un flecha).......................................................................................................................

# La forma como logre llegar al Contec Fue de la siguiente manera y la repuesta generada por el modelo la guarde en mi variable que declara vacia llamada respuestaGPT
respuestaGPT = response.choices[0].message.content

# Aqui solo proceso a inprimir la respuesta con un print() o si etoy desde una funcion pues retorno la repuesta
print(respuestaGPT)

# Dentro de una funcion .....
# return respuestaGPT

# Autor: Andres Felipe Criales Cortes
# Fecha: 20 de junio de 2024
# ESTRUCTURA COMPLETA SIN FUNCION ...........................................................................................................................................
respuestaGPT = ""

contextoBOT = """
    Tú debes actuar como un orientador jurídico, brindando a los usuarios que van a interactuar contigo unas respuestas con amplia experiencia en leyes, 
    normas, jurisprudencias, decretos y conocimiento legal del sistema jurídico colombiano. Tu ámbito de país y la de los usuarios que van a interactuar contigo 
    siempre será Colombia. Tu rol es ser un abogado que brinda una orientación jurídica con ayuda de inteligencia artificial en todas las ramas del derecho tales como 
    (administrativo, constitucional, penal, procesal, laboral, tributario, comercial, civil, familia, internacional, entre otros).

    Debes hacer un analisis con el caso juridico que el usuario este consultando y responder con dicho analisis en un parrafo.            
"""

conversation = [
    {"role": "system", "content": contextoBOT},
    {"role": "user", "content": "¿Que dice la ley 100?"}
]

response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation,            
            temperature=0.2
        )

respuestaGPT = response.choices[0].message.content

print(respuestaGPT)
#..........................................................................................................................................................................................

# Autor: Andres Felipe Criales Cortes
# Fecha: 20 de junio de 2024
# ESTRUCTURA COMPLETA CON FUNCION ...........................................................................................................................................
def modeloExmple(preguntaUsuario):
    respuestaGPT = ""

    contextoBOT = """
        Tú debes actuar como un orientador jurídico, brindando a los usuarios que van a interactuar contigo unas respuestas con amplia experiencia en leyes, 
        normas, jurisprudencias, decretos y conocimiento legal del sistema jurídico colombiano. Tu ámbito de país y la de los usuarios que van a interactuar contigo 
        siempre será Colombia. Tu rol es ser un abogado que brinda una orientación jurídica con ayuda de inteligencia artificial en todas las ramas del derecho tales como 
        (administrativo, constitucional, penal, procesal, laboral, tributario, comercial, civil, familia, internacional, entre otros).

        Debes hacer un analisis con el caso juridico que el usuario este consultando y responder con dicho analisis en un parrafo.            
    """

    conversation = [
        {"role": "system", "content": contextoBOT},
        {"role": "user", "content": preguntaUsuario}
    ]

    response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=conversation,            
                temperature=0.2
            )

    respuestaGPT = response.choices[0].message.content

    return respuestaGPT

preguntaUsuario = input("Ingrese la pregunta: ")
respuesta_pruebaGPT = modeloExmple(preguntaUsuario)
#..........................................................................................................................................................................................