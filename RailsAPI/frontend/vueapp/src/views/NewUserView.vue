<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import AccessAPI from '../functions/AccessAPI'
import ManageJWT from '../functions/ManageJWT'
import NavBar from '../components/NavBar.vue'
import AlertBox from '../components/AlertBox.vue'

const router = useRouter()

const { getUserInfo, postJWTCreate, postUserCreate } = AccessAPI()
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
let username = ref('')

async function checkLoggedIn() {
  const response = await getUserInfo()
  if (response.status === 200) {
    router.push({name: 'index'})
  }
  else {
    setJWT('')
  }
}

async function tryCreateUser() {
  if (mail.value === '' || password.value === '' || username.value === '') {
    alert.value = {
      show: true,
      msg: '未入力の項目がありました'
    }
    mail.value = ''
    password.value = ''
    username.value = ''
  }
  else {
    const response1 = await postUserCreate(
      mail.value, password.value, username.value
    )
    if (response1.status === 200) {
      const response2 = await postJWTCreate(
        mail.value, password.value
      )
      setJWT(response2.json.access_token)
      router.push({name: 'index'})
    }
    else if (response1.status === 401) {
      alert.value = {
        show: true,
        msg: response1.json.msg
      }
      mail.value = ''
      password.value = ''
      username.value = ''
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
            <input type="text" class="form-control border border-primary" v-model="mail"/>
          </div>
          <div class="mb-4">
            <label class="mb-2">パスワード</label>
            <input type="password" class="form-control border border-primary" v-model="password"/>
          </div>
          <div class="mb-4">
            <label class="mb-2">ユーザーネーム</label>
            <input type="text" class="form-control border border-primary" v-model="username"/>
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
