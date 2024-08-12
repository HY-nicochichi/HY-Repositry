<script setup>
import { defineProps } from 'vue'

defineProps({
  user: Object
})
</script>

<template>
  <div class="pt-3">
    <nav class="navbar navbar-expand-sm navbar-dark bg-danger px-3 py-2">
      <a class="navbar-brand color-dark d-flex align-items-center" href="/">
        <img src="../assets/logo.png" width="40" alt="" class="flash-item">
        <span class="ps-2 fs-4 fw-bolder">RailsAPI</span>
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#NavBarContent" aria-controls="NavBarContent" aria-expanded="false" aria-label="Toggle navigation">
        <i class="bi bi-list fs-4" style="color:white"></i>
      </button>
      <div class="collapse navbar-collapse justify-content-end" id="NavBarContent">
        <ul v-if="user.login === true" class="navbar-nav">
          <li class="nav-item">
            <a type="button" class="nav-link active me-2" href="/profile">
              "<span class="fw-bolder">{{ user.name }}</span>" 様
            </a>
          </li>
          <li class="nav-item">
            <a type="button" class="nav-link active" href="/logout">ログアウト</a>
          </li>
        </ul>
        <ul v-else class="navbar-nav">
          <li class="nav-item">
            <a type="button" class="nav-link active me-2" href="/login">ログイン</a>
          </li>
          <li class="nav-item">
            <a type="button" class="nav-link active" href="/new_user">会員登録</a>
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
