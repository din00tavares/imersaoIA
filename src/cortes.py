import json
import google.generativeai as genai
from gemini import generate_model


def gerar_cortes(arquivo_audio):
    system_instruction = """Você é um editor de vídeos, o seu trabalho é criar cortes curtos dos vídeos para postar nas redes sociais.\n 
                        Procure os pontos mais importantes e relevantes do áudio e crie quantos cortes forem necessários.\n 
                        Baseado no conteúdo, selecione somente os cortes mais relevantes. \n 
                        Não use áspas simples ou duplas no texto, para que o código não se confunda. \n
                        Envie o retorno em formato de json.\n
                        o resultado deve estar nesta estrutura \n
                        {\n
                        corte: n, \n
                        titulo: Crie um título criativo baseado no conteúdo do corte,\n
                        descricao: Cria uma descrição criativa baseado no conteúdo do corte,\n
                        hashtags: Indique um lista com as melhores hashtags baseadas no corte,\n
                        ponto_corte: Indique o ponto de corte incluindo, inicio e fim, dessa formato "HH:MM:SS.ms", exemplo: ["00:01:55.135", "00:03:24:654"]\n
                        }"""

    model = generate_model(system_instruction=system_instruction)
    audio = genai.upload_file(arquivo_audio)
    print("Gerando cortes a partir do áudio...")
    content = model.generate_content(audio)
    return json.loads(content.text.replace('```json', '').replace('```',''))


def gerar_legenda(arquivo_audio):
    system_instruction = """Faça a transcrição do áudio para criar uma legenda que será processada pelo moviepy"""
    model = generate_model(system_instruction=system_instruction)
    audio = genai.upload_file(arquivo_audio)
    print("Gerando legenda a partir do áudio...")
    content = model.generate_content(audio)
    return json.loads(content.text.replace('```json', '').replace('```',''))