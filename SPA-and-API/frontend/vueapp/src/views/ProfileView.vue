<template>
  <NavBar v-bind:user="user"/>
  <div class="p-3">
    <h4 class="fw-bolder mb-3">
      会員様情報
    </h4>
    <div class="col-sm-9 col-md-6 col-lg-4 border border-primary bg-light mt-4 p-3">
      ユーザーネーム：{{ user.name }}
      <br>
      <a href="/update_profile?param=ユーザーネーム" class="btn btn-primary my-2">変更</a>
      <br>
      <hr class="border-primary">
      メールアドレス：{{ user.mail }}
      <br>
      <a href="/update_profile?param=メールアドレス" class="btn btn-primary my-2">変更</a>
      <br>
      <hr class="border-primary">
      パスワード：＊＊＊＊＊＊
      <br>
      <a href="/update_profile?param=パスワード" class="btn btn-primary my-2">変更</a>
    </div>
    <br>
    <div class="my-2">
      <a href="/delete_user" class="btn btn-danger" @click="confirmDeleteUser">サービス退会</a>
    </div>
    <br>
  </div>
</template>

<script>
import AccessAPI from '../mixins/AccessAPI'
import ManageJWT from '../mixins/ManageJWT'
import NavBar from '../components/NavBar.vue'
  
export default {
  name: 'ProfileView',
  mixins: [
    AccessAPI,
    ManageJWT
  ],
  components: {
    NavBar
  },
  data() {
    return {
      user: {
        login: false,
        name: '',
        mail: ''
      }
    }
  },
  methods: {
    async setUserInfo() {
      const response = await this.getUserInfo()
      if (response.status === 200) {
        this.user = {
          login: true,
          name: response.json.user_info.username,
          mail: response.json.user_info.mail
        }
      }
      else {
        this.setJWT('')
        this.$router.push({name: 'login'})
      }
    },
    confirmDeleteUser() {
      const isConfirmed = confirm('本当に退会しますか？')
      if (isConfirmed === false) {
        event.preventDefault()
      }
    }
  },
  mounted() {
    document.title = '会員情報'
    this.setUserInfo()
  }
}
</script>
