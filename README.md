# 结构估计入门 · Structural Estimation

这是一门面向经济学本科生的实践课。我们从消费者的购买决策出发，用数据估计模型中的参数，再用估计结果回答一个问题：如果价格变了，购买率会怎么变？

有微观经济学、概率与统计的基础即可。实验会解释所用的 Python 代码，建议先了解变量、函数和数组。

## 开始第一课

[打开第 1 课 · 用二元 Logit 估计需求](lessons/01-binary-logit.ipynb)

GitHub 上可以先阅读代码和示例输出。动手时，在下载或克隆的仓库目录打开终端，使用 Python 3.11、3.12 或 3.13 创建虚拟环境。

```bash
python -m venv .venv
```

macOS 或 Linux 用户运行 `source .venv/bin/activate`。Windows PowerShell 用户运行 `.\.venv\Scripts\Activate.ps1`。如果系统用 `python3` 或 `py` 启动 Python，请相应替换创建环境命令中的 `python`。

```bash
python -m pip install -r requirements.txt
python -m jupyterlab
```

在 JupyterLab 中打开第 1 课，从第一格依次运行。实验在本地生成数据，只需在安装依赖时联网。每次做完练习后，可以重启内核并按原顺序重新运行，检查结果能否复现。

## 课程路线

| 单元 | 要解决的问题 |
| --- | --- |
| 1. 二元 Logit 与极大似然 | 观察价格与购买决策，如何从效用模型推出购买概率并估计价格系数？ |
| 2. 抽样误差与推断 | 换一批消费者，估计值会变多少？如何用标准误和置信区间表达不确定性？ |
| 3. 多项 Logit 与产品替代 | 消费者可以选多个产品，也可以不买。某个产品涨价后，需求会流向哪里？ |
| 4. 价格内生性与识别 | 厂商根据需求调整价格时，为什么很难从价格与销量的相关性推断需求？ |
| 5. 反事实与小项目 | 如何比较两个定价方案的预测结果，并说明结论依赖哪些假设？ |

第 1 单元已提供实验和练习。后续单元为课程规划。

## 延伸阅读

Kenneth E. Train（2009），*Discrete Choice Methods with Simulation*，第 2 版，第 2 章介绍离散选择的效用设定，第 3 章推导 Logit 选择概率。 [作者提供的教材](https://eml.berkeley.edu/books/choice2.html)
