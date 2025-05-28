import tempfile
import os
import textract
from app.domain.entities import StoredFile
from app.domain.interfaces import TextExtractor

class TextractTextExtractor(TextExtractor):
    def extract_text(self, file: StoredFile) -> str:

        with tempfile.NamedTemporaryFile(delete=False) as tmp_file: # создаем временный файл
            tmp_file.write(file.content)
            tmp_path = tmp_file.name

        try:
            text = textract.process(tmp_path, extension="txt") # работа с путём к файлу
            return text.decode("utf-8")
        except Exception as e:
            raise RuntimeError(f"Extraction failed: {e}")
        finally:
            os.remove(tmp_path) # удаляем временный файл
