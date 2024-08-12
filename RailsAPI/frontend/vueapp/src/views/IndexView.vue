<script setup>
import { ref, onMounted } from 'vue'
import AccessAPI from '../functions/AccessAPI'
import ManageJWT from '../functions/ManageJWT'
import NavBar from '../components/NavBar.vue'

const { getUserInfo } = AccessAPI()
const { setJWT } = ManageJWT()

let user = ref({
  login: false,
  name: ''
})

async function setUserInfo() {
  const response = await getUserInfo()
  if (response.status === 200) {
    user.value = {
      login: true,
      name: response.json.user_info.username
    }
  }
  else {
    setJWT('')
  }
}

onMounted(() => {
  document.title = 'RailsAPI'
  setUserInfo()
})
</script>

<template>
  <NavBar v-bind:user="user"/>
  <div class="p-3">
    <h4 class="fw-bolder">
      SPA(Vue) & API(Rails) Auth App
    </h4>
  </div>
</template>
