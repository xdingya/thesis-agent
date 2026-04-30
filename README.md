# Thesis Agent – 毕业论文多 Agent 辅助系统

## 项目背景
个人项目，用于完成本科/硕士毕业论文 。  
核心痛点：文献调研、代码实现、论文写作之间的反复切换成本高。  
通过多 Agent 协作实现“从研究问题到论文章节”的半自动化。

## Agent 架构（当前设计）
- **Planner Agent**：任务拆解（文献综述 → 实验 → 代码 → 分析 → 写作）
- **Researcher Agent**：调用学术 API 检索论文、提取关键方法
- **Coder Agent**：生成实验代码（Python/PyTorch）
- **Writer Agent**：自动生成论文初稿（摘要、方法、实验、结果分析）
- **Reviewer Agent**：逻辑检查、引用补全、学术语气修正

## 为什么需要 MiMo Token Plan
- 毕业论文涉及大量长链推理 20+ 步推理链
- 预计未来 2 个月剩余 Token 需求：3 - 5 亿 Token
- 日均吞吐量不高，但需要长期稳定额度支持

## 后续计划
- 完成毕业论文后，开源全部 Agent 代码
- 支持更多 API 后端（包括 MiMo）
