import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import router from './router'; // 引入路由实例

const app = createApp(App)
app.config.globalProperties.$axios = axios  // 全局挂载
//使用路由
app.use(router);
app.mount('#app')

