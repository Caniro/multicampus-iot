<template>
  <div class="pa-3">
    <page-title icon="mdi-car">탐사 차량</page-title>

    <v-row>
      <v-col cols="12" :sm="6">
        <v-img src="http://192.168.117.10:8000/mjpeg/stream/"
          max-width="640" contain></v-img>
      </v-col>
      <v-col cols="6" :sm="3" class="text-center align-self-center">
        <div class="my-3">
          <knob v-model="angle" :options="knobOptions"></knob>
        </div>
        {{ angle.value }}°
      </v-col>
      <v-col cols="6" :sm="3" class="text-center align-self-center">
        <direction-panel @direction="onDirection"></direction-panel>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: 'ExplorationCar',
  data() {
    return {
      angle: {},
      knobOptions: [],
    };
  },
  computed: {

  },
  mounted() {
    for (let i = -90; i <= 90; i += 5) {
      this.knobOptions.push({
        value: i,
        label: i % 20 == 0 ? i : false,
        anchor: true,
      });
    }
    this.angle.value = 0;
  },
  methods: {
    onDirection(dir) {
      console.log('direction:', dir);
      this.$mqtt.publish('iot/hong/control/car', dir);
    }
  },
  watch: {
    angle() {
      this.$mqtt.publish('iot/hong/control/camera', String(this.angle.value));
      console.log('publish', 'iot/hong/control/camera', this.angle.value);
    }
  }
}
</script>

<style>

</style>
