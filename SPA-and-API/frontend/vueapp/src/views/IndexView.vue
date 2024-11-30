<script setup lang="ts">
import { ref, onMounted, Ref } from 'vue'
import AccessAPI from '../functions/AccessAPI'
import ManageJWT from '../functions/ManageJWT'
import NavBar from '../components/NavBar.vue'

const { getUserInfo } = AccessAPI()
const { setJWT } = ManageJWT()

let user: Ref = ref({
  login: false,
  name: '',
  mail: ''
})

async function setUserInfo(): Promise<void> {
  const response: {status: number, json: any} = await getUserInfo()
  if (response.status === 200) {
    user.value = {
      login: true,
      name: response.json.user_name,
      mail: response.json.mail_address
    }
  }
  else {
    setJWT('')
  }
}

onMounted(() => {
  document.title = 'SPA & API'
  setUserInfo()
})
</script>

<template>
  <NavBar v-bind:user="user"/>
  <div class="p-3">
    <h4 class="fw-bolder">
      SPA(Vue) & API(Flask) Auth App
    </h4>
  </div>
</template>
