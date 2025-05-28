import tempfile
import os
import textract
from app.domain.entities import StoredFile
from app.domain.interfaces import TextExtractor


class TextractTextExtractor(TextExtractor):
    def extract_text(self, file: StoredFile) -> str:
        # Создаем временный файл
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(file.content)
            tmp_path = tmp_file.name

        try:
            # textract работает с путём к файлу
            text = textract.process(tmp_path, extension="txt")
            return text.decode("utf-8")
        except Exception as e:
            raise RuntimeError(f"Extraction failed: {e}")
        finally:
            # Удаляем временный файл
            os.remove(tmp_path)
