<script setup lang="ts">
import { ref, onMounted, Ref } from 'vue'
import { useRouter, useRoute, Router, RouteLocationNormalizedLoadedGeneric } from 'vue-router'
import AccessAPI from '../functions/AccessAPI'
import ManageJWT from '../functions/ManageJWT'
import ManageQuery from '../functions/ManageQuery'
import NavBar from '../components/NavBar.vue'

const router: Router = useRouter()
const route: RouteLocationNormalizedLoadedGeneric = useRoute()

const { getUserInfo, getUserDelete } = AccessAPI()
const { setJWT } = ManageJWT()
const { addQuery, pushRouter } = ManageQuery()

let user: Ref = ref({
  login: false,
  name: '',
  mail: ''
})

const client: Ref = ref(route.query.client)

async function setUserInfo(): Promise<void> {
  const response: {status: number, json: any} = await getUserInfo(client.value)
  if (response.status === 200) {
    user.value = {
      login: true,
      name: response.json.user_name,
      mail: response.json.mail_address
    }
  }
  else {
    setJWT('')
    router.push(pushRouter(client.value, '/login'))
  }
}

function confirmDeleteUser(): void {
  if (confirm('本当に退会しますか？') === true) {
    getUserDelete(client.value)
    setJWT('')
    router.push(pushRouter(client.value, '/'))
  }
}

onMounted(() => {
  document.title = '会員様情報'
  setUserInfo()
})
</script>

<template>
  <NavBar v-bind:user="user" v-bind:client="client"/>
  <div class="p-3">
    <h4 class="fw-bolder mb-3">
      会員様情報
    </h4>
    <div v-if="client !== 'webview'" class="col-sm-9 col-md-6 col-lg-4 border border-primary bg-light mt-4 p-3">
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
    <div v-if="client === 'webview'" class="col-sm-9 col-md-6 col-lg-4 border border-primary bg-light mt-4 p-3">
      ユーザーネーム：{{ user.name }}
      <br>
      <a href="/update_profile?client=webview&param=ユーザーネーム" class="btn btn-primary my-2">変更</a>
      <br>
      <hr class="border-primary">
      メールアドレス：{{ user.mail }}
      <br>
      <a href="/update_profile?client=webview&param=メールアドレス" class="btn btn-primary my-2">変更</a>
      <br>
      <hr class="border-primary">
      パスワード：＊＊＊＊＊＊
      <br>
      <a href="/update_profile?client=webview&param=パスワード" class="btn btn-primary my-2">変更</a>
    </div>
    <br>
    <div class="my-2">
      <a v-bind:href="'/delete_user' + addQuery(client)" class="btn btn-danger" v-on:click.prevent="confirmDeleteUser">サービス退会</a>
    </div>
    <br>
  </div>
</template>
