"""
main.py

このスクリプトは、音声の録音 → 文字起こし → テキスト保存 の一連の処理を実行します。

実行例:
    python main.py
"""

from record_audio import record_audio
from transcriber.transcribe_audio import transcribe_audio
from saver.save_text import save_transcription
import os


def main():
    """音声録音・文字起こし・保存を一括で実行するメイン関数"""
    # 保存ディレクトリ設定
    audio_dir = "data/audio"
    text_dir = "data/text"

    os.makedirs(audio_dir, exist_ok=True)
    os.makedirs(text_dir, exist_ok=True)

    print("🎙️  音声を録音します...")
    audio_path = os.path.join(audio_dir, "recorded_audio.wav")
    recorded_file = record_audio(audio_path, duration=10)
    print(f"✅ 録音完了: {recorded_file}")

    print("\n🧠  音声を文字起こししています...")
    transcription = transcribe_audio(recorded_file)
    print(f"✅ 文字起こし結果:\n{transcription}\n")

    print("💾  テキストを保存しています...")
    saved_path = save_transcription(transcription, text_dir)
    print(f"✅ 保存完了: {saved_path}")

    print("\n🌟 全処理が完了しました！")


if __name__ == "__main__":
    main()
