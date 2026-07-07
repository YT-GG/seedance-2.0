# Seedance 2.0 中文快速上手

> 版本：6.6.0 中文精简版
> 用途：把本仓库作为 Codex skill 使用，生成和修复 Seedance 2.0 视频提示词。

## 先回答最关键的问题

这个项目**主要是在 Codex 里当 skill 用**，不是在 VS Code 里启动运行的应用。

- Codex：负责读取 skill，帮你写提示词、规划分镜、续写下一段、排错。
- VS Code：负责打开仓库、查看文档、编辑文件、运行验证脚本。
- Seedance 平台：负责真正生成视频。Codex 输出提示词后，你再粘贴到 Dreamina、即梦、豆包、火山引擎、Runway Seedance 路由等平台。

## 1. 安装到 Codex

在项目根目录运行：

```powershell
python scripts/install_codex_skill.py --force
```

安装完成后重启 Codex。

## 2. 在 Codex 里调用

```text
$seedance-20

帮我把这个想法写成 Seedance 提示词：雨夜咖啡馆里，女主收到一条消息，表情从期待变成失望。
```

如果你的客户端使用 `@seedance-20`，按客户端提示调用即可。

## 3. 得到提示词后做什么

1. 打开你实际使用的 Seedance 平台。
2. 选择对应模式：文生视频、图生视频、视频参考、首帧/尾帧等。
3. 上传需要的参考素材。
4. 把 Codex 输出的最终 Prompt 粘贴进去。
5. 生成视频。
6. 如果结果不理想，把视频结果、截图、尾帧或文字描述交回 Codex，让 `$seedance-20` 帮你修复。

## 4. 常见用法

### 模糊想法

```text
$seedance-20

我想做一个有孤独感的短片：一个人在深夜便利店里，好像突然想起了很重要的事。请先帮我问几个问题，再生成提示词。
```

### 已经知道场景

```text
$seedance-20

场景：出租车后座，男主看着窗外雨水，手里攥着一张旧车票。镜头要克制，不要煽情。请写成 Seedance 提示词。
```

### 有产品图

```text
$seedance-20

[Image1] 是产品参考。保持瓶身、标签、logo、颜色和形状完全不变，只让水珠、光线和背景空气动起来，做 5 秒广告片。
```

### 多段故事

```text
$seedance-20

我要做一个 3 段连续故事：地铁站等待、车厢相遇、两人错过。请先规划整体，再只输出 Clip 01 的提示词。
```

### 继续上一段

```text
$seedance-20

上一段结尾实际画面是：角色站在窗边，右手还停在窗帘上，外面下雨。请从这个真实结尾继续下一段，不要重复上一段动作。
```

## 5. 最小检查命令

维护项目时可以在 VS Code 终端运行：

```powershell
python scripts/validate_skills.py --strict
python scripts/vocab_schema_check.py --strict
python -m unittest discover -s tests -v
```

完整说明见 [zh-USAGE.md](zh-USAGE.md)。
