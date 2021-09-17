<template>
  <div @click="changeState">
    <v-icon class="float-left mr-3"
      x-large :color="stateColor">fas fa-lightbulb</v-icon>
    <div>{{ led.placeTitle }}</div>

    <v-icon :color="iconColor">{{ icon }}</v-icon>
    {{ state }}
  </div>
</template>

<script>
export default {
  name: 'led',
  props: [ 'led', 'topic', ],
  data() {
    return {

    };
  },
  computed: {
    stateColor() {
      return (this.led.state ? this.led.color : 'gray');
    },
    icon() {
      return (this.led.state ? 
            'mdi-checkbox-marked-outline' : 'mdi-checkbox-blank-outline');
    },
    iconColor() {
      return (this.led.state ? 'indigo' : 'gray');
    },
    state() {
      return (this.led.state ? 'On' : 'Off');
    },
  },
  methods: {
    changeState() {
      this.led.state = !this.led.state;

      const place = this.led.place;
      const value = this.led.state ? 'on' : 'off';
      const message = { place, value };
      this.$mqtt.publish(this.topic, JSON.stringify(message));
    }
  }
}
</script>

<style>

</style>