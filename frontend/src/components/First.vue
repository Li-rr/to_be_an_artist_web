<template>
  <div class="">
    <br/>
    <div class="container">
      <div id="input" class="from">
        <div class="row">
          <div class="col-lg-6 col-md-6 col-sm-6 text-center">
            <label class="radio-inline"><input type="radio" id="quatrains" value="1" v-model="genre">绝句</label>
          </div>
          <div class="col-lg-6 col-md-6 col-sm-6 text-center"><label class="radio-inline"><input type="radio" id="acrosticPoem" value="2"
                                                                   v-model="genre">藏头诗</label></div>
        </div>
        <div class="row">
          <div class="input-group">
            <div class="col-lg-10 col-md-8 col-sm-6">
              <input class="form-control" type="text" v-model="title" :placeholder="holder">
            </div>
            <div class="col-lg-2 col-md-4 col-sm-6">
              <span class="input-group-btn"><button v-on:click="geneary" class="btn btn-lg btn-outline-secondary">点击生成</button></span>
            </div>

          </div>
        </div>
      </div>
      <hr/>


      <div id="notice">
        <h3 class="bg-info text-white text-center" >生成结果</h3>
      </div>
      <div id="output" class="text-center">
        <table class="table ">
        <thead>
        <tr><th><h1> 标题：{{title}}</h1></th></tr>
        </thead>
          <tbody>
          <tr>
            <td>
              <h4 v-model="message">{{message}}</h4>
            </td>
          </tr>
          <tr> <td><button class="btn btn-outline-secondary" v-show="show" v-on:click="save">保存</button></td></tr>
          </tbody>
        </table>

      </div>

    </div>
  </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "First",

        data() {
            return {
                title: '',
                message: '',
                genre: '1',
                holder: '请输入关键词',
                show: false
            }
        },
        methods: {
            geneary: function () {
                this.message = '生成中。。。'
                alert(this.title+" "+this.genre);
                axios.get('/api/gen/', {
                    params: {
                        title: this.title,
                        choice: this.genre
                    }
                }).then(this.getGeninfo).catch(err=>{
                    this.message = "我们遇到了一点问题，换个关键词试试"
                    this.show = true
                })
            },
            getGeninfo: function (res) {
                console.log(res)
                console.log(res.data.status)
                if(res.data.status==10){
                    console.log("生成成功")
                    this.message = res.data.poem
                }else if(res.data.status==11){
                    alert("遇到了一点问题")
                    this.message = "再试一次"
                }
                this.show=true
            },
            save: function () {
                // alert(this.childFirst)
                if(this.childFirst == "")
                {
                    alert("请先登录")
                }
                else{
                    axios.get('/api/save/',{
                        params:{
                            title: this.title,
                            content: this.message,
                            user: this.childFirst
                        }
                    }).then(res=>{
                        console.log(res)
                    })
                }
            }
        },
        watch: {
            genre: function () {
                if (this.genre == '1')
                    this.holder = "请输入关键词"
                else if (this.genre == '2')
                    this.holder = "请输入1~4个字"

            }
        },
        props:['childFirst'],
        //生命周期函数
        mounted() {
            //alert(this.childFirst)
        }
    };
</script>

<style scoped>
.no-border {
  border: 1px solid transparent !important;
}
</style>
