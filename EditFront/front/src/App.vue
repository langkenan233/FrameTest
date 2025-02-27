<template>
  <div id="app">
    <!-- 导航栏 -->
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/new-page">New Page</router-link>
    </nav>

    <!-- 路由出口 -->
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
