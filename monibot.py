import nltk
from nltk.stem import SnowballStemmer
import spacy
import nltk
nltk.download('punkt')


# Inicializar el stemmer para normalizar las palabras
stemmer = SnowballStemmer('spanish')

# Cargar el modelo de lenguaje de spaCy
nlp = spacy.load('es_core_news_sm')

cliente_nombre = None
cliente_correo = None
respuesta = None

def preprocess(sentence):
    # Tokenizar la oración en palabras
    words = nltk.word_tokenize(sentence)
    
    # Normalizar y stemmizar las palabras
    stemmed_words = [stemmer.stem(word.lower()) for word in words]
    
    # Devolver la lista de palabras procesadas
    return stemmed_words

def chat():
    global cliente_nombre, cliente_correo, opcion_elegida

    opciones = [
    (1, "Información planes y suscripciones"),
    (2, "Información sobre plataforma"),
    (3, "Enviar pregunta o duda a un asesor"),
    (4, "Otra")
]

    print("Hola, soy MoniBot. ¿En qué puedo ayudarte hoy?")
    
    print("Por favor, elige una opción:")

    for opcion_id, opcion_texto in opciones:
      print(f"{opcion_id}. {opcion_texto}")

    while True:
        user_input = input("Cliente: ")
        
        if user_input.lower() in ["no", "no quiero"]:
            print("Chatbot: Entendido. Si tienes alguna otra pregunta, estaré aquí para ayudarte.")
            break
        
        selected_option_id = None
        for opcion_id, opcion in opciones:
            if str(opcion_id) in user_input:
              selected_option_id = opcion_id
              break
        
        if selected_option_id is not None:
            opcion_elegida = next(opcion for opcion_id, opcion in opciones if opcion_id == selected_option_id)
            print(f"Chatbot: Entendido, elegiste la opción: {opcion_elegida}")

    
            # Mostrar contenido distinto según la opción elegida
            if opcion_elegida == "Información planes y suscripciones":
                print("Aquí puedes encontrar información sobre nuestros planes y suscripciones.")
                # Implementa la lógica adicional para esta opción
                
            elif opcion_elegida == "Información sobre plataforma":
                print("Aquí puedes encontrar información sobre nuestra plataforma.")
                
                
            elif opcion_elegida == "Enviar pregunta o duda a un asesor":
                print("Aquí puedes enviar tu pregunta o duda a uno de nuestros asesores.")
                # Implementa la lógica adicional para esta opción
                
            else:
                print("Opción no válida. Por favor, elige una opción válida.")
                # Implementa la lógica para manejar opciones no válidas

            # Resto del código del chat
        print("Chatbot: ¿Puedo ayudarte en algo más?")
        respuesta = input("Cliente: ")
    # Resto de la implementación del chat
        
        if not cliente_nombre or not cliente_correo:
            print("Chatbot: Por favor, antes me puedes proporcionar tu nombre y correo?")
            cliente_nombre = input("Nombre: ")
            cliente_correo = input("Correo: ")
            
            if not cliente_nombre or not cliente_correo:
                print("Chatbot: Lamentablemente no puedo ayudarte sin los datos necesarios. Lo intentamos de nuevo?")
                respuesta = input("Cliente: ")
                if respuesta.lower() in ["no"]:
                    print("Chatbot: Entendido. Si tienes alguna otra pregunta, estaré aquí para ayudarte.")
                    break
                else:
                    print("Chatbot: Por favor, proporciona tu nombre y correo nuevamente")
                    cliente_nombre = input("Nombre: ")
                    cliente_correo = input("Correo: ")
            else:
                print("Chatbot: Gracias por proporcionar tus datos. Ahora puedo ayudarte mejor.")
                print("Chatbot: Se ha enviado tu pregunta y datos a un asesor. Se pondrá en contacto contigo tan pronto como sea posible.")

        if any(opcion.lower() in user_input.lower() for opcion in opciones):
            opcion_elegida = next((opcion for opcion in opciones if opcion.lower() in user_input.lower()), None)
            print(f"Chatbot: Entendido, elegiste la opción: {opcion_elegida}")
            # Aquí puedes implementar la lógica correspondiente para cada opción elegida por el cliente
        
        print("Chatbot: ¿Puedo ayudarte en algo más?")
        respuesta = input("Cliente: ")
        
        if respuesta.lower() in ["no", "no quiero"]:
            print("Chatbot: Entendido. Si tienes alguna otra pregunta, estaré aquí para ayudarte.")
            break

        # Aquí puedes implementar la lógica adicional para responder a la pregunta del cliente
        print("Chatbot: Gracias por tu pregunta. Ahora puedo proporcionarte una respuesta.")

if __name__ == '__main__':
    chat()
