<template>
  <div>
    <h1>New Page</h1>
    <p>This is a hzx page created in Vue 3.</p>
  </div>
</template>

<script>
export default {
  name: 'hzxPage',
  methods: {
    async fetchData() {
      try {
        const response = await this.$axios.get('/api/hzx');
        console.log(response.data);
      } catch (error) {
        console.error(error);
      }
    }
  },
  created () {
    this.fetchData();
  }
};
</script>

<style scoped>
h1 {
  color: #42b983;
}
</style>