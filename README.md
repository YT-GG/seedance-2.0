# Seedance 2.0 Skill OS 中文精简版

这是一个给 Codex/AI Agent 使用的 Seedance 2.0 视频提示词 skill。它不是一个需要启动的网页或后端项目，而是一套可被 Codex 读取的工作流、参考资料和子 skill，用来把你的中文视频想法整理成更稳定的 Seedance 提示词。

推荐入口：

- 快速上手：[zh-QUICKSTART.md](zh-QUICKSTART.md)
- 详细操作手册：[zh-USAGE.md](zh-USAGE.md)
- 中文指南：[docs/README.zh.md](docs/README.zh.md)
- 主 skill：[SKILL.md](SKILL.md)
- 中文词汇：[skills/seedance-vocab-zh](skills/seedance-vocab-zh/SKILL.md)
- 中文范例：[skills/seedance-examples-zh](skills/seedance-examples-zh/SKILL.md)
- 中文词汇表：[references/vocab/zh.md](references/vocab/zh.md)

## 应该在 Codex 里用，还是在 VS Code 里跑

结论很简单：

| 场景 | 推荐方式 | 原因 |
|---|---|---|
| 想让 AI 帮你写 Seedance 提示词 | 在 Codex 里安装并调用 `$seedance-20` | Codex 会自动读取 `SKILL.md` 和相关子 skill |
| 想看文档、改文档、跑检查 | 在 VS Code 里打开这个仓库 | VS Code 适合编辑和运行 Python 验证脚本 |
| 只想临时参考几条提示词 | 直接打开中文手册复制模板 | 不需要安装 |
| 想把它当成应用运行 | 不适用 | 这个仓库没有网页服务、没有前端启动命令 |

也就是说：**真正使用时放进 Codex 当 skill；维护和查看时用 VS Code。**

## 快速安装到 Codex

在本仓库目录运行：

```powershell
python scripts/install_codex_skill.py --force
```

安装完成后重启 Codex，然后在对话里使用：

```text
$seedance-20

帮我把这个想法写成 Seedance 提示词：一个雨夜咖啡馆里，女主收到消息后表情慢慢变冷。
```

如果你的 Codex 客户端使用 `@seedance-20` 这种入口，也可以按客户端提示调用。核心是让 Codex 加载本仓库的 `SKILL.md`。

## 这个项目能做什么

- 把模糊想法整理成可拍的一段视频提示词。
- 把清晰场景改写成更稳定的 Seedance Prompt。
- 处理图生视频、视频参考、音频参考、首帧/尾帧等工作流。
- 把长故事拆成多个连续 clip，并记录每段的起点、终点和续写状态。
- 根据已经生成的视频结果，写下一段续写提示词。
- 修复常见失败：镜头乱、主体漂移、产品变形、动作太多、文字乱生成等。
- 做版权/IP/真人/品牌相关请求的安全改写。
- 保留中文词汇、中文范例和中文操作说明。

## 中文精简后的结构

```text
seedance-2.0-1/
├── SKILL.md                       # Codex 读取的主 skill
├── README.md                      # 当前中文入口
├── zh-QUICKSTART.md               # 5 分钟快速上手
├── zh-USAGE.md                    # 详细中文操作手册
├── docs/README.zh.md              # 中文指南
├── skills/
│   ├── seedance-prompt/           # 生成完整提示词
│   ├── seedance-prompt-short/     # 生成短提示词
│   ├── seedance-sequence/         # 多段故事规划
│   ├── seedance-continuation/     # 基于上一段继续
│   ├── seedance-vocab-zh/         # 中文词汇和中文压缩
│   ├── seedance-examples-zh/      # 中文范例和安全改写
│   └── ...                        # 镜头、灯光、动作、音频、安全、排错等模块
├── references/
│   ├── vocab/zh.md                # 中文提示词词汇
│   ├── reference-workflow.md      # 图片/视频/音频参考角色分配
│   ├── first-last-frame-guide.md  # 首帧/尾帧控制
│   ├── sequence-project-state.md  # 多段项目状态
│   └── ...                        # 其他生产参考
└── scripts/
    ├── install_codex_skill.py     # 安装到 Codex
    ├── validate_skills.py         # skill 结构检查
    └── ...                        # 其他验证脚本
```

## 最小使用流程

1. 在 VS Code 或终端里进入项目目录。
2. 运行 `python scripts/install_codex_skill.py --force`。
3. 重启 Codex。
4. 在 Codex 对话中输入 `$seedance-20` 加你的需求。
5. Codex 输出 Seedance 提示词。
6. 把提示词复制到 Dreamina、即梦、豆包、火山引擎、Runway Seedance 路由或其他支持 Seedance 的平台。
7. 生成结果回来后，如果要继续或修复，再把结果描述、截图、尾帧或视频交回给 Codex。

## 常用请求示例

```text
$seedance-20

我有一个模糊想法：一个人在凌晨的便利店里突然意识到自己错过了什么。帮我先问几个问题，再写 Seedance 提示词。
```

```text
$seedance-20

[Image1] 是产品图。请保持瓶身、标签、logo和颜色不变，只让光线和水珠动起来，生成一个 5 秒产品广告提示词。
```

```text
$seedance-20

我要做一个 3 段连续故事：第一段地铁站等待，第二段上车相遇，第三段两人错过。请先规划 Clip 01，不要一次写完全部提示词。
```

```text
$seedance-20

上一段视频结尾是：角色站在窗边，手还停在窗帘上。请从这个真实结尾继续下一段，不要重复上一段动作。
```

## 本次精简移除了什么

为了让项目只保留中文操作路径，已移除主动可用的日语、韩语、俄语、西语和英文词汇翻译 skill，以及日/韩 README 入口。核心 Seedance 工作流、中文词汇、中文范例、序列续写、安全改写、参考素材管理和验证脚本仍保留。

历史 release note、来源数据和研究记录可能仍会提到旧版本的多语言能力，它们是版本记录，不再作为当前中文精简版的使用入口。

## 维护时常用检查

```powershell
python scripts/validate_skills.py --strict
python scripts/vocab_schema_check.py --strict
python -m unittest discover -s tests -v
```

更多步骤见 [zh-USAGE.md](zh-USAGE.md)。
