<script setup lang="ts">
import type { Router, RouteLocationNormalizedLoadedGeneric } from 'vue-router'

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
  } else {
    router.push({ name: 'index' })
  }
}
</script>

<template>
  <div class="pt-3">
    <nav class="navbar navbar-expand-sm navbar-dark bg-primary px-3 py-2">
      <a class="navbar-brand color-dark d-flex align-items-center" href="/">
        <svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" viewBox="0 0 24 24" style="color:mediumspringgreen">
          <path fill="currentColor" d="M13.464 19.83h8.922c.283 0 .562-.073.807-.21a1.6 1.6 0 0 0 .591-.574a1.53 1.53 0 0 0 .216-.783a1.53 1.53 0 0 0-.217-.782L17.792 7.414a1.6 1.6 0 0 0-.591-.573a1.65 1.65 0 0 0-.807-.21c-.283 0-.562.073-.807.21a1.6 1.6 0 0 0-.59.573L13.463 9.99L10.47 4.953a1.6 1.6 0 0 0-.591-.573a1.65 1.65 0 0 0-.807-.21c-.284 0-.562.073-.807.21a1.6 1.6 0 0 0-.591.573L.216 17.481a1.53 1.53 0 0 0-.217.782c0 .275.074.545.216.783a1.6 1.6 0 0 0 .59.574c.246.137.525.21.808.21h5.6c2.22 0 3.856-.946 4.982-2.79l2.733-4.593l1.464-2.457l4.395 7.382h-5.859Zm-6.341-2.46l-3.908-.002l5.858-9.842l2.923 4.921l-1.957 3.29c-.748 1.196-1.597 1.632-2.916 1.632"/>
        </svg>
        <span class="ps-2 fs-4 fw-bolder">Nuxt & Flask</span>
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
