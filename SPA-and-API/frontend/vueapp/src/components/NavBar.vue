<script setup lang="ts">
import { defineProps } from 'vue'
import { useRouter, useRoute, Router, RouteLocationNormalizedLoadedGeneric } from 'vue-router'
import { User } from '../common/Interface'
import { setJWT } from '../common/ManageJWT'

interface Props {
  user: User
}

defineProps<Props>()

const router: Router = useRouter()
const route: RouteLocationNormalizedLoadedGeneric = useRoute()

function tryLogout(): void {
  setJWT('')
  if (route.name === 'index') {
    router.go(0)
  }
  else {
    router.push({name: 'index'})
  }
}
</script>

<template>
  <div class="pt-3">
    <nav class="navbar navbar-expand-sm navbar-dark bg-primary px-3 py-2">
      <a class="navbar-brand color-dark d-flex align-items-center" href="/">
        <img src="../assets/logo.png" width="35">
        <span class="ps-2 fs-4 fw-bolder">SPA & API</span>
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#NavBarContent" aria-controls="NavBarContent" aria-expanded="false" aria-label="Toggle navigation">
        <svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" viewBox="0 0 16 16" style="color:white">
          <path fill="currentColor" fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5"/>
        </svg>
      </button>
      <div class="collapse navbar-collapse justify-content-end" id="NavBarContent">
        <ul v-if="user.login === true" class="navbar-nav">
          <li class="nav-item">
            <a type="button" class="nav-link active me-2" href="/user/info">
              "<span class="fw-bolder">{{ user.name }}</span>" 様
            </a>
          </li>
          <li class="nav-item">
            <a type="button" class="nav-link active" v-on:click="tryLogout">ログアウト</a>
          </li>
        </ul>
        <ul v-else class="navbar-nav">
          <li class="nav-item">
            <a type="button" class="nav-link active me-2" href="/user/auth">ログイン</a>
          </li>
          <li class="nav-item">
            <a type="button" class="nav-link active" href="/user/new">会員登録</a>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</template>
