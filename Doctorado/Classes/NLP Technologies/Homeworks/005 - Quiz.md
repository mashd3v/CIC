
# Quiz

### 1. Paradigmatic Relation
Paradigmatic relations are associative or substitutional. Words that belong to the same category or class are paradigmatically related because they can replace each other in the same syntactic position. For example, synonyms are paradigmatically related because you can replace one synonym with another.

### 2. Syntagmatic Relation
Syntagmatic relations are combinatorial. They describe how words in a sentence relate to each other to create meaning. For instance, in a phrase like "strong wind," "strong" and "wind" have a syntagmatic relationship because they co-occur.

### 3. Features Used in Word Vectors
Word vectors capture meaning by encoding syntactic and semantic properties. These features may include:
- Contextual words: Words frequently appearing in similar contexts.
- POS tags: The part-of-speech information of the word.
- Co-occurrence counts: How frequently words co-occur.
- Dependency relations: Syntactic dependencies between words.

### 4. Reason for Applying Term Frequency Function
The term frequency (TF) function is applied to normalize raw word counts to balance document length differences. Words appearing frequently within a document are given proportionally higher weights.

### 5. Formulas of Term Frequency Functions
- **Raw Term Frequency**: `tf(t, d) = count(t in d)`
- **Log-Normalization**: `tf(t, d) = 1 + log(count(t in d))`
- **Double Normalization K**: `tf(t, d) = (K + (1 - K) * (count(t in d)/max count in d))`

### 6. Reason for Applying IDF Function
The Inverse Document Frequency (IDF) function balances out the impact of common terms that occur across all documents. Terms frequently appearing across documents are down-weighted.

### 7. Formula of IDF Function
\[ IDF(t) = \log\left(\frac{N}{1 + df(t)}\right) \]
where:
- \(N\) = Total number of documents.
- \(df(t)\) = Number of documents containing term \(t\).

### 8. Formula of Entropy of Binary Random Variable \(X_w\)
The entropy for a word \(X_w\) representing a binary random variable is:
\[ H(X_w) = - p(X_w) \cdot \log p(X_w) - (1 - p(X_w)) \cdot \log(1 - p(X_w)) \]

### 9. Conditional Entropy of Random Variable \(X_{w1}\) Given \(X_{w2}\)
The conditional entropy of \(X_{w1}\) given \(X_{w2}\) is:
\[ H(X_{w1}|X_{w2}) = - \sum_{x_{w1}, x_{w2}} p(x_{w1}, x_{w2}) \log p(x_{w1}|x_{w2}) \]

### 10. Mutual Information of Random Variables \(X_{w1}\) and \(X_{w2}\)
Mutual information measures the shared information between two random variables:
\[ I(X_{w1}; X_{w2}) = \sum_{x_{w1}, x_{w2}} p(x_{w1}, x_{w2}) \log \frac{p(x_{w1}, x_{w2})}{p(x_{w1}) \cdot p(x_{w2})} \]

### 11. Comparability of Conditional Entropy
The conditional entropy values of \(X_{w1}\) given \(X_{w2}\) and \(X_{w2}\) given \(X_{w1}\) are not directly comparable because the information one word provides about another differs based on their individual distributions. Thus, the asymmetry reflects the varying predictive information in the relationships between different word pairs.