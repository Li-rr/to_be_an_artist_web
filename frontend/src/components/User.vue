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

          <tr v-bind:poem_id="index" v-for="(poemItem,index) in poem_list" :key="index">
<!--            <td  class="text-wrapper" v-for="(item,i_index) in poemItem">-->
<!--              <textarea>{{item}}</textarea>-->
<!--            </td>-->
            <td v-bind:poem_item_id="i_index"  class="text-wrapper" v-for="(item,i_index) in poemItem">{{item}}</td>
            <td><button class="btn-primary btn" @click="edit_btn(index,poem_list)"> 修改</button></td>
            <td><button class="btn-primary btn" @click="del_btn(index)">删除</button>{{index}}</td>
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
            },
            del_btn:function (index) {
                alert("这里是删除按钮=》",index)
            },
            edit_btn:function (index,poem_list) {
                for (var i=0;i<poem_list.length;i++){
                    if (index == i){
                        alert(poem_list[i])
                    }
                }
                alert("这里是编辑按钮=》",index)
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

    };
    // $(function() {     $("button").click(function () {
    //     alert("fuck => "+ $(this).text())
    // }); })
</script>

<style scoped>
.text-wrapper{
   white-space: pre-wrap;
}
</style>
