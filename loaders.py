"""
このファイルは、LangChainのTextLoaderを拡張して、
文字コードを明示的に指定できるようにするためのカスタムローダーを定義しています。
"""
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