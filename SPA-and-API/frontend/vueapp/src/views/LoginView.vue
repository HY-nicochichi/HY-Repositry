<script setup lang="ts">
import { ref, onMounted, Ref } from 'vue'
import { useRouter, useRoute, Router, RouteLocationNormalizedLoadedGeneric } from 'vue-router'
import AccessAPI from '../functions/AccessAPI'
import ManageJWT from '../functions/ManageJWT'
import ManageQuery from '../functions/ManageQuery'
import NavBar from '../components/NavBar.vue'
import AlertBox from '../components/AlertBox.vue'

const router: Router = useRouter()
const route: RouteLocationNormalizedLoadedGeneric = useRoute()

const { getUserInfo, postJWTCreate } = AccessAPI()
const { setJWT } = ManageJWT()
const { pushRouter } = ManageQuery()

let user: Ref = ref({
  login: false,
  name: '',
  mail: ''
})

let alert: Ref = ref({
  show: false,
  msg: ''
})

const client: Ref = ref(route.query.client)

let mail_address: Ref = ref('')
let password: Ref = ref('')

async function checkLoggedIn(): Promise<void> {
  const response: {status: number, json: any} = await getUserInfo(client.value)
  if (response.status === 200) {
    router.push(pushRouter(client.value, '/'))
  }
  else {
    setJWT('')
  }
}

async function tryLogin(): Promise<void> {
  if (mail_address.value === '' || password.value === '') {
    alert.value = {
      show: true,
      msg: '未入力の項目がありました'
    }
    mail_address.value = ''
    password.value = ''
  }
  else {
    const response: {status: number, json: any} = await postJWTCreate(
      client.value, mail_address.value, password.value
    )
    if (response.status === 200) {
      setJWT(response.json.access_token)
      router.push(pushRouter(client.value, '/'))
    }
    else if (response.status === 401) {
      alert.value = {
        show: true,
        msg: response.json.msg
      }
      mail_address.value = ''
      password.value = ''
    }
  }
}

onMounted(() => {
  document.title = 'ログイン'
  checkLoggedIn()
})
</script>

<template>
  <NavBar v-bind:user="user" v-bind:client="client"/>
  <div class="p-3">
    <AlertBox v-bind:alert="alert"/>
    <h4 class="fw-bolder mb-3">
      ログイン
    </h4>
    <div class="col-sm-9 col-md-7 col-lg-5 border border-primary bg-light p-3">
      <div class="row">
        <div class="col">
          <div class="mb-4">
            <label class="mb-2">メールアドレス</label>
            <input type="text" class="form-control border border-primary" v-model="mail_address"/>
          </div>
          <div class="mb-4">
            <label class="mb-2">パスワード</label>
            <input type="password" class="form-control border border-primary" v-model="password"/>
          </div>
          <br>
          <div>
            <button class="btn btn-primary" v-on:click="tryLogin">ログイン</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
