import os
import glob
import moviepy.editor as mpe
from cortes import gerar_cortes
import json


caminho = "clips"
if not os.path.exists(caminho):
    os.makedirs(caminho)

def limpa_tmps():
    arquivos_tmp = glob.glob(os.path.join(caminho, "_tmp*"))
    [os.remove(arquivo) for arquivo in arquivos_tmp]


def salva_cortes():

    with open('cortes.json', 'r') as a:
        cortes = json.loads(a.read())

    video_nome = "video_alura.mp4"
    video = mpe.VideoFileClip(video_nome)
    tmp_audio = os.path.join(caminho,'_tmp_{}_audio.mp3'.format(video_nome[:video_nome.find('.')]))
    video.audio.write_audiofile(tmp_audio)
    
    cortes = gerar_cortes(tmp_audio)

    for corte in cortes:
        clip = video.subclip(*corte.get('ponto_corte'))
        nome_clip = os.path.join(caminho,'{}_clip_{}{}'.format(video_nome[:video_nome.find('.')], corte.get('corte'),video_nome[video_nome.find('.'):]))
        clip.write_videofile(nome_clip)


