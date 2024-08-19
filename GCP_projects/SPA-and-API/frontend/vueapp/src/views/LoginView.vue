<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import AccessAPI from '../functions/AccessAPI'
import ManageJWT from '../functions/ManageJWT'
import NavBar from '../components/NavBar.vue'
import AlertBox from '../components/AlertBox.vue'

const router = useRouter()

const { getUserInfo, postJWTCreate } = AccessAPI()
const { setJWT } = ManageJWT()

let user = ref({
  login: false,
  name: ''
})

let alert = ref({
  show: false,
  msg: ''
})

let mail = ref('')
let password = ref('')

async function checkLoggedIn() {
  const response = await getUserInfo()
  if (response.status === 200) {
    router.push({name: 'index'})
  }
  else {
    setJWT('')
  }
}

async function tryLogin() {
  if (mail.value === '' || password.value === '') {
    alert.value = {
      show: true,
      msg: '未入力の項目がありました'
    }
    mail.value = ''
    password.value = ''
  }
  else {
    const response = await postJWTCreate(
      mail.value, password.value
    )
    if (response.status === 200) {
      setJWT(response.json.access_token)
      router.push({name: 'index'})
    }
    else if (response.status === 401) {
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
