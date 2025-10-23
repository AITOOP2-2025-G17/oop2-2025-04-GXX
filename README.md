# oop2-2025-04-GXX
## リポジトリの目的
音声を録音し，自動的にテキスト変換されtxt形式で保存される．  

## 実行するのに必要なモジュール
1. **requirements.txt** に以下をコピー
    ```
    mlx>=0.11
    numba
    numpy
    torch
    tqdm
    more-itertools
    tiktoken
    huggingface_hub
    scipy
    ```
1. ターミナルで以下を実行  
    ```
    pip install -r requirements.txt
    pip install mlx-whisper
    ```

## 実行手順
main.pyを実行  
　　　↓  
以下が自動的に実行される  
1.  whisperが起動し，10秒間音声を録音する
2.  録音されたwavファイルから音声認識をしてテキストに起こす
3.  テキストをtxtファイルに保存する

## 作成者情報など
| 学籍番号 | 名前       |
| -------- | ---------- |
| k24122   | 稗田花林   |
| k24093   | 武市さやか |
| k24019   | 伊藤拓未   |
| k24036   | 岡澤有真   |