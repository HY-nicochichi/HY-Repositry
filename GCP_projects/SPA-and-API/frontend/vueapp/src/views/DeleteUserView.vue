<script>
import AccessAPI from '../mixins/AccessAPI'
import ManageJWT from '../mixins/ManageJWT'
  
export default {
  name: 'DeleteUserView',
  mixins: [
    AccessAPI,
    ManageJWT
  ],
  methods: {
    async tryDeleteUser() {
      const response1 = await this.getUserInfo()
      if (response1.status === 200) {
        this.getUserDelete()
        this.setJWT('')
        this.$router.push({name: 'index'})
      }
      else {
        this.setJWT('')
        this.$router.push({name: 'login'})
      }
    }
  },
  mounted() {
    this.tryDeleteUser()
  }
}
</script>
