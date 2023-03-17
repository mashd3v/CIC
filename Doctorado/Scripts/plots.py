import seaborn as sns
import pandas as pd, numpy as np
import matplotlib.pyplot as plt

class Plots:
    def __init__(self, metrics):
        self.metrics = metrics

    def plot_classification_report(self, title, x_label, y_label, x_labels, 
                                   y_labels, with_avg_total=False):
        lines = self.metrics[0].split('\n')

        classes = []
        plotMat = []
        for line in lines[2 : (len(lines) - 5)]:
            t = line.split()
            classes.append(t[0])
            v = [float(x) for x in t[1: len(t) - 1]]
            plotMat.append(v)

        if with_avg_total:
            aveTotal = lines[len(lines) - 2].split()
            classes.append('avg/total')
            vAveTotal = [float(x) for x in aveTotal[2:5]]
            plotMat.append(vAveTotal)

        # Crear una figura y un eje
        fig, ax = plt.subplots(figsize=(15, 8))

        sns.heatmap(plotMat, annot=True, fmt='.2%', cmap='Blues', ax=ax,
                    xticklabels=x_labels, yticklabels=y_labels)
        
        # Configurar las etiquetas del eje
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(title)

        # Mostrar la figura
        plt.show()

        # plt.imshow(plotMat, interpolation='nearest', cmap=plt.cm.Blues)
        # plt.title(title)
        # plt.colorbar()
        # x_tick_marks = np.arange(3)
        # y_tick_marks = np.arange(len(classes))
        # plt.xticks(x_tick_marks, ['precision', 'recall', 'f1-score'], rotation=45)
        # plt.yticks(y_tick_marks, classes)
        # plt.tight_layout()

        # plt.ylabel(x_label)
        # plt.xlabel(y_label) 



    def plot_confusion_matrix(self, title, x_label, y_label, labels):
        # Calcular la matriz de confusión en porcentajes
        cm_perc = self.metrics[1] / self.metrics[1].sum(axis=1).reshape(-1,1)

        # Crear una figura y un eje
        fig, ax = plt.subplots(figsize=(10, 8))

        # Mostrar la matriz de confusión como una imagen
        sns.heatmap(cm_perc, annot=True, fmt='.2%', cmap='Blues', ax=ax, 
                    xticklabels=labels, yticklabels=labels)

        # Configurar las etiquetas del eje
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(title)

        # Mostrar la figura
        plt.show()