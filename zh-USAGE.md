# Seedance 2.0 中文详细操作手册

这份手册讲清楚三件事：

- 这个项目到底是什么。
- 应该在 Codex 里用 skill，还是在 VS Code 里直接跑。
- 从安装、调用、生成提示词、粘贴到 Seedance、续写和排错，一步一步怎么做。

## 1. 项目定位

本仓库是一个 **Codex skill 包**。它的核心文件是 [SKILL.md](SKILL.md)，下面还有多个子 skill 和参考资料。

它不负责直接生成视频，也不自带网页界面。它负责让 Codex 像导演助理一样工作：

- 读懂你的创意目标。
- 判断该用文生视频、图生视频、视频参考、首帧/尾帧，还是多段续写。
- 把模糊描述改成清楚、短、可执行的 Seedance Prompt。
- 记录长故事每一段的状态，避免下一段重复或跑偏。
- 在生成失败后给出可操作的修复提示词。

真正生成视频的地方仍然是 Seedance 相关平台，例如 Dreamina、即梦、豆包、火山引擎 Ark、BytePlus、Runway Seedance 路由或其他供应商。

## 2. Codex 和 VS Code 怎么分工

| 工具 | 做什么 | 是否必须 |
|---|---|---|
| Codex | 调用 `$seedance-20`，读取 skill，与你对话并输出提示词 | 推荐必须 |
| VS Code | 打开仓库、阅读文档、修改文件、运行测试 | 维护时使用 |
| Seedance 平台 | 粘贴 Prompt、上传参考素材、生成视频 | 必须 |
| Python | 安装 skill、运行验证脚本 | 维护时需要 |

如果你的目标是“让 AI 帮我写视频提示词”，请用 Codex。

如果你的目标是“我想改这个项目、看文件结构、跑测试”，请用 VS Code。

如果你只是想临时学习提示词写法，可以直接打开 Markdown 文件阅读，不安装也可以。

## 3. 第一次安装

打开 PowerShell，进入项目目录：

```powershell
cd "E:\git\git projects\seedance-2.0-1"
```

安装到 Codex：

```powershell
python scripts/install_codex_skill.py --force
```

脚本会把当前仓库复制到 Codex skills 目录，默认位置通常是：

```text
%USERPROFILE%\.codex\skills\seedance-20
```

安装后重启 Codex。重启是必要的，因为 Codex 需要重新扫描本地 skills。

## 4. 验证安装是否可用

重启 Codex 后输入：

```text
$seedance-20

用一句话说明你能帮我做什么。
```

如果 Codex 能识别并围绕 Seedance 2.0 提示词回答，说明安装成功。

如果你的客户端使用 `@seedance-20` 或通过 UI 选择 skill，就按客户端的入口来。关键不是符号，而是加载名为 `seedance-20` 的 skill。

## 5. 最简单的一次完整流程

1. 你在 Codex 输入想法。
2. `$seedance-20` 帮你整理成提示词。
3. 你打开 Seedance 平台。
4. 选择生成模式。
5. 上传参考图、视频或音频。
6. 粘贴最终 Prompt。
7. 生成视频。
8. 把结果反馈给 Codex，继续优化。

示例：

```text
$seedance-20

我想生成一个 6 秒视频：清晨的厨房里，一只玻璃杯旁边放着新鲜柠檬，阳光慢慢扫过桌面，感觉干净、安静、适合饮品广告。
```

Codex 应该输出类似这样的结构：

- 简短理解。
- 如果信息缺失，问 1 到 3 个关键问题。
- 给出 Seedance 可用 Prompt。
- 提醒参考素材、比例、时长或安全风险。

## 6. 不同任务怎么问

### 6.1 模糊想法

适合你只有感觉，没有镜头设计的时候。

```text
$seedance-20

我想做一个关于“错过”的短片，但不知道怎么拍。画面不要太狗血，想要克制一点。
```

