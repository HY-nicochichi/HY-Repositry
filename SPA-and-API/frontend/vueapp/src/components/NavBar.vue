<script setup lang="ts">
import { defineProps } from 'vue'
import { useRouter, useRoute, Router, RouteLocationNormalizedLoadedGeneric } from 'vue-router'
import ManageJWT from '../functions/ManageJWT'
import ManageQuery from '../functions/ManageQuery'

interface User {
  login: boolean
  name: string
  mail: string
}

interface Props {
  user: User
  client: any
}

const props: Props  = defineProps<Props>()

const router: Router = useRouter()
const route: RouteLocationNormalizedLoadedGeneric = useRoute()

const { setJWT } = ManageJWT()
const { addQuery, pushRouter } = ManageQuery()

function tryLogout(): void {
  setJWT('')
  if (route.name === 'index') {
    router.go(0)
  }
  else {
    router.push(pushRouter(props.client, '/'))
  }
}
</script>

<template>
  <div class="pt-3">
    <nav class="navbar navbar-expand-sm navbar-dark bg-primary px-3 py-2">
      <a v-if="client !== 'webview'" class="navbar-brand color-dark d-flex align-items-center" v-bind:href="'/' + addQuery(client)">
        <img src="../assets/logo.png" width="40" alt="" class="flash-item">
        <span class="ps-2 fs-4 fw-bolder">SPA & API</span>
      </a>
      <a v-if="client === 'webview'" class="navbar-brand color-dark d-flex align-items-center" v-bind:href="'/' + addQuery(client)">
        <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-android flash-item" viewBox="0 0 16 16" style="color:chartreuse">
          <path d="M2.76 3.061a.5.5 0 0 1 .679.2l1.283 2.352A8.9 8.9 0 0 1 8 5a8.9 8.9 0 0 1 3.278.613l1.283-2.352a.5.5 0 1 1 .878.478l-1.252 2.295C14.475 7.266 16 9.477 16 12H0c0-2.523 1.525-4.734 3.813-5.966L2.56 3.74a.5.5 0 0 1 .2-.678ZM5 10a1 1 0 1 0 0-2 1 1 0 0 0 0 2m6 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2"/>
        </svg>
        <span class="ps-2 fs-4 fw-bolder">SPA & API Mobile</span>
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#NavBarContent" aria-controls="NavBarContent" aria-expanded="false" aria-label="Toggle navigation">
        <svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor" class="bi bi-list" viewBox="0 0 16 16" style="color:white">
          <path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5"/>
        </svg>
      </button>
      <div class="collapse navbar-collapse justify-content-end" id="NavBarContent">
        <ul v-if="user.login === true" class="navbar-nav">
          <li class="nav-item">
            <a type="button" class="nav-link active me-2" v-bind:href="'/profile' + addQuery(client)">
              "<span class="fw-bolder">{{ user.name }}</span>" 様
            </a>
          </li>
          <li class="nav-item">
            <a type="button" class="nav-link active" v-on:click="tryLogout">ログアウト</a>
          </li>
        </ul>
        <ul v-else class="navbar-nav">
          <li class="nav-item">
            <a type="button" class="nav-link active me-2" v-bind:href="'/login' + addQuery(client)">ログイン</a>
          </li>
          <li class="nav-item">
            <a type="button" class="nav-link active" v-bind:href="'/new_user' + addQuery(client)">会員登録</a>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<style scoped>
.flash-item {
  animation: flash 3s infinite
}
@keyframes flash {
  0%, 100% {
    opacity: 1
  }
  50% {
    opacity: 0.35
  }
}
</style>
