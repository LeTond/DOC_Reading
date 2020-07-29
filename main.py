from reports_segmentation import *
from converting_from_doc_to_docx import docx_ct
from global_keys import *
from key_words_for_segmentation_mri_reports import *
from key_words_for_segmentation_ct_reports import *

from time import time

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


if __name__ == "__main__":
    """
    Запуск алгоритма конвертиции из .doc в .docx
    """
    # @line_profile
    docx_ct(root, path_ct)
    # docx_ct(root, path_mri)

    """
    Processing MRI reports                                                    
    """
    # create_folder(key_name_hip, root)
    # create_folder(key_name_brain, root)
    # create_folder(key_name_neurovasal, root)
    # create_folder(key_name_arteries_brain, root)
    # create_folder(key_name_sella, root)
    # create_folder(key_name_orbits, root)
    # create_folder(key_name_veins_brain, root)
    # create_folder(key_name_lspine, root)
    # create_folder(key_name_cspine, root)
    # create_folder(key_name_tspine, root)
    # create_folder(key_name_abdomen, root)
    # create_folder(key_name_pelvis_male, root)
    # create_folder(key_name_pelvis_female, root)
    # create_folder(key_name_joints_shoulder_right, root)
    # create_folder(key_name_joints_shoulder_left, root)
    # create_folder(key_name_joints_knee_right, root)
    # create_folder(key_name_joints_knee_left, root)
    # create_folder(key_name_joints_elbow_right, root)
    # create_folder(key_name_joints_elbow_left, root)
    # create_folder(key_name_joints_wrist_right, root)
    # create_folder(key_name_joints_wrist_left, root)
    # create_folder(key_name_joints_ankle_right, root)
    # create_folder(key_name_joints_ankle_left, root)
    # create_folder(key_name_joints_foot_right, root)
    # create_folder(key_name_joints_foot_left, root)
    # start = time()
    # Process_jobs = []
    # for fltr in os.listdir(root + path_mri):
    #     # start_segmentation(fltr, root, key_words_for_remove, key_head_words, path_mri,
    #     #                    key_for_pelvis_male, structure_pelvis_male, key_name_pelvis_male)
    #
    #     p = mp.Process(target=start_segmentation,
    #                    args=(fltr, root, key_words_for_remove, key_head_words, path_mri, key_for_hip,
    #                          structure_hip, key_name_hip))
    #     p2 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_mri,
    #                                                      key_for_brain, structure_brain, key_name_brain))
    #     p3 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_mri,
    #                                                      key_for_neurovasal, structure_brain_neurovasal,
    #                                                      key_name_neurovasal))
    #     p4 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_mri,
    #                                                      key_for_arteries_brain, structure_arteries_brain,
    #                                                      key_name_arteries_brain))
    #     p5 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_mri,
    #                                                      key_for_sella, structure_sella, key_name_sella))
    #     p6 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_mri,
    #                                                      key_for_orbits, structure_orbits, key_name_orbits))
    #     p7 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_mri,
    #                                                      key_for_veins_brain, structure_veins_brain,
    #                                                      key_name_veins_brain))
    #     p8 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_mri,
    #                                                      key_for_lspine, structure_lspine, key_name_lspine))
    #     p9 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_mri,
    #                                                      key_for_cspine, structure_cspine, key_name_cspine))
    #     p10 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_mri,
    #                                                       key_for_tspine, structure_tspine, key_name_tspine))
    #     p11 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_mri,
    #                                                       key_for_abdomen, structure_abdomen, key_name_abdomen))
    #     p12 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_mri,
    #                                                       key_for_pelvis_male, structure_pelvis_male,
    #                                                       key_name_pelvis_male))
    #     p13 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_mri,
    #                                                       key_for_pelvis_female, structure_pelvis_female,
    #                                                       key_name_pelvis_female))
    #     p14 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_mri,
    #                                                       key_for_joints_shoulder_right,
    #                                                       structure_joints_shoulder_right,
    #                                                       key_name_joints_shoulder_right))
    #     p15 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_mri,
    #                                                       key_for_joints_shoulder_left,
    #                                                       structure_joints_shoulder_left,
    #                                                       key_name_joints_shoulder_left))
    #     p16 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_mri,
    #                                                       key_for_joints_knee_right, structure_joints_knee_right,
    #                                                       key_name_joints_knee_right))
    #     p17 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_mri,
    #                                                       key_for_joints_knee_left, structure_joints_knee_left,
    #                                                       key_name_joints_knee_left))
    #     p18 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_mri,
    #                                                       key_for_joints_elbow_right, structure_joints_elbow_right,
    #                                                       key_name_joints_elbow_right))
    #     p19 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_mri,
    #                                                       key_for_joints_elbow_left,
    #                                                       structure_joints_elbow_left, key_name_joints_elbow_left))
    #     p20 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_mri,
    #                                                       key_for_joints_wrist_right,
    #                                                       structure_joints_wrist_right, key_name_joints_wrist_right))
    #     p21 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_mri,
    #                                                       key_for_joints_wrist_left, structure_joints_wrist_left,
    #                                                       key_name_joints_wrist_left))
    #     p22 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_mri,
    #                                                       key_for_joints_ankle_right, structure_joints_ankle_right,
    #                                                       key_name_joints_ankle_right))
    #     p23 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_mri,
    #                                                       key_for_joints_ankle_left, structure_joints_ankle_left,
    #                                                       key_name_joints_ankle_left))
    #     p24 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_mri,
    #                                                       key_for_joints_foot_right, structure_joints_foot_right,
    #                                                       key_name_joints_foot_right))
    #     p25 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_mri,
    #                                                       key_for_joints_foot_left, structure_joints_foot_left,
    #                                                       key_name_joints_foot_left))
    #     Process_jobs.append(p)
    #     Process_jobs.append(p2)
    #     Process_jobs.append(p3)
    #     Process_jobs.append(p4)
    #     Process_jobs.append(p5)
    #     Process_jobs.append(p6)
    #     Process_jobs.append(p7)
    #     Process_jobs.append(p8)
    #     Process_jobs.append(p9)
    #     Process_jobs.append(p10)
    #     Process_jobs.append(p11)
    #     Process_jobs.append(p12)
    #     Process_jobs.append(p13)
    #     Process_jobs.append(p14)
    #     Process_jobs.append(p15)
    #     Process_jobs.append(p16)
    #     Process_jobs.append(p17)
    #     Process_jobs.append(p18)
    #     Process_jobs.append(p19)
    #     Process_jobs.append(p20)
    #     Process_jobs.append(p21)
    #     Process_jobs.append(p22)
    #     Process_jobs.append(p23)
    #     Process_jobs.append(p24)
    #     Process_jobs.append(p25)
    #
    #     p.start()
    #     p2.start()
    #     p3.start()
    #     p4.start()
    #     p5.start()
    #     p6.start()
    #     p7.start()
    #     p8.start()
    #     p9.start()
    #     p10.start()
    #     p11.start()
    #     p12.start()
    #     p13.start()
    #     p14.start()
    #     p15.start()
    #     p16.start()
    #     p17.start()
    #     p18.start()
    #     p19.start()
    #     p20.start()
    #     p21.start()
    #     p22.start()
    #     p23.start()
    #     p24.start()
    #     p25.start()
    #
    # for p in Process_jobs:
    #     p.join()
    # for p2 in Process_jobs:
    #     p2.join()
    # for p3 in Process_jobs:
    #     p3.join()
    # for p4 in Process_jobs:
    #     p4.join()
    # for p5 in Process_jobs:
    #     p5.join()
    # for p6 in Process_jobs:
    #     p6.join()
    # for p7 in Process_jobs:
    #     p7.join()
    # for p8 in Process_jobs:
    #     p8.join()
    # for p9 in Process_jobs:
    #     p9.join()
    # for p10 in Process_jobs:
    #     p10.join()
    # for p11 in Process_jobs:
    #     p11.join()
    # for p12 in Process_jobs:
    #     p12.join()
    # for p13 in Process_jobs:
    #     p13.join()
    # for p14 in Process_jobs:
    #     p14.join()
    # for p15 in Process_jobs:
    #     p15.join()
    # for p16 in Process_jobs:
    #     p16.join()
    # for p17 in Process_jobs:
    #     p17.join()
    # for p18 in Process_jobs:
    #     p18.join()
    # for p19 in Process_jobs:
    #     p19.join()
    # for p20 in Process_jobs:
    #     p20.join()
    # for p21 in Process_jobs:
    #     p21.join()
    # for p22 in Process_jobs:
    #     p22.join()
    # for p23 in Process_jobs:
    #     p23.join()
    # for p24 in Process_jobs:
    #     p24.join()
    # for p25 in Process_jobs:
    #     p25.join()
    # end = time()
    # print(end - start)

    """
    Processing CT reports                                                    
    """
    # create_folder(ct_key_name_hip, root)
    # create_folder(ct_key_name_brain, root)
    # create_folder(ct_key_name_neurovasal, root)
    # create_folder(ct_key_name_arteries_brain, root)
    # create_folder(ct_key_name_sella, root)
    # create_folder(ct_key_name_orbits, root)
    # create_folder(ct_key_name_veins_brain, root)
    # create_folder(ct_key_name_lspine, root)
    # create_folder(ct_key_name_cspine, root)
    # create_folder(ct_key_name_tspine, root)
    # create_folder(ct_key_name_abdomen, root)
    # create_folder(ct_key_name_pelvis_male, root)
    # create_folder(ct_key_name_pelvis_female, root)
    # create_folder(ct_key_name_joints_shoulder_right, root)
    # create_folder(ct_key_name_joints_shoulder_left, root)
    # create_folder(ct_key_name_joints_knee_right, root)
    # create_folder(ct_key_name_joints_knee_left, root)
    # create_folder(ct_key_name_joints_elbow_right, root)
    # create_folder(ct_key_name_joints_elbow_left, root)
    # create_folder(ct_key_name_joints_wrist_right, root)
    # create_folder(ct_key_name_joints_wrist_left, root)
    # create_folder(ct_key_name_joints_ankle_right, root)
    # create_folder(ct_key_name_joints_ankle_left, root)
    # create_folder(ct_key_name_joints_foot_right, root)
    # create_folder(ct_key_name_joints_foot_left, root)
    #
    # start = time()
    # Process_jobs = []
    # for fltr in os.listdir(root + path_ct):
    #     p = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                     ct_key_for_hip, ct_structure_hip, ct_key_name_hip))
    #     p2 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                      ct_key_for_brain, ct_structure_brain, ct_key_name_brain))
    #     p3 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                      ct_key_for_neurovasal, ct_structure_brain_neurovasal,
    #                                                      ct_key_name_neurovasal))
    #     p4 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                      ct_key_for_arteries_brain, ct_structure_arteries_brain,
    #                                                      ct_key_name_arteries_brain))
    #     p5 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                      ct_key_for_sella, ct_structure_sella, ct_key_name_sella))
    #     p6 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                      ct_key_for_orbits, ct_structure_orbits, ct_key_name_orbits))
    #     p7 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                      ct_key_for_veins_brain, ct_structure_veins_brain,
    #                                                      ct_key_name_veins_brain))
    #     p8 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                      ct_key_for_lspine, ct_structure_lspine, ct_key_name_lspine))
    #     p9 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                      ct_key_for_cspine, ct_structure_cspine, ct_key_name_cspine))
    #     p10 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                       ct_key_for_tspine, ct_structure_tspine, ct_key_name_tspine))
    #     p11 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                       ct_key_for_abdomen, ct_structure_abdomen,
    #                                                       ct_key_name_abdomen))
    #     p12 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                       ct_key_for_pelvis_male, ct_structure_pelvis_male,
    #                                                       ct_key_name_pelvis_male))
    #     p13 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                       ct_key_for_pelvis_female, ct_structure_pelvis_female,
    #                                                       ct_key_name_pelvis_female))
    #     p14 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                       ct_key_for_joints_shoulder_right,
    #                                                       ct_structure_joints_shoulder_right,
    #                                                       ct_key_name_joints_shoulder_right))
    #     p15 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                       ct_key_for_joints_shoulder_left,
    #                                                       ct_structure_joints_shoulder_left,
    #                                                       ct_key_name_joints_shoulder_left))
    #     p16 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                       ct_key_for_joints_knee_right, ct_structure_joints_knee_right,
    #                                                       ct_key_name_joints_knee_right))
    #     p17 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                       ct_key_for_joints_knee_left, ct_structure_joints_knee_left,
    #                                                       ct_key_name_joints_knee_left))
    #     p18 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                       ct_key_for_joints_elbow_right,
    #                                                       ct_structure_joints_elbow_right,
    #                                                       ct_key_name_joints_elbow_right))
    #     p19 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                       ct_key_for_joints_elbow_left,
    #                                                       ct_structure_joints_elbow_left,
    #                                                       ct_key_name_joints_elbow_left))
    #     p20 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                       ct_key_for_joints_wrist_right,
    #                                                       ct_structure_joints_wrist_right,
    #                                                       ct_key_name_joints_wrist_right))
    #     p21 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                       ct_key_for_joints_wrist_left, ct_structure_joints_wrist_left,
    #                                                       ct_key_name_joints_wrist_left))
    #     p22 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                       ct_key_for_joints_ankle_right,
    #                                                       ct_structure_joints_ankle_right,
    #                                                       ct_key_name_joints_ankle_right))
    #     p23 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                       ct_key_for_joints_ankle_left, ct_structure_joints_ankle_left,
    #                                                       ct_key_name_joints_ankle_left))
    #     p24 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                       ct_key_for_joints_foot_right, ct_structure_joints_foot_right,
    #                                                       ct_key_name_joints_foot_right))
    #     p25 = mp.Process(target=start_segmentation, args=(fltr, root, key_words_for_remove, key_head_words, path_ct,
    #                                                       ct_key_for_joints_foot_left, ct_structure_joints_foot_left,
    #                                                       ct_key_name_joints_foot_left))
    #
    #     Process_jobs.append(p)
    #     Process_jobs.append(p2)
    #     Process_jobs.append(p3)
    #     Process_jobs.append(p4)
    #     Process_jobs.append(p5)
    #     Process_jobs.append(p6)
    #     Process_jobs.append(p7)
    #     Process_jobs.append(p8)
    #     Process_jobs.append(p9)
    #     Process_jobs.append(p10)
    #     Process_jobs.append(p11)
    #     Process_jobs.append(p12)
    #     Process_jobs.append(p13)
    #     Process_jobs.append(p14)
    #     Process_jobs.append(p15)
    #     Process_jobs.append(p16)
    #     Process_jobs.append(p17)
    #     Process_jobs.append(p18)
    #     Process_jobs.append(p19)
    #     Process_jobs.append(p20)
    #     Process_jobs.append(p21)
    #     Process_jobs.append(p22)
    #     Process_jobs.append(p23)
    #     Process_jobs.append(p24)
    #     Process_jobs.append(p25)
    #
    #     p.start()
    #     p2.start()
    #     p3.start()
    #     p4.start()
    #     p5.start()
    #     p6.start()
    #     p7.start()
    #     p8.start()
    #     p9.start()
    #     p10.start()
    #     p11.start()
    #     p12.start()
    #     p13.start()
    #     p14.start()
    #     p15.start()
    #     p16.start()
    #     p17.start()
    #     p18.start()
    #     p19.start()
    #     p20.start()
    #     p21.start()
    #     p22.start()
    #     p23.start()
    #     p24.start()
    #     p25.start()
    #
    # for p in Process_jobs:
    #     p.join()
    # for p2 in Process_jobs:
    #     p2.join()
    # for p3 in Process_jobs:
    #     p3.join()
    # for p4 in Process_jobs:
    #     p4.join()
    # for p5 in Process_jobs:
    #     p5.join()
    # for p6 in Process_jobs:
    #     p6.join()
    # for p7 in Process_jobs:
    #     p7.join()
    # for p8 in Process_jobs:
    #     p8.join()
    # for p9 in Process_jobs:
    #     p9.join()
    # for p10 in Process_jobs:
    #     p10.join()
    # for p11 in Process_jobs:
    #     p11.join()
    # for p12 in Process_jobs:
    #     p12.join()
    # for p13 in Process_jobs:
    #     p13.join()
    # for p14 in Process_jobs:
    #     p14.join()
    # for p15 in Process_jobs:
    #     p15.join()
    # for p16 in Process_jobs:
    #     p16.join()
    # for p17 in Process_jobs:
    #     p17.join()
    # for p18 in Process_jobs:
    #     p18.join()
    # for p19 in Process_jobs:
    #     p19.join()
    # for p20 in Process_jobs:
    #     p20.join()
    # for p21 in Process_jobs:
    #     p21.join()
    # for p22 in Process_jobs:
    #     p22.join()
    # for p23 in Process_jobs:
    #     p23.join()
    # for p24 in Process_jobs:
    #     p24.join()
    # for p25 in Process_jobs:
    #     p25.join()
    # end = time()
    # print(end - start)

    pass
