<template>
  <div class="pa-3">
    <page-title>오늘의 날씨</page-title>
    <span>
      <v-icon>mdi-clock</v-icon>
      {{ new Date()|moment("YYYY-MM-DD hh:mm:ss") }}
    </span>
    <Weather />
  </div>
</template>

<script>

export default {
  name: 'Home',
}
</script>
