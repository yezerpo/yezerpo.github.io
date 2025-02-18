import { defineUserConfig } from "vuepress";

import theme from "./theme.js";

export default defineUserConfig({
  base: "/",

  lang: "zh-CN",
  title: "也籽呀",
  description: "我在这里分享我的故事",

  theme,
});