import { hopeTheme } from "vuepress-theme-hope";

import navbar from "./navbar.js";
import sidebar from "./sidebar.js";

export default hopeTheme({
  hostname: "https://yezer.cn",

  repo: "yezerpo/yezerpo.github.io",
  docsDir: "src",

  // 导航栏
  navbar,
  titleIcon: true,
  logo: "/common/header.svg",
  navbarTitle: "",

  // 侧边栏
  sidebar,

  // 页脚
  displayFooter: true,
  footer: "苏ICP备2024137980号 | Copyright © 2025-present Kalidium",

  // 博客相关
  blog: {
    avatar: "/common/avatar.webp",
    name: "也籽",
    description: "我在这里分享我的故事",
    intro: "/intro.html",
  },

  // 多语言配置
  metaLocales: {
    editLink: "编辑此页",
  },


  markdown: {
    align: true,
    attrs: true,
    codeTabs: true,
    component: true,
    demo: true,
    figure: true,
    gfm: true,
    imgLazyload: true,
    imgSize: true,
    include: true,
    mark: true,
    plantuml: true,
    spoiler: true,
    sub: true,
    sup: true,
    tabs: true,
    tasklist: true,
    vPre: true,
  },

  // 在这里配置主题提供的插件
  plugins: {
    blog: true,

    comment: {
       provider: "Giscus",
       repo: "yezerpo/yezerpo.github.io",
       repoId: "R_kgDON4MIlA",
       category: "评论池",
       categoryId: "DIC_kwDON4MIlM4Cm5nc",
     },

    components: {
      components: ["Badge", "VPCard"],
    },

    icon: {
      prefix: "fa6-solid:",
    },
  },
});
