<script setup lang="ts">
import type { Router, RouteLocationNormalizedLoadedGeneric } from 'vue-router'

const router: Router = useRouter()
const route: RouteLocationNormalizedLoadedGeneric = useRoute()

const GoodParams: string[] = [
  'メールアドレス',
  'パスワード',
  'ユーザーネーム'
]

let user: Ref<User> = ref({
  login: false,
  name: '',
  mail: ''
})

let alert: Ref<Alert> = ref({
  show: false,
  msg: ''
})

let param: Ref<string> = ref(route.params.param as string || '')

let type: Ref<string> = ref('password')

let current_val: Ref<string> = ref('')
let new_val: Ref<string> = ref('')
let check_val: Ref<string> = ref('')

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

async function tryUpdateUser(): Promise<void> {
  if (current_val.value === '' || new_val.value === '' || check_val.value === '') {
    alert.value = {
      show: true,
      msg: '未入力の項目がありました'
    }
    current_val.value = ''
    new_val.value = ''
    check_val.value = ''
  }
  else {
    const resp: Resp = await accessUserPut(
      param.value, current_val.value, new_val.value, check_val.value
    )
    if (resp.status === 200) {
      router.push({name: 'user-info'})
    }
    else {
      alert.value = {
        show: true,
        msg: resp.json.msg
      }
      current_val.value = ''
      new_val.value = ''
      check_val.value = ''
    }
  }
}

onBeforeMount(() => {
  if (GoodParams.includes(param.value) === true) {
    document.title = param.value + 'の変更'
    if (param.value !== 'パスワード') {
      type.value = 'text'
    }
    setUserInfo()
  }
  else {
    router.push('/404')
  }
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
      <div class="mb-4">
        <label class="mb-2">現{{ param }}</label>
        <input v-bind:type="type" class="form-control border border-primary" v-model="current_val"/>
      </div>
      <div class="mb-4">
        <label class="mb-2">新{{ param }}</label>
        <input v-bind:type="type" class="form-control border border-primary" v-model="new_val"/>
      </div>
      <div class="mb-4">
        <label class="mb-2">新{{ param }}(確認)</label>
        <input v-bind:type="type" class="form-control border border-primary" v-model="check_val"/>
      </div>
      <br>
      <div>
        <button class="btn btn-primary" v-on:click="tryUpdateUser">{{ param }}更新</button>
      </div>
    </div>
  </div>
</template>
