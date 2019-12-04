<template>
    <div id="user" v-show="childUser" class="container">
      <div class="jumbotron">
        <table class="table">
        <thead>
        <tr>
          <th>欢迎用户：</th>
          <th>{{childUserName}}</th>
          <th><button class="btn btn-primary" v-on:click="queryAll">点击查询</button></th>
        </tr>
        </thead>
          <tbody>
          <tr v-for="poemItem in poem_list">
            <td class="text-wrapper" v-for="item in poemItem">{{item}}</td>
<!--            <td class="text-wrapper">{{titleItem}}</td>-->
<!--            <td class="text-wrapper">{{poemItem}}</td>-->
            <td><button class="btn-primary btn"> 修改</button></td>
            <td><button class="btn-primary btn">删除</button></td>
          </tr>
          </tbody>
        </table>
      </div>
<!--      <h1>用户名：{{childUserName}}</h1>-->
<!--      <h1>{{childUser}}</h1>-->
    </div>
</template>

<script>
  import axios from "axios";
    export default {
        name: "User",
        data(){
          return{
              poem_list:"",
              title_list: "",
          }
        },
        methods:{
            queryAll:function () {
                alert(this.childUserName)
                axios.get('/api/queryAll/',{
                    params:{
                        username: this.childUserName
                    }
                }).then(res => {
                    console.log(res.data)
                    if(res.data.status == 4){
                      alert("查询成功");
                      this.poem_list = res.data.c_poem;
                      this.title_list = res.data.title;
                      console.log(res.data)
                    }else if(res.data.status == 5){
                        alert("出了点问题")
                    }
                }).catch(err=>{
                    alert("出现严重错误")
                    console.log(err)
                })
            }
        },
        mounted() {
            //this.showDeal = true
            //alert("-> "+this.$route.query.username)
            //this.msg = this.$route.query.username
        },
        props:['childUser','childUserName'],
        watch: {
            // 监听属性
            childUser:function (newVal,oldVal) {
                alert('新值 '+newVal + ' 旧值 '+oldVal)
            }
        }

    }
</script>

<style scoped>
.text-wrapper{
   white-space: pre-wrap;
}
</style>
