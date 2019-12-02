<template>
  <div id="app">
<!--    <img src="./assets/logo.png">-->
<!--    <p class="col-md-6"><button class="btn btn-primary">测试按钮</button></p>-->
    <router-view/>
  </div>
</template>

<script>
  // 引入组件
  import First from "./components/First";
export default {
  name: 'App',
    components:{
      First
    }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
