# AI-OS Brain Migration Map

版本：
AI-OS Brain Consolidation V1.0

目标：

将现有多个 Brain 相关模块收敛为唯一 AI Brain 核心。

原则：

1. 最大化保留已有代码
2. 不新增功能
3. 不改变系统能力边界
4. 消除重复实现
5. 保持六大核心架构一致


---

# 一、最终目标结构


core/

    brain/

        brain.py
        brain_controller.py
        brain_state.py

        intent_engine.py
        intent_rules.py

        reasoning_engine.py
        decision_engine.py

        model_router.py
        model_adapter.py
        llm_gateway.py

        memory_adapter.py

        request.py
        response.py
        interface.py


        providers/

            base_provider.py
            chatgpt_provider.py
            cloud_provider.py
            real_provider.py

            connectors/


        context/

            context_interpreter.py
            language_parser.py
            goal_extractor.py



---

# 二、文件迁移映射


## 1. 保留核心 Brain


原路径：

core/brain/


保留：

brain.py

brain_controller.py

brain_state.py

intent_engine.py

intent_rules.py

interface.py

memory_adapter.py

model_adapter.py

model_router.py

request.py

response.py


处理：

保持不变。



---

# 2. Brain Intelligence 合并


原：

core/brain/intelligence/brain_intelligence.py


目标：

core/brain/reasoning_engine.py


原因：

该模块承担：

Reasoning Engine

属于 AI Brain 核心能力。



---

# 3. Brain Enhancement 合并


原：

core/brain_enhancement/


文件：

brain_adapter.py

context_interpreter.py

goal_extractor.py

language_parser.py



处理：

brain_adapter.py

合并进入 brain.py 调用链。


context_interpreter.py

language_parser.py

goal_extractor.py


迁移：

core/brain/context/


作用：

用户理解上下文增强。



---

# 4. AI Gateway 合并


原：

ai_gateway/


llm_gateway.py

router.py


处理：

llm_gateway.py

合并：

core/brain/llm_gateway.py


router.py

合并：

core/brain/model_router.py



providers:


保留：

base_provider.py

chatgpt_provider.py

cloud_provider.py

real_provider.py



统一：

core/brain/providers/



---

# 5. ChatGPT Bridge 收敛


原：

chatgpt_bridge/


保留能力：

connector.py

real_connector.py

mock_connector.py

permission.py

protocol.py

session.py


迁移：

core/brain/providers/connectors/


作用：

模型连接适配层。



以下保留待评估：

config.py

request.py

response.py

task_adapter.py

full_workflow.py



原因：

可能与 Brain Runtime 重复。



---

# 三、删除原则


禁止直接删除代码。


所有重复代码：

先迁移

再验证

最后清理。



---

# 四、验证标准


Brain 收敛完成后必须满足：

用户输入

↓

Brain

↓

Intent理解

↓

Reasoning

↓

Model选择

↓

LLM调用

↓

返回结果


并保持：

Memory接口

Planner接口

Agent接口

正常连接。



---

# 五、当前阶段禁止事项


禁止：

新增模型

新增Agent

新增智能层

新增V版本路线


当前唯一目标：

完成 AI Brain 收敛。


