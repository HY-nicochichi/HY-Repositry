<script setup lang="ts">
import type { Router } from 'vue-router'

const router: Router = useRouter()

let user: Ref<User> = ref({
  login: false,
  name: '',
  mail: ''
})

let alert: Ref<Alert> = ref({
  show: false,
  msg: ''
})

let mail: Ref<string> = ref('')
let password: Ref<string> = ref('')
let name: Ref<string> = ref('')

async function checkLoggedIn(): Promise<void> {
  const resp: Resp = await accessUserGet()
  if (resp.status === 200) {
    router.push({name: 'index'})
  }
  else {
    setJWT('')
  }
}

async function tryCreateUser(): Promise<void> {
  if (mail.value === '' || password.value === '' || name.value === '') {
    alert.value = {
      show: true,
      msg: '未入力の項目がありました'
    }
    mail.value = ''
    password.value = ''
    name.value = ''
  }
  else {
    const resp1: Resp = await accessUserPost(
      mail.value, password.value, name.value
    )
    if (resp1.status === 200) {
      const resp2: Resp = await accessJwtPost(
        mail.value, password.value
      )
      setJWT(resp2.json.access_token)
      router.push({name: 'index'})
    }
    else {
      alert.value = {
        show: true,
        msg: resp1.json.msg
      }
      mail.value = ''
      password.value = ''
      name.value = ''
    }
  }
}

onBeforeMount(() => {
  document.title = '会員登録'
  checkLoggedIn()
})
</script>

<template>
  <NavBar v-bind:user="user"/>
  <div class="p-3">
    <AlertBox v-bind:alert="alert"/>
    <h4 class="fw-bolder mb-3">
      会員登録
    </h4>
    <div class="col-sm-9 col-md-7 col-lg-5 border border-primary bg-light p-3">
      <div class="mb-4">
        <label class="mb-2">メールアドレス</label>
        <input type="text" class="form-control border border-primary" v-model="mail"/>
      </div>
      <div class="mb-4">
        <label class="mb-2">パスワード</label>
        <input type="password" class="form-control border border-primary" v-model="password"/>
      </div>
      <div class="mb-4">
        <label class="mb-2">ユーザーネーム</label>
        <input type="text" class="form-control border border-primary" v-model="name"/>
      </div>
      <br>
      <div>
        <button class="btn btn-primary" v-on:click="tryCreateUser">会員登録</button>
      </div>
    </div>
  </div>
</template>
