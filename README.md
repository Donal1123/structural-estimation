# 结构估计入门 · Structural Estimation

这是一门面向经济学本科生的实践课。我们从消费者的购买决策出发，用数据估计模型中的参数，再用估计结果回答一个问题：如果价格变了，购买率会怎么变？

有微观经济学、概率与统计的基础即可。实验会解释所用的 Python 代码，建议先了解变量、函数和数组。

## 课程与实验

[查看完整课程设计](COURSE.md)，包括五个单元的学习目标、课堂实验和结课项目。

| 单元 | 实验 |
| --- | --- |
| 1. 二元 Logit 与极大似然 | [用二元 Logit 估计需求](lessons/01-binary-logit.ipynb) |
| 2. 抽样误差与推断 | [抽样误差、标准误和置信区间](lessons/02-sampling-uncertainty.ipynb) |
| 3. 多项 Logit 与替代 | [两件商品与不购买选项](lessons/03-multinomial-logit.ipynb) |
| 4. 价格内生性与识别 | 计划中 |
| 5. 定价反事实与结课项目 | 计划中 |

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

在 JupyterLab 中按课程顺序打开 Notebook，每份都可以从第一格独立运行。实验在本地生成数据，只需在安装依赖时联网。做完练习后，可以重启内核并按原顺序重新运行，检查结果能否复现。

## 延伸阅读

Kenneth E. Train（2009），*Discrete Choice Methods with Simulation*，第 2 版，第 2 章介绍离散选择的效用设定，第 3 章推导 Logit 选择概率。 [作者提供的教材](https://eml.berkeley.edu/books/choice2.html)
