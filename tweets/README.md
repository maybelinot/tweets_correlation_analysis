# Correlation analysis of tweets

Table below shows correlation between all pairs of tweets binned into 10 minutes frames. 

Highest correlation with value of `0.8532` is between **#ml** and **#analytics** hashtags. The next highest value is between **#startup** and **#bigdata** tags - `0.7623`. 

No correlation was observed between **#startup** and **#acquisition** hashtags, the value is `0.001`. 

Almost equal negative correlation have shown pairs of **#acquisition** with **#conference**, **#meetup** and **#ml**, values are around `-0.3`.

| tag          |   #acquisition |    #ai |   #analytics |   #bigdata |   #conference |   #meetup |     #ml |   #startup |
|:-------------|---------------:|-------:|-------------:|-----------:|--------------:|----------:|--------:|-----------:|
| #acquisition |         1      | 0.0465 |      -0.2315 |    -0.062  |       -0.3074 |   -0.296  | -0.3067 |     0.001  |
| #ai          |         0.0465 | 1      |       0.3348 |     0.5138 |        0.2298 |    0.0741 |  0.283  |     0.667  |
| #analytics   |        -0.2315 | 0.3348 |       1      |     0.6419 |        0.3583 |    0.1639 |  0.8532 |     0.4914 |
| #bigdata     |        -0.062  | 0.5138 |       0.6419 |     1      |        0.2327 |    0.1226 |  0.5412 |     0.7623 |
| #conference  |        -0.3074 | 0.2298 |       0.3583 |     0.2327 |        1      |    0.3118 |  0.3897 |     0.236  |
| #meetup      |        -0.296  | 0.0741 |       0.1639 |     0.1226 |        0.3118 |    1      |  0.1211 |     0.0741 |
| #ml          |        -0.3067 | 0.283  |       0.8532 |     0.5412 |        0.3897 |    0.1211 |  1      |     0.4257 |
| #startup     |         0.001  | 0.667  |       0.4914 |     0.7623 |        0.236  |    0.0741 |  0.4257 |     1      |