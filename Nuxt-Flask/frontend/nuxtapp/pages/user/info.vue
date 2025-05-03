<script setup lang="ts">
import type { Router } from 'vue-router'

const router: Router = useRouter()

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
    router.push({name: 'user-auth'})
  }
}

function confirmDeleteUser(): void {
  if (confirm('本当に退会しますか？') === true) {
    accessUserDelete()
    setJWT('')
    router.push({name: 'index'})
  }
}

onBeforeMount(() => {
  document.title = '会員様情報'
  setUserInfo()
})
</script>

<template>
  <NavBar v-bind:user="user"/>
  <div class="p-3">
    <h4 class="fw-bolder mb-3">
      会員様情報
    </h4>
    <div class="col-sm-9 col-md-6 col-lg-4 border border-primary bg-light mt-4 p-3">
      ユーザーネーム：{{ user.name }}
      <br>
      <a href="/user/update/ユーザーネーム" class="btn btn-primary my-2">変更</a>
      <br>
      <hr class="border-primary">
      メールアドレス：{{ user.mail }}
      <br>
      <a href="/user/update/メールアドレス" class="btn btn-primary my-2">変更</a>
      <br>
      <hr class="border-primary">
      パスワード：＊＊＊＊＊＊
      <br>
      <a href="/user/update/パスワード" class="btn btn-primary my-2">変更</a>
    </div>
    <br>
    <div class="my-2">
      <a class="btn btn-danger" v-on:click.prevent="confirmDeleteUser">サービス退会</a>
    </div>
    <br>
  </div>
</template>
