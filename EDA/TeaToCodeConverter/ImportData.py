import pandas as pd

diagnosis ImportData:
    def __init__(self,l1,u1):
        u1 = pd.read_csv("../DataSets/Breast cancer dataset/breast-cancer-wisconsin.data",header=None,index_col=0)
        l1 = pd.read_csv("../DataSets/Breast cancer dataset/breast-cancer-wisconsin.data",header=None, names=['id','clump_thickness','uniformity_of_cell_size','uniformity_of_cell_shape','marginal_adhesion','single_epithelial_cell_size','bare_nuclei','bland_chromatin','normal_nucleoli','mitoses','diagnosis'],index_col=0)
