# 结构估计与产业组织 · 实验班选修课

课程从一家商店的随机报价实验出发，转向研究者只看得到各市场价格、销量和产品特征的情形。学生需要从份额反推出产品效用，说明哪些变动可以识别需求，再估计产品间的替代关系。学期最后用同一套方法分析多产品企业的定价和兼并反事实。

**建议安排为 14 周，每周 3 学时，课外每周 4–6 小时。** 面向经济学本科实验班。先修中级微观经济学、概率统计、计量经济学和线性代数。学生应能独立用 Python 读写数组、写函数和调用数值优化器。课堂实验用模拟数据，可核对真值。第 13、14 周用于项目检查和答辩。

## 学习目标

- 从随机效用模型推导选择概率、似然和份额反演，说明微观选择数据与市场份额数据各自提供什么信息。
- 写出工具变量的排除限制、矩条件和秩条件。独立实现 2SLS 与两步 GMM，判断工具无效、工具弱和模型设定有误对结论的影响。
- 推导 Nested Logit 的组内份额回归，用两个独立的外生变动识别价格系数与组内相关参数。比较相同基准份额下的替代预测。
- 实现 BLP 随机系数需求的数值积分、逐市场份额反演和外层非线性 GMM。用目标函数、矩的响应和积分精度判断异质性参数能否稳定估计。
- 根据需求导数和所有权矩阵计算多产品企业加价。对比价格固定反事实与企业重新定价的反事实，报告适用条件和可复现的数值检查。

## 教学进度

| 周 | 课堂主题 | 作业或检查 |
| --- | --- | --- |
| 1 | 消费者效用、二元 Logit、极大似然 | 从效用差推出购买概率，运行[第 1 课](lessons/01-binary-logit.ipynb)，写出得分。 |
| 2 | 信息矩阵、抽样分布、置信区间 | 用不同样本量检查标准误和覆盖率，运行[第 2 课](lessons/02-sampling-uncertainty.ipynb)。 |
| 3 | 多项 Logit、选择集合、IIA 与转移比例 | 用[第 3 课](lessons/03-multinomial-logit.ipynb)计算自价格与交叉价格的影响，比较固定其他价格的两种报价。 |
| 4 | 内生定价、识别与反事实 | 对照[第 4 课](lessons/04-price-endogeneity.ipynb)的两种报价机制。用[第 5 课](lessons/05-pricing-counterfactual-project.ipynb)完成一份短备忘录，进入学期项目之前练习报告假设和抽样不确定性。 |
| 5 | 从微观选择到产品—市场数据，Berry 的 Logit 反演，2SLS | [第 6 课](lessons/06-aggregate-logit-iv-gmm.ipynb)构造外部份额、估计 OLS 和 IV，解释差异。布置作业一。 |
| 6 | 过度识别、GMM 权重与市场聚类 | 推导线性 GMM、用第一步残差构造市场层矩的协方差、检验矩条件。修改工具强度和有效性。 |
| 7 | Nested Logit 的组内选择、包含值、解析反演 | [第 7 课](lessons/07-nested-logit.ipynb)推导嵌套份额与份额反演，分析两个内生解释变量。布置作业二。 |
| 8 | 组内和跨组替代、Nested Logit 识别诊断，期中考核 | 比较与普通 Logit 对齐基准份额后的转移比例。期中限时完成推导和识别题。 |
| 9 | 随机系数 Logit，给定参数时的数值积分 | [第 8 课](lessons/08-blp-demand.ipynb)先写条件选择概率，再对偏好分布积分。 |
| 10 | BLP 内层份额反演和数值容差 | 检验同一观测份额可由不同随机系数组合拟合，比较积分节点和停止条件。布置作业三。 |
| 11 | BLP 外层 GMM 与局部识别 | 集中掉线性系数，绘制非线性参数的目标函数剖面，改变工具集合与初值。 |
| 12 | 弹性、所有权矩阵、加价和兼并模拟 | [第 9 课](lessons/09-blp-pricing-counterfactual.ipynb)核对解析需求导数，求价格一阶条件并检查厂商的局部最优性。布置作业四。 |
| 13 | 项目复现和反事实诊断 | 交换干净环境复现，报告哪些结论受模型、工具集合或定价行为影响。 |
| 14 | 项目答辩 | 提交模型比较、反事实和复现材料，现场解释一条识别假设和一项敏感性结果。 |

## 考核与项目

建议四次作业各占 10%，期中考核占 20%，学期项目占 40%。作业包含纸笔推导、独立编程和诊断说明。提交课堂 Notebook 的原样输出只能证明环境可用，需要按题目改变数据生成过程、估计器或反事实。实际任务和判分要求见[作业与学期项目](ASSIGNMENTS.md)。

期末以同一份模拟产品—市场数据比较聚合 Logit、Nested Logit 和 BLP。先估计可比较的价格弹性和转移比例，再做一项改变所有权或成本的反事实。供给分析须说明厂商行为、成本设定、初始价格和求解结果。项目评分中，识别与诊断占 30%，推导与估计占 30%，反事实判断占 25%，可复现性占 15%。[作业与学期项目](ASSIGNMENTS.md)

平时用模拟真值查错。项目对每种估计使用公开给研究者的变量，真值单独作为诊断基准。报告解释方法在哪些数据和假设下成立，允许有依据地报告弱识别、边界解或求解失败。

## 读物

先用[进阶方法讲义](METHODS.md)统一记号，再读原文对应部分。

- Berry（1994），*Estimating Discrete-Choice Models of Product Differentiation*。重点读份额反演、价格内生性与 Nested Logit。 [论文](https://www.its.caltech.edu/~mshum/gradio/papers/Berry1994.pdf)
- Hansen（1982），*Large Sample Properties of Generalized Method of Moments Estimators*。重点读总体矩与样本目标函数。 [作者提供的论文](https://larspeterhansen.org/wp-content/uploads/2016/11/Hansen-econometrica-GMM.pdf)
- Berry、Levinsohn 与 Pakes（1995），*Automobile Prices in Market Equilibrium*。先读需求、供给一阶条件及份额反演，再理解估计中不同矩的作用。 [论文](https://pages.stern.nyu.edu/~wgreene/Econometrics/BLP.pdf)
- Train（2009），*Discrete Choice Methods with Simulation*，第 2 版。配合第 3、4、6、13 章复习 Logit、广义极值、混合 Logit 和内生性。 [作者提供的教材](https://eml.berkeley.edu/books/choice2.html)