它会先帮你明确：

- 主角是谁。
- 发生在哪里。
- 这一段只拍一个什么可见动作。
- 镜头和光线怎么服务这个情绪。

### 6.2 清楚场景

适合你已经知道要拍什么，只需要改成稳定提示词。

```text
$seedance-20

场景：夜晚出租车后座，男主看着窗外雨水，手里攥着一张旧车票。镜头从侧面中近景慢慢推近，车窗反光遮住半张脸。没有音乐，只有雨声和车内低噪。
```

### 6.3 图生视频

适合产品、人物、海报、角色设定图。

```text
$seedance-20

[Image1] 是产品参考。必须保持瓶身、标签、logo、颜色、盖子形状完全不变。只增加水珠下滑、光带扫过玻璃和轻微推镜。请输出 5 秒图生视频提示词。
```

关键规则：

- 一定说明 `[Image1]` 的角色。
- 明确哪些不能变。
- 只让少数元素动。
- 不要让模型生成最终广告文案、字幕和法务文字，这些放到剪辑里加。

### 6.4 视频参考

适合你想借一个视频的运动节奏，但不想复制人物、场景或品牌。

```text
$seedance-20

[Video1] 只参考侧向跟拍节奏，不复制人物、地点、服装或品牌。[Image1] 锁定原创角色外观。请写一个雨夜站台行走的 R2V 提示词。
```

关键规则：

- 每个参考素材只给一个主角色。
- 写清楚不能从参考里继承什么。
- 视频参考经常容易“串味”，所以排除项要明确。

### 6.5 首帧/尾帧

适合你有开始图和结束图，希望模型补中间动作。

```text
$seedance-20

@图1 为首帧，@图2 为尾帧。保持同一角色、服装和房间布局，只生成两帧之间的连续动作：角色从椅子上站起，走到窗边，停在尾帧姿势。
```

关键规则：

- 首帧定义起点。
- 尾帧定义目标。
- Prompt 只写中间如何过渡。
- 不要同时要求风格大变、角色换装、场景变换。

### 6.6 多段连续故事

适合 20 秒以上、多个镜头、多个片段的故事。

```text
$seedance-20

我要做一个 3 段连续故事：
1. 地铁站，女主等车，发现对面站台有熟人。
2. 她上车，车门快关上时两人对视。
3. 车开走，两人错过。

请先做整体规划，再只输出 Clip 01 的最终 Seedance Prompt。
```

重要：不要让 skill 一次输出所有 clip 的最终 Prompt。长故事应该这样做：

1. 先规划全局。
2. 只生成 Clip 01。
3. 你拿 Clip 01 去生成视频。
4. 把 Clip 01 的真实结果交回 Codex。
5. Codex 根据真实结尾写 Clip 02。
6. 重复直到完成。

### 6.7 继续上一段

适合你已经生成了一段，想接下一段。

```text
$seedance-20

上一段实际结尾：女主站在车门内侧，右手扶着金属扶手，车门刚关闭，窗外站台灯光向后滑动。请继续 Clip 02，不要重复上车动作。
```

关键规则：

- 用真实结尾，不用原计划结尾。
- 明确上一段已经完成的动作。
- 明确下一段不能提前出现的内容。
- 如果有尾帧，最好给 Codex 看尾帧。

### 6.8 结果失败后修复

```text
$seedance-20

这次生成失败：产品 logo 变形，镜头突然绕了一圈，背景多出文字。请判断原因，并只改一个最关键变量，给我新版提示词。
```

好的修复通常不是“加更多形容词”，而是：

- 锁定主体。
- 减少动作。
- 固定镜头。
- 缩短提示词。
- 删除互相冲突的要求。
- 一次只改一个变量。

## 7. 中文提示词核心规则

写 Seedance Prompt 时，优先写这些内容：

