# Zira Fonts

基于 [Iosevka](https://github.com/be5invis/Iosevka) 的自定义构建计划（`private-build-plans.toml`）生成 Zira 系列字体：**Zira Mono**、**Zira Sans**、**Zira Serif**。

## 构建流程

推送到 `main` 分支（且改动涉及 `private-build-plans.toml` 或 `.github/workflows/**`），或在 Actions 页面手动触发 **Build Zira Fonts** workflow，GitHub Actions 会自动：

1. 克隆 Iosevka 源码（默认 tag `v34.8.0`，手动触发时可用 `iosevka_ref` 输入覆盖）；
2. 读取 `private-build-plans.toml` 中声明的所有 `[buildPlans.*]` 计划并构建（TTF + WOFF2，提示后）；
3. 将产物整理提交到本仓库：

| 目录 | 内容 |
| --- | --- |
| `zira/ttf` | 提示后的 TTF 字体（取自 Iosevka 构建产物 `dist/*/TTF/*.ttf`） |
| `zira/woff2` | WOFF2 网页字体（取自 `dist/*/WOFF2/*.woff2`） |
| `zira/fonts.css` | 自动生成的 @font-face 样式表（供 Web 项目直接引用，见下文） |

> 由于自动提交只改动 `zira/`，不会再次触发构建，避免循环。

## 通过 jsDelivr 在网页中使用（Web）

构建完成后，`zira/` 下的字体与 `fonts.css` 均可通过 jsDelivr 直接引用（**仓库需为 public**）。

**方式一：引用生成的 CSS（推荐）** —— 自动包含全部字体的 @font-face 规则：

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/dangpangch/fonts@main/zira/fonts.css">
```

```css
font-family: 'Zira Sans'; /* 或 Zira Mono / Zira Serif，支持 Regular/Bold × Upright/Italic */
```

**方式二：直接引用单个 WOFF2：**

```css
@font-face {
  font-family: 'Zira Sans';
  font-weight: 400;
  font-style: normal;
  src: url('https://cdn.jsdelivr.net/gh/dangpangch/fonts@main/zira/woff2/ZiraSans-Regular.woff2') format('woff2');
}
```

**缓存与版本固定（重要）：**

- `@main`（分支）URL 会被 jsDelivr 缓存约 12 小时；更新字体后如需立即生效，可在 https://www.jsdelivr.com/tools/purge 手动清除；
- 推荐在手动触发 workflow 时填写 `tag`（如 `v1.0.0`），构建后会**自动打 tag 并推送**，然后用 `@v1.0.0` 固定版本引用 —— 该 URL 永久缓存、内容不可变，最适合正式使用；
- jsDelivr 对所有文件返回 `Access-Control-Allow-Origin: *`，跨域 `@font-face` 无需额外配置。

## License

Zira 系列字体是 [Iosevka](https://github.com/be5invis/Iosevka) 的派生作品
（Modified Version），与 Iosevka 一样采用 **SIL Open Font License 1.1** 发布。

- 完整许可文本与合规说明见 [`LICENSE.md`](LICENSE.md)（含 Iosevka 原始版权声明与 OFL 1.1 全文）。
- 每个构建出的字体都在元数据中内嵌了 Iosevka 版权声明与 OFL 许可（OFL 条件 2），
  同时 workflow 会把 `LICENSE.md` 一并复制到 `zira/` 随字体发布。
- Iosevka 未声明保留字体名（Reserved Font Name），派生字体改名 “Zira …” 发布符合 OFL 要求。
