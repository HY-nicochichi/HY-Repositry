<script setup lang="ts">
import { defineProps } from 'vue'
import type { Alert } from '~/utils/Interface'

interface Props {
  alert: Alert
}

defineProps<Props>()
</script>

<template>
  <div v-if="alert.show === true" class="alert alert-danger mb-3" role="alert">
    ※ {{ alert.msg }}
  </div>
</template>
