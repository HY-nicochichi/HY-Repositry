<script>
import AccessAPI from '../mixins/AccessAPI'
import ManageJWT from '../mixins/ManageJWT'
  
export default {
  name: 'LogoutView',
  mixins: [
    AccessAPI,
    ManageJWT
  ],
  methods: {
    async tryLogout() {
      const response = await this.getUserInfo()
      this.setJWT('')
      if (response.status === 200) {
        this.$router.push({name: 'index'})
      }
      else {
        this.$router.push({name: 'login'})
      }
    }
  },
  mounted() {
    this.tryLogout()
  }
}
</script>
