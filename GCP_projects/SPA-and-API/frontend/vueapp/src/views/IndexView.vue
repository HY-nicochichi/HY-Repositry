<template>
  <NavBar v-bind:user="user"/>
  <div class="p-3">
    <h4 class="fw-bolder">
      SPA(Vue) & API(Flask) Auth App
    </h4>
  </div>
</template>

<script>
import AccessAPI from '../mixins/AccessAPI'
import ManageJWT from '../mixins/ManageJWT'
import NavBar from '../components/NavBar.vue'
  
export default {
  name: 'IndexView',
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
        name: ''
      }
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
      }
    }
  },
  mounted() {
    document.title = 'SPA & API'
    this.setUserInfo()
  }
}
</script>
