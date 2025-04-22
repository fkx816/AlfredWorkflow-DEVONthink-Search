<h1 align="center">DEVONthink Search</h1>

强大的 DEVONthink 搜索工具，适用于 DEVONthink 各个版本。

**注意：** 
- DEVONthink 2.x 请使用 7.0 之前的版本，说明文档及代码请查看[相应分支](https://github.com/mpco/AlfredWorkflow-DEVONthink-Search/tree/DEVONthink2.x)。
- 此版本已更新以支持 DEVONthink 4 和 Alfred 5。

[这里下载](https://github.com/mpco/AlfredWorkflow-DEVONthink-Search/releases)

## 用法

- 输入 `dnt + 关键词` 在 Alfred 中搜索所有数据库。搜索结果按照相关度得分排序，与 DEVONthink 中一致。
- 输入 `dnts + 关键词` 在 DEVONthink 的窗口中进行搜索。
    - 按 `回车` 在已经打开的窗口中搜索。
    - 按 `⌘Command + 回车` 在新建窗口中搜索。
- 输入 `dnd` 选择需要搜索的数据库
    - 按 `回车` 确认，接着输入 `关键词` 以进行搜索。
    - 按 `⌘Command + 回车` 列出该数据库中的所有标签（Tag）。选择某个标签，然后按下回车键，可列出所有附有该标签的文档。
    - 按 `⌥Option + 回车` 列出该数据库中的智能文件夹。
- 输入 `dnm + 标签1, 标签2, ……`，列出所有数据库中同时附有这些标签的文档。多个标签以英文逗号分隔。**注意：标签必须是准确完整的，如标签"aBcD"，不能输入"aBc"，不能输入"abcd"。**
- Workspace 相关动作:
    - 输入 `