<script setup lang="ts">
import type { Ref } from 'vue'
import type { Response, User } from '~/utils/Interface'
import { accessUserGet } from '~/utils/AccessAPI'
import { setJWT } from '~/utils/ManageJWT'
import NavBar from '~/components/NavBar.vue'

let user: Ref<User, User> = ref({
  login: false,
  name: '',
  mail: ''
})

async function setUserInfo(): Promise<void> {
  const response: Response = await accessUserGet()
  if (response.status === 200) {
    user.value = {
      login: true,
      name: response.json.name,
      mail: response.json.mail
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
      Nuxt & Rails Auth App
    </h4>
  </div>
</template>
