from pathlib import Path

def save_str_sequential_same_dir(text: str, base_filename: str = "output") -> str:
    """
    このスクリプト（save.text.py）と同じディレクトリに文字列を
    上書きせずに連番で.txtファイルとして保存

    Args:
        text (str): 保存する文字列
        base_filename (str): ファイル名のベース

    Returns:
        str: 保存したファイルのパス
    """
    # save.text.py と同じディレクトリを取得
    output_path = Path(__file__).parent
    output_path.mkdir(parents=True, exist_ok=True)  # 念のため

    # 既存の txt ファイルを確認して次の番号を決定
    existing_files = list(output_path.glob(f"{base_filename}*.txt"))
    numbers = []
    for f in existing_files:
        stem = f.stem
        suffix = stem.replace(base_filename, "")
        if suffix.isdigit():
            numbers.append(int(suffix))
    next_num = max(numbers, default=0) + 1

    file_path = output_path / f"{base_filename}{next_num}.txt"

    # 書き込み
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"✅ 保存完了: {file_path}")
    return str(file_path)


# 使用例
if __name__ == "__main__":
    text = "録音→文字起こし結果を保存（save.text.py と同じディレクトリ）"
    save_str_sequential_same_dir(text)
