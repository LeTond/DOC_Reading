"""
Сегментируем МРТ, КТ, Рентген исследования.
Создаем два каталога и сохраняем в них рассортированные и обработанные заключения.
Удаляем шапку заключения, ФИО пациента, Дату рождения, область исследования, ФИО Врача
"""

from docx import Document
import os
import docx


def create_folder(key_name: str, root: str):
    new_path = root + '/' + key_name
    try:
        os.mkdir(new_path)
    except FileExistsError:
        print(f"Такая папка существует: {new_path}")
    else:
        pass


def start_segmentation(fltr: str, root: str, key_words_for_remove: tuple, key_head_words: tuple, path: str,
                       key_for_: tuple, structure: tuple, key_name: str):
    new_path = root + '/' + key_name
    try:
        # Отфильтровывает документы с расширением .docx
        if ".docx" in fltr:
            path2 = root + path + '/' + fltr
            conclusion = Document(path2)
            # Фильтруем текст по ключемым словам
            for para in conclusion.paragraphs:
                # Фильтрация по ключу
                for key_for in list(key_for_):
                    if key_for in para.text or key_for.capitalize() in para.text:
                        new_doc_step1 = docx.Document()
                        for parag_ in range(len(conclusion.paragraphs)):
                            # Отфильтровываем всё до параграфа со словом пациент ...
                            for key_word in key_head_words:
                                if key_word in conclusion.paragraphs[parag_].text \
                                        or key_word.capitalize() in conclusion.paragraphs[parag_].text:
                                    for index_key_word in range(parag_):
                                        conclusion.paragraphs[index_key_word].text = None
                            # Отфильтровываем, параграфы со словами врач и тд.....
                            for remove_key in key_words_for_remove:
                                if remove_key in conclusion.paragraphs[parag_].text \
                                        or remove_key.capitalize() in conclusion.paragraphs[parag_].text:
                                    conclusion.paragraphs[parag_].text = None
                        # Вставляем путь для области исследования
                        text = f"{structure} \n {key_name} \n -report-text-below-"
                        new_doc_step1.add_paragraph(text)
                        # Создаем новый текстовый документ на базе предыдущего без включения пустых параграфов
                        for pg in range(len(conclusion.paragraphs)):
                            if conclusion.paragraphs[pg].text == "":
                                pass
                            else:
                                new_doc_step1.add_paragraph(conclusion.paragraphs[pg].text)
                        # Сохраняем docx со старым названием + (new) по новому пути в папку
                        new_doc_step1.save(new_path + '/' + '(new)' + fltr)
    except ValueError:
        print(f"Необработанный документ: {fltr}")
    else:
        pass
