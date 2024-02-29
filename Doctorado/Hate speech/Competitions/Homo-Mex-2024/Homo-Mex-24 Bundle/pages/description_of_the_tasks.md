## Track 1: Hate speech detection track (Multi-class)

The objective of this task is to predict the label of each individual tweet. The three possible labels a tweet can have are LGBT+phobic, not LGBT+phobic, and not LGBT+related. We define each one of these labels next:

- **LGBT+phobic (P).** Tweets contain hate speech directed against any person whose sexual orientation and/or gender identity differs from cis-heterosexuality.
- **Not LGBT+phobic (NP).** Tweets are those that do not include any hate speech against the LGBT+ population but do mention this community.
- **Not LGBT+related (NR).** Tweets are those that are not related in any way to the LGBT+ community.

In this first track, participants will be able to assign one label to each tweet, e.g. Tweet X can be assigned the label "P", and Tweet Y can be assigned with label "NR".

Given that each tweet can have one of these tree labels, the output submission must have two columns, first column corresponds to the ID of the tweet and the second column corresponds to your prediction value for each tweet indicating "P", "NP" or "NR". E. g.

ID_Track1, "P" - this tweet defined as LGBT+phobic.
ID_Track1, "NR" - this tweet defined as not LGBT+phobic related.

## Track 2: Fine-grained hate speech detection track (Multi-labeled)

The objective of this task is to predict one or more label(s) of each individual tweet that contains LGBT+phobic hate speech.

The labels in this sub-track are related to various phobias related to LGBT+phobia. Each one of these phobias is described next:

- **Lesbophobia (L).** Is homophobia explicitly directed at homosexual people who identify as female.
- **Gayphobia (G).** Is homophobia explicitly directed at homosexuals who identify as male.
- **Biphobia (B).** Refers to hate speech directed against people who are attracted to more than one gender.
- **Transphobia (T).** Refers to hate speech directed against non-cis-gendered people.
- **Other LGBT+phobia (O).** Is hate speech against other sexual and gender minorities not included in any of the categories described above (e.g "aphobia" which describes the hatred received by people who do not feel sexual attraction).

In this second track, participants will be able to assign one or more labels to each tweet, e.g. Tweet X can be assigned the labels "L", "G", "B", and Tweet Y can be assigned only the label "O".

Given that each tweet can have one to five labels, the output submission must follow this strict order: "L", "G", "B", "T", "O".

The tweets assigned less than five labels must include the string "0" in place of the label(s) that were not predicted for such tweets, e.g.

ID_Track2, "1", "1", "1", "0", "O" - this tweet would be assigned the labels "L", "G" and "O". The zeros indicate that "B" and "O" were not predicted for this instance.
ID_Track2, "0", "0", "1", "0, "0" - this tweet would be assigned only the label "B". The zeros indicate that "L", "G", "T" and "O" were not predicted for this instance.

## Track 3: Homophobic lyrics detection track (Binary)

The objective of this task is to predict if a phrase of a lyrics song contains LGBT+phobic hate speech. This is a binary task (LGBT+phobic (P), not LGBT+phobic (NP)). We define each one of these labels next:

- **LGBT+phobic (P).** Lyrics contain hate speech directed against any person whose sexual orientation and/or gender identity differs from cis-heterosexuality.
- **Not LGBT+phobic (NP).** Lyrics are those that do not include any hate speech against the LGBT+ population but do mention this community.

In this last track, participants will be able to assign one of the two labels to each tweet, e.g. Tweet X can be assigned the label "P", and Tweet Y can be assigned with label "NP".

Given that each tweet can have one of these tree labels, the output submission must have two columns, first column corresponds to the ID of the tweet and the second column corresponds to your prediction value for each tweet indicating "P" or "NP". E. g.

ID_Track2, "P" - this tweet defined as LGBT+phobic.
ID_Track2, "NP" - this tweet defined as not LGBT+phobic related.
