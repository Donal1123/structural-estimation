# 结构估计与产业组织 · Structural Estimation

这是一门面向经济学本科实验班的选修课。从消费者的购买决策出发，学习如何用产品—市场数据识别需求、估计产品间的替代关系，并分析企业重新定价后的反事实。

建议修过中级微观经济学、概率统计、计量经济学和线性代数，并能独立使用 Python 完成基本的数值计算。前五课用于建立基础，进阶实验要求自己写推导、改估计器和解释识别诊断。

## 课程与实验

[14 周课程安排](COURSE.md) · [进阶方法讲义](METHODS.md) · [作业与学期项目](ASSIGNMENTS.md)

| 单元 | 实验 |
| --- | --- |
| 1. 二元 Logit 与极大似然 | [用二元 Logit 估计需求](lessons/01-binary-logit.ipynb) |
| 2. 抽样误差与推断 | [抽样误差、标准误和置信区间](lessons/02-sampling-uncertainty.ipynb) |
| 3. 多项 Logit 与替代 | [两件商品与不购买选项](lessons/03-multinomial-logit.ipynb) |
| 4. 价格内生性与识别 | [随机报价与内生报价](lessons/04-price-endogeneity.ipynb) |
| 5. 定价反事实与入门项目 | [比较两种定价方案](lessons/05-pricing-counterfactual-project.ipynb) |
| 6. 市场份额反演、IV 与 GMM | [聚合 Logit 与两步 GMM](lessons/06-aggregate-logit-iv-gmm.ipynb) |
| 7. Nested Logit | [份额反演、识别与组内替代](lessons/07-nested-logit.ipynb) |
| 8. BLP 随机系数需求 | [份额反演与非线性 GMM](lessons/08-blp-demand.ipynb) |
| 9. 多产品定价与兼并反事实 | [需求弹性、加价与价格求解](lessons/09-blp-pricing-counterfactual.ipynb) |

## 运行 Notebook

GitHub 上可以先阅读代码和示例输出。动手时，在下载或克隆的仓库目录打开终端，使用 Python 3.11、3.12 或 3.13 创建虚拟环境。

```bash
python -m venv .venv
```

macOS 或 Linux 用户运行 `source .venv/bin/activate`。Windows PowerShell 用户运行 `.\.venv\Scripts\Activate.ps1`。如果系统用 `python3` 或 `py` 启动 Python，请相应替换创建环境命令中的 `python`。

```bash
python -m pip install -r requirements.txt
python -m jupyterlab
```

请下载或克隆完整仓库，从仓库目录启动 JupyterLab。各 Notebook 都可以从第一格运行，后两课会调用仓库内的需求函数。数据由实验在本地生成。做完练习后，重启内核并依次运行，检查结果能否复现。

## 延伸阅读

Berry（1994）、Hansen（1982）、Berry、Levinsohn 与 Pakes（1995）和 Train（2009）的阅读章节见[课程安排](COURSE.md#读物)。
