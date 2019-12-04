<template>
    <div id="user" v-show="childUser">
      <h1>用户名：{{msg}}</h1>
      <h1>{{childUser}}</h1>
    </div>
</template>

<script>
    export default {
        name: "User",
        data(){
          return{
              msg: 'fuck you too',
              // showDeal : this.childUser
          }
        },
        mounted() {
            //this.showDeal = true
            //alert("-> "+this.$route.query.username)
            //this.msg = this.$route.query.username
        },
        props:['childUser'],
        watch: {
            // 监听属性
            childUser:function (newVal,oldVal) {
                alert('新值 '+newVal + ' 旧值 '+oldVal)
            }
        }

    }
</script>

<style scoped>

</style>
