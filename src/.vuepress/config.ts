import { defineUserConfig } from "vuepress";

import theme from "./theme.js";

export default defineUserConfig({
  base: "/",

  lang: "zh-CN",
  title: "也籽呀",
  description: "在这里，我随便写点什么。",

  theme,
});