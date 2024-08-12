<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import AccessAPI from '../functions/AccessAPI'
import ManageJWT from '../functions/ManageJWT'

const router = useRouter()

const { getUserInfo } = AccessAPI()
const { setJWT } = ManageJWT()

async function tryLogout() {
  const response = await getUserInfo()
  setJWT('')
  if (response.status === 200) {
    router.push({name: 'index'})
  }
  else {
    router.push({name: 'login'})
  }
}

onMounted(() => {
  tryLogout()
})

</script>
