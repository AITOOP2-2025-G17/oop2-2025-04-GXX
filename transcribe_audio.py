import mlx_whisper
from pathlib import Path


def transcribe_audio(audio_file_path: str) -> str:
    """
    指定された音声ファイルを文字起こしする。

    Args:
        audio_file_path (str): 音声ファイルのパス

    Returns:
        str: 文字起こし結果のテキスト
    """
    model_path = Path(__file__).parent / "whisper-base-mlx"

    print("🧠 文字起こし中...")
    result = mlx_whisper.transcribe(audio_file_path, path_or_hf_repo=str(model_path))
    print("✅ 文字起こし完了")

    return result["text"]
