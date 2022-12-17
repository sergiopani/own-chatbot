import openai

openai.api_key = "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"

conversation = ""


def ia_model():
    return openai.Completion.create(
        model="text-davinci-003",
        prompt=conversation,
        temperature=0.7,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )


error = ''
while True:
    question = input("Sergio: ")
    conversation = "n\Sergio: " + question + "\nAi: "
    response = ia_model()
    # Si no nos ha llegado respuesta de la ia
    if not response:
        error = 'No se ha podido realizar la conexion, reinicia el chat!'
        break
    answer = response["choices"][0]["text"].strip()
    conversation += answer
    print("AI: " + answer + "\n")


print('Error: ' + error)
