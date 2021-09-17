<template>
  <div class="pa-3">
    <page-title icon="mdi-access-point-network" class="mt-3">MQTT 모니터링</page-title>
    <hr class="my-3">

    <div class="my-3">
      <div v-if="Object.keys(sensors).length === 0">데이터 수신 중...</div>
      <div v-for="(devices, place) in sensors" :key="place">
        <m-title icon="fas fa-map-marker-alt">{{ place }}</m-title>
        <hr class="mt-1 mb-3" color="lightgray">
        <v-row>
          <v-col class="pa-3" cols="12" sm="4"
                v-for="(value, device) in devices" :key="device">
            <temperature v-if="device==='temp'" :value="value"></temperature>
            <humidity v-if="device==='humi'" :value="value"></humidity>
            <illumination v-if="device==='illu'" :value="value"></illumination>
          </v-col>
        </v-row>
      </div>
      <hr class="my-3 blue-grey darken-1">

      <m-title class="mt-10" icon="mdi-devices"> 장치 제어</m-title>
      <hr class="my-3">
      <v-row>
        <v-col cols="6" sm="4" v-for="(led, ix) in leds" :key="ix">
          <led :led="led" :topic="topic"></led>
        </v-col>
      </v-row>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Mqtt',
  data() {
    return {
      sensors: {
        // [place]: { [device]: value } 이런 형식
      },
      topic: 'iot/hong/control',
      leds: [
        { place: 'livingroom', placeTitle: '거실', color: 'red', state: false },
        { place: 'kitchen', placeTitle: '부엌', color: 'green', state: true },
        { place: 'bedroom', placeTitle: '침실', color: 'blue', state: false },
      ]
    };
  },
  mqtt: {
    'iot/hong/sensors/#': function(value, topic) {
      const [,,, place, device] = topic.split('/');

      this.$set(this.sensors, place, {
        ...this.sensors[place],
        [device]: value
      });

      // if (!this.sensors[place]) // 처음 받은 장소 초기화
      //   this.sensors[place] = {};
      // this.sensors[place][device] = value;
      // this.sensors = { ...this.sensors };
    }
  },
  mounted() {
    this.$mqtt.subscribe('iot/hong/sensors/#');
  },
  unmounted() {
    this.$mqtt.unsubscribe('iot/hong/sensors/#');
  },
}
</script>

<style>

</style>