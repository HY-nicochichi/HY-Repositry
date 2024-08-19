<script setup>
import { defineProps } from 'vue'

defineProps({
  alert: Object
})
</script>

<template>
  <div v-if="alert.show === true" class="alert alert-danger mb-3" role="alert">
    ※ {{ alert.msg }}
  </div>
</template>
