import os
import glob

def combine_files(input_folder, output_file):
    
    # 出力ファイルを書き込みモードで開く
    with open(output_file, 'a', encoding='utf-8') as outfile:
        # フォルダ内のすべてのファイルを取得
        files = glob.glob(os.path.join(input_folder, '*.txt'))
        
        for file_path in files:
            # ファイル名を取得
            file_name = os.path.basename(file_path)
            
            try:
                # 各ファイルを読み込む
                with open(file_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    
                    # マーカーとファイル名を追加
                    outfile.write(f"<START> {file_name}\n")
                    outfile.write(content)
                    if not content.endswith('\n'):
                        outfile.write('\n')
                    outfile.write("<END>\n\n")
                    
            except Exception as e:
                print(f"エラー: ファイル {file_name} の処理中にエラーが発生しました: {str(e)}")

# 使用例
if __name__ == "__main__":
    input_folder = "."  # 入力フォルダのパス
    output_file = "c:\\temp\\combined_output.txt"  # 出力ファイルのパス
    
    combine_files(input_folder, output_file)
    print("ファイルの結合が完了しました。")
