<template>
  <div v-if="alert.show === true" class="alert alert-danger mb-3" role="alert">
    ※ {{ alert.msg }}
  </div>
</template>

<script>
export default {
  name: 'AlertBox',
  props: [
    'alert'
  ]
}
</script>
