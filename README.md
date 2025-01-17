# Проект "Управление инфинитивом и герундием в английском языке"
### Материалы
[Таблица с данными](https://yadi.sk/d/3k7dFlu33Qon73) <br>
[Код на R](https://github.com/kategerasimenko/hsecxg_project/blob/master/'analysis'.R)
## Рабочая гипотеза
Выбор - управление инфинитивом или герундием зависит от:
* переходности главного глагола (герундий - прямой объект, инфинитив не всегда. Но не смогла сделать этот признак)
* контроля или подъема аргумента (инфинитив - всегда контроль)
* в теор.литературе "ориентированности инфинитивной конструкции на будущее", тут - некоторых сем.классов обоих глаголов
## Данные
### Материал исследования
из 50 тыс. первых предложений из раздела B корпуса BNC было выделено всего 5581 конструкций, в тч:
* глагол управляет инфинитивом с *to* - 4895 вхождений
* глагол управляет инфинитивом без *to* - 71 вхождение
* глагол управляет герундием - 615 вхождений
Два замечания:
* выборка создавалась автоматически, [здесь код](https://github.com/kategerasimenko/hsecxg_project/blob/master/preprocessing/extract_BNC.py)
* 71 вхождение глагола с инфинитивом без *to* также считается инфинитивом - кажется, что этот вид управления прописывается закрытым списком глаголов.
### Факторы выбора конструкции
Что очень хотелось бы сделать - уметь различать разные контексты одного глагола (remember, stop, где возможны оба варианта управления, но различаются значения), т.е. чтобы признаки не зависели только от матричного глагола. 
* зависимая переменная - инфинитив (1) или герундий (0)
* признаки:
  * есть ли глагол в списке [English control verbs из Википедии](https://en.wiktionary.org/wiki/Category:English_control_verbs)
  * кластер матричного глагола (словоформы) из 10 кластеров ИЛИ из 20 кластеров
  * кластер зависимого глагола (леммы) из 10 кластеров ИЛИ из 20 кластеров
Кластеры строились через KMeans и с векторами из [предтренированной модели Word2Vec на Google News](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit). [Код и списки слов по кластерам](https://github.com/kategerasimenko/hsecxg_project/blob/master/preprocessing/clustering.ipynb)
## Мультифакторный анализ
* логистическая регрессия:
  * хорошо (значимо) проявляет себя класс матричного глагола (и м10, и м20):
  ```
  Call:
  glm(formula = answer ~ m10, family = "binomial", data = data)

  Deviance Residuals: 
      Min       1Q   Median       3Q      Max  
  -3.2062   0.1084   0.4293   0.5625   0.7389  

  Coefficients:
              Estimate Std. Error z value Pr(>|z|)    
  (Intercept)   1.1587     0.1370   8.457  < 2e-16 ***
  m101          0.1987     0.1581   1.257 0.208725    
  m102          2.8382     0.3025   9.382  < 2e-16 ***
  m103          0.6402     0.1769   3.619 0.000296 ***
  m104          3.9752     0.4316   9.210  < 2e-16 ***
  m105          0.9237     0.2134   4.328 1.50e-05 ***
  m106          0.5306     0.1923   2.758 0.005808 ** 
  m107          0.6049     0.2160   2.800 0.005105 ** 
  m108          1.1792     0.2165   5.446 5.16e-08 ***
  m109          0.7313     0.2149   3.403 0.000666 ***
  ---
  Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

  (Dispersion parameter for binomial family taken to be 1)

    Null deviance: 3872.4  on 5580  degrees of freedom
  Residual deviance: 3448.3  on 5571  degrees of freedom
  AIC: 3468.3

  Number of Fisher Scoring iterations: 7
  ```
  ```
  Call:
  glm(formula = answer ~ m20, family = "binomial", data = data)

  Deviance Residuals: 
      Min       1Q   Median       3Q      Max  
  -2.8908   0.1757   0.3247   0.5177   1.8465  

  Coefficients:
              Estimate Std. Error z value Pr(>|z|)    
  (Intercept)  0.77319    0.49355   1.567 0.117209    
  m201        -1.57882    0.55900  -2.824 0.004738 ** 
  m202         3.38976    0.53639   6.320 2.62e-10 ***
  m203        -1.07547    0.58813  -1.829 0.067453 .  
  m204         1.44601    0.53660   2.695 0.007044 ** 
  m205         1.51567    0.54190   2.797 0.005159 ** 
  m206         1.12271    0.52119   2.154 0.031231 *  
  m207         1.58681    0.54161   2.930 0.003392 ** 
  m208         2.08901    0.87873   2.377 0.017439 *  
  m209         1.52940    0.89084   1.717 0.086014 .  
  m2010       -2.27727    0.74104  -3.073 0.002119 ** 
  m2011        2.09714    0.56486   3.713 0.000205 ***
  m2012        0.47723    0.51447   0.928 0.353608    
  m2013        1.16890    0.50876   2.298 0.021587 *  
  m2014        2.18864    0.77082   2.839 0.004520 ** 
  m2015        2.14299    0.55281   3.877 0.000106 ***
  m2016       -0.04051    0.51718  -0.078 0.937563    
  m2017        3.17630    0.57986   5.478 4.31e-08 ***
  m2018        0.70729    0.50867   1.390 0.164385    
  m2019       -2.22848    0.57592  -3.869 0.000109 ***
  ---
  Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

  (Dispersion parameter for binomial family taken to be 1)

      Null deviance: 3872.4  on 5580  degrees of freedom
  Residual deviance: 3003.6  on 5561  degrees of freedom
  AIC: 3043.6

  Number of Fisher Scoring iterations: 6
  ```
  * с классом вложенного глагола сложнее: <br>
  класс из 10 (в10) значим:
  ```
  Call:
  glm(formula = answer ~ e10, family = "binomial", data = data)

  Deviance Residuals: 
      Min       1Q   Median       3Q      Max  
  -2.7304   0.3708   0.4126   0.5147   0.8250  

  Coefficients:
              Estimate Std. Error z value Pr(>|z|)    
  (Intercept)   0.9029     0.1767   5.109 3.24e-07 ***
  e101          1.0516     0.2121   4.958 7.12e-07 ***
  e102          1.5178     0.1967   7.717 1.20e-14 ***
  e103          1.7402     0.3012   5.777 7.61e-09 ***
  e104          1.0230     0.2171   4.712 2.46e-06 ***
  e105          1.2994     0.2192   5.927 3.08e-09 ***
  e106          1.8766     0.3004   6.247 4.18e-10 ***
  e107          2.8002     0.4214   6.644 3.04e-11 ***
  e108          1.3727     0.3236   4.241 2.22e-05 ***
  e109          0.4519     0.1998   2.262   0.0237 *  
  ---
  Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

  (Dispersion parameter for binomial family taken to be 1)

      Null deviance: 3872.4  on 5580  degrees of freedom
  Residual deviance: 3714.4  on 5571  degrees of freedom
  AIC: 3734.4

  Number of Fisher Scoring iterations: 6
  ```
  класс из 20 (в20) - не очень, и AIC хуже:
  ```
  Call:
  glm(formula = answer ~ e20, family = "binomial", data = data)

  Deviance Residuals: 
      Min       1Q   Median       3Q      Max  
  -2.5527   0.4607   0.4660   0.4826   0.9005  

  Coefficients:
                Estimate Std. Error z value Pr(>|z|)    
  (Intercept)    2.02438    0.28436   7.119 1.09e-12 ***
  e201           0.14102    0.29460   0.479   0.6322    
  e202          -0.42136    0.30079  -1.401   0.1613    
  e203          -0.85581    0.37129  -2.305   0.0212 *  
  e204          -1.33123    1.25732  -1.059   0.2897    
  e205          -0.33798    0.56383  -0.599   0.5489    
  e206           0.24430    0.51456   0.475   0.6349    
  e207          -0.77162    0.63426  -1.217   0.2238    
  e208           0.06714    0.31059   0.216   0.8289    
  e209           0.85902    0.46136   1.862   0.0626 .  
  e2010         14.54169 1199.77239   0.012   0.9903    
  e2011         -0.23262    0.32769  -0.710   0.4778    
  e2012          0.16503    0.30329   0.544   0.5863    
  e2013        -18.59045 2399.54474  -0.008   0.9938    
  e2014          1.19449    0.77515   1.541   0.1233    
  e2015          0.97847    0.48043   2.037   0.0417 *  
  e2016         14.54169  254.35139   0.057   0.9544    
  e2017          0.88434    0.65755   1.345   0.1787    
  e2018          0.22691    0.59764   0.380   0.7042    
  e2019          1.00212    0.46035   2.177   0.0295 *  
  ---
  Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

  (Dispersion parameter for binomial family taken to be 1)

      Null deviance: 3872.4  on 5580  degrees of freedom
  Residual deviance: 3774.3  on 5561  degrees of freedom
  AIC: 3814.3

  Number of Fisher Scoring iterations: 15
  ```
  * совместить класс матричного глагола из 20 и класс вложенного глагола из 10:
  ```
  Call:
  glm(formula = answer ~ m20 + e10, family = "binomial", data = data)

  Deviance Residuals: 
      Min       1Q   Median       3Q      Max  
  -3.3739   0.1515   0.2779   0.4600   2.2169  

  Coefficients:
              Estimate Std. Error z value Pr(>|z|)    
  (Intercept)  -0.1355     0.5494  -0.247 0.805137    
  m201         -1.8434     0.5728  -3.218 0.001289 ** 
  m202          3.3560     0.5454   6.153 7.60e-10 ***
  m203         -1.0555     0.6073  -1.738 0.082214 .  
  m204          1.4637     0.5464   2.679 0.007392 ** 
  m205          1.1052     0.5553   1.990 0.046556 *  
  m206          0.9329     0.5325   1.752 0.079764 .  
  m207          1.4805     0.5529   2.677 0.007418 ** 
  m208          1.8906     0.8891   2.126 0.033476 *  
  m209          1.6854     0.9034   1.866 0.062090 .  
  m2010        -2.4915     0.7643  -3.260 0.001114 ** 
  m2011         1.9132     0.5750   3.327 0.000878 ***
  m2012         0.5499     0.5263   1.045 0.296132    
  m2013         1.3122     0.5204   2.522 0.011678 *  
  m2014         2.2249     0.7815   2.847 0.004412 ** 
  m2015         1.9231     0.5652   3.403 0.000667 ***
  m2016        -0.1991     0.5293  -0.376 0.706865    
  m2017         3.1379     0.5906   5.313 1.08e-07 ***
  m2018         0.5970     0.5200   1.148 0.250950    
  m2019        -2.2323     0.5882  -3.795 0.000148 ***
  e101          0.9505     0.2508   3.790 0.000151 ***
  e102          1.4474     0.2369   6.109 1.00e-09 ***
  e103          1.6848     0.3574   4.714 2.43e-06 ***
  e104          0.7991     0.2581   3.097 0.001958 ** 
  e105          0.8477     0.2594   3.268 0.001082 ** 
  e106          1.4591     0.3382   4.314 1.60e-05 ***
  e107          2.4676     0.4598   5.367 8.03e-08 ***
  e108          1.1165     0.3787   2.948 0.003196 ** 
  e109          0.1151     0.2374   0.485 0.627815    
  ---
  Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

  (Dispersion parameter for binomial family taken to be 1)

      Null deviance: 3872.4  on 5580  degrees of freedom
  Residual deviance: 2874.8  on 5552  degrees of freedom
  AIC: 2932.8

  Number of Fisher Scoring iterations: 6
  ```
  * контроль: сам по себе значим, но AIC большеват
  ```
  Call:
  glm(formula = answer ~ c, family = "binomial", data = data)

  Deviance Residuals: 
      Min       1Q   Median       3Q      Max  
  -2.4779   0.3083   0.5292   0.5292   0.5292  

  Coefficients:
              Estimate Std. Error z value Pr(>|z|)    
  (Intercept)  1.89494    0.04565  41.510   <2e-16 ***
  c1           1.12742    0.13685   8.239   <2e-16 ***
  ---
  Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

  (Dispersion parameter for binomial family taken to be 1)

      Null deviance: 3872.4  on 5580  degrees of freedom
  Residual deviance: 3785.0  on 5579  degrees of freedom
  AIC: 3789

  Number of Fisher Scoring iterations: 5
  ```
  * встроить контроль в м20+в10 - ничего не меняет, он не значим:
  ```
  Call:
  glm(formula = answer ~ c + m20 + e10, family = "binomial", data = data)

  Deviance Residuals: 
      Min       1Q   Median       3Q      Max  
  -3.3471   0.1491   0.2776   0.4550   2.2166  

  Coefficients:
              Estimate Std. Error z value Pr(>|z|)    
  (Intercept)  -0.1333     0.5496  -0.242 0.808426    
  c1            0.2333     0.1665   1.401 0.161221    
  m201         -1.8586     0.5731  -3.243 0.001182 ** 
  m202          3.2883     0.5474   6.008 1.88e-09 ***
  m203         -1.0585     0.6076  -1.742 0.081470 .  
  m204          1.4043     0.5481   2.562 0.010406 *  
  m205          1.0897     0.5556   1.961 0.049833 *  
  m206          0.8919     0.5333   1.672 0.094447 .  
  m207          1.4806     0.5531   2.677 0.007427 ** 
  m208          1.8866     0.8893   2.121 0.033893 *  
  m209          1.5828     0.9061   1.747 0.080672 .  
  m2010        -2.4950     0.7642  -3.265 0.001095 ** 
  m2011         1.8637     0.5762   3.235 0.001218 ** 
  m2012         0.5435     0.5265   1.032 0.301880    
  m2013         1.2922     0.5206   2.482 0.013068 *  
  m2014         2.2217     0.7816   2.842 0.004477 ** 
  m2015         1.9133     0.5653   3.384 0.000713 ***
  m2016        -0.2065     0.5295  -0.390 0.696492    
  m2017         2.9362     0.6075   4.833 1.34e-06 ***
  m2018         0.5331     0.5220   1.021 0.307074    
  m2019        -2.2338     0.5884  -3.796 0.000147 ***
  e101          0.9528     0.2511   3.795 0.000148 ***
  e102          1.4572     0.2373   6.141 8.21e-10 ***
  e103          1.6850     0.3577   4.710 2.47e-06 ***
  e104          0.7958     0.2584   3.080 0.002068 ** 
  e105          0.8401     0.2597   3.235 0.001217 ** 
  e106          1.4359     0.3388   4.238 2.25e-05 ***
  e107          2.4428     0.4608   5.302 1.15e-07 ***
  e108          1.1231     0.3789   2.965 0.003032 ** 
  e109          0.1078     0.2377   0.453 0.650275    
  ---
  Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

  (Dispersion parameter for binomial family taken to be 1)

      Null deviance: 3872.4  on 5580  degrees of freedom
  Residual deviance: 2872.8  on 5551  degrees of freedom
  AIC: 2932.8

  Number of Fisher Scoring iterations: 6
  ```
  * лучшая модель - м20 и в10. Остальные комбинации были опробованы, но из-за незначимости в20 и контроля они были отвергнуты.
* дерево решений:
![tree](https://raw.githubusercontent.com/kategerasimenko/hsecxg_project/master/tree.png "Tree")
только три пути справа ведут к герундию, остальные к инфинитиву.

## Анализ результатов статистического анализа
### Логистическая регрессия
Рассмотрим слова и долю инфинитива в наиболее значимых категориях в модели м20+в10: <br>
m: 2 11 15 17 19 <br>
e: 1 2 3 6 7 <br>


**m2**
```
['failing', 'wanted', 'seeking', 'requiring', 'compelled', 'threatening', 'voted', 'motivated', 'forced', 'intend', 'decided', 'want', 'instructed', 'threatened', 'prefer', 'proposing', 'need', 'plans', 'destined', 'promised', 'pledged', 'Seeking', 'ordered', 'planning', 'allowed', 'contemplating', 'planned', 'pressured', 'chose', 'scheduled', 'tended', 'intending', 'expected', 'prepared', 'wanting', 'wishing', 'wished', 'intended', 'expecting', 'required', 'Want', 'advised', 'refusing', 'Refusing', 'invited', 'meant', 'tend', 'persuaded', 'needed', 'expect', 'needing', 'going', 'urged', 'agreed', 'encouraged', 'permitted', 'deciding', 'refuse', 'Intending', 'requested', 'preferring', 'tempted', 'preparing', 'wishes', 'opted', 'looking', 'refused', 'pressed', 'bound', 'pressing', 'asked', 'demanded']
```
примерно волеизъявление, доля инфинитива 0.98

**m11**
```
['avoids', 'resolves', 'decides', 'refuses', 'makes', 'desires', 'rearranges', 'helps', 'proposes', 'manages', 'purports', 'wants', 'goes', 'uses', 'works', 'determines', 'pretends', 'strives', 'serves', 'asks', 'continues', 'learns', 'seeks', 'lets', 'intends', 'transforms', 'undertakes', 'chooses', 'survives', 'tends', 'fails', 'knows', 'brings', 'recommends', 'considers', 'exists', 'aspires', 'prefers', 'likes', 'takes', 'needs', 'enjoys', 'allows', 'comes', 'finds', 'happens', 'understands']
```
глаголы 3sg, доля инфинитива 0.95

**m15**
```
['appears', 'dreaded', 'gimmicks', 'means', 'bait', 'convoluted', 'forbearing', 'seems', 'seemed', 'barbel', 'dread', 'bent', 'reappears', 'whispers', 'seeming', 'longing', 'returns', 'dull', 'acts', 'minded', 'WOAD', 'contrive', 'proves', 'turns', 'contrives', 'daring', 'promises', 'leaves', 'moves', 'blows', 'implies', 'seem', 'reverses', 'reassuring']
```
семантически разношерстно, но инфинитив - 0.95

**m17**
```
['Struggling', 'try', 'struggling', 'attempting', 'struggled', 'hopes', 'hoped', 'sought', 'AIMING', 'attempted', 'hoping', 'conspired', 'helped', 'Hoping', 'endeavored', 'striven', 'attempt', 'strive', 'failed', 'tries', 'tried', 'Aim', 'managed', 'aiming', 'attempts', 'trying', 'aim', 'hope', 'striving', 'aims', 'struggle', 'helping', 'strove', 'Try']
```
стремление, инфинитив - 0.98

**m19**
```
['restrict', 'quit', 'forbidden', 'stop', 'avoid', 'prohibit', 'justify', 'comply', 'Stop', 'destroy', 'reduce', 'prevent', 'Consent', 'remedy', 'resist', 'postpone', 'notice', 'obey', 'resolve', 'deny', 'warrant', 'justified']
```
волеизъявление, прекращение... больше герундий, но есть и инфинитив (доля 0.19)



**e1**
```
['profess', 'talk', 'admire', 'urge', 'implore', 'guess', 'consider', 'want', 'hate', 'appreciate', 'disappoint', 'complain', 'blame', 'refrain', 'like', 'prefer', 'enjoy', 'ask', 'swear', 'shew', 'miss', 'congratulate', 'read', 'insist', 'tell', 'pray', 'invite', 'criticize', 'believe', 'remember', 'wait', 'worry', 'wonder', 'mean', 'doubt', 'remind', 'praise', 'sacrifice', 'suggest', 'think', 'crave', 'hear', 'imagine', 'begrudge', 'do', 'acknowledge', 'quarrel', 'strive', 'excuse', 'feel', 'realize', 'proclaim', 'perceive', 'beg', 'love', 'say', 'forget', 'recommend', 'await', 'admit', 'know', 'choose', 'condone', 'expect', 'rely', 'owe', 'beware', 'disagree', 'contend', 'unstinting', 'warn', 'reckon', 'resent', 'argue', 'assure', 'oppose', 'astound', 'refuse', 'foresee', 'disapprove', 'ignore', 'preach', 'despise', 'watch', 'listen', 'thank', 'seem', 'mention', 'fail', 'deny', 'fear', 'regret', 'see', 'look', 'contemplate', 'wish', 'please', 'agree', 'let', 'endure', 'decide', 'overlook', 'undeserving']
```
чувства, мысли, доля инфинитива 0.88

**e2**
```
['favour', 'staff', 'result', 'practise', 'sponsor', 'award', 'offer', 'review', 'visit', 'vet', 'function', 'accord', 'reward', 'her', 'transplant', 'copy', 'near', 'sum', 're-sign', 'chair', 'answer', 'assist', 'nacab', 'challenge', 'murder', "forgettin'", 'interview', 'act', 'range', 'judge', 'power', 'lodge', 'appear', 'survey', 'farm', 'co-operate', 'test', 'value', 'institute', 'beneficially', 'concern', 'lysine', 'adequately', 'trade', 'bus', 'question', 'outcross', 'crop', 'market', 'number', 'matter', ';', 'last', 'railcoach', 'major', 'alternate', 'need', 'yield', 'mistrust', 'gross', 'land', 'place', 'separate', 'limit', 'minimise', 'school', 'estimate', 'licence', 'report', 'count', 'study', 'claim', 'close', 'barrack', 'sign', 'display', 'share', 'risk', 'tender', 'charge', "'ave", 'store', 'mind', 'state', 'reference', 'comfort', 'associate', 'tour', 'escort', 'treasure', 'be', 'care', 'subtly', 'interest', 'exercise', 'fundamentally', 'house', 'advocate', 'diet', 'attempt', 'request', 'plan', 'train', 'over-provide', 'sketch', 'order', 'machine', 'focus', 'guarantee', 're-assessing', 'force', 'encourage/reinforce', 'increase', 'work', 'appeal', 'promise', 'substitute', 'release', 'lecture', 'account', 'stock', 'age', 'step', 'legering', 'police', 'resort', 'suspect', 'bridge', 'free', 'flow', 'deal', 'budget', 'transfer', 'fulfil', 'benefit', 'note', 'sound', 'sort', 'quote', 'obscure', 'import', 'abuse', 'regard', 'aid', 'long', 'stress', 'call', 'criticise', 'show', 'suit', 'bear', 'grade', 'control', 'piece', 'part', 'name', 'support', 'breed', 'approach', 'barlaston', '’', 'discipline', 'light', 'contact', 'ferry', 'board', 'press', 'fee', 'link', 'influence', 'experiment', 'specialise', '.', 'notice', 'service', 'shop', 'direct', 'galvanise', 'master', 'object', 'subsidise', 'conflict', 'cost', 'view', 'draft', 'progress', 'lasing', 'price', 'travel', 'requite', 'date', 'balance', 'clear', 'rule', 'record', 'telephone', 'recognise', 'supply', 'exchange', 'modernise', 'open', 'worship', 'gain', 'deposit', 'aim', 'ensure', 'present', 'organise', 'entirely', 'sample', '‘', 'favourably', 'wastepaper', 'capitalise', 'base', 'signal', 'target', 'emphasise', 'list', 'complete', 'live', 'delegate', 'foxhunt', 'change', 'properly', 'advance', 're-enter', 'materialise', 'experience', 'very', 'trust', 'update', 'set', 'utilise', 'breach', "again'", 'reserve', 'appropriate', 'queue', 'demand', 'co-opt', 'figure', ',', 'lower', 'broadcast', 'permit', 'track', 'check', 'jeopardise', 'flood', 'publicise', 'form', 'campaign', 'issue', 'end', 'reason', 'reform', 'project', 'decline', 'search', 'have', 'realise', 'quarry', 'milk', 'either']
```
мусорный класс, в который попали ошибки аннотации - видимо, означают "инфинитив" (после to) - 0.92

**e3**
```
['mystify', 'thrive', 'coincide', 'imbue', 'circulate', 'sway', 'denote', 'capitalize', 'boost', 'enable', 'rejuvenate', 'incite', 'mislead', 'rediscover', 'induce', 'repress', 'forge', 'emulate', 'commemorate', 'create', 'encourage', 'celebrate', 'reorient', 'unify', 'translate', 'facilitate', 'accelerate', 'attract', 'blend', 'emphasize', 'reflect', 'incorporate', 'stimulate', 'instil', 'reinforce', 'vitalize', 'improve', 'nurture', 'impress', 'promote', 'combine', 'brighten', 'bring', 'penetrate', 'civilize', 'evoke', 'express', 'strengthen', 'resonate', 'accentuate', 'revitalize', 'represent', 'conceive', 'invent', 'provoke', 'seduce', 'foster', 'trivialize', 'uplift', 'embody', 'popularize', 'recast', 'elicit', 'duplicate', 'capture', 'divide', 'emerge', 'prosper', 'achieve', 'elevate', 'transmute', 'encapsulate', 'inspire', 'proselytize', 'engender', 'reinvigorate', 'exploit', 'entertain', 'humiliate', 'highlight', 'generate', 'enhance']
```
разношерстный класс глаголов, инфинитив 0.93

**e6**
```
['guide', 'predict', 'advise', 'inquire', 'describe', 'adapt', 'examine', 'manage', 'acquaint', 'detect', 'refer', 'quantify', 'identify', 'react', 'educate', 'gauge', 'assign', 'compare', 'retell', 'delineate', 'discover', 'explore', 'inspect', 'communicate', 'address', 'coordinate', 'reconstruct', 'confirm', 'scrutinize', 'illustrate', 'monitor', 'interrogate', 'connect', 'treat', 'prove', 'teach', 'demonstrate', 'devise', 'relate', 'respond', 'explain', 'recognize', 'understand', 'evaluate', 'prepare', 'formulate', 'diagnose', 'regulate', 'compile', 'determine', 'establish', 'classify', 'clarify', 'calculate', 'investigate', 'discuss', 'distinguish', 'interpret', 'uncover', 'gather', 'find', 'assess', 'certify', 'reveal', 'observe', 'scan', 'select', 'navigate', 'locate', 'trace', 'learn', 'correspond', 'tailor', 'consult', 'grapple', 'summarize', 'grasp', 'assert', 'speak', 'disseminate', 'define']
```
еще глаголы, доля инфинитива 0.94

**e7**
```
['extract', 'extinguish', 'remove', 'reconcile', 'stop', 'eradicate', 'lessen', 'placate', 'soothe', 'avoid', 'save', 'alleviate', 'suppress', 'wean', 'justify', 'repopulate', 'steer', 'straighten', 'combat', 'exert', 'eliminate', 'forestall', 'wrest', 'erase', 'protect', 'tackle', 'overcome', 'cope', 'counteract', 'blackmail', 'pacify', 'reduce', 'prevent', 'calm', 'regroup', 'expunge', 'disperse', 'reverse', 'prolong', 'heal', 'compensate', 'preserve', 'restore', 'conserve', 'escape', 'resist', 'subdue', 'exonerate', 'curb', 'persuade', 'appease', 'safeguard', 'defuse', 'keep', 'resolve', 'fix', 'rid', 'mediate', 'convince', 'cure', 'contain', 'counter', 'restrain', 'ameliorate', 'mitigate', 'quell', 'relieve', 'survive', 'banish', 'stem', 'recover', 'ease', 'recapture', 'shield', 'reassure', 'solve', 'hide', 'offset', 'soften', 'satisfy']
```
и еще глаголы, инфинитивов 0.98.

Таким образом:
* модель (логистическая регрессия) выделила наиболее "инфинитивные" кластеры в обоих глаголах
* только в матричном глаголе оказался "герундивный" кластер, во вложенном глаголе таких кластеров нет ни в в10, ни в в20

### Дерево решений
Дерево решений также работает на основе "инфинитивности" кластеров (для узлов можно понять, какое значение процента инфинитивов разделяет кластеры в двух ветвях), значит, всё упирается в кластеризацию - необходимо сделать так, чтобы кластеризовались глаголы, участвующие в инфинитивном и герундивном управлении.


## Обсуждение использованных квантитативных методов
Я выгрузила предсказания логистической регрессии и дерева (вероятности), подобрала порог вероятности, с которого стоит считать ответ единицей (инфинитивом) и посмотрела, каковы результаты. [Код](https://github.com/kategerasimenko/hsecxg_project/blob/master/Prediction%20report.ipynb)
* метрика - f1_score, причем оценивается по классу 0 (герундий, находится в очевидном меньшинстве)
* вероятности явно завышены моделями, поэтому порог выходит далеким от 0.5.
* результаты:
  * логистическая регрессия
  ```
  порог - 0.76
               precision    recall  f1-score   support

            0       0.48      0.45      0.47       615
            1       0.93      0.94      0.94      4966

  avg / total       0.88      0.89      0.88      5581
  ```
  * дерево решений
  ```
  порог - 0.73
               precision    recall  f1-score   support

            0       0.52      0.42      0.47       615
            1       0.93      0.95      0.94      4966

  avg / total       0.89      0.89      0.89      5581
  ```
* результаты схожи - в герундии путаница, какие-то инфинитивы попадают в герундии (ущерб precision), а какие-то герундии - в инфинитивы (ущерб recall).
* но все же лучше подбрасывания монетки с весами 0.9 / 0.1.
