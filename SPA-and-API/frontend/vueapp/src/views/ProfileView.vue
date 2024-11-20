<script setup lang="ts">
import { ref, onMounted, Ref } from 'vue'
import { useRouter, Router } from 'vue-router'
import AccessAPI from '../functions/AccessAPI'
import ManageJWT from '../functions/ManageJWT'
import NavBar from '../components/NavBar.vue'

const router: Router = useRouter()

const { getUserInfo, getUserDelete } = AccessAPI()
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
    router.push({name: 'login'})
  }
}

function confirmDeleteUser(): void {
  if (confirm('本当に退会しますか？') === true) {
    getUserDelete()
    setJWT('')
    router.push({name: 'index'})
  }
}

onMounted(() => {
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
      <a href="/update_profile?param=ユーザーネーム" class="btn btn-primary my-2">変更</a>
      <br>
      <hr class="border-primary">
      メールアドレス：{{ user.mail }}
      <br>
      <a href="/update_profile?param=メールアドレス" class="btn btn-primary my-2">変更</a>
      <br>
      <hr class="border-primary">
      パスワード：＊＊＊＊＊＊
      <br>
      <a href="/update_profile?param=パスワード" class="btn btn-primary my-2">変更</a>
    </div>
    <br>
    <div class="my-2">
      <a href="/delete_user" class="btn btn-danger" v-on:click.prevent="confirmDeleteUser">サービス退会</a>
    </div>
    <br>
  </div>
</template>
