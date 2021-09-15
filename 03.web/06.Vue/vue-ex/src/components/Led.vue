<template>
  <div>
    <div>
      <span v-if="state">
        <i class="led-icon fas fa-lightbulb" :style="{color:color}"></i>
      </span>
      <span v-else>
        <i class="led-icon fas fa-lightbulb" ></i>
      </span>
    </div>
    <div class="led-label">{{ place }}</div>
    <div>
      <input type="checkbox" v-model="checkState" @change="onStateChange">
      {{ state ? 'On' : 'Off' }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'Led',
  props: ['index', 'place', 'color', 'state'],
  data() {
    return {
      checkState: false,
    };
  },
  mounted() {
    this.checkState = this.state;
  },
  methods: {
    onStateChange() {
      this.$emit('led-state-change', this.index, this.checkState);
    },
  }
}
</script>

<style scoped>
.led-icon {
  font-size: 2rem;
}
</style>
