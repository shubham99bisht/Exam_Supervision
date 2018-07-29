import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

def make_pdf(final_li):

    classroom = []
    with open('classroom.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            classroom.append(row[0])
    classroom.sort()


    fig, ax = plt.subplots()

    # hide axes
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')

    #df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABcd'))

    df = pd.DataFrame(final_li, columns=(["Dates"]+classroom))

    ax.table(cellText=df.values, colLabels=df.columns, loc='center')

    fig.tight_layout()

    #plt.show()

    from matplotlib.backends.backend_pdf import PdfPages
    pp = PdfPages('Exm_Supervision_Chart.pdf')
    pp.savefig()
    pp.close()
