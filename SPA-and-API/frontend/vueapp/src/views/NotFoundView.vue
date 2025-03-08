<script setup lang="ts">
import { onMounted } from 'vue'

onMounted(() => {
  document.title = '404 Not Found'
})
</script>

<template>
  <div class="m-4">
    <h1>404 Not Found</h1>
    <p>お探しのページがありません</p>
    <br>
    <a href="/">TOPページ</a>
  </div>
</template>
