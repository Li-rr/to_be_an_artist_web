<template>
  <div id="app" class="">
    <nav class="navbar navbar-expand-sm bg-dark navbar-dark row">
      <div class="col-sm-6 col-md-8 col-lg-10"><h3 class="text-info">To be an artist</h3></div>
      <div class="col-sm-6 col-md-4 col-lg-2  ">
        <button class="btn btn-outline-info justify-content-end" v-show="displayLoginBtn" id="login" data-toggle="modal"
                data-target="#login-modal">登录
        </button>
        <button class="btn btn-outline-info justify-content-end" v-show="displayLoginBtn" id="logon" data-toggle="modal"
                data-target="#logon-modal">注册
        </button>
        <button class="btn btn-outline-info justify-content-end" v-show="!displayLoginBtn" id="quiet" v-on:click="quiet">退出</button>
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
            <button id="logon_close" type="button" class="btn btn-secondary" data-dismiss="modal">关闭</button>
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
                  <input type="text"  class="form-control" v-model="login_user"  placeholder="请输入用户名">
                </div>
              </div>
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text">密码：</span>
                </div>
                <div class=" ">
                  <input type="password" class="form-control" v-model="login_passwd"  placeholder="请输入密码">
                </div>
              </div>
            </form>
          </div>

          <!-- 模态框底部 -->
          <div class="modal-footer">
            <button type="button" class="btn btn-outline-info" v-on:click="login">提交</button>
            <button id="login_close" type="button" class="btn btn-secondary" data-dismiss="modal">关闭</button>
          </div>

        </div>
      </div>
    </div>
    <!--    这里是分隔线-->
<!--    这里是分隔线-->
    <!-- 引入组件 fuck you vue-->
    <first :childFirst="login_user"></first>
    <!--    引入组件 User-->
    <user :childUser="deal_user" :childUserName="login_user"></user>
    <router-view/>
  </div>
</template>

<script>
  // 引入组件
  import First from "./components/First";
  import User from "./components/User";
  import axios from "axios";
export default {
    name: 'App',
    data(){
      return{
        logon_user : "lqx",
          logon_pass1 : "123",
          logon_pass2 :"123",
          login_user : "",
          login_passwd: "123",
          msg:"fuck you",
          childFirst: "fuck",
          deal_user:"",
          displayQuitBtn: false,
          displayLoginBtn: true
      }
    },
    methods:{
      logon:function () {
          console.log(this.logon_user+" "+this.logon_pass1+" "+this.logon_pass2)
          if (this.logon_pass1 != this.logon_pass2){
              alert("两次密码不匹配")
          }else{
              alert("输入密码正确")
              axios.post('/api/logon/',
                  {
                      username:this.logon_user,
                      passward:this.logon_pass1
                  },
                  {headers:{'X-CSRFToken' : this.getCookie('csrftoken'),
                      'Content-Type':'application/json'}}
              ).then(this.getSuccessInfo).catch(err =>{
                  alert(err)  // 弹出错误信息
              })
          }
      },
        getCookie:function (name) {
          var value = '; '+document.cookie;
          var parts = value.split('; '+name+'=');
          if(parts.length===2) return parts.pop().split(';').shift()
        },
        setCookie:function(name,value,days){
          var exp = new Date();
          exp.setTime(exp.getTime() + days*24*60*60*1000);
          document.cookie = name + "="+escape(value)+";expires="+exp.toGMTstring();
        },
        getSuccessInfo:function (response) {
          alert("注册成功")
          $('#logon_close').click();
          $('#login').click();
        },
        login:function () {
          alert(this.login_user+"=="+this.login_passwd);
          axios.post('/api/login/',{
              username: this.login_user,
              passward: this.login_passwd
          }, {
              headers:{'Content-Type':'application/json'}}
          ).then(this.getLoginSuccess).catch(err => {
              console.log("这里是错误信息")
              console.log(err)
          })
        },
        getLoginSuccess: function (response) {
            //alert("session_id",response.data.session_id)
            //alert(typeof(response.data.status))
            if (response.data.status==1)
            {
                //alert("登录成功");

                $('#login_close').click();  //关闭模态框
                this.deal_user = true
                console.log("deal_user  "+this.deal_user)
                this.displayLoginBtn = false
                //this.$router.push('/user?username='+this.login_user); //页面重定向
            }else if(response.data.status==0){
                alert("登录失败，用户名或密码错误")
            }
            console.log(response)
        },
        quiet:function () {
            alert(this.login_user)
            axios.get('/api/quit/',{
                params:{
                    username: this.login_user
                }
            }).then(res=>{
                console.log(res)
                if(res.data.status == 2){
                    this.displayLoginBtn = true
                    this.deal_user = false
                    alert("退出成功")
                }else if(res.data.status == 3){
                    alert("退出遇到点问题，请关闭浏览器")
                }
            }).catch(err=>{
                alert("遇到了点问题。。")
            })
        },

    },
    components:{
      First,
      User
    },
}
</script>

<style>

</style>
