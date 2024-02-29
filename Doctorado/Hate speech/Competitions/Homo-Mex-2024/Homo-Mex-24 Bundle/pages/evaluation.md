# Evaluation

To evaluate the model performance of the participants (ranking) the F1-score will be used. Consider that for the multi-class and multi-label tracks the F1 score will be computed as a macro average (macro-F1 score) and for the binary track the F1 will be computed as binary-F1. Additionally, the following metrics will be reported:

- Track 1:
  - F1-score (macro-average)
  - precision (macro-average)
  - recall (macro-average)
- Track 2:
  - F1-score (macro-average)
  - Hamming-Loss
  - Exact match ratio
- Track 3:
  - F1-score (binary)
  - precision (binary)
  - recall (binary)

## Metrics

- $$F1-score = 2 \frac{precision \cdot recall}{precision + recall}$$

- $$precision = \frac{tp}{tp+fp}$$

- $$recall = \frac{tp}{tp+fn}$$

### Macro average

With any binary evaluation measure $B(t_p, t_n, f_p, f_n)$ calculated based on the number of true positives ($t_p$), true negatives ($t_n$), false positives ($f_p$) and false negatives ($f_n$). Let $t_{p\lambda}$, $f_{p\lambda}$, $t_{n\lambda}$ and $f_{n\lambda}$ be the number of true positives, false positives, true negatives and false negatives after binary evaluation for a label $\lambda$. The macro-averaged version of $B$, compute as follows:

$$B_{\text{macro}} = \frac{1}{q} \sum_{\lambda = 1}^q B(t_{p\lambda}, f_{p\lambda}, t_{n\lambda}, f_{n\lambda})$$

### Hamming Loss

$$\text{Hamming-Loss} = \frac{1}{m} \sum_{i=1}^m \frac{Y_i \Delta Z_i}{M}$$

where $\Delta$ is the symmetric difference of two sets, or in boolean logic the XOR operation; $m$ is the number of samples; $M$ is the number of labels; $Y_i$ is the set of true labels; $Z_i$ is the set of predicted labels.

### Exact match ratio

$$\text{MR} = \frac{1}{n} \sum_{i=1}^n I(y_i = \hat{y_i})$$

where $I$ is the indicator function.

## References

Any doubts about the metric computation, please refer to the following:

- [multi-label metrics](https://mmuratarat.github.io/2020-01-25/multilabel_classification_metrics)
- [Averaging metrics](https://www.evidentlyai.com/classification-metrics/multi-class-metrics#:~:text=Macro%2Daveraging,-Here%20is%20how&text=Calculate%20the%20number%20of%20true,averaged%20precision%20and%20recall%20scores.)
- [Hamming loss](https://link.springer.com/chapter/10.1007/978-0-387-09823-4_34)
- [Precision, recall and F1 score](https://towardsdatascience.com/accuracy-precision-recall-or-f1-331fb37c5cb9)
