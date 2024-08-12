<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import AccessAPI from '../functions/AccessAPI'
import ManageJWT from '../functions/ManageJWT'
import NavBar from '../components/NavBar.vue'
import AlertBox from '../components/AlertBox.vue'

const router = useRouter()
const route = useRoute()

const { getUserInfo, postUserUpdate } = AccessAPI()
const { setJWT } = ManageJWT()

let user = ref({
  login: false,
  name: ''
})

let alert = ref({
  show: false,
  msg: ''
})

let param = ref(route.query.param)

let type = ref('password')

let current_value = ref('')
let new_value= ref('')
let check_value = ref('')

async function setUserInfo() {
  const response = await getUserInfo()
  if (response.status === 200) {
    user.value = {
      login: true,
      name: response.json.user_info.username
    }
  }
  else {
    setJWT('')
    router.push({name: 'login'})
  }
}

async function tryUpdateUser() {
  if (current_value.value === '' || new_value.value === '' || check_value.value === '') {
    alert.value = {
      show: true,
      msg: '未入力の項目がありました'
    }
    current_value.value = ''
    new_value.value = ''
    check_value.value = ''
  }
  else {
    const response = await postUserUpdate(
      param.value, current_value.value, new_value.value, check_value.value
    )
    if (response.status === 200) {
      router.push({name: 'profile'})
    }
    else if (response.status === 401) {
      alert.value = {
        show: true,
        msg: response.json.msg
      }
      current_value.value = ''
      new_value.value = ''
      check_value.value = ''
    }
  }
}

onMounted(() => {
  document.title = param.value + 'の変更'
  if (param.value !== 'パスワード') {
    type.value = 'text'
  }
  setUserInfo()
})
</script>

<template>
  <NavBar v-bind:user="user"/>
  <div class="p-3">
    <AlertBox v-bind:alert="alert"/>
    <h4 class="fw-bolder mb-3">
      {{ param }}の変更
    </h4>
    <div class="col-sm-9 col-md-7 col-lg-5 border border-primary bg-light p-3">
      <div class="row">
        <div class="col">
          <div class="mb-4">
            <label class="mb-2">現{{ param }}</label>
            <input v-bind:type="type" class="form-control border border-primary" v-model="current_value">
          </div>
          <div class="mb-4">
            <label class="mb-2">新{{ param }}</label>
            <input v-bind:type="type" class="form-control border border-primary" v-model="new_value">
          </div>
          <div class="mb-4">
            <label class="mb-2">新{{ param }}(確認)</label>
            <input v-bind:type="type" class="form-control border border-primary" v-model="check_value">
          </div>
          <br>
          <div>
            <button class="btn btn-primary" v-on:click="tryUpdateUser">{{ param }}更新</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
