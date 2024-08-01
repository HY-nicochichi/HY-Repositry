<template>
  <NavBar v-bind:user="user"/>
  <div class="p-3">
    <AlertBox v-bind:alert="alert"/>
    <h4 class="fw-bolder mb-3">
      {{ param }}の変更
    </h4>
    <div class="col-sm-9 col-md-7 col-lg-5 border border-primary bg-light p-3">
      <div class="row">
        <div class="col">
          <div class="mb-4">
            <label class="mb-2">現{{ param }}</label>
            <input v-bind:type="type" class="form-control border border-primary" ref="current_value">
          </div>
          <div class="mb-4">
            <label class="mb-2">新{{ param }}</label>
            <input v-bind:type="type" class="form-control border border-primary" ref="new_value">
          </div>
          <div class="mb-4">
            <label class="mb-2">新{{ param }}(確認)</label>
            <input v-bind:type="type" class="form-control border border-primary" ref="check_value">
          </div>
          <br>
          <div>
            <button class="btn btn-primary" v-on:click="tryUpdateUser">{{ param }}更新</button>
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
  name: 'UpdateProfileView',
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
      },
      param: this.$route.query.param,
      type: 'password'
    }
  },
  methods: {
    async setUserInfo() {
      const response = await this.getUserInfo()
      if (response.status === 200) {
        this.user = {
          login: true,
          name: response.json.user_info.username
        }
      }
      else {
        this.setJWT('')
        this.$router.push({name: 'login'})
      }
    },
    async tryUpdateUser() {
      if (this.$refs.current_value.value === '' || this.$refs.new_value.value === '' || this.$refs.check_value.value === '') {
        this.alert = {
          show: true,
          msg: '未入力の項目がありました'
        }
        this.$refs.current_value.value = ''
        this.$refs.new_value.value = ''
        this.$refs.check_value.value = ''
      }
      else {
        const response = await this.postUserUpdate(
          this.param, this.$refs.current_value.value, this.$refs.new_value.value, this.$refs.check_value.value
        )
        if (response.status === 200) {
          this.$router.push({name: 'profile'})
        }
        else if (response.status === 401) {
          this.alert = {
            show: true,
            msg: response.json.msg
          }
          this.$refs.current_value.value = ''
          this.$refs.new_value.value = ''
          this.$refs.check_value.value = ''
        }
      }
    }
  },
  mounted() {
    document.title = this.param + 'の変更'
    if (this.param !== 'パスワード') {
      this.type = 'text'
    }
    this.setUserInfo()
  }
}
</script>
