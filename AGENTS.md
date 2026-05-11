# Codex 项目说明

## 语言规则

你和用户交流时，默认使用中文。

解释项目、代码、报错、测试结果、修改计划时，必须使用中文。

专业术语可以保留英文，但要给中文解释，例如：

- function：函数
- pytest：Python 测试框架
- IoU：交并比
- precision：精确率
- recall：召回率
- false positive：误检
- false negative：漏检

代码里的函数名、变量名、文件名、命令、Git commit message 可以使用英文。

不要输出大段纯英文，除非用户明确要求。

## 项目目的

这是一个用于学习 Codex CLI 的安全测试项目。

这个项目用于练习：

- 读取代码
- 小步修改代码
- 运行测试
- 根据测试失败 debug
- 查看 git diff
- 回滚错误修改
- 遵守项目规则

## 安全规则

不要修改本项目目录之外的文件。

不要删除文件，除非用户明确要求。

修改代码前，必须先用中文说明：

1. 准备修改哪个文件
2. 为什么要修改
3. 修改后如何验证
4. 是否会影响已有功能

优先做最小修改。

不要一次性重写整个项目。

## 编码规则

使用 Python 3。

函数要短小、清晰、容易测试。

新增功能时，要尽量补充 pytest 测试。

代码中的函数名和变量名使用英文。

如果逻辑不直观，可以添加中文注释。

## 当前项目主题

本项目实现基础目标检测指标：

- IoU：Intersection over Union，交并比
- TP：True Positive，正确检测
- FP：False Positive，误检
- FN：False Negative，漏检
- precision：精确率
- recall：召回率

当前已有功能：

- box_area(box)：计算检测框面积
- iou(box_a, box_b)：计算两个检测框的 IoU
- precision(tp, fp)：计算精确率
- recall(tp, fn)：计算召回率

## 工作流程

当用户让你修改代码时，按这个流程：

1. 先读取相关文件
2. 用中文给出修改计划
3. 等用户确认
4. 再做最小修改
5. 修改后说明改了哪些文件
6. 建议用户运行测试命令
7. 根据测试结果继续 debug

默认测试命令：

python -m pytest -q

默认检查修改命令：

git diff
git status --short

## 回答风格

回答要直接、结构清楚。

优先格式：

1. 结论
2. 依据
3. 下一步操作
