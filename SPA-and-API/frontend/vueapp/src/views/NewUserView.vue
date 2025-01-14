<script setup lang="ts">
import { ref, onMounted, Ref } from 'vue'
import { useRouter, Router } from 'vue-router'
import { Response, User, Alert } from '../common/Interface'
import { getUserInfo, postJWTCreate, postUserCreate } from '../common/AccessAPI'
import { setJWT } from '../common/ManageJWT'
import NavBar from '../components/NavBar.vue'
import AlertBox from '../components/AlertBox.vue'

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

let mail_address: Ref<string, string> = ref('')
let password: Ref<string, string> = ref('')
let user_name: Ref<string, string> = ref('')

async function checkLoggedIn(): Promise<void> {
  const response: Response = await getUserInfo()
  if (response.status === 200) {
    router.push({name: 'index'})
  }
  else {
    setJWT('')
  }
}

async function tryCreateUser(): Promise<void> {
  if (mail_address.value === '' || password.value === '' || user_name.value === '') {
    alert.value = {
      show: true,
      msg: '未入力の項目がありました'
    }
    mail_address.value = ''
    password.value = ''
    user_name.value = ''
  }
  else {
    const response1: Response = await postUserCreate(
      mail_address.value, password.value, user_name.value
    )
    if (response1.status === 200) {
      const response2: Response = await postJWTCreate(
        mail_address.value, password.value
      )
      setJWT(response2.json.access_token)
      router.push({name: 'index'})
    }
    else if (response1.status === 401) {
      alert.value = {
        show: true,
        msg: response1.json.msg
      }
      mail_address.value = ''
      password.value = ''
      user_name.value = ''
    }
  }
}

onMounted(() => {
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
          <div class="mb-4">
            <label class="mb-2">ユーザーネーム</label>
            <input type="text" class="form-control border border-primary" v-model="user_name"/>
          </div>
          <br>
          <div>
            <button class="btn btn-primary" v-on:click="tryCreateUser">会員登録</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
