# 结构估计与产业组织 · 实验班选修课

课程从一家商店的随机报价实验出发，转向研究者只看得到各市场价格、销量和产品特征的情形。学生需要从份额反推出产品效用，说明哪些变动可以识别需求，再估计产品间的替代关系。学期最后用同一套方法分析多产品企业的定价和兼并反事实。

**建议安排为 14 周，每周 3 学时，另预留 4–6 小时自学。** 面向经济学本科实验班。建议先学中级微观经济学、概率统计、计量经济学和线性代数，并能用 Python 读写数组、写函数和调用数值优化器。课堂实验用模拟数据，可用真值核对模型和估计。

## 学习目标

- 从随机效用模型推导选择概率、似然和份额反演，说明微观选择数据与市场份额数据各自提供什么信息。
- 写出工具变量的排除限制、矩条件和秩条件。独立实现 2SLS 与两步 GMM，判断工具无效、工具弱和模型设定有误对结论的影响。
- 推导 Nested Logit 的组内份额回归，用两个独立的外生变动识别价格系数与组内相关参数。比较相同基准份额下的替代预测。
- 实现 BLP 随机系数需求的数值积分、逐市场份额反演和外层非线性 GMM。用目标函数、矩的响应和积分精度判断异质性参数能否稳定估计。
- 根据需求导数和所有权矩阵计算多产品企业加价。对比价格固定反事实与企业重新定价的反事实，报告适用条件和可复现的数值检查。

## 教学进度

| 周 | 知识与方法 | 建议自学时间 |
| --- | --- | --- |
| 1 | [二元 Logit 与极大似然](lessons/01-binary-logit.ipynb)。从效用差推出购买概率，写出对数似然和得分函数。 | 4 小时 |
| 2 | [信息矩阵、抽样分布与置信区间](lessons/02-sampling-uncertainty.ipynb)。用重复模拟理解标准误、覆盖率与样本量。 | 4 小时 |
| 3 | [多项 Logit 与产品替代](lessons/03-multinomial-logit.ipynb)。学习外部选项、IIA、自价格与交叉价格效应。 | 4 小时 |
| 4 | [价格内生性](lessons/04-price-endogeneity.ipynb)与[定价反事实](lessons/05-pricing-counterfactual-project.ipynb)。比较两种报价机制，理解抽样不确定性与情景假设。 | 4–5 小时 |
| 5 | [聚合 Logit 反演与 IV](lessons/06-aggregate-logit-iv-gmm.ipynb)。构造外部份额，对照 OLS 与 2SLS，区分排除限制和秩条件。 | 4–5 小时 |
| 6 | 过度识别、两步 GMM 与市场聚类。用第一步残差构造权重，区分工具弱与工具无效。 | 5–6 小时 |
| 7 | [Nested Logit](lessons/07-nested-logit.ipynb)的组内选择、包含值与解析反演。理解价格与组内份额的联合识别。 | 4–5 小时 |
| 8 | 组内与跨组替代。对齐普通 Logit 与 Nested Logit 的基准份额，比较转移比例。 | 4–5 小时 |
| 9 | [BLP 随机系数需求](lessons/08-blp-demand.ipynb)。从给定类型的选择概率出发，对偏好分布积分。 | 4–5 小时 |
| 10 | BLP 内层份额反演。比较积分节点和停止条件，理解不同随机系数怎样拟合同一观测份额。 | 5–6 小时 |
| 11 | BLP 外层 GMM 与局部识别。集中掉线性系数，读目标函数剖面，比较不同工具集合。 | 5–6 小时 |
| 12 | [需求弹性、加价与多产品定价](lessons/09-blp-pricing-counterfactual.ipynb)。用所有权矩阵求价格一阶条件，核对厂商的局部最优性。 | 5–6 小时 |
| 13 | [综合案例](ASSIGNMENTS.md#综合案例)。在同一组模拟市场中比较聚合 Logit、Nested Logit 和 BLP 的识别与替代预测。 | 5–6 小时 |
| 14 | 兼并与成本反事实。比较价格固定和重新定价的预测，分析结论如何随需求模型、成本或定价假设而变。 | 4–6 小时 |

## 自学材料

按主题选读推导、编程练习和综合案例。各模块的用时包含在上表的自学时间内。 [进阶自学与建议用时](ASSIGNMENTS.md)

## 读物

先用[进阶方法讲义](METHODS.md)统一记号，再读原文对应部分。

- Berry（1994），*Estimating Discrete-Choice Models of Product Differentiation*。重点读份额反演、价格内生性与 Nested Logit。 [论文](https://www.its.caltech.edu/~mshum/gradio/papers/Berry1994.pdf)
- Hansen（1982），*Large Sample Properties of Generalized Method of Moments Estimators*。重点读总体矩与样本目标函数。 [作者提供的论文](https://larspeterhansen.org/wp-content/uploads/2016/11/Hansen-econometrica-GMM.pdf)
- Berry、Levinsohn 与 Pakes（1995），*Automobile Prices in Market Equilibrium*。先读需求、供给一阶条件及份额反演，再理解估计中不同矩的作用。 [论文](https://pages.stern.nyu.edu/~wgreene/Econometrics/BLP.pdf)
- Train（2009），*Discrete Choice Methods with Simulation*，第 2 版。配合第 3、4、6、13 章复习 Logit、广义极值、混合 Logit 和内生性。 [作者提供的教材](https://eml.berkeley.edu/books/choice2.html)
