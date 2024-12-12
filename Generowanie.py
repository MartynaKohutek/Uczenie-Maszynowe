import numpy as np
from sklearn.metrics import cohen_kappa_score, matthews_corrcoef, confusion_matrix, recall_score, precision_score, f1_score
TP = 50
TN = 0
FP = 25
FN = 25
recall = 0
precision = 0

while TN < 51:
    print('************TP=',TP,'*********')
    if TP+FP == 0:
        print('0 w mianowniku!')
    else:
        precision = TP / (TP + FP)  # Precyzja
        print(f"Precision: {precision:.4f}")
    if TP+FN == 0:
            print('0 w mianowniku!')
    else:
            recall = TP / (TP + FN)     # Czułość (Recall)
            print(f"Recall: {recall:.4f}")
    if precision+recall == 0:
        print('0 w mianowniku!')
    else:
        f1 = 2 * (precision * recall) / (precision + recall)  # F1-score
        print(f"F1-score: {f1:.4f}")
    if TN+FP == 0:
        print('0 w mianowniku!')
    else:
        TNR = TN / (TN + FP)  # Swoistość
        gmean = np.sqrt(recall * TNR)
        print(f"Gmean: {gmean:.4f}")
    

    # MCC
    mcc = (TP * TN - FP * FN) / np.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
    print(f"MCC: {mcc:.4f}")
    


    # Cohen's Kappa
    total = TP + FP + TN + FN
    po = (TP + TN) / total  # Obserwowana zgodność
    pe = ((TP + FN) * (TP + FP) + (TN + FP) * (TN + FN)) / (total ** 2)  # Zgoda przypadkowa
    if 1-pe ==0:
         print('0 w mianowniku!')
    else:
        kappa = (po - pe) / (1 - pe)
        print(f"Cohen's Kappa: {kappa:.4f}")


    TP-=5
    TN+=5
