<template>
  <div>
    <v-icon x-large class="mr-3 float-left"
        :color="color">{{ icon }}</v-icon>
    <div class="font-weight-bold">습도</div>
    <span>{{ value }}%</span>
  </div>
</template>

<script>
export default {
  name: 'Humidity',
  props: ['value'],
  data() {
    return {
      icons: [ 'mdi-water','mdi-water-alert', ],
      colors: [ 'blue lighten-4', 'indigo', ],
    }
  },
  computed: {
    color() {
      return this.colors[this.index];
    },
    icon() {
      return this.icons[this.index];
    },
    index() {
      return (this.value < 50 ? 0 : 1);
    }
  },
}
</script>

<style>

</style>