from reports_segmentation import *
from converting_from_doc_to_docx import docx_ct
from global_keys import *
from key_words_for_segmentation_mri_reports import *
from key_words_for_segmentation_ct_reports import *
from export_authomatization import *
from functools import lru_cache
from time import time
from multiprocessing import Pool
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


@lru_cache(maxsize=64)
def mri_preproc_start():
    start = time()
    for pat in key_for_area_list:
        Process_jobs = deque()
        create_folder_area(pat[1], root)
        for fltr in os.listdir(root + path_mri_copy):
            p = mp.Process(target=start_segmentation,
                           args=(fltr, root, path_mri_copy, pat[0], pat[1]))
            Process_jobs.append(p)
            p.start()
        for p in Process_jobs:
            p.join()

    for paths in create_path_list:
        create_folder_pathology(paths[0], root, paths[1])

    for pat in global_pathology_mri_list:
        Process_jobs = []
        for fltr in os.listdir(root + '/' + pat[1].replace('//', '/')):
            p = mp.Process(target=contin_segmentation,
                           args=(fltr, root, key_words_for_remove, key_head_words, pat[0], pat[1], pat[2]))
            Process_jobs.append(p)
            p.start()
        for p in Process_jobs:
            p.join()
    end = time()
    print(end - start)

def mri_preproc_end():
    start = time()
    for pat in global_pathology_mri_list:
        Process_jobs = []
        for fltr in os.listdir(root + '/' + pat[1].replace('//', '/')):
            p = mp.Process(target=remove_segmented,
                           args=(fltr, root, pat[1], pat[2]))
            Process_jobs.append(p)
            p.start()
        for p in Process_jobs:
            p.join()

    for pat in global_pathology_mri_list:
        Process_jobs = []
        for fltr in os.listdir(root + '/' + pat[1].replace('//', '/')):
            p = mp.Process(target=segment_else,
                           args=(fltr, root, key_words_for_remove, key_head_words, pat[1]))
            Process_jobs.append(p)
            p.start()
        for p in Process_jobs:
            p.join()
    end = time()
    print(end - start)



def ct_preproc_start():
    # start = time()
    # Process_jobs = []
    # for fltr in os.listdir(root + path_ct):
    #     p = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                     ct_key_for_hip, ct_structure_hip, ct_key_name_hip))
    start = time()
    for pat in key_for_area_list:
        Process_jobs = []
        create_folder_area(pat[1], root)
        for fltr in os.listdir(root + path_mri_copy):
            p = mp.Process(target=start_segmentation,
                           args=(fltr, root, key_words_for_remove, key_head_words, path_mri_copy, pat[0], pat[1]))
            Process_jobs.append(p)
            p.start()
        for p in Process_jobs:
            p.join()

    for paths in create_path_list:
        create_folder_pathology(paths[0], root, paths[1])

    for pat in global_pathology_mri_list:
        Process_jobs = []
        for fltr in os.listdir(root + '/' + pat[1].replace('//', '/')):
            p = mp.Process(target=contin_segmentation,
                           args=(fltr, root, pat[0], pat[1], pat[2]))
            Process_jobs.append(p)
            p.start()
        for p in Process_jobs:
            p.join()

    for pat in global_pathology_mri_list:
        Process_jobs = []
        for fltr in os.listdir(root + '/' + pat[1].replace('//', '/')):
            p = mp.Process(target=remove_segmented,
                           args=(fltr, root, pat[1], pat[2]))
            Process_jobs.append(p)
            p.start()
        for p in Process_jobs:
            p.join()

    for pat in global_pathology_mri_list:
        Process_jobs = []
        for fltr in os.listdir(root + '/' + pat[1].replace('//', '/')):
            p = mp.Process(target=segment_else,
                           args=(fltr, root, pat[1]))
            Process_jobs.append(p)
            p.start()
        for p in Process_jobs:
            p.join()
    end = time()
    print(end - start)

if __name__ == "__main__":
    """
    Запуск алгоритма конвертиции из .doc в .docx
    """
    # @line_profile
    # docx_ct(root, path_ct)
    # docx_ct(root, path_mri)
    """
    Processing MRI reports
    """
    mri_preproc_start()
    mri_preproc_end()



    """
    Processing CT reports
    """
    # ct_preproc_start()
    """
    exporting reports to server
    """
    # export(export_link, root)

    # for dirpath, dirnames, filenames in os.walk('/home/lg/Dropbox/Conclusion/MEDICAL REPORTS/МРТ Тексты'):
    #     # перебрать каталоги
    #     for dirname in dirnames:
    #         print(os.path.join(dirpath, dirname))

    pass
