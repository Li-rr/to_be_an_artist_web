<template>
  <div id="app">
    <nav class="navbar navbar-expand-sm bg-dark navbar-dark row">
      <div class="col-sm-6 col-md-8 col-lg-10"><a class="navbar-brand ">To be an artist</a></div>
      <div class="col-sm-6 col-md-4 col-lg-2  ">
        <button class="btn btn-outline-info justify-content-end" id="login" data-toggle="modal"
                data-target="#login-modal">登录
        </button>
        <button class="btn btn-outline-info justify-content-end" id="logon" data-toggle="modal"
                data-target="#logon-modal">注册
        </button>
      </div>
    </nav>

       <!--    组件位置-->
    <!--  注册模态框-->
    <div class="modal fade" id="logon-modal">
      <div class="modal-dialog">
        <div class="modal-content">

          <!-- 模态框头部 -->
          <div class="modal-header">
            <h4 class="modal-title">创建你的账户</h4>
            <button type="button" class="close" data-dismiss="modal">&times;</button>
          </div>

          <!-- 模态框 -->
          <div class="modal-body">
            <form class="">
              <div class="input-group mb-3 ">
                <div class="input-group-prepend">
                  <span class="input-group-text ">用户名：</span>
                </div>
                <div class="">
                  <input type="text" class="form-control" v-model="logon_user" placeholder="请输入用户名">
                </div>
              </div>
              <div class="input-group mb-3 ">
                <div class="input-group-prepend">
                  <span class="input-group-text">密码：</span>
                </div>
                <div class=" ">
                  <input type="password" class="form-control" v-model="logon_pass1" placeholder="请输入密码">
                </div>
              </div>
              <div class="input-group mb-3 ">
                <div class="input-group-prepend">
                  <span class="input-group-text  ">确认密码：</span>
                </div>
                <div class="">
                  <input type="password" class="form-control" v-model="logon_pass2" placeholder="请在输入一边密码">
                </div>
              </div>
            </form>
          </div>

          <!-- 模态框底部 -->
          <div class="modal-footer">
            <button type="button" class="btn btn-outline-info" v-on:click="logon">提交</button>
            <button type="button" class="btn btn-secondary" data-dismiss="modal">关闭</button>
          </div>

        </div>
      </div>
    </div>
    <!--    这里是分隔线-->
    <!--    登录模态框-->

    <div class="modal fade" id="login-modal">
      <div class="modal-dialog">
        <div class="modal-content">

          <!-- 模态框头部 -->
          <div class="modal-header">
            <h4 class="modal-title">用户名密码登录</h4>
            <button type="button" class="close" data-dismiss="modal">&times;</button>
          </div>

          <!-- 模态框 -->
          <div class="modal-body">
            <form class="">
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text ">用户名：</span>
                </div>
                <div class="">
                  <input type="text" class="form-control "  placeholder="请输入用户名">
                </div>
              </div>
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text">密码：</span>
                </div>
                <div class=" ">
                  <input type="text" class="form-control "  placeholder="请输入密码">
                </div>
              </div>
            </form>
          </div>

          <!-- 模态框底部 -->
          <div class="modal-footer">
            <button type="button" class="btn btn-outline-info">提交</button>
            <button type="button" class="btn btn-secondary" data-dismiss="modal">关闭</button>
          </div>

        </div>
      </div>
    </div>
    <!--    这里是分隔线-->
<!--    这里是分隔线-->
    <router-view/>
  </div>
</template>

<script>
  // 引入组件
  import First from "./components/First";
  import axios from "axios";
export default {
    name: 'App',
    data(){
      return{
        logon_user : "lqx",
          logon_pass1 : "123",
          logon_pass2 :"123",
      }
    },
    methods:{
      logon:function () {
          console.log(this.logon_user+" "+this.logon_pass1+" "+this.logon_pass2)
          if (this.logon_pass1 != this.logon_pass2){
              alert("两次密码不匹配")
          }else{
              alert("输入密码正确")

              // axios.get('/api/token/').then(response=>{
              //     var cookie_data = response.data['token'];
              //     this.post_a(cookie_data)
              // })
              axios.post('/api/logon/',
                  {
                      username:this.logon_user,
                      passward:this.logon_pass1
                  },
                  {headers:{'X-CSRFToken' : this.getCookie('csrftoken')}}
              ).then(res=>{
                  console.log(res)  // 请求成功打印res
              }).catch(err =>{
                  alert(err)  // 弹出错误信息
              })
          }
      },
        post_a: function (CSRFToken) {
            axios.post("/api/logon/",{
                username:this.username,
                passward:this.passward
            },{
                headers:{'X-CSRFToken':CSRFToken}
            }).then(res=>{
                console.log(res)  // 请求成功打印res
            }).catch(err=>{
                console.log(err)  // 请求失败打印err
            })
        },
        getCookie:function (name) {
          var value = '; '+document.cookie;
          var parts = value.split('; '+name+'=');
          if(parts.length===2) return parts.pop().split(';').shift()
        }
    },
    components:{
      First
    }
}
</script>

<style>

</style>
