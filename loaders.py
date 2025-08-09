"""
このファイルは、LangChainのTextLoaderを拡張して、
文字コードを明示的に指定できるようにするためのカスタムローダーを定義しています。
"""
import pandas as pd
from langchain_core.documents import Document
from langchain_community.document_loaders.base import BaseLoader
from langchain_community.document_loaders import TextLoader

class CustomTextLoader(TextLoader):
    """
    文字コードを明示的に指定するためのカスタムTextLoader
    """
    def __init__(self, file_path: str, encoding: str = "utf-8", **kwargs):
        """
        デフォルトのエンコーディングをutf-8に設定
        """
        super().__init__(file_path, encoding=encoding, **kwargs)


class CustomCsvLoader(BaseLoader):
    """
    CSVファイルの全行を1つのドキュメントとして読み込むカスタムローダー。
    各行は「項目名: 値」の形式でテキスト化され、検索精度を向上させます。
    """
    def __init__(self, file_path: str, encoding: str = "utf-8"):
        """ローダーを初期化"""
        self.file_path = file_path
        self.encoding = encoding

    def load(self) -> list[Document]:
        """CSVファイルを読み込み、行ごとに個別のDocumentオブジェクトのリストを返す"""

        df = pd.read_csv(self.file_path, encoding=self.encoding)

        docs = []
        # データフレームの各行をループ処理
        for index, row in df.iterrows():
            row_items = []
            # 行の中の各列をループ処理
            for col_name, value in row.items():
                row_items.append(f"{col_name}: {value}")

            # 1行分の情報をカンマ区切りの文字列に結合
            row_string = ", ".join(row_items)
            page_content = f"従業員情報: {row_string}"

            # メタデータを作成
            metadata = {"source": self.file_path}

            # 行ごとにDocumentオブジェクトを作成してリストに追加
            docs.append(Document(page_content=page_content, metadata=metadata))

        return docs