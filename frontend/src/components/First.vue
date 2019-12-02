<template>
  <div>
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
              <span class="input-group-btn"><button v-on:click="geneary" class="btn btn-outline-secondary">点击生成</button></span>
            </div>

          </div>
        </div>
      </div>
      <hr/>


      <div id="notice">
        <h3 class="bg-info text-white text-center" >生成结果</h3>
      </div>
      <div id="output" class="text-center">
             <h1> 标题：{{title}}</h1>
      <p v-model="message">{{message}}</p>
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
                holder: '请输入关键词'
            }
        },
        methods: {
            geneary: function () {
                this.message = '生成中。。。'
                alert(this.title);
                axios.get('/api/gen', {
                    params: {
                        title: this.title
                    }
                }).then(this.getGeninfo)
            },
            getGeninfo: function (res) {
                console.log(res)
                this.message = res.data
            },
        },
        watch: {
            genre: function () {
                if (this.genre == '1')
                    this.holder = "请输入关键词"
                else if (this.genre == '2')
                    this.holder = "请输入1~4个字"

            }
        }
    };
</script>

<style scoped>

</style>
