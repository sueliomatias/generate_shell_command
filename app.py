import openai
from dotenv import load_dotenv
import subprocess
import os

load_dotenv()

openai.api_key = os.getenv("API_KEY")

def gerar_comando_shell(texto):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=f"Escreva um comando shell que faça o seguinte: {texto}",
        temperature=0.7,
        max_tokens=2048,
        n=1,
        stop="none"
    )
    response["choices"][0]["text"].strip()

def  executar_comando_shell(shell):
    try:
        resultado = subprocess.run(comando, shell=True, check=True)
        print(resultado)
    except subprocess.CalledProcessError as e:
        print(e)

descricao_comando = input("Digite uma descrição para o comando shell: ")
comando = gerar_comando_shell(descricao_comando)
print(f"Comando gerado: {comando}")
executar_comando_shell(comando)