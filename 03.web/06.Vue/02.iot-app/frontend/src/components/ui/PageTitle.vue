<template>
  <div>
    <h2 class="indigo--text darken-4">
      <v-icon size="1.5em" color="indigo darken-2">{{ icon }}</v-icon>
      <slot></slot>
    </h2>
  </div>
</template>

<script>
export default {
  name: 'PageTitle',
  props: ['icon',],
};
</script>

<style>

</style>