import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HelloWorld.vue'; // 假设这是你的主页组件
import NewPage from '../components/NewPage.vue';   // 引入新建的组件

// 导入模块路由
import hzxRoutes from "@/router/modules/hzx";
import lhRoutes from "@/router/modules/lh";
import lknRoutes from "@/router/modules/lkn";
import lukeRoutes from "@/router/modules/luke";
import whlRoutes from "@/router/modules/whl";



// 定义路由规则
const baseRoutes = [
  { path: '/', component: HomePage, name: 'Home' }, // 主页路由
  { path: '/new-page', component: NewPage, name: 'NewPage' }, // 新页面路由
];

const routes = [...hzxRoutes,...lhRoutes,...lknRoutes,...lukeRoutes,...whlRoutes, ...baseRoutes];

// 创建路由实例
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;