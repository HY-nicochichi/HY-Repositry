<script setup lang="ts">
let user: Ref<User> = ref({
  login: false,
  name: '',
  mail: ''
})

async function setUserInfo(): Promise<void> {
  const resp: Resp = await accessUserGet()
  if (resp.status === 200) {
    user.value = {
      login: true,
      name: resp.json.name,
      mail: resp.json.mail
    }
  }
  else {
    setJWT('')
  }
}

onBeforeMount(() => {
  document.title = 'Nuxt & Flask'
  setUserInfo()
})
</script>

<template>
  <NavBar v-bind:user="user"/>
  <div class="p-3">
    <h4 class="fw-bolder">
      Nuxt & Flask Auth App
    </h4>
  </div>
</template>
