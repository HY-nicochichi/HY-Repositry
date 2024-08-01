<template>
  <NavBar v-bind:user="user"/>
  <div class="p-3">
    <AlertBox v-bind:alert="alert"/>
    <h4 class="fw-bolder mb-3">
      ログイン
    </h4>
    <div class="col-sm-9 col-md-7 col-lg-5 border border-primary bg-light p-3">
      <div class="row">
        <div class="col">
          <div class="mb-4">
            <label class="mb-2">メールアドレス</label>
            <input type="text" class="form-control border border-primary" ref="mail"/>
          </div>
          <div class="mb-4">
            <label class="mb-2">パスワード</label>
            <input type="password" class="form-control border border-primary" ref="password"/>
          </div>
          <br>
          <div>
            <button class="btn btn-primary" v-on:click="tryLogin">ログイン</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AccessAPI from '../mixins/AccessAPI'
import ManageJWT from '../mixins/ManageJWT'
import NavBar from '../components/NavBar.vue'
import AlertBox from '../components/AlertBox.vue'
  
export default {
  name: 'LoginView',
  mixins: [
    AccessAPI,
    ManageJWT
  ],
  components: {
    NavBar,
    AlertBox
  },
  data() {
    return {
      user: {
        login: false,
        name: ''
      },
      alert: {
        show: false,
        msg: ''
      }
    }
  },
  methods: {
    async checkLoggedIn() {
      const response = await this.getUserInfo()
      if (response.status === 200) {
        this.$router.push({name: 'index'})
      }
      else {
        this.setJWT('')
      }
    },
    async tryLogin() {
      if (this.$refs.mail.value === '' || this.$refs.password.value === '') {
        this.alert = {
          show: true,
          msg: '未入力の項目がありました'
        }
        this.$refs.mail.value = ''
        this.$refs.password.value = ''
      }
      else {
        const response = await this.postJWTCreate(
          this.$refs.mail.value, this.$refs.password.value
        )
        if (response.status === 200) {
          this.setJWT(response.json.access_token)
          this.$router.push({name: 'index'})
        }
        else if (response.status === 401) {
          this.alert = {
            show: true,
            msg: response.json.msg
          }
          this.$refs.mail.value = ''
          this.$refs.password.value = ''
        }
      }
    }
  },
  mounted() {
    document.title = 'ログイン'
    this.checkLoggedIn()
  }
}
</script>
