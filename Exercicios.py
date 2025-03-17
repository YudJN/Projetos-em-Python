import pytube
import ffmpeg
import openai
import os

# Definindo a chave de API do OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")  # Carregar a chave de API de variáveis de ambiente

def baixa_Audio(url):
    yt = pytube.YouTube(url)
    try:
        stream = yt.streams.filter(only_audio=True).first()  # Pegando o stream de áudio
        if not stream:
            print("Nenhum áudio disponível para este vídeo.")
            return None
        filename = "audio.webm"
        stream.download(filename=filename)  # Baixando o arquivo de áudio

        # Convertendo para WAV com o ffmpeg
        wav_filename = "audio.wav"
        try:
            ffmpeg.input(filename).output(wav_filename, format='wav', loglevel='error').run()
        except Exception as e:
            print(f"Erro na conversão do áudio: {e}")
            return None

        return wav_filename
    except Exception as e:
        print(f"Erro ao tentar baixar o áudio: {e}")
        return None

def transcrever_audio(arquivo_audio):
    try:
        with open(arquivo_audio, "rb") as audio_file:
            transcript = openai.Audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                language="pt"
            )
        return transcript["text"]
    except Exception as e:
        print(f"Erro ao transcrever áudio: {e}")
        return None

def gerar_resumo(texto):
    response = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=[{
            "role": "system", 
            "content": "Você é um assistente que resume vídeos detalhadamente. Responda com formatação Markdown."
        }, {
            "role": "user", 
            "content": f"Descreva o seguinte vídeo: {texto}"
        }]
    )
    return response['choices'][0]['message']['content']

def salvar_resumo(resumo):
    with open("resume.md", "w") as md_file:
        md_file.write(resumo)

if __name__ == "__main__":
    url = input("Forneça a URL do vídeo: ")  # Recebendo a URL através do input
    if url:
        arquivo_audio = baixa_Audio(url)
        if arquivo_audio:
            texto_transcrito = transcrever_audio(arquivo_audio)
            if texto_transcrito:
                resumo = gerar_resumo(texto_transcrito)
                salvar_resumo(resumo)
                print("Resumo gerado com sucesso!")
            else:
                print("Erro na transcrição do áudio.")
        else:
            print("Erro no download do áudio.")
    else:
        print("Por favor, forneça uma URL válida.")