1. 主体是谁。
2. 本段只发生一个什么可见动作。
3. 镜头怎么动，或者明确不动。
4. 光从哪里来。
5. 声音是什么。
6. 哪些参考必须保持。
7. 哪些东西不要生成。

不要堆这些空词：

- 电影感
- 高级感
- 氛围感
- 震撼
- 史诗级
- 4K/8K/超清
- 极致细节

把它们拆成可见元素：

| 空词 | 更好的写法 |
|---|---|
| 电影感 | 中近景、轻微推镜、侧逆光、浅景深、低环境声 |
| 高级感 | 干净构图、产品居中、窄条形光扫过材质、无杂物 |
| 氛围感 | 雨声、窗外冷光、室内暖灯、角色停顿 |
| 震撼运镜 | 低机位跟拍到门口急停，结尾锁住手部动作 |

## 8. 文件怎么读

| 文件 | 用途 |
|---|---|
| [SKILL.md](SKILL.md) | Codex 调用入口，不建议初学者先改 |
| [zh-QUICKSTART.md](zh-QUICKSTART.md) | 快速上手 |
| [zh-USAGE.md](zh-USAGE.md) | 当前详细手册 |
| [docs/README.zh.md](docs/README.zh.md) | 中文创作规则摘要 |
| [skills/seedance-vocab-zh/SKILL.md](skills/seedance-vocab-zh/SKILL.md) | 中文词汇和中文压缩 |
| [skills/seedance-examples-zh/SKILL.md](skills/seedance-examples-zh/SKILL.md) | 中文范例 |
| [references/vocab/zh.md](references/vocab/zh.md) | 中文词汇表 |
| [references/reference-workflow.md](references/reference-workflow.md) | 多参考素材怎么分配角色 |
| [references/first-last-frame-guide.md](references/first-last-frame-guide.md) | 首帧/尾帧 |
| [references/sequence-project-state.md](references/sequence-project-state.md) | 多段故事状态 |

## 9. 在 VS Code 里能做什么

VS Code 里不能“启动”这个 skill，因为它不是服务端应用。但你可以：

- 打开 Markdown 文档。
- 修改 `SKILL.md` 或子 skill。
- 修改中文词汇和示例。
- 运行验证脚本。
- 查看 git diff。

常用命令：

```powershell
python scripts/validate_skills.py --strict
python scripts/vocab_schema_check.py --strict
python scripts/content_audit.py --strict
python -m unittest discover -s tests -v
```

改完后重新安装到 Codex：

```powershell
python scripts/install_codex_skill.py --force
```

然后重启 Codex。

## 10. 常见问题

### 我能不能不安装，直接在 VS Code 跑？

如果你只是看文档，可以不安装。  
如果你希望 Codex 自动按这套规则帮你写提示词，就需要安装到 Codex skills 目录。

### 这个项目会调用 Seedance API 吗？

不会。它只帮你生成提示词和工作流说明。真正调用 API 或网页生成视频，需要你在对应平台完成。

### 为什么不能一次写完整长故事的所有 Prompt？

因为生成结果经常和计划结尾不完全一致。下一段应该从上一段“真实生成的结尾”继续，而不是从原计划继续。

### 为什么提示词要短？

Seedance 更容易执行具体、单一、可见的指令。过长的提示词会让主体、动作、镜头和风格互相抢权重。

### 能不能继续保留其他语言翻译？

当前仓库已经精简为中文使用路径。旧版本的多语言内容不再作为主动 skill 入口保留。

## 11. 推荐工作习惯

- 每段视频只让一个动作成为主任务。
- 有参考素材时，先写素材角色，再写动作。
- 产品和人物要明确哪些不能变。
- 字幕、广告语、法务文案尽量后期添加，不交给视频模型生成。
- 长故事先做项目状态，再逐段生成。
- 修复失败时一次只改一个关键变量。

这套 skill 最适合做“导演式提示词”：不是堆参数，而是把情绪翻译成镜头、动作、光线和声音。
