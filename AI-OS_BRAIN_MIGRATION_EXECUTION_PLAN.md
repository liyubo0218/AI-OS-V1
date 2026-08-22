# AI-OS Brain Migration Execution Plan V1.6


## 目标

将现有多个 Brain 相关实现收敛为唯一 AI Brain 架构。

目标：

保留已有能力。

减少重复。

保持系统稳定。


---

# 当前状态

已有：

core/brain

ai_gateway

chatgpt_bridge

core/brain_enhancement


当前代码：

约1194行


---

# 迁移原则


1. 不重写核心逻辑

2. 优先移动和复用

3. 保留旧接口兼容

4. 迁移完成前不删除旧文件

5. 每一步必须可回退


---

# Phase 1
## 建立最终目录


创建：

core/brain/context/


来源：

core/brain_enhancement


迁移：

- language_parser.py
- context_interpreter.py
- goal_extractor.py
- brain_adapter.py


---

创建：

core/brain/providers/chatgpt/


来源：

chatgpt_bridge


迁移：

- connector.py
- protocol.py
- session.py
- request.py
- response.py


---

# Phase 2
## Provider统一


来源：

ai_gateway/providers


合并：

- base_provider
- cloud_provider
- mock_provider
- chatgpt_provider


目标：

统一进入：

core/brain/providers/


---

# Phase 3
## Gateway收敛


旧：

ai_gateway


目标：

成为兼容入口。


最终：

core/brain/llm_gateway.py

负责：

- Provider调用
- 模型请求
- 响应处理


---

# Phase 4
## Import迁移


逐步替换：

ai_gateway.*

↓

core.brain.*


chatgpt_bridge.*

↓

core.brain.providers.chatgpt.*


core.brain_enhancement.*

↓

core.brain.context.*


---

# Phase 5
## 验证


检查：

- Brain启动
- Provider调用
- ChatGPT连接
- 测试通过


---

# Phase 6
## 清理


只有满足：

1. 无生产引用

2. 测试通过

3. Git可回退


才删除旧目录。


---

# 最终目标


Brain:

25-30个Python文件

约1000行代码


保持：

理解用户

模型调度

LLM连接

上下文理解

Memory接口


禁止：

新增第二套Brain

新增第二套Gateway

新增第二套Provider

