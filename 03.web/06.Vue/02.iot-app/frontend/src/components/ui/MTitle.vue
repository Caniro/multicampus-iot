<template>
  <div>
    <h2 class="indigo--text darken-4">
      <v-icon size="1.5rem" color="indigo darken-2">{{ icon }}</v-icon>
      <span style="font-size:1.5rem"><slot></slot></span>
    </h2>
  </div>
</template>

<script>
export default {
  name: 'MTitle',
  props: ['icon',],
};
</script>

<style>

</style>