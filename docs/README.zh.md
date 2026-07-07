# Seedance 2.0 中文指南

这是当前中文精简版的文档入口。完整步骤见根目录的 [zh-USAGE.md](../zh-USAGE.md)，快速版见 [zh-QUICKSTART.md](../zh-QUICKSTART.md)。

## 使用方式

本项目推荐安装到 Codex 后作为 `$seedance-20` skill 使用。VS Code 主要用于查看、编辑和运行验证脚本，不需要启动网页服务。

## 中文提示词规则

- 参考标签保持原样：`[Image1]`、`[Video1]`、`[Audio1]`、`@图1`、`@视频1` 不要翻译或改名。
- 先写参考素材的角色，再写主体动作、镜头、光线、声音和限制。
- 少用“电影感”“高级感”“氛围感”等空词，把它们拆成景别、运镜、光源、材质、色彩、空气和声音。
- 不让模型生成最终字幕、广告语、法务文案或水印，这些应在后期添加。
- 长故事先生成 Clip 01，再根据真实结尾写 Clip 02。

## 常用入口

| 你要做什么 | 先看 |
|---|---|
| 写中文提示词 | `skills/seedance-vocab-zh/SKILL.md` 和 `references/vocab/zh.md` |
| 看中文范例 | `skills/seedance-examples-zh/SKILL.md` |
| 做连续剧情 | `skills/seedance-sequence/SKILL.md` |
| 接着上一段继续 | `skills/seedance-continuation/SKILL.md` |
| 使用参考图片/视频/音频 | `references/reference-workflow.md` |
| 控制首帧/尾帧 | `references/first-last-frame-guide.md` |

## 中文模板

```text
项目目标：[最终想让观众看到或感受到什么]
参考素材：[Image1] 锁定主体；[Video1] 仅参考运镜；[Audio1] 仅参考节奏
本段只拍：[一个可见动作]
镜头：[固定/推近/侧移/跟拍，只选一个主运动]
光线：[真实光源、方向、变化]
声音：[环境声/动作声/台词/无音乐]
限制：[不改主体、不新增文字、不生成水印、不提前出现后续剧情]
```
