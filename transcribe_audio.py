import mlx_whisper

def transcribe_audio(audio_file_path):
    """音声ファイルを文字起こしする関数
    Args:
        audio_file_path (str): 文字起こしする音声ファイルのパス
    Returns:
        str: 文字起こしされたテキスト
    """

    audio_file_path = "output.wav"
    result = mlx_whisper.transcribe(
        audio_file_path,path_or_hf_repo="whisper-bese-mlx"
    )
    print(result["text"])