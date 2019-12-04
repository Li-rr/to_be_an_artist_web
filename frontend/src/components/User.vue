<template>
    <div id="user">
      {{msg}}
    </div>
</template>

<script>
    export default {
        name: "User",
        data(){
          return{
              msg: 'fuck you too'
          }
        },
        mounted() {
            alert("-> "+this.$route.query.username)
            this.msg = this.$route.query.username
        }

    }
</script>

<style scoped>

</style>
