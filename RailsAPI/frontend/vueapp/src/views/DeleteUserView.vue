<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import AccessAPI from '../functions/AccessAPI'
import ManageJWT from '../functions/ManageJWT'

const router = useRouter()

const { getUserInfo, getUserDelete } = AccessAPI()
const { setJWT } = ManageJWT()

async function tryDeleteUser() {
  const response1 = await getUserInfo()
  if (response1.status === 200) {
    getUserDelete()
    setJWT('')
    router.push({name: 'index'})
  }
  else {
    setJWT('')
    router.push({name: 'login'})
  }
}

onMounted(() => {
  tryDeleteUser()
})
</script>
