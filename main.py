from Algorithm.reports_segmentation import *
from Algorithm.doc_renamer import *
from Keys.global_keys import *

from Algorithm.converting_from_doc_to_docx import docx_

# from Keys.key_words_HEAD_mri import *
# from Keys.key_words_JOINTS_mri import *
from Keys.key_words_SPINE_mri import *
# from Keys.key_words_PELVIS_mri import *

from Algorithm.export_authomatization import *
from time import time
from collections import deque

import multiprocessing as mp


def line_profile(func):
    def wrapper(*args, **kwargs):
        from line_profiler import LineProfiler
        prof = LineProfiler()
        try:
            return prof(func)(*args, **kwargs)
        finally:
            prof.print_stats()

    return wrapper


def mri_start_mkdirs():
    """
    Запуск создания директорий и начала сегментации документов
    :return: None
    """
    for pat in key_for_area_list:
        process_jobs = deque()
        create_folder_area(pat[1], root)
        for prepared_document in os.listdir(root + path_mri_copy):
            p = mp.Process(target=start_segmentation,
                           args=(prepared_document, root, path_mri_copy, pat[0], pat[1]))
            process_jobs.append(p)
            p.start()
        for p in process_jobs:
            p.join()


def mri_start_preprocess():
    """
    Запуск создания папок по названию ключевого слова,
    фильтрации документов,
    удаления шапок и подписей в документах
    :return: None
    """
    for pat in global_pathology_mri_list:
        create_folder_pathology(pat[1], root, pat[2])
        for prepared_document in os.listdir(root + '/' + pat[3].replace('//', '/')):
            continue_segmentation(
                prepared_document, root, key_words_for_remove, pat[0], pat[1], pat[2], pat[3], conclusion_key_words
            )


def mri_start_preprocess_end():
    """
    Запуск удаления  "избыточных" документов и сегментирование "Прочих" патологий
    :return:
    """
    start = time()

    for pat in global_pathology_mri_list:
        process_jobs = []
        for prepared_document in os.listdir(root + '/' + pat[3].replace('//', '/')):
            p = mp.Process(target=remove_segmented,
                           args=(prepared_document, root, pat[1], pat[2], pat[3]))
            process_jobs.append(p)
            p.start()
        for p in process_jobs:
            p.join()

    for pat in global_pathology_mri_list:
        process_jobs = []
        for prepared_document in os.listdir(root + '/' + pat[3].replace('//', '/')):
            p = mp.Process(target=segment_else,
                           args=(prepared_document, root, key_words_for_remove, pat[1]))
            process_jobs.append(p)
            p.start()
        for p in process_jobs:
            p.join()

    end = time()
    print(end - start)


if __name__ == "__main__":
    """
    Запуск алгоритма конвертации из .doc в .docx
    """
    # @line_profile
    # docx_(root, path_mri)
    """
    Processing MRI reports
    """
    # mri_start_mkdirs()
    # mri_start_preprocess()
    # mri_start_preprocess_end()
    """
    exporting reports to server
    """
    # export(export_link, root, recursion_way)

    """
    rename dicom document
    """
    # rename_file('/home/lg/ITMO/New_21_22_23/00023/', list_file_to_dcm('/home/lg/ITMO/New_21_22_23/00023/'))