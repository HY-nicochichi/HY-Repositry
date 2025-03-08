<script setup lang="ts">
import type { Ref } from 'vue'
import type { Router } from 'vue-router'
import type { Response, User, Alert } from '~/utils/Interface'
import { accessJwtPost, accessUserGet } from '~/utils/AccessAPI'
import { setJWT } from '~/utils/ManageJWT'
import NavBar from '~/components/NavBar.vue'
import AlertBox from '~/components/AlertBox.vue'

const router: Router = useRouter()

let user: Ref<User, User> = ref({
  login: false,
  name: '',
  mail: ''
})

let alert: Ref<Alert, Alert> = ref({
  show: false,
  msg: ''
})

let mail: Ref<string, string> = ref('')
let password: Ref<string, string> = ref('')

async function checkLoggedIn(): Promise<void> {
  const response: Response = await accessUserGet()
  if (response.status === 200) {
    router.push({name: 'index'})
  }
  else {
    setJWT('')
  }
}

async function tryLogin(): Promise<void> {
  if (mail.value === '' || password.value === '') {
    alert.value = {
      show: true,
      msg: '未入力の項目がありました'
    }
    mail.value = ''
    password.value = ''
  }
  else {
    const response: Response = await accessJwtPost(
      mail.value, password.value
    )
    if (response.status === 200) {
      setJWT(response.json.access_token)
      router.push({name: 'index'})
    }
    else {
      alert.value = {
        show: true,
        msg: response.json.msg
      }
      mail.value = ''
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
  <NavBar v-bind:user="user"/>
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
            <input type="text" class="form-control border border-primary" v-model="mail"/>
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
