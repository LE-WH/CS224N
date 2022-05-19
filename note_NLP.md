Notes from CS224N
====

Lecture 5
----

- Dependency parser. 

    - dropout 




Lecture 6
----

* RNN

* LSTN as the most successful RNN model

Lecture 7
----

* Translation?
    - Old-fashioned methods
    - seq2seq methods: using 2 LSTN models for the source sentence and target sentence.
    - multi-layer RNN, (often 2 is the best)
    - beam search. Normalize by length.
    - BLEU algo. for evaluating.

* Beam search
    - always find k possible ways. And then generate future ways from those k ways, then choose k most possible ways.