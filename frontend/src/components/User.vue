<template>
    <div id="user" v-show="childUser" class="jumbotron">
      <div class="">
        <table class="table table-hover table-condensed text-center">

        <thead>
        <tr><th colspan="4"><h4>用户使用记录</h4></th></tr>
        <tr>
          <th><h4>欢迎用户：</h4></th>
          <th><h4>{{childUserName}}</h4></th>
          <th colspan="2"><button id="queryAll" class="btn btn-primary" v-on:click="queryAll">点击查询</button></th>
        </tr>
        </thead>
          <tbody>

          <tr class="text-center" v-bind:poem_id="index" v-for="(poemItem,index) in poem_list" :key="index">
<!--            <td  class="text-wrapper" v-for="(item,i_index) in poemItem">-->
<!--              <textarea>{{item}}</textarea>-->
<!--            </td>-->
            <td v-bind:poem_item_id="i_index"  class="text-wrapper" v-for="(item,i_index) in poemItem">{{item}}</td>
            <td><button class="btn-outline-primary btn" data-toggle="modal" dat data-target="#editModal" @click="edit_btn(index,poem_list)"> 修改</button></td>
            <td><button class="btn-outline-primary btn" @click="del_btn(index)">删除</button></td>
          </tr>
          </tbody>
        </table>
      </div>
<!--      <h1>用户名：{{childUserName}}</h1>-->
<!--      <h1>{{childUser}}</h1>-->

<!--      定义模态框-->
        <!-- 模态框 -->
      <div class="modal fade" id="editModal">
     <div class="modal-dialog modal-lg">
      <div class="modal-content">

        <!-- 模态框头部 -->
        <div class="modal-header">
          <h4 class="modal-title" >{{modal_title}}</h4>
          <button type="button" class="close" data-dismiss="modal">&times;</button>
        </div>

        <!-- 模态框主体 -->
        <div class="modal-body">
          <h4 v-for="item in modal_content">{{item}}</h4>
          <hr>
          <textarea class="form-control" rows="5" v-model="edit_content">
          </textarea>
        </div>

        <!-- 模态框底部 -->
        <div class="modal-footer">
          <button type="button" class="btn btn-outline-primary" v-on:click="edit_submit_btn">提交</button>
          <button id="edit_btn_dismiss" type="button" class="btn btn-secondary" data-dismiss="modal">关闭</button>
        </div>

      </div>
    </div>
  </div>
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
              modal_title:"",
              modal_content: "",
              edit_content: "", // 用于修改的古诗
              id_list: "",
              edit_index: "",   // 用于记录古诗的ID

          }
        },
        methods:{
            queryAll:function () {
                //alert(this.childUserName)
                axios.get('/api/queryAll/',{
                    params:{
                        username: this.childUserName
                    }
                }).then(res => {
                    console.log(res.data)
                    if(res.data.status == 4){
                      //alert("查询成功");
                      this.poem_list = res.data.c_poem;
                      this.title_list = res.data.title;
                      this.id_list = res.data.id_list
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
                alert("这里是删除按钮=》"+index)
                for(var i=0; i < this.id_list.length;i++){
                    if(i==index){
                        //alert(this.id_list[i]+" "+this.title_list[i])
                        var del_id = this.id_list[i];
                    }
                }
                axios.get('/api/delrecord/',{
                    params:{
                        id: del_id
                    }
                }).then(this.getSuccessInfo).catch(err=>{
                    alert("出现了严重错误");
                    console.log(err);
                })

            },
            edit_btn:function (index,poem_list) {
                for (var i=0;i<poem_list.length;i++){
                    if (index == i){
                        //alert(poem_list[i])
                        var p_content = poem_list[i]
                    }
                }
                // 创建数组，设诗的总长度为x，每一段的长度为4/x
                var fuck_poem_container = p_content[1].split('\n')
                for (var i=0; i<fuck_poem_container.length;i++){
                    console.log("===>",fuck_poem_container[i])
                }

                this.modal_title = p_content[0]
                this.modal_content = fuck_poem_container
                this.edit_content = p_content[1]
                this.edit_index = this.id_list[index]
                //alert('这是古诗编号: '+this.edit_index)
                //alert("这里是编辑按钮=》",index)
            },
            edit_submit_btn:function () {
                //alert("古诗内容："+this.edit_content+"\n"+"古诗编号："+this.edit_index)
                axios.post('/api/isave/',{
                    p_content: this.edit_content,
                    p_index: this.edit_index
                },{
                    headers: {'Content-Type':'application/json'}
                }).then(this.getSuccessInfo).catch(err=>{
                    console.log(err); // 打印错误信息
                })
            },
            getSuccessInfo:function (res) {
                if(res.data.status==6){
                    //alert("修改成功")
                    $('#edit_btn_dismiss').click(); // 关闭模态框
                    $('#queryAll').click(); //重新查询
                }else if(res.data.status==7){
                    alert("我们遇到了一点问题")
                }else if(res.data.status==8){
                    alert("删除成功")
                     $('#queryAll').click(); //重新查询
                }else if(res.data.status==9){
                    alert("我们遇到了一点问题")
                }
            }
        },
        mounted() {
            //this.showDeal = true
            //alert("-> "+this.$route.query.username)
            //this.msg = this.$route.query.username
        },
        props:['childUser','childUserName','childQuitUser'],
        watch: {
            // 监听属性
            childUser:function (newVal,oldVal) {
                //alert('新值 '+newVal + ' 旧值 '+oldVal)
            },
            // 监听是否退出
            childQuitUser:function (newVal,oldVal) {
                //alert('这里是User组件 新值 '+newVal + ' 旧值 '+oldVal)
                if(newVal ==true){  // 确认退出
                    this.poem_list = "";
                    this.modal_title = "";
                    this.modal_title = "";
                    this.modal_content = "";
                    this.edit_content = "";
                    this.edit_index = "";
                    this.id_list = "";
                }
            }
        }

    };
</script>

<style scoped>
.text-wrapper{
   white-space: pre-wrap;
}
</style>
