"""
毕业论文多 Agent 协作系统 - 伪代码演示
仅用于展示架构逻辑，不包含真实 API 调用。
"""

class BaseAgent:
    """所有 Agent 的基类"""
    def __init__(self, name):
        self.name = name

    def process(self, input_data):
        """子类需要实现的具体处理逻辑"""
        raise NotImplementedError


class PlannerAgent(BaseAgent):
    """将研究问题拆解为多个阶段"""
    def process(self, research_question):
        print(f"[Planner] 拆解问题: {research_question}")
        # 长链推理的第一步：生成任务列表
        tasks = [
            "literature_review",
            "experiment_design",
            "code_implementation",
            "result_analysis",
            "paper_writing"
        ]
        print(f"[Planner] 生成任务列表: {tasks}")
        return tasks


class ResearcherAgent(BaseAgent):
    """检索论文、提取核心信息"""
    def process(self, task):
        if task != "literature_review":
            return None
        print("[Researcher] 正在检索相关论文...")
        # 模拟从 arXiv 等获取论文摘要
        papers = [
            {"title": "Attention Is All You Need", "key_method": "Transformer"},
            {"title": "BERT: Pre-training of Deep Bidirectional Transformers", "key_method": "Masked LM"}
        ]
        summaries = [f"{p['title']} - 核心方法: {p['key_method']}" for p in papers]
        print(f"[Researcher] 提取到 {len(summaries)} 篇论文摘要")
        return summaries


class CoderAgent(BaseAgent):
    """根据实验设计生成代码"""
    def process(self, experiment_spec):
        print(f"[Coder] 收到实验规格: {experiment_spec}")
        # 模拟生成 Python 代码
        code = f"""
# 自动生成的实验代码
import torch
import torch.nn as nn

class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        # 模型定义
        self.fc = nn.Linear(768, 2)

    def forward(self, x):
        return self.fc(x)

# 训练循环
def train(model, dataloader):
    optimizer = torch.optim.Adam(model.parameters())
    for epoch in range(3):
        for batch in dataloader:
            # 前向传播、反向传播
            pass
    return model
"""
        print("[Coder] 代码生成完毕")
        return code


class WriterAgent(BaseAgent):
    """根据分析结果撰写论文章节"""
    def process(self, analysis_result):
        print(f"[Writer] 接收到分析结果: {analysis_result[:100]}...")
        # 生成章节初稿
        draft = f"""
# 实验部分

根据上述分析，{analysis_result[:200]}。这表明我们的方法在主要指标上优于基线。
详细数据见表 1。
"""
        print("[Writer] 论文章节初稿生成完毕")
        return draft


class ReviewerAgent(BaseAgent):
    """检查逻辑、补充引用、修正语气"""
    def process(self, chapter_draft):
        print("[Reviewer] 正在检查逻辑一致性...")
        # 补全引用
        revised = chapter_draft + "\n\n参考文献：\n[1] Vaswani et al., 2017\n"
        print("[Reviewer] 已补充引用，修正结束")
        return revised


def main():
    """主流程：多 Agent 协作的长链推理"""
    # 初始研究问题
    research_question = "如何提高小样本场景下的文本分类准确率？"

    # 1. Planner 拆解任务
    planner = PlannerAgent("Planner")
    tasks = planner.process(research_question)

    # 2. 执行每个任务（简化的顺序执行）
    researcher = ResearcherAgent("Researcher")
    coder = CoderAgent("Coder")
    writer = WriterAgent("Writer")
    reviewer = ReviewerAgent("Reviewer")

    # 模拟数据传递
    literature_summaries = None
    generated_code = None
    analysis_result = None
    chapter_draft = None

    for task in tasks:
        if task == "literature_review":
            literature_summaries = researcher.process(task)
        elif task == "code_implementation":
            # 假设实验设计来自之前的分析
            generated_code = coder.process("使用 Transformer 进行文本分类")
        elif task == "result_analysis":
            # 模拟分析结果
            analysis_result = "模型在测试集上准确率达到 92.3%，优于基线 5.2%"
        elif task == "paper_writing":
            if analysis_result:
                chapter_draft = writer.process(analysis_result)
            else:
                print("[Warning] 缺少分析结果，无法撰写")
        elif task == "experiment_design":
            pass  # 可扩展

    # 3. 最后审阅
    if chapter_draft:
        final_chapter = reviewer.process(chapter_draft)
        print("\n=== 最终论文章节 ===\n", final_chapter)
    else:
        print("论文撰写未完成，缺少必要输入")

    print("\n[System] 多 Agent 协作流程结束")


if __name__ == "__main__":
    main()
